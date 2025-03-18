# RAG Application with FastAPI, FAISS, and OpenAI

## Overview
This project is a **Retrieval-Augmented Generation (RAG) API**, which retrieves relevant information from a document store and generates responses using a Large Language Model (LLM). It uses **FastAPI** for the API, **FAISS** or **ChromaDB** for vector storage, and **OpenAI's API** or any open-source LLM for response generation.

## Features
- Accepts and stores documents for retrieval
- Uses an embedding model to store and search for relevant documents
- Queries stored documents and generates responses using an LLM
- Exposes API endpoints via FastAPI
- Containerized with Docker and deployed locally using Kubernetes (Minikube)

## Project Structure
```
├── api
│   ├── __init__.py
│   ├── main.py
│   ├── routers
│   │   ├── __init__.py
│   │   ├── ingest.py
│   │   ├── query.py
│
├── k8s
│   ├── deployment.yaml
│   ├── service.yaml
│
├── rag
│   ├── __init__.py
│   ├── llm.py
│   ├── rag_pipeline.py
│   ├── vectorstore.py
│
├── .env.example
├── .gitignore
├── deploy.sh
├── Dockerfile
├── requirements.txt
├── README.md
```

## Setup Instructions

### 1️⃣ Install Dependencies
Ensure you have **Python 3.10+**, **uv**, and **Docker** installed. Then, install dependencies:

```bash
uv pip install -r requirements.txt
```

### 2️⃣ Configure Environment Variables
Copy the `.env.example` file to `.env` and insert your OpenAI API key:

```bash
cp .env.example .env
```
Edit `.env` and add your **OpenAI API key**:
```
OPENAI_API_KEY=your-api-key-here
```

### 3️⃣ Run the API Locally
Run the FastAPI server:

```bash
uvicorn api.main:app --host 0.0.0.0 --port 8000
```

OpenAPI docs available at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Docker Deployment

### 4️⃣ Build the Docker Image
```bash
docker build -t rag-api .
```

### 5️⃣ Run the Docker Container
```bash
docker run -p 8000:8000 --env-file .env rag-api
```

## Kubernetes Deployment (Minikube)

### 6️⃣ Start Minikube
```bash
minikube start
```

### 7️⃣ Deploy the Application
```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

### 8️⃣ Get API URL
```bash
minikube service rag-api-service --url
```

## Automate Deployment
Run the deployment script to automate Docker and Kubernetes setup:

```bash
./deploy.sh
```

## API Endpoints

| Method | Endpoint       | Description                  |
|--------|--------------|------------------------------|
| POST   | /ingest      | Uploads documents to the vector store |
| POST   | /query       | Accepts user queries and returns generated responses |
| GET    | /health      | Health check for API status |

## Technologies Used
- **FastAPI** – Web framework for API
- **FAISS / ChromaDB** – Vector storage
- **OpenAI API** – LLM response generation
- **Docker** – Containerization
- **Kubernetes (Minikube)** – Local deployment
- **uvicorn** – ASGI server for FastAPI

## Future Improvements
- Implement authentication for API endpoints
- Support for additional LLM providers (e.g., Hugging Face)
- Optimize FAISS indexing for better performance

## License
This project is licensed under the MIT License.

---
