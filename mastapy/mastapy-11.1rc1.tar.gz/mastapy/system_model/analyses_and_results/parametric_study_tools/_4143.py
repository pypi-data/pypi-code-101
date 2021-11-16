'''_4143.py

SynchroniserHalfParametricStudyTool
'''


from typing import List

from mastapy.system_model.part_model.couplings import _2329
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6671
from mastapy.system_model.analyses_and_results.system_deflections import _2541
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4145
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_HALF_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'SynchroniserHalfParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('SynchroniserHalfParametricStudyTool',)


class SynchroniserHalfParametricStudyTool(_4145.SynchroniserPartParametricStudyTool):
    '''SynchroniserHalfParametricStudyTool

    This is a mastapy class.
    '''

    TYPE = _SYNCHRONISER_HALF_PARAMETRIC_STUDY_TOOL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SynchroniserHalfParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2329.SynchroniserHalf':
        '''SynchroniserHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2329.SynchroniserHalf)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6671.SynchroniserHalfLoadCase':
        '''SynchroniserHalfLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6671.SynchroniserHalfLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None

    @property
    def component_system_deflection_results(self) -> 'List[_2541.SynchroniserHalfSystemDeflection]':
        '''List[SynchroniserHalfSystemDeflection]: 'ComponentSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentSystemDeflectionResults, constructor.new(_2541.SynchroniserHalfSystemDeflection))
        return value
