
import os
import platform
import re
import subprocess
import sys

__version__ = '0.0.1'
__appauthor__ = 'larryw3i & Contributors'


def run():
    base_path = os.path.dirname(os.path.abspath(__file__))
    bash_path = os.path.join(base_path, 'getcodium.sh')
    mirrors_path = os.path.join(base_path, 'codium.mirrors')

    system = platform.system().lower()
    sys_argv = ' '.join(sys.argv[1:])

    # wait for you to contribute the code
    os.system(
        f'cd {base_path};bash ./getcodium.sh {sys_argv};cd {os.getcwd()}' if
        system == 'linux' else
        ''
    )
