import click
from .helper import tabulateList
from ..constants import DATE_FORMATS, TIME, TODAY, DEFAULT_PROJECT
from ..db import Database
from ..task import Task
from tabulate import tabulate

@click.command('list', help="List tasks.")
@click.option('--date', default=TODAY, type=click.DateTime(formats=DATE_FORMATS))
@click.option('-c', '--completed', is_flag=True)
@click.option('-p', '--project')
def List(date, project, completed):
  db = Database()
  items = db.getTasks(date, project, completed)
  if len(items) > 0:
    tasks = []
    for item in items:
      task = Task(item['title'], item['date'], item['time'], item['recur'], item['project'], item['rowid'], item['is_completed'])
      tasks.append(task.to_list(['rowid', 'title', 'time', 'project']))
    headers = ["Id", "Title", TIME, "Project"]
    tabulateList(tasks, headers)
