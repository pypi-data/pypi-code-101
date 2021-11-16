'''_683.py

CylindricalGearPlungeShaverDatabase
'''


from mastapy.gears.manufacturing.cylindrical import _564
from mastapy.gears.manufacturing.cylindrical.cutters import _682
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_PLUNGE_SHAVER_DATABASE = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters', 'CylindricalGearPlungeShaverDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearPlungeShaverDatabase',)


class CylindricalGearPlungeShaverDatabase(_564.CylindricalCutterDatabase['_682.CylindricalGearPlungeShaver']):
    '''CylindricalGearPlungeShaverDatabase

    This is a mastapy class.
    '''

    TYPE = _CYLINDRICAL_GEAR_PLUNGE_SHAVER_DATABASE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearPlungeShaverDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
