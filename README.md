# Repository

## Overview
This repository implements a system for PDF ingestion, embedding storage, and a reasoning engine for retrieval-augmented querying.

## Architecture / How It Works
The system operates through two primary pipelines:

1.  **Data Ingestion and Storage**: `main.py` coordinates the flow from `ingestion/pdf_parser.py` (text extraction) to `ingestion/chunker.py` (text segmentation), then through `embeddings/embedder.py` for vectorization, and finally to `database/chroma_store.py` for persistence.
2.  **Reasoning and Retrieval**: `rpe.py` serves as the interface, utilizing `reasoning/engine.py` to build prompts and query models. This process involves `retrieval/search.py` for document lookup and `reasoning/context_ranker.py` to prioritize retrieved context.

## Project Structure
```text
database/
  └── chroma_store.py
embeddings/
  └── embedder.py
ingestion/
  ├── chunker.py
  └── pdf_parser.py
reasoning/
  ├── context_ranker.py
  └── engine.py
retrieval/
  └── search.py
main.py
rpe.py
```

## Key Components
- **`rpe.py`**: User interface providing `agent()`, `show_sources()`, and `show_help()`.
- **`main.py`**: Entry point for data processing via the `ingest()` function.
- **`reasoning/engine.py`**: Core logic for model interaction via `reasoning_engine()`, `ask_model()`, and `build_prompt()`.
- **`ingestion/pdf_parser.py`**: Handles PDF loading and text extraction using `load_papers()` and `extract_text()`.
- **`ingestion/chunker.py`**: Manages text splitting via `chunk_text()` and `is_valid_chunk()`.
- **`retrieval/search.py`**: Performs vector search using `search_papers()`.
- **`database/chroma_store.py`**: Manages storage of vectors via `store_chunks()`.
- **`embeddings/embedder.py`**: Generates embeddings via `embed_chunks()`.
- **`reasoning/context_ranker.py`**: Ranks retrieved information using `rank_context()`.

## Technologies Used
- **Language**: Python
- **Libraries**: 
    - `chromadb`: Vector database storage and retrieval.
    - `sentence_transformers`: Embedding generation.
    - `fitz` (PyMuPDF): PDF text extraction.
    - `prompt_toolkit`: CLI interface and history management.
    - `rich`: Console formatting and markdown rendering.
    - `requests`: External model API communication.

## Usage
Data ingestion is initiated via:
```bash
python main.py
```