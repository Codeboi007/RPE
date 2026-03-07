from sentence_transformers import SentenceTransformer

model = SentenceTransformer("BAAI/bge-large-en")

def embed_chunks(chunks):

    embeddings = model.encode(chunks)

    return embeddings