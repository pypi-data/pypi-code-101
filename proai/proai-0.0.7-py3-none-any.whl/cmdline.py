import os
import subprocess
import logging

log = logging.getLogger(__name__)


def run(command, chdir=None):
    if chdir:
        log.info(f'Temporarily changing working directory to {chdir}')
        initial_cwd = os.getcwd()
        os.chdir(chdir)

    log.warning(f'Running: {" ".join(command)}')
    output = subprocess.run(command, capture_output=True)

    if chdir:
        os.chdir(initial_cwd)

    return {
        'stderr': output.stderr.decode("utf-8").splitlines(),
        'stdout': output.stderr.decode("utf-8").splitlines()
    }
