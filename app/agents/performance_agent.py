from app.agents.base_agent import BaseAgent


class PerformanceAgent(BaseAgent):
    def analyze(self, data):
        efficiency = data.mean().mean()
        return {
            "agent": self.name,
            "metric": "Efficiency",
            "value": round(float(efficiency), 2),
        }
