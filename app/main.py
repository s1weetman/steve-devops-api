from fastapi import FastAPI

from app.routes import health, ops

app = FastAPI(
    title="Steve DevOps Operational API",
    description=(
        "A local DevSecOps learning API for operational automation, "
        "Docker, Kubernetes, and CI/CD practice."
    ),
    version="0.1.0",
)

app.include_router(health.router)
app.include_router(ops.router)


@app.get("/")
def read_root() -> dict[str, str]:
    return {
        "message": "Steve DevOps Operational API",
        "docs": "/docs",
        "health": "/health",
    }
