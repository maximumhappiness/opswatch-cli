"""Describes the deployment."""


def describe_deployment(successful: bool) -> str:
    """Return a readable deployment status."""
    if successful:
        return "Deployment erfolgreich"

    return "Deployment fehlgeschlagen"
