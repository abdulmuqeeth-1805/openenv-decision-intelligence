import sys
import os
sys.path.append(os.path.dirname(__file__))

from fastapi import FastAPI
import uvicorn

from openenv_env.environment import DecisionIntelligenceEnv

app = FastAPI()
env = None

@app.get("/")
def root():
    return {"message": "Decision Intelligence Environment"}

@app.post("/reset")
def reset():
    global env
    env = DecisionIntelligenceEnv(task_id="easy")
    return env.reset()

def main():
    uvicorn.run(app, host="0.0.0.0", port=7860)

if __name__ == "__main__":
    main()