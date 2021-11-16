from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='Calima',
      version='2.0.2',
      description='Python interface for Pax Calima Fan',
      long_description=readme(),
      keywords='pax calima fan bluetooth ble',
      author='Timo Mutta',
      author_email='unknown@unknown.com',
      url='https://github.com/timutta/pycalima',
      license='Apache 2.0',
      packages=['pycalima'],
      install_requires=['bluepy'],
      entry_points ={
        'console_scripts': ['calima=pycalima.cmdline:main'],
      },
      include_package_data=True)
