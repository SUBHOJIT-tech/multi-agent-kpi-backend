from app.agents.performance_agent import PerformanceAgent
from app.agents.risk_agent import RiskAgent
from app.agents.recommendation_agent import RecommendationAgent


class KPIEngine:
    def __init__(self):
        self.agents = [
            PerformanceAgent("Performance Agent"),
            RiskAgent("Risk Agent"),
            RecommendationAgent("Recommendation Agent"),
        ]

    def run(self, data):
        results = []
        for agent in self.agents:
            results.append(agent.analyze(data))
        return results
