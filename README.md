# Repository

## Overview
A system for ingesting PDF documents, storing them in a vector database, and performing reasoning over the content via a model-driven engine.

## Architecture / How It Works
The system follows a pipeline from document ingestion to reasoning:
1. **Ingestion**: PDFs are loaded and text is extracted, then split into validated chunks.
2. **Storage**: Chunks are embedded and stored in a Chroma database.
3. **Reasoning**: A reasoning engine builds prompts and queries a model, utilizing a context ranker to process retrieved information.
4. **Interface**: An agent interface provides interaction, help, and source tracking.

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
- **`rpe.py`**: Provides the user interface via `agent()`, `show_sources()`, and `show_help()`.
- **`main.py`**: Orchestrates the ingestion process via `ingest()`.
- **`reasoning/engine.py`**: Handles model interaction and prompt construction through `reasoning_engine()`, `ask_model()`, and `build_prompt()`.
- **`ingestion/pdf_parser.py`**: Extracts text from PDF files using `load_papers()` and `extract_text()`.
- **`ingestion/chunker.py`**: Processes text into segments using `chunk_text()` and `is_valid_chunk()`.
- **`database/chroma_store.py`**: Manages data persistence via `store_chunks()`.
- **`embeddings/embedder.py`**: Generates vector representations of text chunks.
- **`retrieval/search.py`**: Performs searches across the stored papers.
- **`reasoning/context_ranker.py`**: Ranks retrieved context for the reasoning engine.

## Technologies Used
- **Language**: Python
- **Libraries**: 
  - `chromadb` (Vector database)
  - `sentence_transformers` (Embeddings)
  - `fitz` (PDF processing)
  - `prompt_toolkit` (CLI interface)
  - `rich` (Console formatting)
  - `requests` (HTTP requests)

## Usage
```bash
python main.py
```