"""Fetch CPU load and print the result."""

import psutil

MEMORY_WARNING_THRESHOLD = 90.0
MEMORY_INCREASED_THRESHOLD = 60.0

def memory_load() -> float:
    """Return memory usage statistics."""
    return psutil.virtual_memory().percent


def evaluate_memory_usage(memory_usage: float) -> str:
    """Evaluates memory usage from memory_load."""
    if memory_usage > MEMORY_WARNING_THRESHOLD:
        memory_msg = "Warning: high memory usage!"
    else:
        memory_msg = "Memory usage normal"
    return memory_msg
