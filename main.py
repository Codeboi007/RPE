from ingestion.pdf_parser import load_papers
from ingestion.chunker import chunk_text
from embeddings.embedder import embed_chunks
from database.chroma_store import store_chunks


def ingest():

    papers = load_papers()

    for paper in papers:

        chunks = chunk_text(paper["text"])

        embeddings = embed_chunks(chunks)

        store_chunks(chunks, embeddings, paper["title"])

        print("Indexed:", paper["title"])


if __name__ == "__main__":

    ingest()