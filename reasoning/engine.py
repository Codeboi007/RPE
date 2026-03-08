import requests
from reasoning.context_ranker import rank_context

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
MODEL = "qwen-rpe:latest"

def ask_model(prompt):

    print("[Model] Sending request to Ollama...")

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }

    r = requests.post(OLLAMA_URL, json=payload)

    print("[Model] Response received")

    return r.json()["response"]


def build_prompt(query, context):

    return f"""
You are a highly precise AI research assistant specialized in analyzing academic papers.

Your task is to answer the user's question using ONLY the research excerpts provided below.
Treat the excerpts as the sole source of truth.

-------------------------------------
RESEARCH EXCERPTS
-------------------------------------
{context}
-------------------------------------

USER QUESTION
-------------------------------------
{query}
-------------------------------------

OBJECTIVE
Determine what concept or mechanism the user is asking about and explain it clearly using ONLY the provided excerpts.

ASSUMPTIONS ABOUT THE USER
- The user understands machine learning and deep learning fundamentals.
- Explanations should therefore focus on the *research insight*, not beginner explanations.

INSTRUCTIONS

1. Carefully identify the main concept or mechanism asked in the question.
2. Search the research excerpts for passages relevant to that concept.
3. Extract the key ideas and explain them clearly and logically.
4. If multiple excerpts discuss different aspects of the concept, synthesize them into one explanation.
5. If figures, tables, equations, or diagrams are referenced in the excerpts, explicitly mention them so the reader can check the original paper.
6. Do NOT invent information that is not present in the excerpts.
7. If the excerpts do not contain enough information to fully answer the question, explicitly state what is missing.

STRICT RULES

- Use ONLY the provided excerpts as evidence.
- Do NOT speculate or introduce external knowledge.
- Do NOT fabricate figure numbers or citations.
- If a figure/table is mentioned, only reference it if it appears in the excerpts.
- If the excerpts contain conflicting information, acknowledge the conflict.

OUTPUT FORMAT

Concept:
Provide a concise definition of the concept or idea being asked about.

Explanation:
Explain the concept clearly using only the information contained in the excerpts.

Important details from the paper:
- Key mechanism or finding
- Important assumptions or design choices
- Experimental results or observations (if mentioned)

Figures or tables referenced in the excerpts:
- List any figures/tables/diagrams mentioned in the excerpts
- If none are mentioned, write: "No figures or tables referenced in the provided excerpts."

Limitations / Missing Information:
Explain what the excerpts do not provide if the answer cannot be fully derived.

Conclusion:
Provide a short summary of the main takeaway.
"""


def reasoning_engine(query, docs, meta, dist):

    print("[Engine] Ranking context")

    context = rank_context(docs, meta, dist)

    prompt = build_prompt(query, context)

    answers = []

    for i in range(3):

        print(f"[Engine] Reasoning attempt {i+1}/3")

        response = ask_model(prompt)

        answers.append(response)

    print("[Engine] Evaluating answers")

    best = max(answers, key=evaluate_answer)

    return best

def evaluate_answer(answer):

    score = 0

    if len(answer) > 150:
        score += 1

    if "conclusion" in answer.lower():
        score += 1

    if "method" in answer.lower():
        score += 1

    if "research" in answer.lower():
        score += 1

    return score