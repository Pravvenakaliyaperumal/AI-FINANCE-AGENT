from agents.finance_agent import FinanceAgent
from agents.order_agent import OrderAgent

class AgentRouter:
    def __init__(self):
        self.finance_agent = FinanceAgent()
        self.order_agent = OrderAgent()

    def route(self, query: str):
        """Simple intent detection (mock version)."""
        q = query.lower()
        if any(word in q for word in ["spend", "refund", "total", "month", "finance"]):
            return self.finance_agent.respond(query)
        elif any(word in q for word in ["order", "purchase", "recent", "bought"]):
            return self.order_agent.respond(query)
        else:
            return (
                "I'm not sure which area that falls under 🤔.\n"
                "You can ask things like:\n"
                "- 'Show my October spending'\n"
                "- 'List my recent orders'"
            )
