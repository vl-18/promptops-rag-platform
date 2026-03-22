from openai import OpenAI
from config.settings import settings
import time


class LLMClient:

    def __init__(self):

        if not settings.DEMO_MODE:
            self.client = OpenAI(api_key=settings.OPENAI_API_KEY)

        self.model = settings.MODEL_NAME


    def generate(self, prompt: str, temperature: float = 0.2):

        start_time = time.time()

        # DEMO MODE (no API call)
        # if settings.DEMO_MODE:
        #     response_text = (
        #         "This is a demo response generated without calling the LLM API. "
        #         "In a real system, the model would generate an answer based on "
        #         "the retrieved policy context."
        #     )

        if settings.DEMO_MODE:

            if "craft" in prompt:
                response_text = ("Structured policy-based response (CRAFT-style)."
                                 "In a real system, the model would generate an answer based on"
                                "the retrieved policy context")
            else:
                response_text = ("Detailed explanatory response (CRISPE-style)."
                                "In a real system, the model would generate an answer based on"
                                "the retrieved policy context")

            latency = time.time() - start_time

            return {
                "response": response_text,
                "tokens": 0,
                "latency": latency
            }

        # REAL MODE
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=temperature
        )

        response_text = response.choices[0].message.content

        # Token usage (important!)
        tokens = response.usage.total_tokens if response.usage else 0

        latency = time.time() - start_time

        return {
            "response": response_text,
            "tokens": tokens,
            "latency": latency
        }