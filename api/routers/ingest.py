from fastapi import APIRouter
from pydantic import BaseModel
from rag.rag_pipeline import RAGPipeline

pipeline = RAGPipeline()
router = APIRouter()

class IngestRequest(BaseModel):
    documents: list[str]

@router.post("/ingest")
async def ingest_docs(request: IngestRequest):
    try:
        pipeline.ingest(request.documents)
        return {"message": "Documents ingested successfully."}
    except Exception as e:
        return {"error": str(e)}