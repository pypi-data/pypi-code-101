from pathlib import Path
import sys
import force_absolute_imports


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('pass files and/or folders to check')
        raise SystemExit(2)

    for p in map(Path, sys.argv[1:]):
        if p.is_file():
            force_absolute_imports.check_file(p)
        elif p.is_dir():
            force_absolute_imports.check_folder(p)
        else:
            raise ValueError(f'{p}: is not a file or folder')
