import crosspress
import argparse


def main():
    ap = argparse.ArgumentParser(description="Cross-platform lightweight keyboard simulator")

    group = ap.add_mutually_exclusive_group(required=True)
    group.add_argument("-t", "--tap", type=str, help="Keyboard sequence")
    group.add_argument("-l", "--list", action='store_true', help="Shortcuts list and syntax help")

    args = ap.parse_args()

    if args.tap:
        crosspress.tap(args.tap)

    if args.list:
        keys = ", ".join(sorted([*crosspress.kdict]))
        print(keys)
        print('\nSequence and combitantion example: "h, e, l, l, o, left ctrl + enter"')
