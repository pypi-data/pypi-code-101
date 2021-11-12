import os
import sys
import time
import shutil
import ctypes

from twine.settings import Settings as twine_Settings
from twine.commands.upload import upload as twine_upload

join = os.path.join

class Const:
	bat_name = 'uploadtool_build_source.bat'

def UploadByTwine(info, timeout=20000):
	"""直接调用twine的cmd貌似不起效果."""
	def _valid_dist_files(_dist_dir, _timeout):
		def _is_files_ready():
			tgz_flag, whl_flag = False, False
			for _name in os.listdir(_dist_dir):
				if _name[-3:].lower() == '.gz':
					tgz_flag = True
				if _name[-4:].lower() == '.whl':
					whl_flag = True
			return tgz_flag and whl_flag
		
		def _rec_for_timeout(_left_time):
			time.sleep(0.5)
			_left_time -= 500
			if (_left_time <= 0):
				raise Exception("[TimeOutError]: Failed to wait files ready.")
			return _left_time
		
		if not os.path.exists(_dist_dir) or not _is_files_ready():
			print("\n\nWaiting... (if wait too long, please ctrl+c to finish it.)\n")
			while not os.path.exists(_dist_dir):
				_timeout = _rec_for_timeout(_timeout)
			while not _is_files_ready():
				_timeout = _rec_for_timeout(_timeout)
			

	setting = twine_Settings(username=info.count, password=info.password)
	
	# 提取dist下所有文件(.tgz and .whl)
	aim_path, dist_files = join(info.path, 'dist'), []
	_valid_dist_files(aim_path, timeout)
	for _name in os.listdir(aim_path):
		_path = join(info.path, 'dist', _name)
		if os.path.isfile(_path):
			dist_files += [_path]
	
	
	twine_upload(setting, dist_files)
	

class UploadInfo:
	"""
	记录用于上传使用的信息
	Record the information used for uploading
	"""
	def __init__(self, pkg_name, count=None, password=None, show_cmd=True):
		self.name = pkg_name
		self.path = os.getcwd()
		self.show = show_cmd
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
		
	def BuildAndUpload(self):
		"""
		调用setup、twine，生成.tar.gz和.whl文件
		"""
		tmp_file_path = self.__build_temp_files()
		os.system(tmp_file_path)
		UploadByTwine(self)
		self.__clean_temp_files(tmp_file_path)
		
	def __build_temp_files(self):
		setup_path = join(self.path, 'setup.py')
		bat_path = join(self.path, Const.bat_name)
		
		# 注入bat
		f = open(bat_path, 'w')
		f.write("python {} bdist_wheel\n".format(setup_path))
		f.write("python {} sdist".format(setup_path))
		f.close()
		
		return bat_path
	
	def __clean_temp_files(self, bat_path):
		
		# 清除零时文件
		try:
			os.remove(bat_path)
		except:
			print("Failed to clean up bat<tmp>.")
			
	
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
		self.BuildAndUpload()
		os.system('pause')
		
	
	def __call__(self):
		self.Upload()
		
		
		
if __name__ == '__main__':
	ut = UploadTool('pkg name', "pypi count", "pypi password")
	ut()
		