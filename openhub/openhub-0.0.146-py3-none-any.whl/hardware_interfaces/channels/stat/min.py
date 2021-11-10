from .stat_interface import StatInterface

class Min(StatInterface):
    def __init__(self,dct=None,id=None,value=None):
        super().__init__(dct=dct, id=None, value=None)

    def update(self, value):
        if value < self.value:
            self.value = value
            self.check_if_value_updated()
