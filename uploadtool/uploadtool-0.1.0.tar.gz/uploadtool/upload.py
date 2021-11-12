import os
import sys
import shutil

join = os.path.join

class UploadInfo:
	"""
	记录用于上传使用的信息
	Record the information used for uploading
	"""
	def __init__(self, pkg_name, count=None, password=None, setup_py_dir=''):
		self.name = pkg_name
		self.path = setup_py_dir
		self.count, self.password = count, password
		self.itp = os.path.dirname(sys.executable)
		self.pkg_path = join(self.itp, "Lib", "site-packages")
	
class UploadTool(UploadInfo):
	def RemoveLast(self):
		if os.path.exists(join(self.path, self.name)):
			shutil.rmtree(join(self.path, self.name))
			print("Empty Left. ")
		else:
			print("Already Empty.")
	def RemoveDist(self):
		if os.path.exists(join(self.path, 'dist')):
			shutil.rmtree(join(self.path, 'dist'))
			print("Remove last dist")
		else:
			print("Already Empty.")
	def CopyFrom(self):
		if os.path.exists(join(self.pkg_path, self.name)):
			shutil.copytree(join(self.pkg_path, self.name), join(self.path, self.name))
			print("Do copy.")
		else:
			print("Can not Find pkg from site_packages.")
	def UpdateFiles(self):
		self.RemoveLast()
		self.CopyFrom()
		print("Finish Source Update.")
	def BuildSetup(self):
		os.system("python setup.py bdist_wheel --universal")
		os.system("python setup.py sdist")
		twine_cmd = "twine upload --repository pypi dist/* {} {}".format('-u ' + str(self.count) if self.count else "", "-p " + str(self.password) if self.password else "")
		print("[Debug]: ", twine_cmd)
		os.system(twine_cmd)
		os.system("pause")
	
	def Upload(self):
		"""
		执行上传命令
		Execute upload command
		"""
		if not os.path.exists(join(self.pkg_path, self.name)):
			err_str = "\n\n[Critical Error]: \n\t在Lib/site-package下找不到{}这个你想上传的包.\n\tThe package {} you want to upload cannot be found under Lib / site-package\n\n'''在之前的版本中会先在当前目录下删除这个'过时'的包，然后才会去Lib/site-package下寻找。我之前被这个bug整了一次，损失了快两个小时。特此备注为CriticalError\n\nIn previous versions, the 'obsolete' package will be deleted in the current directory before looking in Lib/site-package. I was fixed by this bug before and lost nearly two hours. It is hereby noted as critical error'''".format(self.name, self.name)
			raise Exception(err_str)
		self.UpdateFiles()
		self.RemoveDist()
		self.BuildSetup()
	
	def __call__(self):
		self.Upload()
		
		
		
if __name__ == '__main__':
	ut = UploadTool('pkg name', "pypi count", "pypi password")
	ut()
		