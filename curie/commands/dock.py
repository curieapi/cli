import typer
import httpx
from rich.console import Console
from curie.auth import get_api_key

console = Console()

def dock(
    protein: str = typer.Option(..., "--protein", "-p", help="Path to protein PDB file"),
    ligand: str = typer.Option(..., "--ligand", "-l", help="Ligand SMILES string or path to .sml file"),
    output: str = typer.Option(None, "--output", "-o", help="Save docked pose PDB to file")
):
    """Dock a small molecule ligand to a protein structure."""
    api_key = get_api_key()

    try:
        protein_pdb = open(protein).read()
    except FileNotFoundError:
        console.print(f"[red]Protein file not found: {protein}[/red]")
        raise typer.Exit(1)

    # accept SMILES string or .sml file
    if ligand.endswith(".sml"):
        try:
            ligand_smiles = open(ligand).read().strip()
        except FileNotFoundError:
            console.print(f"[red]Ligand file not found: {ligand}[/red]")
            raise typer.Exit(1)
    else:
        ligand_smiles = ligand

    with console.status("[bold green]Docking ligand...", spinner="dots"):
        try:
            response = httpx.post(
                "https://api.curie.sh/v1/run",
                headers={"Authorization": f"Bearer {api_key}"},
                json={
                    "model": "mit/diffdock",
                    "protein_pdb": protein_pdb,
                    "ligand_smiles": ligand_smiles
                },
                timeout=120.0
            )
            response.raise_for_status()
        except httpx.ConnectError:
            console.print("[red]Could not connect to Curie API. Check your internet connection.[/red]")
            raise typer.Exit(1)

    data = response.json()
    confidence = data.get("confidence", 0)

    console.print(f"[green]✓ Docked successfully[/green]")
    console.print(f"  Model:      mit/diffdock")
    console.print(f"  Confidence: {confidence:.3f}")

    if output:
        with open(output, "w") as f:
            f.write(data.get("pose_pdb", ""))
        console.print(f"  Saved to:   {output}")