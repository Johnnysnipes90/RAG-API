from chromadb import Client
from sentence_transformers import SentenceTransformer
from typing import List

class VectorStore:
    def __init__(self):
        self.client = Client()
        self.collection = self.client.get_or_create_collection("docs")
        self.embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

    def add_documents(self, docs: List[str]):
        embeddings = self.embedding_model.encode(docs).tolist()
        print(embeddings)
        for i, doc in enumerate(docs):
            self.collection.add(documents=[doc], embeddings=[embeddings[i]], ids=[f"doc_{i}"])

    def query(self, text: str, k: int = 3):
        query_embedding = self.embedding_model.encode([text])[0].tolist()
        results = self.collection.query(query_embeddings=[query_embedding], n_results=k)
        return results["documents"][0]