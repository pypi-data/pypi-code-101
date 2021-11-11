#!python

# This file is a part of NanamiLang Project
# This project licensed under GNU GPL version 2
# Initially made by @jedi2light (aka Stoian Minaiev)

"""NanamiLang Eval"""

import os
import argparse
from nanamilang import Program, datatypes


def main():
    """NanamiLang Eval Main function"""

    parser = argparse.ArgumentParser('NanamiLang Evaluator')
    parser.add_argument('program', help='Path to source code')
    args = parser.parse_args()

    assert args.program
    assert os.path.exists(args.program)

    with open(args.program, encoding='utf-8') as r:
        inp = r.read()

    assert inp, 'A program source code could not be an empty string'

    # Define NanamiLang Standard Library location

    nml_stdlib_path = os.path.join(
        os.environ.get('XDG_DATA_HOME')
        or os.path.join(os.environ.get('HOME'), '.local'),
        'nanamilang/stdlib.nml'
    )

    if not os.path.exists(nml_stdlib_path):
        print('Unable to continue, NanamiLang Standard Library is missing')
        print('If you are using the latest version of NanamiLang, consider')
        print('running: "nanamilang-mngr.py --populate" and then try again')
        return 1

    # Load NanamiLang Standard Library

    with open(nml_stdlib_path, 'r', encoding='utf-8') as handler:
        Program(handler.read()).evaluate()

    dt = Program(inp).evaluate()

    # Be strict, require program to return 0 or 1, no exceptions

    if isinstance(dt, datatypes.IntegerNumber):
        return dt.reference()
    else:
        raise ValueError(f'Program returned non-integer result, but: {dt}')

    # Return exit code to system and exit NanamiLang Evaluator after evaluating


if __name__ == "__main__":

    main()
