#!/usr/bin/env bash
set -e

kubectl apply -f k8s/local/deployment.yaml
kubectl apply -f k8s/local/service.yaml
kubectl get pods
kubectl get services
