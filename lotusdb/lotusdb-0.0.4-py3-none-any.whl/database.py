import os, json
class Database:
  def __init__(self, path = 'data.db'):
    self.path = path
    if not os.path.exists(path): 
      with open(path, 'x') as f: f.close()
  def put(self, data):
    with open(self.path, 'a') as f: f.write(json.dumps(data, separators=(',', ':')) + '\n'); f.close()
  def find(self, cb):
    with open(self.path, 'r') as f:
      r = ''
      for l in f:
        j = json.loads(l)
        try:
          if cb(j): r = j; break
        except: None
      f.close(); return r
  def remove(self, cb):
    with open(self.path, 'r') as r, open(self.path + '.bak', 'w') as w:
      o = True
      for l in r:
        try:
          if not cb(json.loads(l)): o = False
          else: o = True
        except: None
        if o: w.write(l)
      r.close(); w.close(); os.remove(self.path); os.rename(self.path + '.bak', self.path)