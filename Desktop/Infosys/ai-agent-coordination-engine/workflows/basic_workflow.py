from typing import TypedDict

from langgraph.graph import StateGraph, START, END

from agents.business_agent import BusinessAnalysisAgent
from agents.recommendation_agent import RecommendationAgent


class AgentState(TypedDict):
    request: str
    analysis: str
    recommendation: str


business_agent = BusinessAnalysisAgent()
recommendation_agent = RecommendationAgent()


def business_analysis_node(state: AgentState):
    analysis = business_agent.analyze(state["request"])

    return {
        "analysis": analysis
    }


def recommendation_node(state: AgentState):
    recommendation = recommendation_agent.recommend(
        state["analysis"]
    )

    return {
        "recommendation": recommendation
    }


graph = StateGraph(AgentState)

graph.add_node(
    "business_analysis",
    business_analysis_node
)

graph.add_node(
    "recommendation",
    recommendation_node
)

graph.add_edge(
    START,
    "business_analysis"
)

graph.add_edge(
    "business_analysis",
    "recommendation"
)

graph.add_edge(
    "recommendation",
    END
)

workflow = graph.compile()