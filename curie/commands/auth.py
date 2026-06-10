import typer
import json
import os
from pathlib import Path
from rich.console import Console

console = Console()
app = typer.Typer(help="Manage Curie API authentication.")
CONFIG_PATH = Path.home() / ".curie" / "config.json"

@app.command()
def login():
    """Save your Curie API key."""
    api_key = typer.prompt("Enter your Curie API key", hide_input=True)
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
    CONFIG_PATH.write_text(json.dumps({"api_key": api_key}))
    console.print("[green]✓ Authenticated successfully[/green]")
    console.print(f"  Key saved to {CONFIG_PATH}")

@app.command()
def logout():
    """Remove your saved Curie API key."""
    if CONFIG_PATH.exists():
        CONFIG_PATH.unlink()
        console.print("[green]✓ Logged out successfully[/green]")
    else:
        console.print("[yellow]No saved API key found[/yellow]")