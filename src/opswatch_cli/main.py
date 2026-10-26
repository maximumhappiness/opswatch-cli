"""OpsWatch CLI: Command-line Tool for system monitoring."""

import json
from typing import Annotated

import typer

from opswatch_cli.cpu import cpu_load, evaluate_cpu_usage
from opswatch_cli.deployment import describe_deployment
from opswatch_cli.memory import evaluate_memory_usage, memory_load
from opswatch_cli.status import evaluate_status

app = typer.Typer()


def collect_status_data() -> dict:
    """Collect currecnt system status data."""
    version = "0.1.0"
    status_code = 0
    deployment_status = describe_deployment(successful=True)
    system_status = evaluate_status(status_code)
    cpu_workload = cpu_load()
    cpu_message = evaluate_cpu_usage(cpu_workload)
    memory_percent = memory_load()
    memory_message = evaluate_memory_usage(memory_percent)

    return {
        "version": version,
        "deployment": deployment_status,
        "status": system_status,
        "cpu_percent": cpu_workload,
        "cpu_status": cpu_message,
        "memory_percent": memory_percent,
        "memory_status": memory_message,
    }


@app.callback()
def cli() -> None:
    """Monitor system health from the command line."""

@app.command()
def status(json_output: Annotated[bool,typer.Option("--json",help="Output status as JSON.")] = False) -> None:
#def status(json_output: bool = False) -> None:
    """Monitor system health from the command line."""
    status_data = collect_status_data()

    if json_output:
        typer.echo(
            json.dumps(
                status_data,
                indent=4,
            )
        )
        return

    typer.echo("OpsWatch CLI running!")
    typer.echo(f"Deployment: {status_data['deployment']}")
    typer.echo(f"Version: {status_data['version']}")
    typer.echo(f"Status: {status_data['status']}")
    typer.echo(f"CPU load: {status_data['cpu_percent']:.1f}%")
    typer.echo(f"{status_data['cpu_status']}")
    typer.echo(f"Memory load: {status_data['memory_percent']:.1f}%")
    typer.echo(f"{status_data['memory_status']}")


if __name__ == "__main__":
    app()
