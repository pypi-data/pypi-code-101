import sys, os
from . import Path, Put, Snapshot

import time

try:
    from core.config import DELAY_INTERVAL 
except ImportError as error:
    sys.exit('Please DELAY_INTERVAL in configure .config.py')

try:
    from core.utils import send_email as send_email
except ImportError as error:
    print('No utility found, using system defaults')
    from .utils import send_email as send_email
finally:

    __all__ = ['Sentinel']

    class Sentinel:

        INTERVAL = DELAY_INTERVAL

        def __init__(self, src_path:Path, dst_path:Path):
            self.src = src_path
            self.dst = dst_path

        def snap(self):
            """
            Returns a snapshot of the current src directory
            """
            return Snapshot(self.src)

        def changes(self, interval=INTERVAL):
            """
            Returns the changes in a given directory that happened 
            within the specified interval
            """
            snap1 = self.snap()
            time.sleep(interval)
            snap2 = self.snap()
            return snap1.compare(snap2)

        def transfer_files(self):
            """
            If changes are found, place them in the Put directory
            """
            changes = self.changes()
            for status, files in changes.items():
                if status == 'created':
                    for f in files:
                        print(f)
                        print(self.dst)
                        try:
                            Put(f, self.dst).put()
                            utils.send_email(f'{f.__class__.__name__} Transfer Found', f.__str__())
                        except Exception as e:
                            utils.send_email(f'{f.__class__.__name__} Transfer Found', f'AN ERROR OCCURED: {e} ')
                            print(e)

        def run(self):
            """
            Consistant loop of transfer_files
            """
            while True:
                self.transfer_files()


        
