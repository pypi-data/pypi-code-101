"""# Entrypoint
"""
from .launcher import LiteraryLauncher, launch_new_instance
if __name__ == '__main__' and (not LiteraryLauncher.initialized()):
    launch_new_instance()