# Overview
This repository contains a system for ingesting PDF documents, storing them, and providing reasoning capabilities over the ingested data. The system is structured into several modules for ingestion, reasoning, and storage.

# Architecture / How It Works
- **Ingestion**: The ingestion process involves parsing PDF documents to extract text and then chunking the text into manageable pieces. This is handled by `ingestion/pdf_parser.py` and `ingestion/chunker.py`.
- **Reasoning**: The reasoning process involves querying the ingested data and providing answers based on the context. This is managed by `reasoning/engine.py` and `reasoning/context_ranker.py`.
- **Storage**: The storage component handles the storage of text chunks in a database. This is facilitated by `database/chroma_store.py`.

# Project Structure
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
```

# Key Components
- **`rpe.py`**: Contains functions `agent()`, `show_sources()`, `show_help()`. Imports `prompt_toolkit`, `prompt_toolkit.completion`, `prompt_toolkit.history`, `prompt_toolkit.styles`.
- **`reasoning/engine.py`**: Contains functions `ask_model()`, `build_prompt()`, `reasoning_engine()`. Imports `reasoning.context_ranker`, `requests`.
- **`main.py`**: Contains function `ingest()`. Imports `database.chroma_store`, `embeddings.embedder`, `ingestion.chunker`, `ingestion.pdf_parser`.
- **`ingestion/pdf_parser.py`**: Contains functions `extract_text()`, `load_papers()`. Imports `fitz`, `re`.
- **`ingestion/chunker.py`**: Contains functions `is_valid_chunk()`, `chunk_text()`. No imports.
- **`database/chroma_store.py`**: Contains function `store_chunks()`. Imports `chromadb`.
- **`reasoning/context_ranker.py`**: Contains no functions. No imports.

# Technologies Used
- **Python**: 9 files.
- **Markdown**: 2 files.
- **Libraries**: `chromadb`, `fitz`, `prompt_toolkit`, `re`, `requests`, `rich`, `sentence_transformers`.

# Usage
```bash
python main.py
```

# Notes / Limitations
- **High Dependency on External Libraries**: `rpe.py` has a high dependency on external libraries, which could lead to maintenance issues if these libraries are deprecated or undergo significant changes.
- **Tight Coupling**: `main.py` has a tight coupling between ingestion components (`pdf_parser`, `chunker`), which could make it difficult to replace or modify these components in the future.