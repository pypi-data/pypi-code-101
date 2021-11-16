#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import sys

from ewoksorange.bindings import ows_to_ewoks


def main(argv):
    import os

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help=".ows (xml) file to convert")
    parser.add_argument("output", help="Entry to treat")
    options = parser.parse_args(argv[1:])
    graph = ows_to_ewoks(filename=options.input, preserve_ows_info=False)
    graph.dump(options.output)


if __name__ == "__main__":
    main(sys.argv)
