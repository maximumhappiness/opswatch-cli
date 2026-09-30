"""OpsWatch CLI: Command-line Tool for system monitoring."""

import json
from typing import Annotated

import typer

from opswatch_cli.cpu import cpu_load, evaluate_cpu_usage
from opswatch_cli.deployment import describe_deployment
from opswatch_cli.memory import evaluate_memory_usage, memory_load
from opswatch_cli.status import evaluate_status

app = typer.Typer()


@app.callback()
def cli() -> None:
    """Monitor system health from the command line."""


@app.command()
def status(
json_output: Annotated[
bool,
typer.Option(help="Output status as JSON."),
] = False) -> None:
#def status(json_output: bool = False) -> None:
    """Monitor system health from the command line."""
    version = "0.1.0"
    status_code = 0
    deployment_status = describe_deployment(successful=True)
    status = evaluate_status(status_code)
    cpu_workload = cpu_load()
    cpu_msg = evaluate_cpu_usage(cpu_workload)
    memory_usage = memory_load()
    memory_msg = evaluate_memory_usage(memory_usage)

    status_data = {
    "version": version,
    "deployment": deployment_status,
    "status": status,
    "cpu_percent": cpu_workload,
    "cpu_status": cpu_msg,
    "memory_percent": memory_usage,
    "memory_status": memory_msg,
    }

    if json_output:
        typer.echo(
            json.dumps(
                status_data,
                indent=4,
                ))

    typer.echo("OpsWatch CLI running!")
    typer.echo(f"Deployment: {deployment_status}")
    typer.echo(f"Version: {version}")
    typer.echo(f"Status: {status}")
    typer.echo(f"CPU load: {cpu_workload:.1f}%")
    typer.echo(f"{cpu_msg}")
    typer.echo(f"Memory load: {memory_usage:.1f}%")
    typer.echo(f"{memory_msg}")


if __name__ == "__main__":
    app()
