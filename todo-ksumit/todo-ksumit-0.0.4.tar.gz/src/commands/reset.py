import click
from ..db import Database

@click.command('reset', help="Reset Table")
@click.confirmation_option(prompt="Are you sure?")
def Reset():
  db = Database()
  db.createTable()