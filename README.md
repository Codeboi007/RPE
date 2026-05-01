# Overview
This repository contains a system for ingesting, processing, and reasoning over documents. It leverages embeddings, a vector database, and a reasoning engine to provide insights and answers based on the ingested content.

# Architecture / How It Works
- **Ingestion**: The system ingests documents, primarily PDFs, and processes them into chunks. These chunks are then embedded and stored in a vector database.
- **Reasoning**: The reasoning engine retrieves relevant chunks from the database, ranks them based on context, and generates responses based on the ranked context.
- **Retrieval**: The retrieval module handles searching through the stored embeddings to find the most relevant chunks for a given query.

# Project Structure
```
database/
  - chroma_store.py
embeddings/
  - embedder.py
ingestion/
  - chunker.py
reasoning/
  - context_ranker.py
  - engine.py
retrieval/
  - search.py
- main.py
- rpe.py
- README.md
- readme.md
```

# Key Components
- **`main.py`**: Contains the `ingest()` function, which orchestrates the ingestion process.
- **`rpe.py`**: Provides user interaction functions `agent()`, `show_sources()`, and `show_help()`.
- **`reasoning/engine.py`**: Handles the core reasoning logic with functions `ask_model()`, `build_prompt()`, and `reasoning_engine()`.
- **`retrieval/search.py`**: Manages the search functionality with `search_papers()`.
- **`database/chroma_store.py`**: Manages storage of document chunks with `store_chunks()`.
- **`embeddings/embedder.py`**: Handles embedding of document chunks with `embed_chunks()`.
- **`ingestion/chunker.py`**: Processes documents into chunks with `is_valid_chunk()`.

# Technologies Used
- **Python**: Used for all code files.
- **ChromaDB**: For vector database operations.
- **Sentence Transformers**: For generating embeddings.
- **Requests**: For making HTTP requests in the reasoning engine.

# Usage
```bash
python main.py
```

# Notes / Limitations
- **Lack of Modularization**: The `main.py` and `rpe.py` files contain significant functionality without clear separation into smaller, reusable modules.
- **Tight Coupling**: The `main.py` file directly depends on multiple modules, which could lead to tight coupling and make the system harder to maintain.
- **Critical Modules**: `reasoning/engine.py` and `retrieval/search.py` are critical due to their roles in core reasoning and search functionalities, respectively.