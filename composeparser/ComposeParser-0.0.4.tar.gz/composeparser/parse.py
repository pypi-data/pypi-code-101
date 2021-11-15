import ctypes
import json
import os

class GoString(ctypes.Structure):
    _fields_ = [("p",ctypes.c_char_p), ("n",ctypes.c_int)]


class ComposeParser(object):
    def __init__(self, path):
        self.path = path
        abs_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/'
        self.lib = ctypes.CDLL(os.path.join(abs_path,"libparse.so"))
        self.lib.load.argtypes = [GoString]
        self.lib.load.restype = ctypes.c_char_p

    def load(self):

        s = GoString()
        d = self.path.encode('utf-8')
        s.p = ctypes.c_char_p(d)
        s.n = ctypes.c_int(len(d))
        result = json.loads(self.lib.load(s).decode('utf-8'))
        if "error" in result.keys():
            raise Exception(result)
        return result

def main():
    q = './docker-compose.yml'
    parser = ComposeParser(q)
    result = parser.load()
    print(result)


if __name__ == '__main__':
    main()