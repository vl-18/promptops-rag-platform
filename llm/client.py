from openai import OpenAI
from config.settings import settings


class LLMClient:

    def __init__(self):

        if not settings.DEMO_MODE:
            self.client = OpenAI(api_key=settings.OPENAI_API_KEY)

        self.model = settings.MODEL_NAME


    def generate(self, prompt: str):

        # DEMO MODE (no API call)
        if settings.DEMO_MODE:

            return (
                "This is a demo response generated without calling the LLM API. "
                "In a real system, the model would generate an answer based on "
                "the retrieved policy context."
            )

        # REAL MODE
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.2
        )

        return response.choices[0].message.content