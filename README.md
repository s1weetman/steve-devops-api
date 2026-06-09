# Steve DevOps API

This project is a local DevSecOps operational API built with FastAPI. It is intended as a learning project for building APIs, Dockerizing services, deploying locally to Kubernetes, connecting CI/CD workflows, and eventually exploring cloud deployment.

The current phase contains the first working local FastAPI application with safe DevOps-style operational endpoints. Docker, Kubernetes, and CI/CD assets will be added in later phases.

## Run Locally

```bash
cd /Users/sweetman/git/steve-devops-api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
./scripts/run-local.sh
```

Swagger UI is available at:

```text
http://localhost:8000/docs
```

## Test the API

```bash
http http://localhost:8000/
http http://localhost:8000/health
http http://localhost:8000/ops/whoami
http http://localhost:8000/ops/uptime
http http://localhost:8000/ops/disk
http http://localhost:8000/ops/files
http http://localhost:8000/ops/python-version
```

## Run with Docker

```bash
docker build -t steve-devops-api:local .
docker run --rm -p 8000:8000 steve-devops-api:local
```

Test the containerized API:

```bash
http http://localhost:8000/
http http://localhost:8000/health
http http://localhost:8000/ops/python-version
```

Docker validation note:

The app runs inside a container. Port 8000 on the Mac maps to port 8000 inside the container, so the API remains available locally at:

```text
http://localhost:8000/docs
```

## Run in Local Kubernetes

```bash
docker build -t steve-devops-api:local .
kubectl apply -f k8s/local/deployment.yaml
kubectl apply -f k8s/local/service.yaml
kubectl get pods
kubectl get services
```

Test the Kubernetes service:

```bash
http http://localhost:30080/health
```

`imagePullPolicy: Never` tells Kubernetes to use the local Docker image instead of pulling from a remote registry. NodePort `30080` exposes the app locally through Kubernetes. The `/health` endpoint is used for both liveness and readiness checks.

## GitHub Actions CI

The GitHub Actions CI workflow runs on pushes to `main` and pull requests targeting `main`. It installs the Python dependencies from `requirements.txt`, runs the pytest test suite, and builds the Docker image with the existing Dockerfile.

This prepares the project for future Azure Container Registry and AKS deployment work without adding cloud deployment steps yet.

## CI/CD Notes

GitHub Actions is transitioning JavaScript actions from Node.js 20 to Node.js 24. This repository proactively opts into Node.js 24 with `FORCE_JAVASCRIPT_ACTIONS_TO_NODE24` so future action runtime deprecations are less likely to break the workflow unexpectedly.
