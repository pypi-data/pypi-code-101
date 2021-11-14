import click
from ..db import Database

@click.command('complete')
@click.argument('id', type=int)
def Complete(id):
  '''Make task done.'''
  db = Database()
  db.completeTask(id)
  