'''_3780.py

ConceptGearPowerFlow
'''


from mastapy.system_model.part_model.gears import _2246
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6540
from mastapy.gears.rating.concept import _505
from mastapy.system_model.analyses_and_results.power_flows import _3810
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'ConceptGearPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGearPowerFlow',)


class ConceptGearPowerFlow(_3810.GearPowerFlow):
    '''ConceptGearPowerFlow

    This is a mastapy class.
    '''

    TYPE = _CONCEPT_GEAR_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConceptGearPowerFlow.TYPE'):
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
    def component_detailed_analysis(self) -> '_505.ConceptGearRating':
        '''ConceptGearRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_505.ConceptGearRating)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis is not None else None
