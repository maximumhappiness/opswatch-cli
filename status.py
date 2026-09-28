"""Describes the status."""


def evaluate_status(status_code: int) -> str:
    """Evaluates staus codes and describes them."""
    if status_code == 0:
        return "Gesund"
    if status_code == 1:
        return "Warnung"
    return "Critical State"
