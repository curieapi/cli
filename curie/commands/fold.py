import typer
import httpx
from rich.console import Console
from rich.spinner import Spinner
from curie.auth import get_api_key

console = Console()

def fold(
    sequence: str = typer.Argument(..., help="Amino acid sequence to fold"),
    output: str = typer.Option(None, "--output", "-o", help="Save PDB to file"),
    model: str = typer.Option("esm/esmfold-v1", "--model", "-m", help="Model to use")
):
    """Predict protein structure from an amino acid sequence."""
    api_key = get_api_key()

    with console.status("[bold green]Folding protein...", spinner="dots"):
        try:
            response = httpx.post(
                "https://api.curie.sh/v1/run",
                headers={"Authorization": f"Bearer {api_key}"},
                json={"model": model, "sequence": sequence},
                timeout=60.0
            )
            response.raise_for_status()
        except httpx.ConnectError:
            console.print("[red]Could not connect to Curie API. Check your internet connection.[/red]")
            raise typer.Exit(1)

    data = response.json()

    if response.status_code == 401:
        console.print("[red]Invalid API key. Run `curie auth login` or set CURIE_API_KEY[/red]")
        raise typer.Exit(1)
    elif response.status_code == 429:
        retry = response.headers.get("Retry-After", "?")
        console.print(f"[red]Rate limited. Retry after {retry}s[/red]")
        raise typer.Exit(1)
    elif response.status_code >= 500:
        console.print("[red]Curie API error. Check https://status.curie.sh[/red]")
        raise typer.Exit(1)

    plddt = data.get("plddt", [])
    mean_plddt = sum(plddt) / len(plddt) if plddt else 0

    console.print(f"[green]✓ Folded successfully[/green]")
    console.print(f"  Model:      {model}")
    console.print(f"  Residues:   {len(sequence)}")
    console.print(f"  Mean pLDDT: {mean_plddt:.1f}")

    if output:
        with open(output, "w") as f:
            f.write(data.get("pdb", ""))
        console.print(f"  Saved to:   {output}")