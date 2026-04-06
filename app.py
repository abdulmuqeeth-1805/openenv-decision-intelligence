from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, Any
import sys
import os

sys.path.append(os.path.dirname(__file__))

from openenv_env.environment import DecisionIntelligenceEnv

app = FastAPI()

env = None

class ResetRequest(BaseModel):
    task_id: str = "easy"

class StepRequest(BaseModel):
    action: Dict[str, int]
    task_id: str = "easy"

@app.get("/")
def root():
    return {"message": "Decision Intelligence Environment for OpenEnv Hackathon"}

@app.post("/reset")
def reset(request: ResetRequest):
    global env
    env = DecisionIntelligenceEnv(task_id=request.task_id)
    state = env.reset()
    return {"state": state}

@app.post("/step")
def step(request: StepRequest):
    global env
    if env is None:
        env = DecisionIntelligenceEnv(task_id=request.task_id)
        env.reset()
    state, reward, done, info = env.step(request.action)
    return {"state": state, "reward": reward, "done": done, "info": info}

@app.get("/state")
def get_state():
    if env is None:
        return {"error": "Environment not initialized. Call /reset first."}
    return {"state": env.get_state()}