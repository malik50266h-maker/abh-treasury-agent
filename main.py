from fastapi import FastAPI
import uvicorn
import os

app = FastAPI()

AIRWALLEX_CLIENT_ID = os.getenv("AIRWALLEX_CLIENT_ID", "")
AIRWALLEX_API_KEY = os.getenv("AIRWALLEX_API_KEY", "")
AIRWALLEX_URL = "https://api-demo.airwallex.com"

@app.get("/")
def home():
    return {"message": "ABH Treasury Agent", "status": "live"}

@app.get("/health")
def health():
    return {"status": "ok", "keys_loaded": bool(AIRWALLEX_API_KEY)}

@app.post("/run-agent")
def run_agent(data: dict):
    return {"result": "Executed", "status": "Funds Secured", "sandbox": AIRWALLEX_URL}

if __name__ == "__main__":
    uvicorport=8000)
