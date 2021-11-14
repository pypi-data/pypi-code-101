import click
from ..db import Database
from ..task import Task
from ..constants import DEFAULT_PROJECT, DATE_FORMATS, TIME_FORMATS, TODAY, RECUR_CHOICES

@click.command('update', help="Update a existing task.")
@click.option('-d', '--date', type=click.DateTime(formats=DATE_FORMATS))
@click.option('-t', '--time', type=click.DateTime(formats=TIME_FORMATS))
@click.option('-r', '--recur', type=click.INT)
@click.argument('id')
def Update(id, date, time, recur):
  if date: date = str(date.date())
  if time: time = str(time.time())
  db = Database()
  db.updateTask(id, None, None, date, time, recur)