from rich.console import Console
from rich.table import Table
import pyfiglet

console = Console()

def print_banner():
    art = pyfiglet.figlet_format("CURIE", font="banner3-D")
    console.print()
    console.print("  [bold cyan]·[/bold cyan] [dim]· · · · · · · · · · · · · · · · · · · · · · · · · · ·[/dim] [bold cyan]·[/bold cyan]")
    console.print()
    console.print(f"[bold cyan]{art}[/bold cyan]", end="")
    console.print()
    console.print("  [bold white]⬡  Biology[/bold white]   [bold white]⬡  Chemistry[/bold white]   [bold white]⬡  Physics[/bold white]")
    console.print()
    console.print('  [dim]❝  Nothing in life is to be feared, only to be understood.  ❞[/dim]')
    console.print('  [dim]                              — Marie Skłodowska Curie[/dim]')
    console.print()
    console.print("  [bold cyan]·[/bold cyan] [dim]· · · · · · · · · · · · · · · · · · · · · · · · · · ·[/dim] [bold cyan]·[/bold cyan]")
    console.print()

    table = Table(show_header=True, header_style="bold cyan", box=None, padding=(0, 2))
    table.add_column("Command", style="bold white", min_width=20)
    table.add_column("Description", style="dim")
    table.add_column("Example", style="cyan")

    table.add_row("curie fold", "Predict protein structure", "curie fold MKTIIALSYIFCLVFA")
    table.add_row("curie dock", "Dock a small molecule", "curie dock --protein p.pdb --ligand 'SMILES'")
    table.add_row("curie embed", "Generate protein embeddings", "curie embed MKTIIALSYIFCLVFA")
    table.add_row("curie models", "List available models", "curie models --domain biology")
    table.add_row("curie auth login", "Save your API key", "curie auth login")

    console.print(table)
    console.print()
    console.print("  [bold cyan]·[/bold cyan] [dim]· · · · · · · · · · · · · · · · · · · · · · · · · · ·[/dim] [bold cyan]·[/bold cyan]")
    console.print(f"  [dim]v0.1.0  ·  [/dim][bright_blue]https://curie.sh[/bright_blue]  [dim]·  Get your API key at curie.sh/dashboard/keys[/dim]")
    console.print()