import typer
import httpx
import json
from rich.console import Console
from curie.auth import get_api_key

console = Console()

def embed(
    sequence: str = typer.Argument(..., help="Amino acid sequence to embed"),
    output: str = typer.Option(None, "--output", "-o", help="Save embeddings to JSON file")
):
    """Generate protein language model embeddings for a sequence."""
    api_key = get_api_key()

    with console.status("[bold green]Generating embeddings...", spinner="dots"):
        try:
            response = httpx.post(
                "https://api.curie.sh/v1/run",
                headers={"Authorization": f"Bearer {api_key}"},
                json={"model": "meta/esm-2-650m", "sequence": sequence},
                timeout=30.0
            )
            response.raise_for_status()
        except httpx.ConnectError:
            console.print("[red]Could not connect to Curie API. Check your internet connection.[/red]")
            raise typer.Exit(1)

    data = response.json()
    embedding = data.get("embedding", [])

    console.print(f"[green]✓ Embeddings generated[/green]")
    console.print(f"  Model:      meta/esm-2-650m")
    console.print(f"  Residues:   {len(sequence)}")
    console.print(f"  Dimensions: {len(embedding)}")

    if output:
        with open(output, "w") as f:
            json.dump({"sequence": sequence, "embedding": embedding}, f)
        console.print(f"  Saved to:   {output}")