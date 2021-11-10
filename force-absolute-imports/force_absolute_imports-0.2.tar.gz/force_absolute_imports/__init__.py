from pathlib import Path
import re


def check_line(line):
    if re.match(r'from\s*\.', line):
        raise SystemExit(1)


def check_file(file):
    with open(file) as f:
        for line in f:
            check_line(line)


def check_folder(folder):
    for file in Path(folder).rglob('*.py'):
        check_file(file)
