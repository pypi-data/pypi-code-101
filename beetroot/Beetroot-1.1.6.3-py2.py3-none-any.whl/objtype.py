#Dependency function of like almost every class
from .exception import *

def objtype(obj):
    return str(type(obj))[8:-2]