'''_4082.py

HypoidGearParametricStudyTool
'''


from typing import List

from mastapy.system_model.part_model.gears import _2259
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6607
from mastapy.system_model.analyses_and_results.system_deflections import _2485
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4017
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'HypoidGearParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidGearParametricStudyTool',)


class HypoidGearParametricStudyTool(_4017.AGMAGleasonConicalGearParametricStudyTool):
    '''HypoidGearParametricStudyTool

    This is a mastapy class.
    '''

    TYPE = _HYPOID_GEAR_PARAMETRIC_STUDY_TOOL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'HypoidGearParametricStudyTool.TYPE'):
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
    def component_system_deflection_results(self) -> 'List[_2485.HypoidGearSystemDeflection]':
        '''List[HypoidGearSystemDeflection]: 'ComponentSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentSystemDeflectionResults, constructor.new(_2485.HypoidGearSystemDeflection))
        return value
