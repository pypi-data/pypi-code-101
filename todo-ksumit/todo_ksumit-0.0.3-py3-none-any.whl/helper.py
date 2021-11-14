import datetime
import textwrap
import os

from .constants import TODAY, TOMORROW

def cursor_to_dict_list(cursor):
  tasks = []
  cols = [col[0] for col in cursor.description]
  for row in cursor.fetchall():
      tasks.append(dict(zip(cols, row)))
  return tasks

def to_good_date(date):
  if date == TODAY: return 'today'
  if date == TOMORROW: return 'tomorrow'
  try: 
    dt = datetime.datetime.strptime(date, '%Y-%m-%d')
    days = (dt - datetime.datetime.now()).days
    if days >= 1 and days <= 7: return dt.strftime('%A')
    return dt.strftime('%d %b')
  except: return '-'

def to_good_time(time):
  try: return datetime.datetime.strptime(time, '%H:%M:%S').strftime('%I:%M %p')
  except: return '-'

def nextRecurDate(date, recur):
  if (date > TODAY): return date
  dt = datetime.datetime.strptime(date, '%Y-%m-%d')
  
  while dt < datetime.datetime.now():
    dt = dt + datetime.timedelta(days=int(recur))
  return dt.strftime('%Y-%m-%d')

def wrapText(value):
  width = getWidthSize()
  wrapper = textwrap.TextWrapper(width=width)
  return wrapper.fill(text=value)

def getWidthSize():
  size = os.get_terminal_size()
  return size.columns // 2

def getRecurText(recur):
  if (not recur): return '-'
  recur = int(recur)
  if recur == 1:
    return 'Daily'
  if recur == 7:
    return 'Weekly'
  if recur == 2:
    return 'Other Day'
  if recur == 14:
    return 'Biweekly'
  if recur == 30 or recur == 31:
    return 'monthly'
  return recur