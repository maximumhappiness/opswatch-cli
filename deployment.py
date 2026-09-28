"""Describes the deployment."""


def describe_deployment(successful: bool) -> str:
    """Return a redable deployment status."""
    if successful:
        return "Deployment erfolgreich"

    return "Deployment fehlgeschlagen"
