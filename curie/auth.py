import json
import typer
from pathlib import Path
from rich.console import Console

console = Console()
CONFIG_PATH = Path.home() / ".curie" / "config.json"

def get_api_key() -> str:
    # 1. environment variable
    import os
    key = os.environ.get("CURIE_API_KEY")
    if key:
        return key

    # 2. config file
    if CONFIG_PATH.exists():
        data = json.loads(CONFIG_PATH.read_text())
        key = data.get("api_key")
        if key:
            return key

    # 3. neither found
    console.print("[red]No API key found.[/red]")
    console.print("  Run [bold]curie auth login[/bold] or set [bold]CURIE_API_KEY[/bold]")
    console.print("  Get your key at https://curie.sh/dashboard/keys")
    raise typer.Exit(1)