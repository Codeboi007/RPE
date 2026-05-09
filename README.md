# README

## Overview
This repository contains a system for ingesting PDF documents, processing their content, and providing reasoning capabilities based on the ingested data. The system is structured into several modules that handle different aspects of the workflow, from document ingestion to reasoning and response generation.

## Architecture / How It Works
- **Ingestion**: Handles the parsing and chunking of PDF documents.
  - `ingestion/pdf_parser.py`: Extracts text from PDFs and loads them.
  - `ingestion/chunker.py`: Validates and chunks the extracted text into manageable pieces.
- **Database**: Manages the storage of document chunks.
  - `database/chroma_store.py`: Stores chunks using ChromaDB.
- **Embeddings**: Generates embeddings for the document chunks.
  - `embeddings/embedder.py`: Uses Sentence Transformers to create embeddings.
- **Reasoning**: Provides reasoning capabilities based on the ingested data.
  - `reasoning/engine.py`: Manages the reasoning process, including building prompts and asking a model.
  - `reasoning/context_ranker.py`: Ranks the context for better reasoning accuracy.

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
main.py
rpe.py
README.md
readme.md
```

## Key Components
- **`rpe.py`**: Contains functions `agent()`, `show_sources()`, `show_help()`. Imports `prompt_toolkit` for interactive command-line interface.
- **`main.py`**: Contains function `ingest()`. Imports modules for database storage, embedding, and ingestion.
- **`ingestion/pdf_parser.py`**: Contains functions `extract_text()`, `load_papers()`. Imports `fitz` for PDF handling and `re` for regular expressions.
- **`ingestion/chunker.py`**: Contains functions `is_valid_chunk()`, `chunk_text()`. No external imports.
- **`database/chroma_store.py`**: Contains function `store_chunks()`. Imports `chromadb` for database operations.
- **`embeddings/embedder.py`**: Contains function `embed_chunks()`. Imports `sentence_transformers` for embedding generation.
- **`reasoning/engine.py`**: Contains functions `ask_model()`, `build_prompt()`, `reasoning_engine()`. Imports