import click, datetime
from tabulate import tabulate
from .helper import tabulateList
from ..constants import TIME, TODAY
from ..db import Database
from ..helper import to_good_date
from ..task import Task

@click.command('listall', help="List All tasks.")
@click.option('-c', '--completed', is_flag=True)
@click.option('-f', '--find', default="")
@click.option('-s', '--sort', default="date", type=click.Choice(['date', 'project', 'time', 'rowid', 'title', 'recur']))
def ListAll(find, completed, sort):
  db = Database()
  items = db.getAllTasks(find, completed, sort)
  if len(items) > 0:
    tasks = []
    for item in items:
      task = Task(item['title'], item['date'], item['time'], item['recur'], item['project'], item['rowid'], item['is_completed'])
      tasks.append(task.to_list(['rowid', 'title', 'date', 'time', 'recur', 'project']))
    dt = datetime.datetime.strptime(TODAY, '%Y-%m-%d')
    today = dt.strftime('%d %b')
    headers = ["Id", "Title", today, TIME, "Recur", "Project"]
    tabulateList(tasks, headers)
