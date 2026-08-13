from app.config.settings import PROJECT_NAME, PROJECT_VERSION


def get_health_status() -> dict:
    """Return the current application health status."""

    return {
        "status": "healthy",
        "project": PROJECT_NAME,
        "version": PROJECT_VERSION,
    }