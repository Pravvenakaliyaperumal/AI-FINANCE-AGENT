import yaml
from agents.router import AgentRouter

def load_adk_config(path="config/adk_config.yaml"):
    with open(path, "r") as f:
        cfg = yaml.safe_load(f)
    print("✅ Loaded ADK manifest for:", cfg["project"])
    return cfg

if __name__ == "__main__":
    config = load_adk_config()
    print("🧩 Multi-Agent Finance System (ADK Compatible) Ready!")
    router = AgentRouter()

    while True:
        query = input("\nUser: ")
        if query.lower() in ["exit", "quit"]:
            print("Goodbye! 👋")
            break

        response = router.route(query)
        print("\n🤖 AI System:", response)
