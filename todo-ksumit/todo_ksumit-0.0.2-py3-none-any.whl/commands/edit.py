import click
from ..db import Database

@click.command('edit', help="Edit title of a task.")
@click.argument('id', type=int)
def Edit(id):
  db = Database()
  task = db.getTask(id)
  ans = click.edit(task['title'], editor='vi')
  if ans and (ans != '' or ans != '\n'): db.updateTask(id, ans)