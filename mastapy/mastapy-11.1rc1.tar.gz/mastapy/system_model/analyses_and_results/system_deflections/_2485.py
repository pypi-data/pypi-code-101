'''_2485.py

HypoidGearSystemDeflection
'''


from mastapy.system_model.part_model.gears import _2259
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6607
from mastapy.system_model.analyses_and_results.power_flows import _3814
from mastapy.gears.rating.hypoid import _404
from mastapy.system_model.analyses_and_results.system_deflections import _2416
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'HypoidGearSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidGearSystemDeflection',)


class HypoidGearSystemDeflection(_2416.AGMAGleasonConicalGearSystemDeflection):
    '''HypoidGearSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _HYPOID_GEAR_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'HypoidGearSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2259.HypoidGear':
        '''HypoidGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2259.HypoidGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6607.HypoidGearLoadCase':
        '''HypoidGearLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6607.HypoidGearLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None

    @property
    def power_flow_results(self) -> '_3814.HypoidGearPowerFlow':
        '''HypoidGearPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_3814.HypoidGearPowerFlow)(self.wrapped.PowerFlowResults) if self.wrapped.PowerFlowResults is not None else None

    @property
    def component_detailed_analysis(self) -> '_404.HypoidGearRating':
        '''HypoidGearRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_404.HypoidGearRating)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis is not None else None
