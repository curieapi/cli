from rich.console import Console
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
    console.print(f"  [dim]v0.1.0  ·  [/dim][bright_blue]https://curie.sh[/bright_blue]  [dim]·  curie --help to get started[/dim]")
    console.print()