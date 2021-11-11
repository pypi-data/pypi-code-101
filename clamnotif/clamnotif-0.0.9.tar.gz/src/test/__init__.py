import os
import sys
import logging

# sys.path.insert(0, os.path.abspath(
#     os.path.join(os.path.dirname(__file__), '.')))

logging.basicConfig(format='[ClamNotif] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG)
