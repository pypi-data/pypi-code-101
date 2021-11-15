from inspect import getfullargspec
from functools import wraps
from .stubs import FuncNotImplemented

def eat_interrupt(func):
    """Wrapper to make functions stop on Ctrl-C without killing program"""
    @wraps(func)
    def wrapper(*args,**kwargs):
        try:
            return func(*args,**kwargs)
        except KeyboardInterrupt as e:
            print(f"ALERT! Ctrl-C Safe Function <{func.__qualname__}> interupted, continuing program")
    return wrapper

def eat_arg(func):
    """Wrapper to make functions ignore an extra first argument (like self or cls)"""
    @wraps(func)
    def wrapper(_,*args,**kwargs):
        return func(*args,**kwargs)
    return wrapper

def try_override(func):
    """Tries to override a method, falls back to inhereted on exception"""
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except Exception as e:
            print(f"{func.__name__} recieved exception: {e}, falling back on super().{func.__name__}")
            getattr(super(self.__class__, self),func.__name__)(*args,**kwargs)
    return wrapper

class Partial():
    """Partial parameter @ hack: allows partial application with func@Partial(args,kw=arg)"""
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
    def __rmatmul__(self, other):
        @wraps(other)
        def wrapper(*args, **kwargs):
            return other(*self.args, *args, **self.kwargs, **kwargs)
        return wrapper

def method_with_attrs(method):
    fs = getfullargspec(method)
    do_loop = ((len(fs.args) - len((fs.defaults if fs.defaults is not None else [])))<= 2 and fs.varargs is None)
    class _f():
        loop_over_args = do_loop
        func = staticmethod(method)
        _getattr = FuncNotImplemented
        _setattr = FuncNotImplemented
        _dir = FuncNotImplemented
        def __init__(self,parent):
            super(_f,self).__setattr__('parent',parent)
        def __call__(self,*args,**kwargs):
            if self.loop_over_args:
                return [self.func(super(_f,self).__getattribute__('parent'),arg,**kwargs) for arg in args]
            else:
                return self.func(super(_f,self).__getattribute__('parent'),*args,**kwargs)
        @classmethod
        def getter(cls, getfunc):
            cls._getattr = staticmethod(getfunc)
        @classmethod
        def setter(cls, setfunc):
            cls._setattr = staticmethod(setfunc)
        @classmethod
        def lister(cls, listfunc):
            cls._dir = staticmethod(listfunc)
        def __dir__(self):
            return self._dir(super(_f,self).__getattribute__('parent'))
        def __getattr__(self,attr):
            return self._getattr(super(_f,self).__getattribute__('parent'),attr)
        def __setattr__(self,attr,val):
            return self._setattr(super(_f,self).__getattribute__('parent'),attr,val)
    _f.__name__ = method.__name__
    _f.__doc__ = method.__doc__
    _f.__qualname__ = method.__qualname__
    return property(_f)


