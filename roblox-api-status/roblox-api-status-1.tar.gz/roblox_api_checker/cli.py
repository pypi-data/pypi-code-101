from . import __init__
from sys import argv,stdout

print = stdout.write

available = [
  'down',
  'up',
  'all',
  'start'
]
def main():
  if len(argv) == 2 and argv in available:
    if argv[1] == available[0]:
      print(__init__.statuscli('down'))
    if argv[1] == available[1]:
      print(__init__.statuscli('up'))
    if argv[1] == available[2]:
      print(__init__.statuscli('all'))
  elif len(argv) == 1:
    print(__init__.statuscli('all'))
  else:
    print("What? I will use default argument instead")
    print(__init__.statuscli('all'))
def server():
  try:
    ip = argv[1]
  except IndexError:
    ip = "localhost"
  try:
    port = int(argv[2])
  except IndexError:
    port = 80
  try:
    usessl = True if argv[3] == 'usessl' else False
    if usessl:
      ssl_context = (argv[4],argv[5])
  except IndexError:
    usessl = False
  __init__.serverstatus(ip,port,usessl,ssl_context)