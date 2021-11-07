import os
import shutil
import tempo
class aon:
	k=0
	def make(self,path):
	
		empty('tempo.py')
		file=open(path,'r')
		content=file.read()
	
		fc=open('tempo.py','w')
		fc.seek(0)
		fc.write('tempo='+content)
		fc.close()
	
	def load(self):
		if self.k==0:
			self.k=self.k+1
			load()
		else:
			self.k=0
			t=tempo.tempo
			return t
	
	def empty(self,path):
		fc=open(path,'w')
		fc.write('')
		fc.close()
	
