'''_575.py

CylindricalManufacturedGearSetLoadCase
'''


from mastapy.gears.rating.cylindrical import _427
from mastapy._internal import constructor
from mastapy.gears.manufacturing.cylindrical import _579
from mastapy.gears.analysis import _1167
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_MANUFACTURED_GEAR_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical', 'CylindricalManufacturedGearSetLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalManufacturedGearSetLoadCase',)


class CylindricalManufacturedGearSetLoadCase(_1167.GearSetImplementationAnalysis):
    '''CylindricalManufacturedGearSetLoadCase

    This is a mastapy class.
    '''

    TYPE = _CYLINDRICAL_MANUFACTURED_GEAR_SET_LOAD_CASE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalManufacturedGearSetLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rating(self) -> '_427.CylindricalGearSetRating':
        '''CylindricalGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_427.CylindricalGearSetRating)(self.wrapped.Rating) if self.wrapped.Rating is not None else None

    @property
    def manufacturing_configuration(self) -> '_579.CylindricalSetManufacturingConfig':
        '''CylindricalSetManufacturingConfig: 'ManufacturingConfiguration' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_579.CylindricalSetManufacturingConfig)(self.wrapped.ManufacturingConfiguration) if self.wrapped.ManufacturingConfiguration is not None else None
