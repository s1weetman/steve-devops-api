#!/usr/bin/env bash
set -e

kubectl apply -f k8s/ghcr/deployment.yaml
kubectl apply -f k8s/ghcr/service.yaml
kubectl rollout status deployment/steve-devops-api
kubectl get pods
kubectl get services
