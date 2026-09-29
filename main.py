"""OpsWatch CLI: Command-line Tool for system monitoring."""

from cpu import cpu_load, evaluate_cpu_usage
from deployment import describe_deployment
from status import evaluate_status


def main() -> None:
    """Run the main program."""
    version = "0.1.0"
    status_code = 0
    deployment_status = describe_deployment(successful=True)
    status = evaluate_status(status_code)
    cpu_workload = cpu_load()
    cpu_msg = evaluate_cpu_usage(cpu_workload)

    print("OpsWatch CLI running!")
    print(f"Deployment: {deployment_status}")
    print(f"Version: {version}")
    print(f"Status: {status}")
    print(f"CPU Load: {cpu_workload:.1f}%")
    print(f"{cpu_msg}")


if __name__ == "__main__":
    main()
