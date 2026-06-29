from fastapi import FastAPI

from .routes import (
    router
)

app = FastAPI(
    title="GraphMind AI",
    description="Enterprise Agentic GraphRAG API",
    version="0.1.0"
)

app.include_router(router)


@app.get("/")
def root():

    return {

        "message": "Welcome to GraphMind AI 🚀"

    }