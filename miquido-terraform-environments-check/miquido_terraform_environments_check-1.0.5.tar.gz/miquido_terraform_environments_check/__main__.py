import os
import sys

environments = os.getenv('ENVIRONMENTS').split(' ')


def run_os(cmd: str):
    exit_code = os.system(cmd)
    print(f'exit code = {exit_code}')
    if exit_code != 0:
        sys.exit(exit_code)


for environment in environments:
    os.chdir(environment)
    run_os('terraform init -backend=false')
    run_os('terraform validate')
    os.chdir('../')
