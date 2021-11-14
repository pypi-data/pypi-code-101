#!/usr/bin/python3

import sys
import os
import re
from xtable import xtable
import xmltodict
import argparse
import json
import traceback


def mysqlx_main():
    parser = argparse.ArgumentParser(description="yet another mysql client CLI tool/shell")
    parser.add_argument(
        "-v",
        "--pivot",
        dest="pivot",
        action="store_true",
        default=False,
        help="pivot wide tables.",
    )
    parser.add_argument(
        "-w",
        "--widthhint",
        dest="widthhint",
        default=None,
        help="hint for col width. '0:20,2:30,'",
    )
    parser.add_argument(
        "-p",
        "--page",
        dest="page",
        type=int,
        default=2**30,
        help="rows per page. print header line again",
    )
    parser.add_argument(
        "-X",
        "--debug",
        dest="debug",
        action="store_true",
        default=False,
        help="debug mode",
    )
    parser.add_argument(
        "--csv",
        dest="csv",
        action="store_true",
        default=False,
        help="dump as CSV",
    )
    parser.add_argument(
        "--json",
        dest="json",
        action="store_true",
        default=False,
        help="dump as json",
    )
    parser.add_argument(
        "--yaml",
        dest="yaml",
        action="store_true",
        default=False,
        help="dump as yaml",
    )
    parser.add_argument(
        "--markdown",
        dest="markdown",
        action="store_true",
        default=False,
        help="dump as markdown",
    )
    parser.add_argument(
        "--html",
        dest="html",
        action="store_true",
        default=False,
        help="dump as html",
    )
    parser.add_argument(
        "--plain",
        "--nocolor",
        dest="plain",
        action="store_true",
        default=False,
        help="no ansi color",
    )
    parser.add_argument(
        "--nowrap",
        "--nowrap",
        dest="nowrap",
        action="store_true",
        default=False,
        help="when specified, output will be limited to current terminal width",
    )
    parser.add_argument(
        "--wrap",
        "--wrap",
        dest="wrap",
        action="store_true",
        default=False,
        help="wrap mode. widthhint will be disabled in this mode.",
    )
    parser.add_argument(
        "--timeout",
        dest="timeout",
        type=int,
        default=1,
        help="read timeout. default 1s",
    )
    args = parser.parse_args()

    if args.nowrap:
        args.plain = True
    if args.plain:
        os.environ["force_ansicolor"] = "0"

    def xtimeout_call(fn=None, msg="timeouted.") :
        import signal
        TIMEOUT = 1
        def interrupted(signal, frame):
            print("# {}".format(msg), file=sys.stderr, flush=True)
            return 0
        signal.signal(signal.SIGALRM, interrupted)
        signal.alarm(TIMEOUT)
        res = fn()
        signal.alarm(0)
        return res


if __name__ == "__main__":
    mysqlx_main()
