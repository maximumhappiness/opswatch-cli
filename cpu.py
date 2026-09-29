"""Fetch CPU load and print the result."""

import psutil


def cpu_load() -> float:
    """Return the current CPU utilization as a percentage."""
    return psutil.cpu_percent(interval=1)
