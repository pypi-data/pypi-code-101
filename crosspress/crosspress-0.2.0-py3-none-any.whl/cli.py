from crosspress import (tap, kdict)
import argparse


def crosspress():
    ap = argparse.ArgumentParser(description="Cross-platform lightweight keyboard simulator")

    group = ap.add_mutually_exclusive_group(required=True)
    group.add_argument("-t", "--tap", type=str, help="Keyboard sequence")
    group.add_argument("-l", "--list", action="store_true", help="Shortcuts list and syntax help")

    args = ap.parse_args()

    if args.tap:
        tap(args.tap)

    if args.list:
        keys = ", ".join(sorted([*kdict]))
        print(keys)
        print("\nSequence and combitantion example: \"h, e, l, l, o, left ctrl + enter\"")


if __name__ == "__main__":
    crosspress()
