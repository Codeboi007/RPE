from retrieval.search import search_papers

query = "what is chacha20"

docs, meta = search_papers(query)

for i in range(len(docs)):

    print("\nResult", i+1)
    print("Paper:", meta[i]["paper"])
    print(docs[i][:500])