from app.agents.base_agent import BaseAgent


class RiskAgent(BaseAgent):
    def analyze(self, data):
        volatility = data.std().mean()
        level = "High" if volatility > 10 else "Low"
        return {
            "agent": self.name,
            "metric": "Risk",
            "value": level,
        }
