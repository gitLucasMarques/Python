from fastapi import FastAPI
from api.router import router as api_router

app = FastAPI(
    title="My FastAPI Application",
    description="This is a FastAPI application for gerenciament of tasks.",
    version="1.0.0"
)

app.include_router(api_router, prefix="/tasks", tags=["tasks"])

@app.get("/", tags=["Root"])

async def read_root():
    return {"message": "Welcome to the FastAPI application!"}