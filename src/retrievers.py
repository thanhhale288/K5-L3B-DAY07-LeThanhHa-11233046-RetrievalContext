"""Three retrieval methods over the same Day 6 corpus (strategy B chunks).

All retrievers implement starter/agentic.Retriever:
    search(query, *, filters=None, top_k=3) -> list[chunk]
and return the Day 7 chunk contract plus `score`, `rank`, `strategy`.

- DenseRetriever : bge-m3 query embedding -> pgvector cosine (HNSW) on Day 6 `rag_chunks`.
- BM25Retriever  : rank_bm25 Okapi over the exported chunks.json (same chunk IDs/text as the DB).
- HybridRetriever: Reciprocal Rank Fusion of several retrievers' candidate lists.

Filters only come from the question's user-provided `filter` field (e.g. {"pillar": "Environment"}),
never from gold labels. Errors propagate; there is no fallback to fake results.
"""
from __future__ import annotations

import re
import sys
import time
import unicodedata
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from llm import load_env  # noqa: E402

FILTER_KEYS = {'pillar', 'page', 'source_id'}  # whitelisted; mapped to DB columns below
_DB_COLUMN = {'pillar': 'pillar', 'page': 'page', 'source_id': 'document_id'}


def _check_filters(filters: dict[str, Any] | None) -> dict[str, Any]:
    filters = filters or {}
    unknown = set(filters) - FILTER_KEYS
    if unknown:
        raise ValueError(f'filter không hỗ trợ: {sorted(unknown)} (cho phép {sorted(FILTER_KEYS)})')
    return filters


def _matches(chunk: dict[str, Any], filters: dict[str, Any]) -> bool:
    for key, value in filters.items():
        actual = chunk.get(key, chunk.get('metadata', {}).get(key))
        if actual != value:
            return False
    return True


def _ranked(results: list[dict[str, Any]], strategy: str) -> list[dict[str, Any]]:
    return [{**r, 'rank': i + 1, 'strategy': strategy} for i, r in enumerate(results)]


# ---------------------------------------------------------------- dense
class BgeM3Embedder:
    """Same model and normalisation as Day 6 (`starter/src/embeddings.py`): bge-m3, 1024-d, L2-normalised."""

    def __init__(self, model_name: str = 'BAAI/bge-m3') -> None:
        import os
        os.environ.setdefault('HF_HUB_OFFLINE', '1')  # model is already cached by Day 6
        from sentence_transformers import SentenceTransformer
        self.model_name = model_name
        self.model = SentenceTransformer(model_name, local_files_only=True)
        dim_fn = getattr(self.model, 'get_embedding_dimension', None) or self.model.get_sentence_embedding_dimension
        self.dimensions = int(dim_fn())

    def embed_query(self, text: str) -> list[float]:
        if not text.strip():
            raise ValueError('query rỗng')
        return self.model.encode(text, normalize_embeddings=True, convert_to_numpy=True).tolist()


class DenseRetriever:
    name = 'dense'

    def __init__(self, database_url: str | None = None, *, strategy: str = 'B',
                 embedder: BgeM3Embedder | None = None) -> None:
        import os
        import psycopg
        load_env()
        self.database_url = database_url or os.environ.get('DATABASE_URL')
        if not self.database_url:
            raise RuntimeError('Thiếu DATABASE_URL')
        self.strategy = strategy
        self.embedder = embedder or BgeM3Embedder()
        self.conn = psycopg.connect(self.database_url, autocommit=True)
        with self.conn.cursor() as cur:
            cur.execute('SELECT DISTINCT vector_dims(embedding) FROM rag_chunks WHERE strategy = %s', (strategy,))
            dims = [r[0] for r in cur.fetchall()]
        if dims != [self.embedder.dimensions]:
            raise RuntimeError(f'Số chiều index {dims} khác query embedding {self.embedder.dimensions}')

    def search(self, query: str, *, filters: dict[str, Any] | None = None, top_k: int = 3) -> list[dict[str, Any]]:
        filters = _check_filters(filters)
        vec = '[' + ','.join(f'{x:.8f}' for x in self.embedder.embed_query(query)) + ']'
        where, params = ['strategy = %s'], [self.strategy]
        for key, value in filters.items():
            where.append(f'{_DB_COLUMN[key]} = %s')  # column name from whitelist only
            params.append(value)
        sql = f"""SELECT chunk_id, document_id, source, page, text, pillar, metadata,
                         1 - (embedding <=> %s::vector) AS score
                  FROM rag_chunks WHERE {' AND '.join(where)}
                  ORDER BY embedding <=> %s::vector LIMIT %s"""
        with self.conn.cursor() as cur:
            cur.execute(sql, [vec, *params, vec, top_k])
            rows = cur.fetchall()
        results = []
        for chunk_id, doc_id, source, page, text, pillar, metadata, score in rows:
            meta = dict(metadata or {})
            if pillar is not None:
                meta.setdefault('pillar', pillar)
            results.append({'id': chunk_id, 'source_id': doc_id, 'source': source, 'page': page,
                            'text': text, 'metadata': meta, 'score': float(score)})
        return _ranked(results, self.name)


# ---------------------------------------------------------------- lexical
def tokenize_vi(text: str, *, bigrams: bool = False) -> list[str]:
    """Syllable tokens (NFC, casefold). Vietnamese words are often 2 syllables,
    so `bigrams=True` adds joined adjacent syllables (e.g. 'lao_động') as extra terms."""
    tokens = re.findall(r'\w+', unicodedata.normalize('NFC', text).casefold())
    if bigrams:
        tokens = tokens + [f'{a}_{b}' for a, b in zip(tokens, tokens[1:])]
    return tokens


class BM25Retriever:
    def __init__(self, chunks: list[dict[str, Any]], *, bigrams: bool = False, k1: float = 1.5, b: float = 0.75) -> None:
        from rank_bm25 import BM25Okapi
        if not chunks:
            raise ValueError('chunks rỗng')
        self.name = 'bm25+bigram' if bigrams else 'bm25'
        self.chunks = chunks
        self.bigrams = bigrams
        self.index = BM25Okapi([tokenize_vi(c['text'], bigrams=bigrams) for c in chunks], k1=k1, b=b)

    def search(self, query: str, *, filters: dict[str, Any] | None = None, top_k: int = 3) -> list[dict[str, Any]]:
        filters = _check_filters(filters)
        scores = self.index.get_scores(tokenize_vi(query, bigrams=self.bigrams))
        order = sorted(range(len(self.chunks)), key=lambda i: (-scores[i], self.chunks[i]['id']))
        results = []
        for i in order:
            if scores[i] <= 0:
                break
            if _matches(self.chunks[i], filters):
                results.append({**self.chunks[i], 'score': float(scores[i])})
                if len(results) == top_k:
                    break
        return _ranked(results, self.name)


# ---------------------------------------------------------------- hybrid
class HybridRetriever:
    """RRF: score(d) = sum_r 1 / (k + rank_r(d)). Rank-based, so dense cosine and BM25
    scores need no normalisation. Each retriever contributes its top `candidates`."""

    def __init__(self, retrievers: list[Any], *, k: int = 60, candidates: int = 20) -> None:
        self.retrievers = retrievers
        self.k = k
        self.candidates = candidates
        self.name = 'hybrid(' + '+'.join(r.name for r in retrievers) + ')'

    def search(self, query: str, *, filters: dict[str, Any] | None = None, top_k: int = 3) -> list[dict[str, Any]]:
        fused: dict[str, dict[str, Any]] = {}
        for r in self.retrievers:
            for item in r.search(query, filters=filters, top_k=self.candidates):
                entry = fused.setdefault(item['id'], {**{k: v for k, v in item.items() if k not in ('score', 'rank', 'strategy')},
                                                      'score': 0.0, 'components': {}})
                entry['score'] += 1.0 / (self.k + item['rank'])
                entry['components'][r.name] = {'rank': item['rank'], 'score': item['score']}
        results = sorted(fused.values(), key=lambda c: (-c['score'], c['id']))[:top_k]
        return _ranked(results, self.name)


def timed_search(retriever: Any, query: str, **kwargs: Any) -> tuple[list[dict[str, Any]], float]:
    start = time.perf_counter()
    results = retriever.search(query, **kwargs)
    return results, (time.perf_counter() - start) * 1000
