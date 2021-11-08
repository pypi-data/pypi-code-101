
# module-level docstring
__doc__='''
General Utils module
====================

A collection of tools that do not fit in other modules.
'''

import pickle
from pathlib import Path
from typing import Any
import logging
log = logging.getLogger( __file__ )

def pickle_this( data: Any, save_file: Path ) -> None:
    ''' Stores `data` to a file '''
    with save_file.open(mode="wb") as fp:   #Pickling
        pickle.dump(data, fp)
        log.debug( "Successfully stored data to file %s.", save_file )
        

def unpickle_this( save_file: Path ) -> Any:
    ''' Reads data from a file that was created by `pickle_this` '''
    if not save_file.is_file():
        log.debug( "Could not find file %s.", save_file )
        return
    with save_file.open(mode="rb") as fp:   # Unpickling
        log.debug( "Successfully retrieved data from file %s.", save_file )
        return pickle.load(fp)
