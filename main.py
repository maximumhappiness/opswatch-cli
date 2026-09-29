"""OpsWatch CLI: Command-line Tool for system monitoring."""

from cpu import cpu_load
from deployment import describe_deployment
from status import evaluate_status


def main() -> None:
    """Run the main program."""
    version = "0.1.0"
    status_code = 0
    deployment_status = describe_deployment(successful=True)
    status = evaluate_status(status_code)
    cpu_workload = cpu_load()

    print("OpsWatch CLI running!")
    print(deployment_status)
    print(f"Version: {version}")
    print(f"Status: {status}")
    print(f"CPU Load: {cpu_workload:.1f}%")

    if cpu_workload >= 80.0:
        print("Warning high CPU-Load")


if __name__ == "__main__":
    main()
