# Day 7 setup — wired to Day 6

This branch connects Day 7 retrieval to the completed Day 6 pipeline:

| Day 6 artifact | Value used by Day 7 |
|---|---|
| Vector store | PostgreSQL + pgvector table `rag_chunks` |
| Embedding model | `BAAI/bge-m3` (1024-d, L2-normalized) |
| Default strategy | `B` (paragraph chunks; best Day 6 coherence) |
| Corpus | `data/fpt_esg_report_2025.pdf` (49 content pages) |
| Benchmark seed | Day 6 `data/benchmark.json` (15 dev / 5 test) + 4 abstention stubs |

## Prerequisites

1. **Day 6 index populated** — either:
   - Day 6 Docker: `cd <day6>/starter && docker compose -p day6_student_starter up -d --wait` then `python -m src.run`, **or**
   - Local Postgres 16 + pgvector with the same `DATABASE_URL` user/db.
2. Python **3.11+**, network once to download `BAAI/bge-m3` if not cached.
3. Optional LLM key (`OPENROUTER_API_KEY` or `OPENAI_API_KEY`) for a real tool-calling controller. Without a key the CLI uses `HeuristicController` so dense retrieval still boots.

## Configure

```bash
cd starter
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Edit DATABASE_URL:
#   Docker Day 6 → …@127.0.0.1:55433/day6_lab
#   Local Postgres → …@127.0.0.1:5432/day6_lab
# Set DAY6_REPO to the Day 6 checkout if it is not a sibling directory.
```

**Secrets the user must set (never commit):**

| Variable | Required? | Purpose |
|---|---|---|
| `DATABASE_URL` | Yes | Day 6 Postgres connection |
| `EMBEDDING_MODEL` | Optional (default `BAAI/bge-m3`) | Must match Day 6 index |
| `DAY6_STRATEGY` | Optional (default `B`) | `A` / `B` / `C` column in `rag_chunks` |
| `OPENROUTER_API_KEY` or `OPENAI_API_KEY` | For real agent LLM | Tool-calling controller |
| `LLM_MODEL` / `OPENAI_BASE_URL` | Optional | Model id / OpenAI-compatible base URL |

No fake embeddings: query vectors always come from Sentence Transformers `BAAI/bge-m3`.

## Export Day 6 → Day 7 JSON

```bash
# Default unions strategies A+B into chunks.json (covers long gold quotes).
# Dense search still uses DAY6_STRATEGY (default B) against pgvector.
python export_day6.py --output data/converted
```

Writes `chunks.json`, `questions.json`, `agent_cases.json`, `export_meta.json` under `starter/data/converted/` (gitignored).

Alternatively, if you already exported raw Day 6 JSON arrays:

```bash
python convert_day6.py --chunks <day6_chunks.json> --questions <day6_questions.json> --output data/converted
```

## Run three retrieval methods

```bash
# 1) Dense (Day 6 vector store) — required
python dense.py --chunks data/converted/chunks.json --questions data/converted/questions.json \
  --split dev --output results/dev-dense

# 2) Lexical TF-IDF baseline (offline)
python baseline.py --chunks data/converted/chunks.json --questions data/converted/questions.json \
  --split dev --output results/dev-tfidf

# 3) Hybrid RRF (dense + TF-IDF)
python hybrid.py --chunks data/converted/chunks.json --questions data/converted/questions.json \
  --split dev --output results/dev-hybrid
```

Answerable-only questions are scored for Hit metrics. Abstention stubs are excluded from `dense`/`hybrid`/`baseline` validation.

## Agent smoke test

```bash
# Default context budget is 2400 (Day 6 paragraph chunks are large).
python run_agent_cli.py --question "FPT đặt mục tiêu Net Zero vào năm nào?"
```

Without `OPENROUTER_API_KEY` / `OPENAI_API_KEY`, this uses `HeuristicController` (search once, cite top context). Dense retrieval still hits the real Day 6 index.

## Unit tests (mocked; no live store required)

```bash
cd ..   # repo root
python -m unittest discover -s tests -v
```

## Notes / blockers

- If `rag_chunks` is empty, re-run Day 6 `python -m src.run` after Postgres is up.
- Day 6 Docker was not available in every cloud image; this environment used local Postgres 16 + pgvector on port **5432** while keeping Day 6’s Docker port **55433** in `.env.example`.
- Full Day 7 benchmark still needs manual answer grading + abstention review (`BENCHMARK.md`); this setup focuses on a bootable scaffold and dense retrieval against Day 6.
