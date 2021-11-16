'''_851.py

CylindricalGearSetTIFFAnalysisDutyCycle
'''


from typing import List

from mastapy.gears.gear_two_d_fe_analysis import _853
from mastapy._internal import constructor, conversion
from mastapy.gears.analysis import _1165
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_TIFF_ANALYSIS_DUTY_CYCLE = python_net_import('SMT.MastaAPI.Gears.GearTwoDFEAnalysis', 'CylindricalGearSetTIFFAnalysisDutyCycle')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearSetTIFFAnalysisDutyCycle',)


class CylindricalGearSetTIFFAnalysisDutyCycle(_1165.GearSetDesignAnalysis):
    '''CylindricalGearSetTIFFAnalysisDutyCycle

    This is a mastapy class.
    '''

    TYPE = _CYLINDRICAL_GEAR_SET_TIFF_ANALYSIS_DUTY_CYCLE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearSetTIFFAnalysisDutyCycle.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gears(self) -> 'List[_853.CylindricalGearTIFFAnalysisDutyCycle]':
        '''List[CylindricalGearTIFFAnalysisDutyCycle]: 'Gears' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Gears, constructor.new(_853.CylindricalGearTIFFAnalysisDutyCycle))
        return value
