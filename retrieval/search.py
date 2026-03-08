import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("BAAI/bge-large-en")

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(name="research_papers")


def search_papers(query, n_results=10):

    query_embedding = model.encode(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )

    docs = results["documents"][0]
    meta = results["metadatas"][0]
    dist = results["distances"][0]

    return docs, meta, dist