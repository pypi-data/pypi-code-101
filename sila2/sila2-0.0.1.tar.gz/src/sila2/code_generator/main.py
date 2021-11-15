import os
from argparse import ArgumentParser
from typing import List, Optional

import sila2.code_generator
from sila2.code_generator.generator import CodeGenerator
from sila2.framework import Feature


def main(argv: Optional[List[str]] = None):
    parser = ArgumentParser(
        prog=sila2.code_generator.__name__, description="Generate Python code for given SiLA 2 feature definitions"
    )
    parser.add_argument("feature_definitions", nargs="+", help="SiLA 2 feature definitions")
    parser.add_argument("-o", "--out-dir", help="Output directory (default: '.')", default=".")

    args = parser.parse_args(argv)

    os.makedirs(args.out_dir, exist_ok=True)
    for feature_definition_file in args.feature_definitions:
        feature = Feature(open(feature_definition_file).read())
        feature_out_dir = os.path.join(args.out_dir, feature._identifier.lower())
        os.makedirs(feature_out_dir, exist_ok=True)

        generator = CodeGenerator(feature)
        generator.generate_all(feature_out_dir)
        generator.reformat_files(feature_out_dir)
