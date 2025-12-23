class BaseAgent:
    def __init__(self, name: str):
        self.name = name

    def analyze(self, data):
        raise NotImplementedError("Subclasses must implement analyze()")
