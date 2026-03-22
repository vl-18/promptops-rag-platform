import json
import time
from evaluation.prompts import relevance_prompt, faithfulness_prompt
from config.settings import settings
import random

class Evaluator:
    def __init__(self, llm):
        self.llm = llm   # reuse your existing LLM client

    def _call_judge(self, prompt):
        response = self.llm.generate(prompt, temperature=0)

        try:
            return json.loads(response)
        except:
            return {"error": "Invalid JSON", "raw": response}

    def evaluate_relevance(self, query, response):
        prompt = relevance_prompt(query, response)
        result = self._call_judge(prompt)

        return result.get("relevance", None), result.get("reason", "")

    def evaluate_faithfulness(self, query, context, response):
        prompt = faithfulness_prompt(query, context, response)
        result = self._call_judge(prompt)

        return result.get("faithfulness", None), result.get("reason", "")

    
    def evaluate_all(self, query, context, response, latency, tokens):

        # DEMO MODE → return fake metrics
        if settings.DEMO_MODE:
            return {
                "relevance": round(random.uniform(0.7, 0.95), 2),
                "faithfulness": round(random.uniform(0.7, 0.95), 2),
                "latency": latency,
                "tokens": tokens,
                "details": {
                    "relevance_reason": "Mocked (relevance) evaluation in demo mode.",
                    "faithfulness_reason": "Mocked (faithfulness) evaluation in demo mode."
                }
            }

        # REAL MODE → actual evaluation
        relevance, rel_reason = self.evaluate_relevance(query, response)
        faithfulness, faith_reason = self.evaluate_faithfulness(query, context, response)

        return {
            "relevance": relevance,
            "faithfulness": faithfulness,
            "latency": latency,
            "tokens": tokens,
            "details": {
                "relevance_reason": rel_reason,
                "faithfulness_reason": faith_reason
            }
        }