import argparse
from typing import List
from pyland import main_scaffold


def main(args: List[str]) -> bool:
    parser = argparse.ArgumentParser(prog="pyland init")
    parser.add_argument(
        "--simple",
        action="store_true",
        default=False,
        required=False,
        help="generate simple demo project by project name",
    )
    parser.add_argument(
        "--sub",
        action="store_true",
        default=False,
        required=False,
        help="sub project has no conftest.py and main.py",
    )
    parser.add_argument(
        "--topo",
        action="store_true",
        default=False,
        required=False,
        help="topo project format services.py and test_01.py",
    )
    parser.add_argument(
        "--project",
        default='demo',
        required=False,
        help="generate demo project by project name",
    )

    parsed_args = parser.parse_args(args)

    return main_scaffold(project=parsed_args.project,
                         simple=parsed_args.simple,
                         sub=parsed_args.sub,
                         topo=parsed_args.topo
                         )
