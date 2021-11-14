import click
from ..db import Database
from ..task import Task
from ..constants import DEFAULT_PROJECT, DATE_FORMATS, TIME_FORMATS, TODAY, RECUR_CHOICES

@click.command('add', help="Add a new task.")
@click.option('-p', '--project', default=DEFAULT_PROJECT)
@click.option('-d', '--date', default=TODAY, type=click.DateTime(formats=DATE_FORMATS))
@click.option('-t', '--time', type=click.DateTime(formats=TIME_FORMATS))
@click.option('-r', '--recur', type=click.INT)
@click.argument('title')
def Add(title, project, date, time, recur):
  if date: date = str(date.date())
  if time: time = str(time.time())
  task = Task(title, date, time, recur, project)
  db = Database()
  db.createTask(task)