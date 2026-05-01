# Overview
This repository contains a system for ingesting PDF documents, storing them, and reasoning over their contents. The system is structured to handle document ingestion, chunking, embedding, and querying.

# Architecture / How It Works
- **Ingestion**: The system ingests PDF documents using `ingestion/pdf_parser.py` to extract text and `ingestion/chunker.py` to split the text into manageable chunks.
- **Storage**: Chunks are stored using `database/chroma_store.py`, which leverages ChromaDB for efficient storage and retrieval.
- **Embedding**: Text chunks are embedded using `embeddings/embedder.py` with Sentence Transformers to create vector representations.
- **Reasoning**: The system reasons over the stored and embedded documents using `reasoning/engine.py`, which interacts with the stored data to answer queries.

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
- **`rpe.py`**: Contains `agent()`, `show_sources()`, `show_help()`. Imports `prompt_toolkit`, `prompt_toolkit.completion`, `prompt_toolkit.history`, `prompt_toolkit.styles`.
- **`main.py`**: Contains `ingest()`. Imports `database.chroma_store`, `embeddings.embedder`, `ingestion.chunker`, `ingestion.pdf_parser`.
- **`ingestion/pdf_parser.py`**: Contains `extract_text()`, `load_papers()`. Imports `fitz`, `re`.
- **`ingestion/chunker.py`**: Contains `is_valid_chunk()`, `chunk_text()`.
- **`database/chroma_store.py`**: Contains `store_chunks()`. Imports `chromadb`.
- **`embeddings/embedder.py`**: Contains `embed_chunks()`. Imports `sentence_transformers`.
- **`reasoning/engine.py`**: Contains `ask_model()`, `build_prompt()`, `reasoning_engine()`. Imports `reasoning.context_ranker`, `requests`.
- **`reasoning/context_ranker.py`**: Contains `rank_context()`.
- **`README.md`**: Contains `extracts`, `stores`.

# Technologies Used
- **Python**: 9 files
- **Markdown**: 2 files
- **Libraries**: `chromadb`, `sentence