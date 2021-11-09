class Map(dict):
    def __init__(self, *args, **kwargs):
        super(Map, self).__init__(**kwargs)
        for arg in args:
            if isinstance(arg, dict):
                for k, v in arg.items():
                    self[k] = v

        if kwargs:
            for k, v in kwargs.items():
                self[k] = v

    def __getattr__(self, attr):
        # return self.get(attr)
        try:
            return self.__getitem__(attr)
        except KeyError:
            raise AttributeError

    def __setattr__(self, key, value):
        self.__setitem__(key, value)

    def __setitem__(self, key, value):
        super(Map, self).__setitem__(key, value)
        # self.__dict__.update({key: value})

    def __delattr__(self, item):
        self.__delitem__(item)

    def __delitem__(self, key):
        super(Map, self).__delitem__(key)
        # del self.__dict__[key]

    def __str__(self):
        return super(dict, self).__str__()

    def __repr__(self):
        return super(dict, self).__repr__()

    def __eq__(self, other):
        return self.__class__ == other.__class__ and super(Map, self).__eq__(other)

    @classmethod
    def from_dict(cls, obj):
        ret = cls.__new__(cls)
        super(Map, ret).update(obj)
        return ret

    # def copy(self):
    #     attributes = super().copy()
    #     obj = Map(attributes)
    #     obj.__class__ = self.__class__
    #     obj.__module__ = self.__module__
    #     return obj
