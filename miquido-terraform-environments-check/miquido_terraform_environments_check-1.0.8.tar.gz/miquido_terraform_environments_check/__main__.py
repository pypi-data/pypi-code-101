import os
import sys

environments = os.getenv('ENVIRONMENTS').split(' ')


def run_os(cmd: str):
    exit_code = os.system(cmd)
    if exit_code != 0:
        sys.exit(1)


if __name__ == '__main__':
    project_dir = os.getcwd()
    for environment in environments:
        os.chdir(environment)
        run_os('terraform init -backend=false')
        run_os('terraform validate')
        os.chdir(project_dir)
