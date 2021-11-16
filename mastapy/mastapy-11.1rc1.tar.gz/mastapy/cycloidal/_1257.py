'''_1257.py

RingPinsMaterialDatabase
'''


from mastapy.materials import _240
from mastapy.cycloidal import _1256
from mastapy._internal.python_net import python_net_import

_RING_PINS_MATERIAL_DATABASE = python_net_import('SMT.MastaAPI.Cycloidal', 'RingPinsMaterialDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('RingPinsMaterialDatabase',)


class RingPinsMaterialDatabase(_240.MaterialDatabase['_1256.RingPinsMaterial']):
    '''RingPinsMaterialDatabase

    This is a mastapy class.
    '''

    TYPE = _RING_PINS_MATERIAL_DATABASE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'RingPinsMaterialDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
