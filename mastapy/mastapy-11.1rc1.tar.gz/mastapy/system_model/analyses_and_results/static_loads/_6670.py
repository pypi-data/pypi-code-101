'''_6670.py

StraightBevelSunGearLoadCase
'''


from mastapy.system_model.part_model.gears import _2275
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6663
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_SUN_GEAR_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'StraightBevelSunGearLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelSunGearLoadCase',)


class StraightBevelSunGearLoadCase(_6663.StraightBevelDiffGearLoadCase):
    '''StraightBevelSunGearLoadCase

    This is a mastapy class.
    '''

    TYPE = _STRAIGHT_BEVEL_SUN_GEAR_LOAD_CASE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'StraightBevelSunGearLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2275.StraightBevelSunGear':
        '''StraightBevelSunGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2275.StraightBevelSunGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None
