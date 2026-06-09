#!/usr/bin/env bash
set -e

kubectl delete -f k8s/local/service.yaml
kubectl delete -f k8s/local/deployment.yaml
