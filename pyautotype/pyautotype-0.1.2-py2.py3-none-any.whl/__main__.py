import argparse

from .pyautotype import pyautotype


def main():
    parser = argparse.ArgumentParser(description='pyautotype')
    parser.add_argument('-w', '--wait', type=int, default=5, help='wait time before type start')
    args = parser.parse_args()
    pyautotype(args.wait)


if __name__ == '__main__':
    main()
