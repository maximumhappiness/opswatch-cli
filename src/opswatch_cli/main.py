"""OpsWatch CLI: Command-line Tool for system monitoring."""

import typer

from opswatch_cli.cpu import cpu_load, evaluate_cpu_usage
from opswatch_cli.deployment import describe_deployment
from opswatch_cli.status import evaluate_status

app = typer.Typer()


@app.callback()
def cli() -> None:
    """Monitor system health from the command line."""


@app.command()
def status() -> None:
    """Monitor system health from the command line."""
    version = "0.1.0"
    status_code = 0
    deployment_status = describe_deployment(successful=True)
    status = evaluate_status(status_code)
    cpu_workload = cpu_load()
    cpu_msg = evaluate_cpu_usage(cpu_workload)

    typer.echo("OpsWatch CLI running!")
    typer.echo(f"Deployment: {deployment_status}")
    typer.echo(f"Version: {version}")
    typer.echo(f"Status: {status}")
    typer.echo(f"CPU Load: {cpu_workload:.1f}%")
    typer.echo(f"{cpu_msg}")


if __name__ == "__main__":
    app()
