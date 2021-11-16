'''_6799.py

PlanetCarrierAdvancedTimeSteppingAnalysisForModulation
'''


from mastapy.system_model.part_model import _2195
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6638
from mastapy.system_model.analyses_and_results.system_deflections import _2510
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6791
from mastapy._internal.python_net import python_net_import

_PLANET_CARRIER_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation', 'PlanetCarrierAdvancedTimeSteppingAnalysisForModulation')


__docformat__ = 'restructuredtext en'
__all__ = ('PlanetCarrierAdvancedTimeSteppingAnalysisForModulation',)


class PlanetCarrierAdvancedTimeSteppingAnalysisForModulation(_6791.MountableComponentAdvancedTimeSteppingAnalysisForModulation):
    '''PlanetCarrierAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    '''

    TYPE = _PLANET_CARRIER_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PlanetCarrierAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2195.PlanetCarrier':
        '''PlanetCarrier: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2195.PlanetCarrier)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6638.PlanetCarrierLoadCase':
        '''PlanetCarrierLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6638.PlanetCarrierLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None

    @property
    def system_deflection_results(self) -> '_2510.PlanetCarrierSystemDeflection':
        '''PlanetCarrierSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2510.PlanetCarrierSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None
