"""
entry point for third party to call
afford 2 calling choices
"""

# """
# choice 1
# same as executing command `pyland` at term, example following:
# ❯ python main.py
# usage: pyland [-h] [--version] [--no-color] {init,server,platform}
# pyland: error: the following arguments are required: command, args
# """
#
# if __name__ == "__main__":
#     import pyland
#     sys.exit(pyland.main())


"""
choice 2
same as executing command `pyland platform` at term
❯ python main.py
usage: Process some integrated operations with Auto platform.
       [-h] (--import IMPORT | --list LIST | --run RUN)
Process some integrated operations with Auto platform.: error: one of the arguments --import --list --run is required
"""

if __name__ == "__main__":
    import pyland
    import sys

    sys.exit(pyland.main(['platform', *sys.argv[1:]]))
