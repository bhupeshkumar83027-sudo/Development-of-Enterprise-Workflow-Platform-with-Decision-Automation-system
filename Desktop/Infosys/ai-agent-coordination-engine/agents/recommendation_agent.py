from agents.llm import get_llm
from prompts.recommendation_prompt import recommendation_prompt


class RecommendationAgent:

    def __init__(self):
        self.llm = get_llm()

    def recommend(self, analysis: str) -> str:

        prompt = recommendation_prompt.format(
            analysis=analysis
        )

        response = self.llm.invoke(prompt)

        return response.content