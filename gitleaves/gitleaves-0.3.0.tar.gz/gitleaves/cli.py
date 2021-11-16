import gitleaves.reports as reportslib

from typer import Typer, echo

app = Typer()


@app.command()
def genreports():
    echo("Generating reports...")
    reportslib.gen_ghwiki_reports()


@app.command()
def uploadreports():
    echo("Uploading reports...")
    reportslib.upload_ghwiki_reports()


if __name__ == "__main__":
    app()
