from setuptools import setup
import distutils
from setuptools import Distribution
import os
import subprocess
from distutils.command.build_py import build_py as _build_py

class Distr(Distribution):
    def has_c_libraries(self):
        return True

class build_py(_build_py):
    def run(self):
        abs_path = os.path.dirname(os.path.abspath(__file__)) + '/'
        for cmd in ('go mod tidy',
                    'go mod vendor',
                    'make lib'):
            subprocess.check_call(cmd.split(' '), cwd=abs_path)
        src_so = 'lib/libparse.so'
        dest_so = os.path.join(self.build_lib, 'libparse.so')
        distutils.dir_util.mkpath(self.build_lib)
        distutils.file_util.copy_file(src_so, dest_so)
        super(build_py, self).run()

setup(name='ComposeParser',
      version='0.0.4',
      description='Docker Compose Parser',
      author='Uchenic',
      author_email='uchenic@protonmail.com',
      url='',
      zip_safe= False,

      cmdclass={
        'build_py': build_py,
      },
      packages=['composeparser'],


     )
