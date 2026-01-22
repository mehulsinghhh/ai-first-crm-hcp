from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from agent.graph import agent_app

app = FastAPI(title="AI-First CRM HCP Module")

# CORS (REQUIRED for frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/agent")
def run_agent(payload: dict):
    state = {
        "user_input": payload.get("input", ""),
        "interaction_id": None,
        "hcp_name": None,
        "structured_data": {},
        "summary": None,
        "tool_result": {}
    }

    result = agent_app.invoke(state)
    return result
