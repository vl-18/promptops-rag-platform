from prompts.base_prompt import BasePrompt


class CraftPrompt(BasePrompt, framework_name="craft"):

    def build_prompt(self, query, context):

        prompt = f"""### craft framework
Context:
{context}

Role:
You are a company policy assistant helping employees understand internal policies.

Action:
Answer the user question using only the provided context.

Format:
Provide a clear and concise explanation.

Tone:
Professional and helpful.

User Question:
{query}

Answer:
"""

        return prompt