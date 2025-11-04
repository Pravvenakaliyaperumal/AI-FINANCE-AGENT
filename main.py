from agents.router import AgentRouter

if __name__ == "__main__":
    print("🧩 Multi-Agent Finance System Ready!")
    router = AgentRouter()

    while True:
        query = input("\nUser: ")
        if query.lower() in ["exit", "quit"]:
            print("Goodbye! 👋")
            break

        response = router.route(query)
        print("\n🤖 AI System:", response)
