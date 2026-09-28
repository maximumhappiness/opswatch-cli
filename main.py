"""OpsWatch CLI: Command-line Tool for system monitoring."""

from deployment import describe_deployment
from fetch_cpu_load import cpu_load
from status import evaluate_status


def main() -> None:
    """Run the main program."""
    version = "0.1.0"
    status = "Bereit"
    status_code = 0

    deployment_status = describe_deployment(successful=True)
    print(deployment_status)
    status = evaluate_status(status_code)
    cpu_workload = cpu_load()

    print("OpsWatch CLI läuft!")
    print(f"Version: {version}")
    print(f"Status: {status}")
    print(f"CPU Load: {cpu_workload} %")


if __name__ == "__main__":
    main()
