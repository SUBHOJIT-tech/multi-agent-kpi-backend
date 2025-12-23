from app.agents.base_agent import BaseAgent


class RecommendationAgent(BaseAgent):
    def analyze(self, data):
        return {
            "agent": self.name,
            "metric": "Recommendation",
            "value": "Optimize underperforming KPIs",
        }
