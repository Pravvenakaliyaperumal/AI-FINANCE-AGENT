from fastapi import FastAPI
from pydantic import BaseModel
from agents.router import AgentRouter

app = FastAPI(title="AI Finance Agent API", version="1.0")

# Initialize the router (our agent system)
router = AgentRouter()

class QueryRequest(BaseModel):
    query: str

@app.get("/")
def root():
    return {"message": "AI Finance Agent is running 🚀"}

@app.post("/query")
def handle_query(req: QueryRequest):
    response = router.route(req.query)
    return {"user_query": req.query, "ai_response": response}
