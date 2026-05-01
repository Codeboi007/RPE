# Overview
This repository contains a system for ingesting PDF documents, processing their content, and providing reasoning capabilities based on the ingested data. The system is structured into several modules that handle different aspects of the process, including ingestion, reasoning, and storage.

# Architecture / How It Works
- **Ingestion**: The ingestion process is handled by `ingestion/pdf_parser.py` and `ingestion/chunker.py`. These modules are responsible for parsing PDF files and chunking the text into manageable pieces for further processing.
- **Reasoning**: The reasoning process is managed by `reasoning/engine.py` and `reasoning/context_ranker.py`. These modules are responsible for querying the stored data and retrieving relevant information based on user input.
- **Storage**: Data storage is managed by `database/chroma_store.py`, which handles the storage and retrieval of text chunks using ChromaDB.

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
main.py
rpe.py
README.md
readme.md
```

# Key Components
- **`rpe.py`**: Contains functions `agent()`, `show_sources()`, and `show_help()`. Imports `prompt_toolkit`, `prompt_toolkit.completion`, `prompt_toolkit.history`, `prompt_toolkit.styles`, `reasoning.engine`, `retrieval.search`, `rich`.
- **`reasoning/engine.py`**: Contains functions `ask_model()`, `build_prompt()`, and `reasoning_engine()`. Imports `reasoning.context_ranker`, `requests`, `sentence_transformers`.
- **`main.py`**: Contains function `ingest()`. Imports `database.chroma_store`, `embeddings.embedder`, `ingestion.chunker`, `ingestion.pdf_parser`.
- **`ingestion/pdf_parser.py`**: Contains functions `extract_text()` and `load_papers()`. Imports `fitz`, `re`.
- **`ingestion/chunker.py`**: Contains functions `is_valid_chunk()` and `chunk_text()`. No imports.
- **`database/chroma_store.py`**: Contains function `store_chunks()`. Imports `chromadb`.
- **`reasoning/context_ranker.py`**: Contains no functions. No imports.

# Technologies Used
- **Python**: 9 files
- **Markdown**: 2 files
- **Libraries**: `chromadb`, `fitz`, `prompt_toolkit`, `re`, `requests`, `rich`, `sentence_transformers`

# Usage
```bash
python main.py
```

# Notes / Limitations
- **High Dependency on External Libraries**: `rpe.py` has a high dependency on external libraries, which could lead to issues if these libraries undergo breaking changes.
- **Tightly Coupled Ingestion Process**: The ingestion process is tightly coupled with PDF files, making it difficult to extend support to other file formats without significant changes.