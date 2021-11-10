"""Console script for ooc"""

import argparse
import sys
from  config import Config
from counter import Player, Gate


def main():
    parser = argparse.ArgumentParser(
        description="Count objects using OpenCV2. Press 'q' to stop and exit video.")

    # Add arguments
    parser.add_argument(
        '-s','--source', required=True, help='Path to source video')
    parser.add_argument(
        '-t', '--show', dest='show', action='store_true', help='Shows the video')
    parser.add_argument(
        '-d','--debug', dest='debug', action='store_true', help='Runs in debug mode')
    parser.add_argument(
        '-c','--config', dest='config', help='Path to config file')
    
    # Defaults
    parser.set_defaults(show=True, debug=False, config='./ooc/config.json')
    
    # Parse
    args = parser.parse_args()

    # Run
    config = Config(args.config and args.config)
    player = Player(args.source, config.data, show=args.show, debug=args.debug)
    player.start()

    return 0


if __name__ == "__main__":
    sys.exit(main())
