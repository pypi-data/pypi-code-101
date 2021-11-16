'''_6368.py

WormGearCriticalSpeedAnalysis
'''


from mastapy.system_model.part_model.gears import _2276
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6686
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6303
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses', 'WormGearCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearCriticalSpeedAnalysis',)


class WormGearCriticalSpeedAnalysis(_6303.GearCriticalSpeedAnalysis):
    '''WormGearCriticalSpeedAnalysis

    This is a mastapy class.
    '''

    TYPE = _WORM_GEAR_CRITICAL_SPEED_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'WormGearCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2276.WormGear':
        '''WormGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2276.WormGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6686.WormGearLoadCase':
        '''WormGearLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6686.WormGearLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None
