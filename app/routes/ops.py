from fastapi import APIRouter

from app.services import system_service

router = APIRouter(prefix="/ops", tags=["operations"])


@router.get("/whoami")
def whoami() -> dict[str, object]:
    return system_service.get_current_user()


@router.get("/uptime")
def uptime() -> dict[str, object]:
    return system_service.get_uptime()


@router.get("/disk")
def disk_usage() -> dict[str, object]:
    return system_service.get_disk_usage()


@router.get("/files")
def project_files() -> dict[str, object]:
    return system_service.list_project_files()


@router.get("/python-version")
def python_version() -> dict[str, object]:
    return system_service.get_python_version()
