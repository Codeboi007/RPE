# Repository

## Overview
Generates repository documentation from parsed source.

Project type: Unknown

Parsed surface: **10 files** · **18 functions** · **0 classes**

## Architecture / How It Works
The system consists of several modules:
- **ingestion**: `ingestion/chunker.py`, `ingestion/pdf_parser.py` are responsible for text processing and paper loading.
- **docs**: `readme.md` is used to generate repository documentation.

## Project Structure
```text
database/
  - database/chroma_store.py
embeddings/
  - embeddings/embedder.py
ingestion/
  - ingestion/chunker.py
  - ingestion/pdf_parser.py
reasoning/
  - reasoning/context_ranker.py
  - reasoning/engine.py
retrieval/
  - retrieval/search.py
root/
```

## Key Components
- **`rpe.py`**: 
  - symbols `agent()`, `show_sources()`, `show_help()`
  - imports prompt_toolkit, prompt_toolkit.completion, prompt_toolkit.history, prompt_toolkit.styles, reasoning.engine, retrieval.search, rich.console, rich.markdown, rich.panel, rich.table, sys, time
- **`reasoning/engine.py`**: 
  - symbols `ask_model()`, `build_prompt()`, `reasoning_engine()`
  - imports reasoning.context_ranker, requests
- **`main.py`**: 
  - symbols `ingest()`
  - imports database.chroma_store, embeddings.embedder, ingestion.chunker, ingestion.pdf_parser
- **`ingestion/pdf_parser.py`**: 
  - symbols `extract_text()`, `load_papers()`
  - imports fitz, re
- **`retrieval/search.py`**: 
  - symbols `search_papers()`
  - imports chromadb, sentence_transformers
- **`ingestion/chunker.py`**: 
  - symbols `is_valid_chunk()`, `chunk_text()`
  - imports none
- **`database/chroma_store.py`**: 
  - symbols `store_chunks()`
  - imports chromadb
- **`embeddings/embedder.py`**: 
  - symbols `embed_chunks()`
  - imports sentence_transformers
- **`reasoning/context_ranker.py`**: 
  - symbols `rank_context()`
  - imports none
- **`readme.md`**: 
  - no detected symbols
  - imports none

## Technologies Used
- **py**: 9 file(s)
- **md**: 1 file(s)
- **requests**

## Usage
```bash
python main.py
```

## Notes / Limitations
- The system has high coupling between modules, as indicated by the architectural risks.
- The system has complexity in UI/UX, as indicated by the architectural risks.