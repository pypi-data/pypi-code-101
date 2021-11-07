import os
import shutil

def make(path):
	
	empty('tempo.py')
	file=open(path,'r')
	content=file.read()
	
	fc=open('tempo.py','w')
	fc.seek(0)
	fc.write('tempo='+content)
	fc.close()
	
	
def load():
	import tempo
	t=tempo.tempo
	return t
	
def empty(path):
	fc=open(path,'w')
	fc.write('')
	fc.close()
	
