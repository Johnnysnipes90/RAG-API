# RAG-API
A Retrieval-Augmented Generation (RAG) API built with FastAPI, FAISS/ChromaDB for vector search, and OpenAI LLM for response generation. Containerized with Docker and deployed on Kubernetes using Minikube.



# 🚀 RAG-API: Retrieval-Augmented Generation with FastAPI & Kubernetes

## 📌 Overview
**RAG-API** is a **Retrieval-Augmented Generation (RAG)** system that efficiently retrieves relevant information from stored documents and generates responses using a **Large Language Model (LLM)**.  

The project is built using **FastAPI**, **FAISS/ChromaDB** for vector search, and **OpenAI/Hugging Face LLM** for response generation. The API is **containerized with Docker** and deployed locally on **Kubernetes (Minikube)**.

---

## 📂 Project Structure

```
/rag-api
├── api/                     # API Implementation
│   ├── __init__.py
│   ├── main.py               # FastAPI app entry point
│   ├── routers/              # API route handlers
│   │   ├── __init__.py
│   │   ├── ingest.py         # Handles document ingestion
│   │   ├── query.py          # Handles user queries
│
├── k8s/                      # Kubernetes Deployment Files
│   ├── deployment.yaml       # Defines API deployment
│   ├── service.yaml          # Defines service (NodePort/LoadBalancer)
│
├── rag/                      # Retrieval-Augmented Generation (RAG) Pipeline
│   ├── __init__.py
│   ├── llm.py                # Handles LLM calls (OpenAI/HuggingFace)
│   ├── rag_pipeline.py       # Manages RAG workflow (retrieval + response)
│   ├── vectorstore.py        # Handles FAISS/ChromaDB storage
│
├── .env.example              # Environment variables template
├── .gitignore                # Ignore unnecessary files
├── Dockerfile                # Defines Docker container
├── deploy.sh                 # Shell script to automate deployment
├── requirements.txt          # Python dependencies
└── README.md                 # Documentation
```

---

## 🛠️ Tech Stack
- **Backend:** FastAPI
- **Vector Storage:** FAISS / ChromaDB
- **LLM:** OpenAI API / HuggingFace
- **Containerization:** Docker
- **Deployment:** Kubernetes (Minikube)
- **Orchestration:** Shell script for automation

---

## 🔧 Setup & Installation

### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/your-username/rag-api.git
cd rag-api
```

### 2️⃣ **Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### 3️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 4️⃣ **Set Up Environment Variables**
Copy `.env.example` to `.env` and update values:
```bash
cp .env.example .env
```
Modify `.env` with API keys and database details.

### 5️⃣ **Run the API Locally**
```bash
uvicorn api.main:app --reload --host 0.0.0.0 --port 8000
```
The API will be available at **[http://localhost:8000](http://localhost:8000)**.

---

## 🚀 API Endpoints

| Method | Endpoint | Description |
|--------|---------|-------------|
| `POST` | `/ingest` | Uploads and stores documents for retrieval. |
| `POST` | `/query` | Accepts a query and returns an LLM-generated response. |
| `GET`  | `/health` | Checks API health status. |

### 🛠 **Testing API with cURL**
- **Ingest Documents**
```bash
curl -X POST "http://localhost:8000/ingest" -H "Content-Type: application/json" -d '{"text": "Your document content"}'
```
- **Query API**
```bash
curl -X POST "http://localhost:8000/query" -H "Content-Type: application/json" -d '{"query": "Your question"}'
```
- **Health Check**
```bash
curl -X GET "http://localhost:8000/health"
```

---

## 🐳 Docker Setup

### 1️⃣ **Build Docker Image**
```bash
docker build -t rag-api .
```

### 2️⃣ **Run Docker Container**
```bash
docker run -p 8000:8000 --env-file .env rag-api
```

---

## ☸️ Kubernetes Deployment with Minikube

### 1️⃣ **Start Minikube**
```bash
minikube start
```

### 2️⃣ **Apply Kubernetes Manifests**
```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

### 3️⃣ **Check Pods & Services**
```bash
kubectl get pods
kubectl get services
```

### 4️⃣ **Access API in Minikube**
For **LoadBalancer:**
```bash
minikube service rag-api-service
```
For **NodePort:**
```bash
kubectl port-forward service/rag-api-service 8000:80
```
API will be available at **[http://localhost:8000](http://localhost:8000)**.

---

## 📊 Future Improvements
✅ Support multiple document formats (PDF, DOCX).  
✅ Add Redis caching for query responses.  
✅ Improve scalability with auto-scaling in Kubernetes.  

---

## 👨‍💻 Contributing
1. **Fork the repo**
2. **Create a new branch** (`feature-xyz`)
3. **Commit changes** (`git commit -m "Add feature XYZ"`)
4. **Push to GitHub** (`git push origin feature-xyz`)
5. **Open a Pull Request**

---

## 📜 License
This project is licensed under the **MIT License**.

---

## 🙌 Acknowledgments
Special thanks to **OpenAI**, **FAISS**, **HuggingFace**, and the **FastAPI** community.

---

🔗 **GitHub Repository**: [your-github-link](https://github.com/your-username/rag-api)






