from fastapi import APIRouter
from pydantic import BaseModel
from rag.rag_pipeline import RAGPipeline

pipeline = RAGPipeline()
router = APIRouter()

class QueryRequest(BaseModel):
    """Query set for api"""
    query: str

@router.post("/query")
async def query_docs(request: QueryRequest):
    """Used to query docs"""
    try:
        response = pipeline.query(request.query)
        return {"response": response}
    except Exception as e:
        return {"error": str(e)}