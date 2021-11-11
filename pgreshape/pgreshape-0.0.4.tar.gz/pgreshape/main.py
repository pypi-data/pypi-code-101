import typer

app = typer.Typer(help="pgreshape CLI user manager.")


@app.command()
def new(column: str):
    """
    Name for new column
    """
    typer.echo(f"Creating new column: {column}")


def main():
    return app()


if __name__ == "__main__":
    main()
