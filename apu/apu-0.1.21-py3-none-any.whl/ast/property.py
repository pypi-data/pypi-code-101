'''make a classmethod to a property'''


class ClassProperty(property):
    """inherit property to make a class method a property"""
    def __get__(self, cls, owner):
        '''get the function as class property'''
        return self.fget.__get__(None, owner)()
