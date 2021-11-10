#microlang ver 1
import json
class ML():
  def __init__(self):
    pass
  def ver(self):
    return "1"
  def prev_ver(self):
    return "1"
  def open(self,work,file_name,write):
    if work == "w":
      with open(file_name,"w") as file:
        file.write(write)
        file.close()
    elif work == "r":
      with open(file_name) as file:
        print(file.read())
        file.close()
    elif work == "h":
      with open(file_name) as file:
        
        print(hash(file.read()))
        
        file.close()
        

      
    
def get_ver():
  print("CURRENT VERSION IS..... 1")

def prev_ver():
  print("PREVIOUS VERSION IS ...... 1")
def open_command(w,ml):
  if w == 'w':

    naming = input("NAME THE FILE")
    write = input("WRITE IN THE FILE")
    ml.open("w",naming,write)
  elif w == "r":
    naming = input("NAME THE FILE")
    ml.open("r",naming,None)
  elif w == "make hash":
    naming = input("NAME THE FILE")
    ml.open("h",naming,None)
  elif w == "add hash":
    naming = input("NAME THE FILE")
    text = input("ENTER TEXT TO BE HASHED")
    v = hash(text)
    ml.open("w",naming,str(v))


def do_make(ver,ml):
  run = True
  text = ''
  while run:

    
    text = input("DO... ADD SUB MULTIPLY DIVIDE") 
    if text == "BACK":
      run = False
      start(ver,ml)
    elif text == "ADD":
      num1 = input("ENTER NUM 1")
      num2 = input("ENTER NUM 2")
      print(int(num1) + int(num2))
      run = False
      start(ver,ml)
    elif text == "SUB":
      num1 = input("ENTER NUM 1")
      num2 = input("ENTER NUM 2")
      print(int(num1) - int(num2))
      run = False
      start(ver,ml)
    elif text == "MULTIPLY":
      num1 = input("ENTER NUM 1")
      num2 = input("ENTER NUM 2")
      print(int(num1) * int(num2))
      run = False
      start(ver,ml)
    elif text == "DIVIDE":
      num1 = input("ENTER NUM 1")
      num2 = input("ENTER NUM 2")
      print(int(num1) / int(num2))
      run = False
      start(ver,ml)
    

    else:
      print("ERROR GOING BACK TO COMMAND SHELL")
      run = False
      start(ver,ml)

def start(ver,ml):

  if ver == "THROW":
    run = True
    text = ''
    while run:
      
      text = input(">>")
      if text == "END":
        run = False
        print("BROKE OUT OF LOOP")
      elif text == "DO":
        do_make(ver,ml)
      elif text == "TEST":
        print("SUCCESS RUNNING VER... " + ver)
      elif text == "OPEN:":
        open_command('w',ml)
      elif text == "OPEN;":
        open_command('r',ml)
      
      elif text == "GETHASH":
        
        open_command("make hash",ml)
      elif text == "MAKEHASH":
        open_command("add hash",ml)
     
      else:
        print("INVALID COMMAND")
    
    

        
  if ver == "1":
    run = True
    text = ''
    while run:
      
      text = input(">>")
      if text == "END":
        run = False
        print("BROKE OUT OF LOOP")
      elif text == "DO":
        do_make(ver,ml)
      elif text == "TEST":
        print("SUCCESS RUNNING VER... " + ver)
      elif text == "OPEN:":
        open_command('w',ml)
      elif text == "OPEN;":
        open_command('r',ml)
      elif text == "GETHASH":
        
        open_command("make hash",ml)
      elif text == "MAKEHASH":
        open_command("add hash",ml)
        
        
      else:
        print("INVALID COMMAND")
    
  #else:
    #print("ERROR... PLEASE ENTER 'THROW' AT... Start()")
  


    
    


