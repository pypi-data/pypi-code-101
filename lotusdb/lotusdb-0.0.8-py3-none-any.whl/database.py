from typing import Any, Callable
import os, json
class Database:
  def __init__(self, path: str = 'data.db'):
    self.path = path
    if not os.path.exists(path): 
      with open(path, 'x') as f: f.close()
  def put(self, data: Any) -> None:
    with open(self.path, 'a') as f: f.write(json.dumps(data, separators=(',', ':')) + '\n'); f.close()
  def find(self, cb: Callable[[Any], bool]) -> Any:
    with open(self.path, 'r') as f:
      r = None
      for l in f:
        j = json.loads(l)
        try:
          if cb(j): r = j; break
        except: pass
      f.close(); return r
  def remove(self, cb: Callable[[Any], bool]) -> None:
    with open(self.path, 'r') as r, open(self.path + '.bak', 'w') as w:
      o = True
      for l in r:
        try:
          if cb(json.loads(l)): o = False
          else: o = True
        except: o = True
        if o: w.write(l)
      r.close(); w.close(); os.remove(self.path); os.rename(self.path + '.bak', self.path)