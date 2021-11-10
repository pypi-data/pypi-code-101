from pathlib import Path
import re


def check_line(line: str):
    if re.match(r'from\s*\.', line):
        raise ValueError(1)


def check_file(file):
    file = Path(file)
    if file.suffix != '.py':
        raise ValueError('not a python file')
    with open(file) as f:
        for linenumber, line in enumerate(f, start=1):
            try:
                check_line(line)
            except ValueError:
                print(f'relative import: {file}:{linenumber} {line.strip()}')


def check_folder(folder: Path):
    for file in Path(folder).rglob('*.py'):
        check_file(file)
