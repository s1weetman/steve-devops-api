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
