import typer
from curie.commands import fold, dock, embed, models, auth
from curie.banner import print_banner

app = typer.Typer(
    name="curie",
    help="Curie — scientific AI infrastructure.",
    no_args_is_help=False,
    invoke_without_command=True
)

app.add_typer(auth.app, name="auth")
app.command()(fold.fold)
app.command()(dock.dock)
app.command()(embed.embed)
app.command()(models.models)

@app.callback()
def main(ctx: typer.Context):
    if ctx.invoked_subcommand is None:
        print_banner()

if __name__ == "__main__":
    app()