'''_4125.py

ShaftHubConnectionParametricStudyTool
'''


from typing import List

from mastapy.system_model.part_model.couplings import _2323
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6652
from mastapy.system_model.analyses_and_results.system_deflections import _2521
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4048
from mastapy._internal.python_net import python_net_import

_SHAFT_HUB_CONNECTION_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'ShaftHubConnectionParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftHubConnectionParametricStudyTool',)


class ShaftHubConnectionParametricStudyTool(_4048.ConnectorParametricStudyTool):
    '''ShaftHubConnectionParametricStudyTool

    This is a mastapy class.
    '''

    TYPE = _SHAFT_HUB_CONNECTION_PARAMETRIC_STUDY_TOOL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ShaftHubConnectionParametricStudyTool.TYPE'):
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
    def planetaries(self) -> 'List[ShaftHubConnectionParametricStudyTool]':
        '''List[ShaftHubConnectionParametricStudyTool]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Planetaries, constructor.new(ShaftHubConnectionParametricStudyTool))
        return value

    @property
    def component_system_deflection_results(self) -> 'List[_2521.ShaftHubConnectionSystemDeflection]':
        '''List[ShaftHubConnectionSystemDeflection]: 'ComponentSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentSystemDeflectionResults, constructor.new(_2521.ShaftHubConnectionSystemDeflection))
        return value
