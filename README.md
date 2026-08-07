# Repository

## Overview
Generates repository documentation from parsed source.

Project type: Unknown

Parsed surface: **11 files** · **18 functions** · **0 classes**

## Architecture / How It Works
- **ingestion**: `ingestion/chunker.py`, `ingestion/pdf_parser.py`
- **docs**: `README.md`, `readme.md`

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
- **`rpe.py`**: symbols `agent()`, `show_sources()`, `show_help()`; imports prompt_toolkit, prompt_toolkit.completion, prompt_toolkit.history, prompt_toolkit.styles.
- **`reasoning/engine.py`**: symbols `ask_model()`, `build_prompt()`, `reasoning_engine()`; imports reasoning.context_ranker, requests.
- **`main.py`**: symbols `ingest()`; imports database.chroma_store, embeddings.embedder, ingestion.chunker, ingestion.pdf_parser.
- **`ingestion/pdf_parser.py`**: symbols `extract_text()`, `load_papers()`; imports fitz, re.
- **`retrieval/search.py`**: symbols `search_papers()`; imports chromadb, sentence_transformers.
- **`ingestion/chunker.py`**: symbols `is_valid_chunk()`, `chunk_text()`; imports none.
- **`database/chroma_store.py`**: symbols `store_chunks()`; imports chromadb.
- **`embeddings/embedder.py`**: symbols `embed_chunks()`; imports sentence_transformers.
- **`reasoning/context_ranker.py`**: symbols `rank_context()`; imports none.
- **`README.md`**: symbols no detected symbols; imports none.
- **`readme.md`**: symbols no detected symbols; imports none.

## Technologies Used
- **py**: 9 file(s)
- **md**: 2 file(s)
- **requests**

## Usage
```bash
python main.py
```

