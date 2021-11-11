
def install(module,status=True):
    try:
        import sys
        import subprocess
        import importlib
        importlib.import_module(module)
        if status == True:
            print("already installed ")
    except ImportError:
        if status == True:
            print("installing now")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', module])

def uninstall(module,status=True):
    import sys
    import subprocess
    import os
    os.system("python -m pip uninstall "+module+" -y")
#   subprocess.run([sys.executable + ' -m'+' pip'+' uninstall ', module," -y"])
    
        

def checkmoduleinstalled(module,status=True):
    try:
        import importlib
        importlib.import_module(module)
        if status == True:
            print("already installed ")
    except ImportError:
        if status == True:
            print("not innstalled")
        return False
def updatepip():
    import subprocess
    import sys
    import os
    os.system('pip install --upgrade pip')
