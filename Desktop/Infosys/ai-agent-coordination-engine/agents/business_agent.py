from agents.llm import get_llm
from prompts.business_prompt import business_prompt


class BusinessAnalysisAgent:

    def __init__(self):
        self.llm = get_llm()

    def analyze(self, business_request: str) -> str:

        prompt = business_prompt.format(
            business_request=business_request
        )

        response = self.llm.invoke(prompt)

        return response.content