import sys
from inspect import currentframe
from types import ModuleType
from .wrappers import method_with_attrs

class SugarModule(ModuleType):
    def __new__(cls,global_vars=None,**kwargs):
        if global_vars is None:
            g = currentframe().f_back.f_globals
        else:
            g = global_vars
        sys.modules[g['__name__']].__class__ = cls
        return sys.modules[g['__name__']]

    def __init__(self,global_vars=None,mutable=False,private_default=False,export_all=False,doc=None,**kwargs):
        if global_vars is None:
            g = currentframe().f_back.f_globals
        else:
            g = global_vars
        super(SugarModule,self).__init__(g['__name__'],doc)
        getattr,setattr = SugarModule._getattr, SugarModule._setattr
        setattr(self,'_priv_def',private_default and not export_all)
        setattr(self,'_mut_def',mutable)
        setattr(self,'_mutable',[])
        setattr(self,'_immutable', [])
        setattr(self,'_private',['_private', '_immutable','_priv_def','_mut_def',
                        '_getattr','_setattr','private','meta'])
        if export_all:
            setattr(self,'export', (lambda self, x: x))
        else:
            setattr(self,'__all__', ['_can_access','_can_modify'])
        g.update(dict(
            this = self,
            private = getattr(self,'private'),
            mutable = getattr(self,'mutable'),
            immutable = getattr(self,'immutable'),
            public = getattr(self,'public'),
            mut = getattr(self,'mut'),
            const = getattr(self,'const'),
            export = getattr(self,'export'),
            meta = getattr(self,'meta'),
            _getattr = getattr(self,'_getattr'),
            _setattr = getattr(self,'_setattr'),
            ))
        getattr(self,'meta')(**kwargs)

    def _getattr(self, attr):
        return super(SugarModule,self).__getattribute__(attr)

    def _setattr(self, attr, val):
        super(SugarModule,self).__setattr__(attr, val)

    def _can_access(self, attr):
        if attr in SugarModule._getattr(self,'_private'):
            return False
        elif SugarModule._getattr(self,'_priv_def'):
            if attr.startswith('__'):
                return True
            elif attr in self.__all__:
                return True
            elif attr not in super(SugarModule,self).__dir__():
                return True
            else:
                return False
        else:
            return True

    def _can_modify(self, attr):
        if attr in SugarModule._getattr(self,'_mutable'):
            return True
        elif attr.startswith('_'):
            return False
        elif attr in SugarModule._getattr(self,'_immutable'):
            return False
        elif SugarModule._getattr(self,'_mut_def'):
            return True
        else:
            return False

    def __getattribute__(self, attr):
        if SugarModule._getattr(self,'_can_access')(attr):
            return SugarModule._getattr(self,attr)
        else:
            raise AttributeError(f"Unauthorized to access {self.__name__}.{attr}")

    def __setattr__(self, attr, val):
        if self._can_modify(attr):
            SugarModule._setattr(self,attr,val)
        else:
            raise AttributeError(f"{self.__name__}.{attr} is immutable")

    def __dir__(self):
        return list(filter(self._can_access, super(SugarModule,self).__dir__()))

    @method_with_attrs
    def private(self,v):
        if isinstance(v,str):
            name = v
        else:
            name = v.__name__
        SugarModule._setattr(self,'_private',SugarModule._getattr(self,'_private')+[name])
        return v

    private.fget.getter(_getattr)

    private.fget.setter(_setattr)

    @private.fget.lister
    def _(self):
        return list(filter(lambda v: not self._can_access(v), super(SugarModule,self).__dir__()))

    @method_with_attrs
    def public(self,v):
        if isinstance(v,str):
            if v.startswith('private.'):
                name = v[8:]
            else:
                name = v
        else:
            name = v.__name__
        SugarModule._setattr(self,'__all__',self.__all__+[name])
        return v

    public.fget.getter(getattr)

    @public.fget.setter
    def _(self,attr,val):
        if attr in super(SugarModule,self).__dir__():
            if not self._can_access(attr):
                raise AttributeError(f"Unauthorized to access {self.__name__}.{attr}")
            if not self._can_modify(attr):
                raise AttributeError(f"{self.__name__}.{attr} is immutable")
        if not attr in self.__all__:
            SugarModule._setattr(self,'__all__',self.__all__+[attr])
        setattr(self,attr,val)


    public.fget.lister(dir)

    export = public

    @method_with_attrs
    def mutable(self,v):
        if isinstance(v,str):
            name = v
        else:
            name = v.__name__
        SugarModule._setattr(self,'_mutable',self._mutable+[name])
        return v

    @mutable.fget.getter
    def _(self,attr):
        if not self._can_access(attr):
            raise AttributeError(f"Unauthorized to access {self.__name__}.{attr}")
        if (attr in SugarModule._getattr(self,'_immutable') or
                (attr in dir(self) and not SugarModule._getattr(self,'_mut_def'))):
            raise AttributeError(f"{self.__name__}.{attr} is immutable")
        if attr not in self._mutable:
            SugarModule._setattr(self,'_mutable',self._mutable+[attr])
            if attr not in dir(self):
                setattr(self,attr,None)
        return getattr(self,attr)

    @mutable.fget.setter
    def _(self,attr,val):
        if not self._can_access(attr):
            raise AttributeError(f"Unauthorized to access {self.__name__}.{attr}")
        if (attr in SugarModule._getattr(self,'_immutable') or
                (attr in dir(self) and not SugarModule._getattr(self,'_mut_def'))):
            raise AttributeError(f"{self.__name__}.{attr} is immutable")
        if attr not in self._mutable:
            SugarModule._setattr(self,'_mutable',self._mutable+[attr])
        setattr(self,attr,val)

    @mutable.fget.lister
    def _(self):
        return list(filter(self._can_modify, dir(self)))

    mut = mutable

    @method_with_attrs
    def immutable(self,v):
        if isinstance(v,str):
            name = v
        else:
            name = v.__name__
        SugarModule._setattr(self,'_immutable',SugarModule._getattr(self,'_immutable')+[name])
        return v

    immutable.fget.getter(getattr)

    @immutable.fget.setter
    def _(self,attr,val):
        if not self._can_access(attr):
            raise AttributeError(f"Unauthorized to access {self.__name__}.{attr}")
        if attr in dir(self):
            raise AttributeError(f"{self.__name__}.{attr} already exists")
        SugarModule._setattr(self,'_immutable',SugarModule._getattr(self,'_immutable')+[attr])
        SugarModule._setattr(self,attr,val)

    @immutable.fget.lister
    def _(self):
        return list(filter(lambda v: not self._can_modify(v), dir(self)))

    const = immutable

    @method_with_attrs
    def meta(self,doc=None,**kwargs):
        if doc is not None:
            SugarModule._setattr(self,'__doc__',doc)
        for tag, val in kwargs.items():
            SugarModule._setattr(self,f'__{tag}__',val)

    @meta.fget.getter
    def _(self,attr):
        if self._can_access(attr):
            return attr
        else:
            return 'private.'+attr
