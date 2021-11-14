from datasette import hookimpl
import click


@hookimpl
def register_commands(cli):
    @cli.command()
    def hello_world():
        "Print 'Hello world'"
        click.echo("Hello world")
