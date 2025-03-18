from fastapi import FastAPI
from api.routers import ingest, query

app = FastAPI(title="RAG API")

app.include_router(ingest.router)
app.include_router(query.router)

@app.get("/")
@app.get("/home")
async def home():
    return {
        "status": "success",
        "message": "Welcome to the RAG application",
    }

@app.get("/health")
async def health():
    return {"status": "ok"}