from fastapi import FastAPI, HTTPException
import ceejiye_core
import os

app = FastAPI(title="CeejiyeDB REST API")

# Initialize store with default path
db = ceejiye_core.CeejiyeStore(os.getenv("DB_PATH", "data.json"))

@app.get("/execute/{command}")
def execute_command(command: str):
    """
    Executes a Somali command via REST.
    Example: /execute/SOOQAAD%20magac
    """
    response = db.execute(command)
    if response.startswith("ERROR:"):
        raise HTTPException(status_code=400, detail=response)
    return {"response": response.strip()}

@app.get("/xaalad")
def get_xaalad():
    return {"xaalad": db.execute("XAALAD").strip()}

@app.post("/kaydi/{key}")
def kaydi(key: str, value: str):
    res = db.execute(f"KAYDI {key} {value}")
    return {"status": res.strip()}

@app.get("/sooqaad/{key}")
def sooqaad(key: str):
    res = db.execute(f"SOOQAAD {key}")
    if res.startswith("ERROR:"):
        raise HTTPException(status_code=404, detail=res)
    return {"key": key, "value": res.strip()}
