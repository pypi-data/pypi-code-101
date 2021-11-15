import os

def pip_version():
  cmd = "pip --version"
  returned_value = os.system(cmd) 

def update_pip():
  cmd = "python -m pip install --upgrade pip"
  returned_value = os.system(cmd)

def package_installer():
  package = input("Enter the name of the package: ")
  cmd = "pip install "+package
  returned_value = os.system(cmd)
