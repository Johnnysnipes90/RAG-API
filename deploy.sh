#!/bin/bash

eval $(minikube docker-env)
docker build -t rag-api:latest .
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
minikube service rag-service