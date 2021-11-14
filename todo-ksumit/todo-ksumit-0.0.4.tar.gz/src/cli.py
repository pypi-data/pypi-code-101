import click
from .commands import Add, Delete, List, Move, Reset, Complete, ListAll, Edit, Update
from .db import Database

@click.group(invoke_without_command=True, help="This is your task manager")
@click.option('-d', '--delete', multiple=True)
@click.option('-c', '--complete', multiple=True)
def cli(delete, complete):
  db = Database()
  for id in delete:
    db.deleteTask(id)

  for id in complete:
    db.completeTask(id)

cli.add_command(Add)
cli.add_command(Edit)
cli.add_command(Update)
cli.add_command(Delete)
cli.add_command(List)
cli.add_command(Complete)
cli.add_command(Move)
cli.add_command(Reset)
cli.add_command(ListAll)