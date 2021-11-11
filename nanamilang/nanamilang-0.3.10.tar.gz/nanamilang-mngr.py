#!/usr/bin/env python3

# This file is a part of NanamiLang Project
# This project licensed under GNU GPL version 2
# Initially made by @jedi2light (aka Stoian Minaiev)

"""NanamiLang STDLib Manager"""

import os
import sys
import argparse
import urllib.request

XDG_DATA_HOME = os.environ.get('XDG_DATA_HOME') or os.path.join(os.environ.get('HOME'), '.local/')


def main():
    """NanamiLang STDLib Main function"""

    parser = argparse.ArgumentParser('NanamiLang STDLib Manager')
    parser.add_argument('--status',
                        help='Show the current status',
                        action='store_true', default=False)
    parser.add_argument('--populate',
                        help='Populate NanamiLang STDLib',
                        action='store_true', default=False)
    args = parser.parse_args()

    nml_stdlib_dir = os.path.join(XDG_DATA_HOME, 'nanamilang')
    if not os.path.exists(nml_stdlib_dir):
        os.mkdir(nml_stdlib_dir)

    if args.populate:
        remote = 'https://nanamilang.jedi2light.moe/assets/stdlib.nml'
        print(f'NanamiLang STDLib Manager. Populating from {remote} ...')
        if urllib.request.urlretrieve(remote, os.path.join(nml_stdlib_dir, 'stdlib.nml')):
            print('NanamiLang STDLib Manager :: Populating -> Populated library from remote storage!')
            return 0
        else:
            print('NanamiLang STDLib Manager :: Populating -> For some reason, unable to populate. Sorry')
            return 1

    if args.status:
        print('NanamiLang STDLib Manager. Checking status... ', end='')
        print('STDLib Installed!' if os.path.exists(os.path.join(nml_stdlib_dir, 'stdlib.nml')) else 'STDLib Missing!')


if __name__ == '__main__':
    sys.exit(main() or int(0))
