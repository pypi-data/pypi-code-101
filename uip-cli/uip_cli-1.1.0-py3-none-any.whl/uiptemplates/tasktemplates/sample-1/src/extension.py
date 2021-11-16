"""Sample-1: implementation of sample Universal Extension module."""
 
from __future__ import (print_function)
from universal_extension import UniversalExtension
from universal_extension import ExtensionResult
 
class Extension(UniversalExtension):
    """Universal Extension sample module."""
 
    def __init__(self):
        """Init class."""
        super(Extension, self).__init__()
 
    def extension_start(self, fields):
        """Universal Extension primary operation."""

        # Print hello message to standard output...
        print('Hello STDOUT!')

        # Print hello message to standard error...
        self.log.info('Hello STDERR!')

        # Return the result with a payload of "Hello" string...
        return ExtensionResult(
            unv_output = 'Hello Extension!'
            )