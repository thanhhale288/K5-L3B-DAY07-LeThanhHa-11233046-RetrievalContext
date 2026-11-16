"""Read-only client for the Day 6 PostgreSQL + pgvector `rag_chunks` table."""

from __future__ import annotations

import json
import logging
import os
from typing import Any

import psycopg
from psycopg.rows import dict_row

logger = logging.getLogger(__name__)

ALLOWED_FILTER_KEYS = {"pillar", "document_id", "source", "page"}


def _vector_literal(values: list[float]) -> str:
    return "[" + ",".join(f"{x:.8f}" for x in values) + "]"


class Day6PgVectorStore:
    """Query the Day 6 index. Does not create schema or upsert (Day 6 owns that)."""

    def __init__(self, database_url: str | None = None, dimensions: int = 1024) -> None:
        self.database_url = database_url or os.getenv("DATABASE_URL")
        if not self.database_url:
            raise ValueError(
                "DATABASE_URL missing — copy starter/.env.example → starter/.env "
                "and point it at the Day 6 Postgres (Docker :55433 or local)."
            )
        if dimensions <= 0:
            raise ValueError(f"dimensions must be > 0, got {dimensions}")
        self.dimensions = dimensions

        with psycopg.connect(self.database_url) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT extversion FROM pg_extension WHERE extname = 'vector'"
                )
                row = cur.fetchone()
                if not row:
                    raise RuntimeError(
                        "pgvector extension not enabled on DATABASE_URL database"
                    )
                cur.execute(
                    """
                    SELECT EXISTS (
                        SELECT 1 FROM information_schema.tables
                        WHERE table_name = 'rag_chunks'
                    )
                    """
                )
                exists = cur.fetchone()[0]
                if not exists:
                    raise RuntimeError(
                        "Table rag_chunks missing — run Day 6 ingestion "
                        "(cd day06/starter && python -m src.run) first."
                    )
                logger.info(
                    "Day6PgVectorStore OK | dim=%s | pgvector=%s",
                    dimensions,
                    row[0],
                )

    def count(self, strategy: str | None = None) -> int:
        with psycopg.connect(self.database_url) as conn:
            with conn.cursor() as cur:
                if strategy is None:
                    cur.execute("SELECT COUNT(*) FROM rag_chunks")
                else:
                    cur.execute(
                        "SELECT COUNT(*) FROM rag_chunks WHERE strategy = %s",
                        (strategy,),
                    )
                return int(cur.fetchone()[0])

    def export_chunks(self, strategy: str) -> list[dict[str, Any]]:
        """Export Day 6 chunks as Day 7-ready dicts (id/source_id/…)."""
        with psycopg.connect(self.database_url) as conn:
            with conn.cursor(row_factory=dict_row) as cur:
                cur.execute(
                    """
                    SELECT chunk_id, document_id, source, page, text, pillar, metadata
                    FROM rag_chunks
                    WHERE strategy = %s
                    ORDER BY page, chunk_id
                    """,
                    (strategy,),
                )
                rows = cur.fetchall()

        chunks: list[dict[str, Any]] = []
        for row in rows:
            meta = row["metadata"]
            if isinstance(meta, str):
                meta = json.loads(meta)
            meta = dict(meta or {})
            if row["pillar"] and "pillar" not in meta:
                meta["pillar"] = row["pillar"]
            chunks.append(
                {
                    "id": row["chunk_id"],
                    "source_id": row["document_id"],
                    "source": row["source"],
                    "page": int(row["page"]),
                    "text": row["text"],
                    "metadata": meta,
                }
            )
        return chunks

    def search(
        self,
        strategy: str,
        query_vector: list[float],
        top_k: int = 3,
        filters: dict[str, Any] | None = None,
    ) -> list[dict[str, Any]]:
        if len(query_vector) != self.dimensions:
            raise ValueError(
                f"query_vector dim={len(query_vector)} ≠ store dim={self.dimensions}"
            )
        if top_k <= 0:
            raise ValueError("top_k must be > 0")

        where_parts = ["c.strategy = %s"]
        params: list[Any] = [_vector_literal(query_vector), strategy]

        if filters:
            for key, value in filters.items():
                if key not in ALLOWED_FILTER_KEYS:
                    raise ValueError(
                        f"Filter key not allowed: {key!r}. "
                        f"Use one of {sorted(ALLOWED_FILTER_KEYS)}"
                    )
                if value is None:
                    continue
                where_parts.append(f"c.{key} = %s")
                params.append(value)

        params.append(top_k)
        sql = f"""
            SELECT
                c.chunk_id,
                c.document_id,
                c.source,
                c.page,
                c.text,
                c.pillar,
                c.metadata,
                1 - (c.embedding <=> q.v) AS score
            FROM rag_chunks AS c,
                 (SELECT %s::vector AS v) AS q
            WHERE {" AND ".join(where_parts)}
            ORDER BY c.embedding <=> q.v
            LIMIT %s
        """

        with psycopg.connect(self.database_url) as conn:
            with conn.cursor(row_factory=dict_row) as cur:
                cur.execute(sql, params)
                rows = cur.fetchall()

        results: list[dict[str, Any]] = []
        for row in rows:
            meta = row["metadata"]
            if isinstance(meta, str):
                meta = json.loads(meta)
            meta = dict(meta or {})
            if row["pillar"] and "pillar" not in meta:
                meta["pillar"] = row["pillar"]
            results.append(
                {
                    "id": row["chunk_id"],
                    "source_id": row["document_id"],
                    "source": row["source"],
                    "page": int(row["page"]),
                    "text": row["text"],
                    "metadata": meta,
                    "score": float(row["score"]) if row["score"] is not None else None,
                    "strategy": "dense",
                }
            )
        return results
