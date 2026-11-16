"""Query/document embeddings — same model contract as Day 6 (BAAI/bge-m3)."""

from __future__ import annotations

import logging
import os

from sentence_transformers import SentenceTransformer

logger = logging.getLogger(__name__)

DEFAULT_MODEL = "BAAI/bge-m3"


class MyEmbedder:
    """Local Sentence Transformers adapter; no mock / random vectors."""

    def __init__(
        self,
        model_name: str | None = None,
        *,
        local_files_only: bool = True,
        batch_size: int = 32,
    ) -> None:
        self.model_name = model_name or os.getenv("EMBEDDING_MODEL") or DEFAULT_MODEL
        self.batch_size = batch_size
        logger.info(
            "Loading embedding model %s (local_files_only=%s)…",
            self.model_name,
            local_files_only,
        )
        try:
            self.model = SentenceTransformer(
                self.model_name, local_files_only=local_files_only
            )
        except Exception:
            if local_files_only:
                logger.warning(
                    "Cache miss for %s; downloading from HuggingFace…", self.model_name
                )
                self.model = SentenceTransformer(
                    self.model_name, local_files_only=False
                )
            else:
                raise

        if hasattr(self.model, "get_embedding_dimension"):
            self.dimensions = int(self.model.get_embedding_dimension())
        else:
            self.dimensions = int(self.model.get_sentence_embedding_dimension())
        if self.dimensions <= 0:
            raise RuntimeError(f"Invalid embedding dimensions: {self.dimensions}")
        logger.info("Embedder ready: %s | dim=%s", self.model_name, self.dimensions)

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        if not texts:
            return []
        embeddings = self.model.encode(
            texts,
            batch_size=self.batch_size,
            show_progress_bar=len(texts) > 64,
            normalize_embeddings=True,
            convert_to_numpy=True,
        )
        return [row.tolist() for row in embeddings]

    def embed_query(self, question: str) -> list[float]:
        if not question or not question.strip():
            raise ValueError("empty query — cannot embed")
        vec = self.model.encode(
            question, normalize_embeddings=True, convert_to_numpy=True
        )
        return vec.tolist()
