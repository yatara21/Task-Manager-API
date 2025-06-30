from fastapi import FastAPI
from database import init_db
from routes import router
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app):
    init_db()
    yield

app = FastAPI()

app.include_router(router)

@app.get("/")
def root():
    return {
        "api": "Task Management API",
        "endpoints": [
            "/health",
            "/tasks",
            "/tasks/{task_id}",
            "/tasks/status/{status}",
            "/tasks/priority/{priority}"
        ]
    }

@app.get("/health")
def health():
    return {
        "status": "ok"
    } 