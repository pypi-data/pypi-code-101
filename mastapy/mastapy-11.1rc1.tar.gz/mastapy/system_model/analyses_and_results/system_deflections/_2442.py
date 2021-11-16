'''_2442.py

ConceptGearSystemDeflection
'''


from mastapy.system_model.part_model.gears import _2246
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6540
from mastapy.system_model.analyses_and_results.power_flows import _3780
from mastapy.gears.rating.concept import _505
from mastapy.system_model.analyses_and_results.system_deflections import _2481
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'ConceptGearSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGearSystemDeflection',)


class ConceptGearSystemDeflection(_2481.GearSystemDeflection):
    '''ConceptGearSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _CONCEPT_GEAR_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConceptGearSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2246.ConceptGear':
        '''ConceptGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2246.ConceptGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6540.ConceptGearLoadCase':
        '''ConceptGearLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6540.ConceptGearLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None

    @property
    def power_flow_results(self) -> '_3780.ConceptGearPowerFlow':
        '''ConceptGearPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_3780.ConceptGearPowerFlow)(self.wrapped.PowerFlowResults) if self.wrapped.PowerFlowResults is not None else None

    @property
    def component_detailed_analysis(self) -> '_505.ConceptGearRating':
        '''ConceptGearRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_505.ConceptGearRating)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis is not None else None
