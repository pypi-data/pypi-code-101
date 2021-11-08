import os

from polidoro_argument import Command
from polidoro_cli import CLI


class Git(object):
    @staticmethod
    @Command(help='Run "git fetch" in all git projects')
    def fetch_all():
        for dir in os.listdir():
            if os.path.isdir(dir):
                os.chdir(dir)
                if os.path.exists('.git'):
                    print(f'Fetching in {dir}...')
                    CLI.execute('git fetch', show_cmd=False)
                os.chdir('..')
