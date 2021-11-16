'''_4906.py

ShaftHubConnectionModalAnalysis
'''


from typing import List

from mastapy.system_model.part_model.couplings import _2323
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6652
from mastapy.system_model.analyses_and_results.system_deflections import _2521
from mastapy.system_model.analyses_and_results.modal_analyses import _4841
from mastapy._internal.python_net import python_net_import

_SHAFT_HUB_CONNECTION_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses', 'ShaftHubConnectionModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftHubConnectionModalAnalysis',)


class ShaftHubConnectionModalAnalysis(_4841.ConnectorModalAnalysis):
    '''ShaftHubConnectionModalAnalysis

    This is a mastapy class.
    '''

    TYPE = _SHAFT_HUB_CONNECTION_MODAL_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ShaftHubConnectionModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2323.ShaftHubConnection':
        '''ShaftHubConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2323.ShaftHubConnection)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6652.ShaftHubConnectionLoadCase':
        '''ShaftHubConnectionLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6652.ShaftHubConnectionLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None

    @property
    def system_deflection_results(self) -> '_2521.ShaftHubConnectionSystemDeflection':
        '''ShaftHubConnectionSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2521.ShaftHubConnectionSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def planetaries(self) -> 'List[ShaftHubConnectionModalAnalysis]':
        '''List[ShaftHubConnectionModalAnalysis]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Planetaries, constructor.new(ShaftHubConnectionModalAnalysis))
        return value
