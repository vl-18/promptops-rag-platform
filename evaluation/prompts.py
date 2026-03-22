def relevance_prompt(query, response):
    return f"""
You are an expert evaluator.

Evaluate how relevant the answer is to the question.

Question:
{query}

Answer:
{response}

Score relevance from 0 to 1:
- 1 = perfectly answers the question
- 0 = completely irrelevant

Return ONLY JSON:
{{
    "relevance": float,
    "reason": "short explanation"
}}
"""

def faithfulness_prompt(query, context, response):
    return f"""
You are an expert evaluator.

Evaluate whether the answer is supported by the given context.

Question:
{query}

Context:
{context}

Answer:
{response}

Score faithfulness from 0 to 1:
- 1 = fully supported by context
- 0 = completely hallucinated

Return ONLY JSON:
{{
    "faithfulness": float,
    "reason": "short explanation"
}}
"""