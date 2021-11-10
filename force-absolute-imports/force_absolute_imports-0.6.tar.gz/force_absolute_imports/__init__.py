from pathlib import Path
import re


def only_absolute_line(line: str) -> bool:
    return not re.match(r'from\s*\.', line)


def only_absolute_file(file) -> bool:
    file = Path(file)
    if file.suffix != '.py':
        print(f'{file} not a python file')
        raise SystemExit(2)

    only_absolute = True

    with open(file) as f:
        for linenumber, line in enumerate(f, start=1):
            if not only_absolute_line(line):
                print(f'relative import: {file}:{linenumber} {line.strip()}')
                only_absolute = False

    return only_absolute


def only_absolute_folder(folder: Path) -> int:
    only_absolute = True
    for file in Path(folder).rglob('*.py'):
        if not only_absolute_file(file):
            only_absolute = False
    return only_absolute
