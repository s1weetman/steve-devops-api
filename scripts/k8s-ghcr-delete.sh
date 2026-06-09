#!/usr/bin/env bash
set -e

kubectl delete -f k8s/ghcr/service.yaml
kubectl delete -f k8s/ghcr/deployment.yaml
