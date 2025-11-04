import json

class OrderAgent:
    def __init__(self, data_path="data/transactions.json"):
        with open(data_path, "r") as f:
            self.transactions = json.load(f)

    def get_recent_orders(self, limit=3):
        """Return recent purchase transactions."""
        purchases = [t for t in self.transactions if t["type"] == "purchase"]
        purchases.sort(key=lambda x: x["date"], reverse=True)
        return purchases[:limit]

    def respond(self, query: str):
        """Responds to queries related to orders."""
        if "order" in query.lower() or "recent" in query.lower():
            orders = self.get_recent_orders()
            summary = "\n".join([f"- {o['category']} (${o['amount']}) on {o['date']}" for o in orders])
            return f"Here are your recent orders:\n{summary}"
        return "I can show your recent orders or order history."
