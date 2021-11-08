from importlib.metadata import version
try:
    __version__ = version('akerbp.models')
except:
   __version__ = 'unknown' 

