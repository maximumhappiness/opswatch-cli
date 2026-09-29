"""Fetch CPU load and print the result."""

import psutil

CPU_WARNING_THRESHOLD = 80.0
CPU_INCREASED_THRESHOLD = 60.0

def cpu_load() -> float:
    """Return the current CPU utilization as a percentage."""
    return psutil.cpu_percent(interval=1)


def evaluate_cpu_usage(cpu_workload: float) ->str:
    """Evaluates CPU Usage and displays a Message."""
    if cpu_workload > CPU_INCREASED_THRESHOLD:
        cpu_msg = "CPU load: increased"
    elif cpu_workload > CPU_WARNING_THRESHOLD:
        cpu_msg = "Warning: High CPU load!"
    else:
        cpu_msg= "CPU Load: Normal"

    return cpu_msg
