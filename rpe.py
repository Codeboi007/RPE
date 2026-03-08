from retrieval.search import search_papers
from reasoning.engine import reasoning_engine

def agent(query):

    print("\n[1] Searching vector database...")

    docs, meta, dist = search_papers(query)

    print("[2] Retrieved chunks:", len(docs))

    print("[3] Starting reasoning engine...")

    answer = reasoning_engine(query, docs, meta, dist)

    print("[4] Reasoning finished")

    return answer


def main():

    print("\nResearch Paper Engine Ready\n")

    while True:

        query = input("Ask me anything-->")

        if query.lower() in ["exit", "quit"]:
            break

        answer = agent(query)

        print("\nAnswer:\n")
        print(answer)
        print("\n")


if __name__ == "__main__":
    main()