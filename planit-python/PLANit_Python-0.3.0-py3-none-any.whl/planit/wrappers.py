import os

from py4j.java_gateway import get_field
from planit import GatewayUtils

from numpy import string_

class BaseWrapper(object):
    """ Base wrapper class which always holds a java counter part instance and a generic way to pass on method calls to the encapsulated 
        Java instance. This allows one to use the Python naming conventions, i.e. get_x instead of getX() this is automatically catered for
        in these wrappers.
    """

    def __init__(self, java_counterpart):
        """Top-level constructor which defines the Java counterpart to each wrapper
            :param   the Java counterpart to the current object
        """
        self._java_counterpart = java_counterpart

    def __getattr__(self, name):
        """All methods invoked on the assignment wrapper are passed on to the Java equivalent class after transforming the method to
        Java style coding convention
        """            
        def method(*args): #collects the arguments of the function 'name' (wrapper function within getattr)    
            java_name = GatewayUtils.to_camelcase(name)
            # pass all calls on to the underlying PLANit project java class which is obtained via the entry_point.getProject call
            if( args ):                
                return getattr(self._java_counterpart, java_name)(*GatewayUtils.convert_args_to_java(args))
            else:
                return getattr(self._java_counterpart, java_name)()               
        return method
    
    @property
    def java(self):
        """ access to the underlying Java object if required
        """
        if (self._java_counterpart == None):
            raise Exception("No Java counterpart has been found for " + self.__class__.__name__)
        return self._java_counterpart 
    
    def field(self, fieldName):
        """ collect a publicly available member on the java object
        """
        return get_field(self.java, fieldName)