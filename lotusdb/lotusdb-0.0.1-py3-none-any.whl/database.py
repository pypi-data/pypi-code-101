import os, json
class Database:
    def __init__(self, path = 'data.db'):
        self.path = path;
        if os.path.exists(path) == False:
            with open(path, 'x') as f: f.close()
    def put(self, data):
        with open(self.path, 'a') as f: f.write(json.dumps(data) + '\n'); f.close()
    def find(self, cb):
        with open(self.path, 'r') as f:
            r: str
            for l in f:
                j = json.loads(l)
                if j: r = l; break
            f.close()
            return r
    def remove(self, data):  
        with open(self.path, 'r') as r, open(self.path + '.bak', 'w') as w:
            for l in r:
                if not json.loads(l): w.write(l)
            r.close(); w.close(); os.remove(self.path); os.rename(self.path + '.bak', self.path)