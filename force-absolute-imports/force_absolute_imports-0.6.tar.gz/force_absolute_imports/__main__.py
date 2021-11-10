from pathlib import Path
import sys
import force_absolute_imports


def main() -> int:
    """
    return codes
    0 - success, all imports are absolute
    1 - some imports are relative
    2 - non existed files, non .py extensions, files are not passed
    """
    if len(sys.argv) == 1:
        print('pass files and/or folders to check')
        return 2

    only_absolute = True
    for p in map(Path, sys.argv[1:]):
        if p.is_file():
            if not force_absolute_imports.only_absolute_file(p):
                only_absolute = False
        elif p.is_dir():
            if not force_absolute_imports.only_absolute_folder(p):
                only_absolute = False
        else:
            print(f'{p}: is not exists or not a file or folder')
            raise SystemExit(2)

    if only_absolute:
        return 0
    return 1


if __name__ == '__main__':
    raise SystemExit(main())
