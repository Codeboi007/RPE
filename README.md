# Repository
## Overview
This repository contains a collection of Python scripts and modules for ingesting, processing, and reasoning about data.

## Architecture / How It Works
The repository is organized into several components:

* **ingestion**: responsible for loading and processing data, implemented in `ingestion/pdf_parser.py` and `ingestion/chunker.py`.
* **reasoning**: responsible for analyzing and reasoning about the data, implemented in `reasoning/engine.py` and `reasoning/context_ranker.py`.
* **retrieval**: responsible for searching and retrieving data, implemented in `retrieval/search.py`.
* **embeddings**: responsible for generating embeddings for the data, implemented in `embeddings/embedder.py`.

## Project Structure
The repository is organized into the following directories:

* `ingestion/`: contains scripts for ingesting and processing data.
* `reasoning/`: contains scripts for analyzing and reasoning about the data.
* `retrieval/`: contains scripts for searching and retrieving data.
* `embeddings/`: contains scripts for generating embeddings for the data.

## Key Components
* **`rpe.py`**: contains functions for interacting with the repository, including `agent()`, `show_sources()`, and `show_help()`.
* **`main.py`**: contains the main entry point for the repository, including the `ingest()` function.
* **`ingestion/pdf_parser.py`**: contains functions for parsing and extracting text from PDFs, including `extract_text()` and `load_papers()`.
* **`ingestion/chunker.py`**: contains functions for chunking text, including `is_valid_chunk()` and `chunk_text()`.
* **`reasoning/engine.py`**: contains functions for reasoning about the data, including `ask_model()`, `build_prompt()`, and `reasoning_engine()`.
* **`retrieval/search.py`**: contains functions for searching and retrieving data, including `search_papers()`.

## Technologies Used
* **Python**: used for implementing the repository's functionality.
* **ChromaDB**: used for storing and retrieving data.
* **Sentence Transformers**: used for generating embeddings for the data.
* **Fitz**: used for parsing and extracting text from PDFs.
* **Requests**: used for making HTTP requests.

## Usage
To run the repository, execute the following command:
```bash
python main.py
```
Note: This command assumes that the repository is installed and configured correctly.