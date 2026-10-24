from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def home():
    return {"message": "ABH Treasury Agent is Live"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/run-agent")
def run_agent(data: dict):
    instruction = data.get("instruction", "check treasury")
    return {
        "result": "Treasury Agent Executed",
        "instruction": instruction,
        "balance": "$50,000",
        "status": "Funds Secured"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
