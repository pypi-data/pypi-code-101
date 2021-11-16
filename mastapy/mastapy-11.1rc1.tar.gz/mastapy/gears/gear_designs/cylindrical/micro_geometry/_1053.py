'''_1053.py

CylindricalGearSetMicroGeometryDutyCycle
'''


from typing import List

from mastapy.gears.rating.cylindrical import _426
from mastapy._internal import constructor, conversion
from mastapy.gears.gear_two_d_fe_analysis import _851
from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1046
from mastapy.gears.analysis import _1169
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_MICRO_GEOMETRY_DUTY_CYCLE = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry', 'CylindricalGearSetMicroGeometryDutyCycle')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearSetMicroGeometryDutyCycle',)


class CylindricalGearSetMicroGeometryDutyCycle(_1169.GearSetImplementationAnalysisDutyCycle):
    '''CylindricalGearSetMicroGeometryDutyCycle

    This is a mastapy class.
    '''

    TYPE = _CYLINDRICAL_GEAR_SET_MICRO_GEOMETRY_DUTY_CYCLE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearSetMicroGeometryDutyCycle.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rating(self) -> '_426.CylindricalGearSetDutyCycleRating':
        '''CylindricalGearSetDutyCycleRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_426.CylindricalGearSetDutyCycleRating)(self.wrapped.Rating) if self.wrapped.Rating is not None else None

    @property
    def tiff_analysis(self) -> '_851.CylindricalGearSetTIFFAnalysisDutyCycle':
        '''CylindricalGearSetTIFFAnalysisDutyCycle: 'TIFFAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_851.CylindricalGearSetTIFFAnalysisDutyCycle)(self.wrapped.TIFFAnalysis) if self.wrapped.TIFFAnalysis is not None else None

    @property
    def meshes(self) -> 'List[_1046.CylindricalGearMeshMicroGeometryDutyCycle]':
        '''List[CylindricalGearMeshMicroGeometryDutyCycle]: 'Meshes' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Meshes, constructor.new(_1046.CylindricalGearMeshMicroGeometryDutyCycle))
        return value
