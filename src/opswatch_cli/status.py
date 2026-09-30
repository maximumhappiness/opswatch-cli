"""Describes the status."""


def evaluate_status(status_code: int) -> str:
    """Evaluates staus codes and describes them."""
    if status_code == 0:
        return "OK"
    if status_code == 1:
        return "Warning"
    return "Critical"
