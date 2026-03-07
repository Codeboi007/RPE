import chromadb

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="research_papers"
)


def store_chunks(chunks, embeddings, title):

    ids = []
    metadatas = []

    for i, chunk in enumerate(chunks):

        ids.append(f"{title}_{i}")

        metadatas.append({
            "paper": title,
            "chunk": i
        })

    collection.add(
        documents=chunks,
        embeddings=embeddings.tolist(),
        ids=ids,
        metadatas=metadatas
    )