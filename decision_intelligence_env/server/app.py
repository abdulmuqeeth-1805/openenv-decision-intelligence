from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Decision Intelligence Environment"}

def main():
    uvicorn.run(app, host="0.0.0.0", port=7860)

if __name__ == "__main__":
    main()

[project]
name = "decision-intelligence-env"
version = "1.0.0"
requires-python = ">=3.10"
dependencies = [
    "fastapi",
    "uvicorn",
    "numpy",
    "openenv-core>=0.2.0",
]

[project.scripts]
openenv-server = "server.app:main"