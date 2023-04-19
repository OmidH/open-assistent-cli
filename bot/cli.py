"""This module provides the bot CLI."""
# src/bot/cli.py

from typing import Optional

import typer

from bot import __app_name__, __version__
from bot import ask_bot

app = typer.Typer()


@app.command()
def ask(
    description: str = typer.Argument(...),
    context: str = typer.Option("", "--conext", "-c"),
    tokens: int = typer.Option(
        1000, "--tokens", "-t", min=50, max=1300),
) -> None:
    """Ask a question."""

    answer = ask_bot.ask_bot(context, description, tokens)
    typer.secho(
        f"""Answer: {answer} """,
        fg=typer.colors.GREEN,
    )


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return
