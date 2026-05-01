# Overview
This repository contains a system for ingesting, processing, and reasoning over documents. It includes functionalities for document ingestion, embedding, retrieval, and reasoning.

# Architecture / How It Works
- **Ingestion**: Handles the parsing and chunking of documents. Modules include `ingestion/chunker.py` and `ingestion/pdf_parser.py`.
- **Embeddings**: Converts text chunks into embeddings using `embeddings/embedder.py`.
- **Database**: Manages the storage of embeddings with `database/chroma_store.py`.
- **Retrieval**: Searches for relevant documents based on queries using `retrieval/search.py`.
- **Reasoning**: Processes and ranks the context of retrieved documents using `reasoning/engine.py` and `reasoning/context_ranker.py`.
- **User Interface**: Provides a command-line interface for interaction, managed by `rpe.py`.

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
- **`main.py`**: Contains the `ingest()` function, which orchestrates the ingestion process. Imports `database.chroma_store`, `embeddings.embedder`, `ingestion.chunker`, and `ingestion.pdf_parser`.
- **`rpe.py`**: Provides user interaction functionalities through `agent()`, `show_sources()`, and `show_help()`. Imports `prompt_toolkit` and related modules for UI components.
- **`reasoning/engine.py`**: Handles the core reasoning process with `ask_model()`, `build_prompt()`, and `reasoning_engine()`. Imports `reasoning.context_ranker` and `requests`.
- **`retrieval/search.py`**: Manages the search functionality with `search_papers()`. Imports `chromadb` and `sentence_transformers`.
- **`embeddings/embedder.py`**: Converts text into embeddings using `embed_chunks()`. Imports `sentence_transformers`.
- **`database/chroma_store.py`**: Manages the storage of embeddings with `store_chunks()`. Imports `chromadb`.
- **`ingestion/chunker.py`**: Handles the chunking of text with `is_valid_chunk()`. No additional imports.
- **`reasoning/context_ranker.py`**: Ranks the context of retrieved documents with `rank_context()`. No additional imports.
- **`README.md`**: Contains documentation and mentions the `handles` class. No additional imports.

# Technologies Used
- **Python**: 9 files
- **Markdown**: 2 files
- **External Libraries**: `chromadb`, `sentence_transformers`, `requests`, `prompt_toolkit`, `rich`

# Usage
```bash
python main.py
```

# Notes / Limitations
- **High Coupling**: `main.py` is tightly coupled with multiple modules (`database`, `embeddings`, `ingestion`), which may introduce maintenance challenges.
- **External Dependencies**: `rpe.py` relies on external libraries (`prompt_toolkit`, `rich`) for UI components, which could introduce maintenance challenges.
- **Critical Dependencies**: `reasoning/engine.py` and `retrieval/search.py` have high dependencies on both internal and external libraries, critical for their functionality.