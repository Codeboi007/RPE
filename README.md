# Repository

## Overview
A system for ingesting PDF documents, storing them into a vector database, and performing reasoning over the stored content.

## Architecture / How It Works
The system follows a pipeline from document ingestion to reasoning:
1. **Ingestion**: PDFs are loaded and text is extracted via `ingestion/pdf_parser.py`, then split into segments using `ingestion/chunker.py`.
2. **Storage**: Text chunks are processed by `embeddings/embedder.py` and stored in a vector database via `database/chroma_store.py`.
3. **Reasoning**: Queries are processed by `reasoning/engine.py`, which utilizes `reasoning/context_ranker.py` to refine context before generating a response.
4. **Interface**: `rpe.py` provides an agent interface for user interaction.

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
```

## Key Components
- **`main.py`**: Entry point for the ingestion process via the `ingest()` function.
- **`rpe.py`**: Implements the user interface with `agent()`, `show_sources()`, and `show_help()`.
- **`reasoning/engine.py`**: Handles model interaction and prompt construction via `reasoning_engine()`, `build_prompt()`, and `ask_model()`.
- **`ingestion/pdf_parser.py`**: Handles document loading and text extraction via `load_papers()` and `extract_text()`.
- **`ingestion/chunker.py`**: Manages text segmentation via `chunk_text()` and `is_valid_chunk()`.
- **`database/chroma_store.py`**: Manages data persistence via `store_chunks()`.
- **`retrieval/search.py`**: Implements document retrieval via `search_papers()`.

## Technologies Used
- **Language**: Python
- **Libraries**: 
  - `chromadb`: Vector database storage.
  - `sentence_transformers`: Text embeddings.
  - `fitz` (PyMuPDF): PDF text extraction.
  - `prompt_toolkit`: Command-line interface components.
  - `rich`: Console formatting and output.
  - `requests`: HTTP requests for model interaction.