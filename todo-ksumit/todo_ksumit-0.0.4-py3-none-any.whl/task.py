from .constants import CYAN, FUTURE_COLOR, PAST_COLOR, PRESENT_COLOR, TODAY, YELLOW
from .helper import getRecurText, to_good_date, to_good_time, wrapText

class Task:
  def __init__(
    self, 
    title, 
    date = None,
    time = None,
    recur = None,
    project = None,
    id = None,
    is_completed = False
    ):
    self.title = title
    self.date = date
    self.time = time
    self.recur = recur
    self.project = project
    self.id = id
    self.is_completed = is_completed

  def to_db_tuple(self):
    t = (
      self.title,
      self.date,
      self.time,
      self.recur,
      self.project,
      self.is_completed
    )
    return t

  def to_list(self, fields):
    items = []
    for field in fields:
      items.append(self.getColor() + self.getFieldValue(field))
    return items

  def getFieldValue(self, field):
    result = None
    if (field == 'title'):
      result = wrapText(self.title)
    if (field == 'date'):
      result = to_good_date(self.date)
    if (field == 'time'):
      result = to_good_time(self.time)
    if (field == 'recur'):
      result = getRecurText(self.recur)
    if (field == 'project'):
      result = self.project
    if (field == 'rowid'):
      result = self.id
    if result: return str(result)
    return '-'
    
  
  def getColor(self):
    if (self.is_completed): return CYAN
    if self.date < TODAY: return PAST_COLOR
    if self.date > TODAY: return FUTURE_COLOR
    return PRESENT_COLOR

    