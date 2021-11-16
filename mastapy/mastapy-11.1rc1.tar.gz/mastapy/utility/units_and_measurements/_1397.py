'''_1397.py

TimeUnit
'''


from mastapy.utility.units_and_measurements import _1398
from mastapy._internal.python_net import python_net_import

_TIME_UNIT = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements', 'TimeUnit')


__docformat__ = 'restructuredtext en'
__all__ = ('TimeUnit',)


class TimeUnit(_1398.Unit):
    '''TimeUnit

    This is a mastapy class.
    '''

    TYPE = _TIME_UNIT

    __hash__ = None

    def __init__(self, instance_to_wrap: 'TimeUnit.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
