'''_2561.py

ZerolBevelGearSystemDeflection
'''


from mastapy.system_model.part_model.gears import _2278
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6689
from mastapy.system_model.analyses_and_results.power_flows import _3881
from mastapy.gears.rating.zerol_bevel import _335
from mastapy.system_model.analyses_and_results.system_deflections import _2428
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'ZerolBevelGearSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('ZerolBevelGearSystemDeflection',)


class ZerolBevelGearSystemDeflection(_2428.BevelGearSystemDeflection):
    '''ZerolBevelGearSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _ZEROL_BEVEL_GEAR_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ZerolBevelGearSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2278.ZerolBevelGear':
        '''ZerolBevelGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2278.ZerolBevelGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6689.ZerolBevelGearLoadCase':
        '''ZerolBevelGearLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6689.ZerolBevelGearLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None

    @property
    def power_flow_results(self) -> '_3881.ZerolBevelGearPowerFlow':
        '''ZerolBevelGearPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_3881.ZerolBevelGearPowerFlow)(self.wrapped.PowerFlowResults) if self.wrapped.PowerFlowResults is not None else None

    @property
    def component_detailed_analysis(self) -> '_335.ZerolBevelGearRating':
        '''ZerolBevelGearRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_335.ZerolBevelGearRating)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis is not None else None
