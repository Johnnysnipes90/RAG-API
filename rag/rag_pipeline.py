from .vectorstore import VectorStore
from .llm import generate_response

class RAGPipeline:
    """Used to run the entire RAG pipeline"""
    def __init__(self):
        self.vector_store = VectorStore()

    def ingest(self, documents):
        """
        Used for ingesting documents
        """
        self.vector_store.add_documents(documents)

    def query(self, user_query: str) -> str:
        """Used for querying documents"""
        context_docs = self.vector_store.query(user_query)
        context = "\n".join(context_docs)
        return generate_response(context, user_query)