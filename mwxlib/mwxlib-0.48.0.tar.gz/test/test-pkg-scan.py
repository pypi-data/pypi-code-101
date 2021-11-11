#! python3
# -*- coding: utf-8 -*-
"""
C:/Python38/Lib/pydoc.py:2116 class ModuleScanner:
C:/Python38/Lib/pydoc.py:2177 def apropos(key):
"""
import warnings
import pkgutil
import pydoc
import misc


N = len(list(pkgutil.iter_modules()))
print("N =", N)

lm = []

def _callback(path, modname, desc):
    lm.append(modname)
    print('\b'*88 + "Scanning {:70s}".format(modname[:70]), end='')

def _error(modname):
    print('\b'*77 + "- failed: {}".format(modname))

@misc.timeit
def scan():
    with warnings.catch_warnings():
        warnings.simplefilter('ignore') # ignore problems during import
        pydoc.ModuleScanner().run(_callback, key='', onerror=_error)

@misc.timeit
def walk():
    ## pkgutil fast? no path, no source, no description
    n = 0
    for _importer, modname, _ispkg in pkgutil.walk_packages(onerror=_error):
        if '.' not in modname:
            n += 1
        _callback(None, modname, '')
        print("{:3d}/{:3d}".format(n, N), end='')

if __name__ == '__main__':
    scan() # => 120s no cache (26s with cache)
    walk() # => 11s no cache (2.5s with cache)
