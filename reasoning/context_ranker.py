def rank_context(docs, meta, distances, top_k=5):

    print("[Context] Ranking retrieved chunks...")

    items = list(zip(docs, meta, distances))
    items.sort(key=lambda x: x[2])

    ranked = items[:top_k]

    print("[Context] Selected top", top_k, "chunks")

    context = []

    for doc, m, d in ranked:

        entry = f"[Paper: {m['paper']}]\n{doc}"
        context.append(entry)

    return "\n\n".join(context)