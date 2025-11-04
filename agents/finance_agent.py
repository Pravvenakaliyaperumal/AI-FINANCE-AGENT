import json

class FinanceAgent:
    def __init__(self, data_path="data/transactions.json"):
        with open(data_path, "r") as f:
            self.transactions = json.load(f)

    def analyze_spending(self, month: str):
        """Analyze total spend and refunds for a given month (e.g., '2024-10')."""
        total_spent = 0
        refunds = 0
        refund_amount = 0

        for t in self.transactions:
            if t["date"].startswith(month):
                if t["type"] == "purchase":
                    total_spent += t["amount"]
                elif t["type"] == "refund":
                    refunds += 1
                    refund_amount += t["amount"]

        return {
            "month": month,
            "total_spent": total_spent,
            "refunds": refunds,
            "refund_amount": refund_amount
        }

    def respond(self, query: str):
        """Simple LLM-like reasoning stub."""
        if "october" in query.lower() or "10" in query:
            summary = self.analyze_spending("2024-10")
            return (
                f"In {summary['month']}, you spent ${summary['total_spent']} "
                f"and received {summary['refunds']} refunds totaling ${summary['refund_amount']}."
            )
        return "I can analyze spending by month, e.g., 'Show my October spending.'"
