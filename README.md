# Overview
This repository contains a system for ingesting PDF documents, processing their content, and answering queries based on the ingested data. The system is structured into several modules that handle different aspects of the process, including ingestion, reasoning, and storage.

# Architecture / How It Works
- **Ingestion**: The `ingestion/pdf_parser.py` module extracts text from PDF files, while `ingestion/chunker.py` splits the text into manageable chunks.
- **Storage**: The `database/chroma_store.py` module stores these chunks in a database using ChromaDB.
- **Reasoning**: The `reasoning/engine.py` module processes user queries, retrieves relevant context, and generates responses. It interacts with the `retrieval/search.py` module to find the most relevant information.

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
- **`rpe.py`**: Contains functions `agent()`, `show_sources()`, `show_help()`. Imports `prompt_toolkit`, `prompt_toolkit.completion`, `prompt_toolkit.history`, `prompt_toolkit.styles`, `reasoning.engine`, `retrieval.search`, `rich`.
- **`main.py`**: Contains function `ingest()`. Imports `database.chroma_store`, `embeddings.embedder`, `ingestion.chunker`, `ingestion.pdf_parser`.
- **`database/chroma_store.py`**: Contains function `store_chunks()`. Imports `chromadb`.
- **`ingestion/pdf_parser.py`**: Contains functions `extract_text()`, `load_papers()`. Imports `fitz`, `re`.
- **`ingestion/chunker.py`**: Contains functions `is_valid_chunk()`, `chunk_text()`.
- **`reasoning/engine.py`**: Contains functions `ask_model()`, `build_prompt()`, `reasoning_engine()`. Imports `reasoning.context_ranker`, `requests`.
- **`reasoning/context_ranker.py`**: Contains no functions. Imports none.
- **`README.md`**: Contains no functions. Imports none.

# Technologies Used
- **Python**: 9 files
- **Markdown**: 2 files
- **Libraries**: `chromadb`, `sentence_transformers`, `prompt_toolkit`, `rich