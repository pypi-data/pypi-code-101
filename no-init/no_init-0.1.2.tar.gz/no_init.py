from pathlib import Path
import sys


def main() -> int:
    """
    return codes:
    0 - success, no __init__.py found
    1 - found __init__.py files
    2 - not a directory or passed (or directory not exists)
    """
    if len(sys.argv) == 1:
        print('pass files and/or folders to check')
        return 2

    n_inits = 0
    for directory in map(Path, sys.argv[1:]):
        for file in directory.rglob('*/__init__.py'):
            print(file)
            n_inits += 1

    if n_inits > 0:
        print(f'error: found {n_inits} __init__.py files')
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
