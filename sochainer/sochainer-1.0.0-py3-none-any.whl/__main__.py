from configparser import ConfigParser
from importlib import resources  # Python 3.7+

from sochainer import sochain

def main():
    """Read the Real Python article feed"""
    # Read URL of the Real Python feed from config file
    cfg = ConfigParser()
    cfg.read_string(resources.read_text("sochainer", "config.cfg"))
    url = cfg.get("feed", "url")

    prices = sochain.get_prices()
    return prices

if __name__ == "__main__":
    main()