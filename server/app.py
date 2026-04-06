
from fastapi import FastAPI, Body
from typing import Dict, Any, Optional
import sys
import os

sys.path.append(os.path.dirname(__file__))

from openenv_env.environment import DecisionIntelligenceEnv

app = FastAPI()

env = None

@app.get("/")
def root():
    return {"message": "Decision Intelligence Environment for OpenEnv Hackathon"}

@app.post("/reset")
def reset(task_id: str = Body("easy", embed=True)):
    global env
    env = DecisionIntelligenceEnv(task_id=task_id)
    state = env.reset()
    return state

@app.post("/step")
def step(action: Dict[str, int] = Body(...), task_id: Optional[str] = Body(None)):
    global env
    if env is None:
        task = task_id if task_id else "easy"
        env = DecisionIntelligenceEnv(task_id=task)
        env.reset()
    state, reward, done, info = env.step(action)
    return {"state": state, "reward": reward, "done": done, "info": info}

@app.get("/state")
def get_state():
    if env is None:
        return {"error": "Environment not initialized. Call /reset first."}
    return env.get_state()