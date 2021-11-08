import argparse
from typing import List
from pyland import run_server


def main(args: List[str]) -> bool:
    parser = argparse.ArgumentParser(
        prog="pyland server",
        description="run local server to debug")
    parser.add_argument(
        "--port",
        default='5000',
        required=False,
        help="local server port",
    )

    parsed_args = parser.parse_args(args)

    # print(vars(parsed_args))
    return run_server(port=parsed_args.port)
