# Repository

## Overview
A retrieval-augmented generation (RAG) system for academic papers. The pipeline ingests PDFs, chunks and embeds text, stores vectors in ChromaDB, retrieves relevant passages, ranks context, and queries a language model via an interactive CLI agent.

## Architecture / How It Works
1. **Ingestion** (`ingestion/pdf_parser.py`, `ingestion/chunker.py`): Extracts text from PDFs using PyMuPDF (`fitz`), splits into chunks, validates with `is_valid_chunk()`.
2. **Embedding** (`embeddings/embedder.py`): Generates vector embeddings via `embed_chunks()` using `sentence-transformers`.
3. **Storage** (`database/chroma_store.py`): Persists chunks and embeddings in ChromaDB via `store_chunks()`.
4. **Retrieval** (`retrieval/search.py`): Finds relevant chunks with `search_papers()` using ChromaDB and sentence-transformers.
5. **Reasoning** (`reasoning/context_ranker.py`, `reasoning/engine.py`): Ranks retrieved context with `rank_context()`, builds prompts via `build_prompt()`, queries an LLM through `ask_model()` and `reasoning_engine()`.
6. **Interface** (`rpe.py`): Interactive agent (`agent()`) with command completion, history, and helpers `show_sources()`, `show_help()` using `prompt_toolkit` and `rich`.

## Project Structure
```text
database/
  - chroma_store.py
embeddings/
  - embedder.py
ingestion/
  - chunker.py
  - pdf_parser.py
reasoning/
  - context_ranker.py
  - engine.py
retrieval/
  - search.py
main.py
rpe.py
README.md
readme.md
```

## Key Components
| Module | Key Symbols | Purpose |
|--------|-------------|---------|
| `main.py` | `ingest()` | Entry point for ingestion pipeline; wires parser, chunker, embedder, store |
| `rpe.py` | `agent()`, `show_sources()`, `show_help()` | Interactive CLI agent with completion, history, rich output |
| `reasoning/engine.py` | `ask_model()`, `build_prompt()`, `reasoning_engine()` | Prompt construction and LLM query logic |
| `reasoning/context_ranker.py` | `rank_context()` | Ranks retrieved chunks for relevance |
| `retrieval/search.py` | `search_papers()` | Vector similarity search over ChromaDB |
| `embeddings/embedder.py` | `embed_chunks()` | Sentence-transformer embedding generation |
| `database/chroma_store.py` | `store_chunks()` | ChromaDB persistence |
| `ingestion/pdf_parser.py` | `extract_text()`, `load_papers()` | PDF text extraction via PyMuPDF |
| `ingestion/chunker.py` | `is_valid_chunk()`, `chunk_text()` | Text chunking and validation |

## Technologies Used
- **Python** (9 modules)
- **ChromaDB** (`chromadb`) — vector storage
- **sentence-transformers** — text embeddings
- **PyMuPDF** (`fitz`) — PDF parsing
- **prompt_toolkit** — interactive CLI (completion, history, styling)
- **rich** — terminal formatting (markdown, panels, tables)
- **requests** — HTTP calls for LLM API

## Usage
```bash
# Ingest papers (place PDFs in expected location, then run)
python main.py

# Launch interactive agent
python rpe.py
```

## Notes / Limitations
- No configuration files detected; paths and model names likely hardcoded in modules.
- LLM endpoint and model specified inside `reasoning/engine.py` (`ask_model`).
- Two README files exist (`README.md`, `readme.md`); content not parsed.
- No test suite or CI configuration observed.