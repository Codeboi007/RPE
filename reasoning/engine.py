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
You are an AI research assistant.

Use the research excerpts below to answer the question.

Research excerpts:
{context}

Question:
{query}

Provide:
- explanation
- key ideas
- limitations
- conclusion
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