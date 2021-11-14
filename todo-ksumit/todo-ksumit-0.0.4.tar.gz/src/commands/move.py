import click
from ..db import Database

@click.command('move', help="Move task to a project.")
@click.argument('id', type=int)
@click.argument('project', type=click.STRING)
def Move(id, project):
  db = Database()
  db.changeTaskProject(id, project)