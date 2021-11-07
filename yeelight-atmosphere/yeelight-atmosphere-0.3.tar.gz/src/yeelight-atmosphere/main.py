import argparse
import logging
import sys

from .const import Settings
from .manager import BulbManager


def set_logging():
    root = logging.getLogger()
    root.setLevel(logging.INFO)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    root.addHandler(handler)


def main():
    set_logging()
    parser = argparse.ArgumentParser()

    parser.add_argument('--choose', '-c', dest='choose', action='store_true', default=False)
    parser.add_argument("--strategy", "-s", type=int, default=Settings.BORDERS_STRATEGY)
    parser.add_argument("--bulb_ip_address", "-i", type=str, default=None)
    parser.add_argument("--timeout", "-t", type=int, default=5)
    parser.add_argument("--delay", "-d", type=float, default=0.3)
    parser.add_argument("--queue_size", "-q", type=int, default=30)

    args = parser.parse_args()

    use_last_bulb = not args.choose
    strategy = args.strategy
    bulb_ip_address = args.bulb_ip_address
    timeout = args.timeout
    delay = args.delay
    Settings.QUEUE_SIZE_CONST = args.queue_size

    logging.info(f"QUEUE_SIZE_CONST: {Settings.QUEUE_SIZE_CONST} SATURATION_FACTOR: {Settings.SATURATION_FACTOR}")

    manager = BulbManager(use_last_bulb, bulb_ip_address, timeout=timeout)
    manager.run_atmosphere(strategy, delay)
