import typer
import httpx
from rich.console import Console
from rich.table import Table
from curie.auth import get_api_key

console = Console()

def models(
    domain: str = typer.Option(None, "--domain", "-d", help="Filter by domain: biology, chemistry, physics")
):
    """List all available Curie models."""
    api_key = get_api_key()

    try:
        response = httpx.get(
            "https://api.curie.sh/v1/models",
            headers={"Authorization": f"Bearer {api_key}"},
            timeout=10.0
        )
        response.raise_for_status()
    except httpx.ConnectError:
        console.print("[red]Could not connect to Curie API. Check your internet connection.[/red]")
        raise typer.Exit(1)

    data = response.json()
    model_list = data.get("models", [])

    if domain:
        model_list = [m for m in model_list if m.get("domain", "").lower() == domain.lower()]

    table = Table(title="Curie Models")
    table.add_column("Model ID", style="cyan")
    table.add_column("Name")
    table.add_column("Domain", style="magenta")
    table.add_column("Latency")
    table.add_column("Price")
    table.add_column("Status", style="green")

    for m in model_list:
        table.add_row(
            m.get("id", ""),
            m.get("name", ""),
            m.get("domain", ""),
            m.get("latency", ""),
            m.get("price", ""),
            "● Live" if m.get("status") == "live" else "○ Coming soon"
        )

    console.print(table)