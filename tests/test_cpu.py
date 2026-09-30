
from opswatch_cli.cpu import evaluate_cpu_usage

def test_cpu_usage_normal() -> None:
    assert evaluate_cpu_usage(50.0) == "CPU load: Normal"


def test_cpu_usage_boundary_60() -> None:
    assert evaluate_cpu_usage(60.0) == "CPU load: Normal"


def test_cpu_usage_increased() -> None:
    assert evaluate_cpu_usage(60.1) == "CPU load: Increased"


def test_cpu_usage_boundary_80() -> None:
    assert evaluate_cpu_usage(80.0) == "CPU load: Increased"


def test_cpu_usage_warning() -> None:
    assert evaluate_cpu_usage(80.1) == "Warning: High CPU load!"