# README.md

## Overview
This repository contains a system for ingesting PDF documents, storing them in a database, and providing reasoning capabilities based on the ingested content.

## Architecture / How It Works
- **Ingestion**: The system processes PDF files to extract text and chunk it into manageable pieces. These chunks are then stored in a database.
- **Reasoning**: User queries are processed through a reasoning engine that retrieves relevant context from the stored chunks and provides answers.

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
root/
  - main.py
  - rpe.py
```

## Key Components
- **`rpe.py`**: Contains functions `agent()`, `show_sources()`, `show_help()`. Imports `prompt_toolkit`, `prompt_toolkit.completion`, `prompt_toolkit.history`, `prompt_toolkit.styles`, `reasoning.engine`, `retrieval.search`, `rich`.
- **`reasoning/engine.py`**: Contains functions `ask_model()`, `build_prompt()`, `reasoning_engine()`. Imports `reasoning.context_ranker`, `requests`.
- **`main.py`**: Contains function `ingest()`. Imports `database.chroma_store`, `embeddings.embedder`, `ingestion.chunker`, `ingestion.pdf_parser`.
- **`ingestion/pdf_parser.py`**: Contains functions `extract_text()`, `load_papers()`. Imports `fitz`, `re`.
- **`ingestion/chunker.py`**: Contains functions `is_valid_chunk()`, `chunk_text()`. No imports.
- **`database/chroma_store.py`**: Contains function `store_chunks()`. Imports `chromadb`.
- **`embeddings/embedder.py`**: Contains function `embed_chunks()`. Imports `sentence_transformers`.
- **`reasoning/context_ranker.py`**: Contains function `rank_context()`. No imports.
- **`README.md`**: Documentation file. No symbols or imports.

## Technologies Used
- **Python**: 9 files
- **Markdown**: 2 files
- **Libraries**: `chromadb`, `fitz`, `prompt_toolkit`, `re`, `requests`, `rich`, `sentence_transformers`

## Usage
```bash
python main.py
```

## Notes / Limitations
- **High Dependency on External Libraries**: `rpe.py` has a high dependency on external libraries, which could lead to maintenance issues if these libraries are deprecated or undergo significant changes.
- **Tightly Coupled Ingestion Process**: The ingestion process in `main.py` is tightly coupled with the database and embedding functionalities, making it difficult to switch to a different database or embedding method.