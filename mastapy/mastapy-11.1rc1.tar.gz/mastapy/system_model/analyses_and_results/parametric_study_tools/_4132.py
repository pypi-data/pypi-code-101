'''_4132.py

SpringDamperConnectionParametricStudyTool
'''


from typing import List

from mastapy.system_model.connections_and_sockets.couplings import _2077
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6660
from mastapy.system_model.analyses_and_results.system_deflections import _2530
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4049
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_CONNECTION_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'SpringDamperConnectionParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('SpringDamperConnectionParametricStudyTool',)


class SpringDamperConnectionParametricStudyTool(_4049.CouplingConnectionParametricStudyTool):
    '''SpringDamperConnectionParametricStudyTool

    This is a mastapy class.
    '''

    TYPE = _SPRING_DAMPER_CONNECTION_PARAMETRIC_STUDY_TOOL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpringDamperConnectionParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2077.SpringDamperConnection':
        '''SpringDamperConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2077.SpringDamperConnection)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign is not None else None

    @property
    def connection_load_case(self) -> '_6660.SpringDamperConnectionLoadCase':
        '''SpringDamperConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6660.SpringDamperConnectionLoadCase)(self.wrapped.ConnectionLoadCase) if self.wrapped.ConnectionLoadCase is not None else None

    @property
    def connection_system_deflection_results(self) -> 'List[_2530.SpringDamperConnectionSystemDeflection]':
        '''List[SpringDamperConnectionSystemDeflection]: 'ConnectionSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConnectionSystemDeflectionResults, constructor.new(_2530.SpringDamperConnectionSystemDeflection))
        return value
