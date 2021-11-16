'''_5991.py

BevelDifferentialGearSetDynamicAnalysis
'''


from typing import List

from mastapy.system_model.part_model.gears import _2241
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6524
from mastapy.system_model.analyses_and_results.dynamic_analyses import _5989, _5990, _5996
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_SET_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses', 'BevelDifferentialGearSetDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialGearSetDynamicAnalysis',)


class BevelDifferentialGearSetDynamicAnalysis(_5996.BevelGearSetDynamicAnalysis):
    '''BevelDifferentialGearSetDynamicAnalysis

    This is a mastapy class.
    '''

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_SET_DYNAMIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BevelDifferentialGearSetDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2241.BevelDifferentialGearSet':
        '''BevelDifferentialGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2241.BevelDifferentialGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_load_case(self) -> '_6524.BevelDifferentialGearSetLoadCase':
        '''BevelDifferentialGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6524.BevelDifferentialGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase is not None else None

    @property
    def bevel_differential_gears_dynamic_analysis(self) -> 'List[_5989.BevelDifferentialGearDynamicAnalysis]':
        '''List[BevelDifferentialGearDynamicAnalysis]: 'BevelDifferentialGearsDynamicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelDifferentialGearsDynamicAnalysis, constructor.new(_5989.BevelDifferentialGearDynamicAnalysis))
        return value

    @property
    def bevel_differential_meshes_dynamic_analysis(self) -> 'List[_5990.BevelDifferentialGearMeshDynamicAnalysis]':
        '''List[BevelDifferentialGearMeshDynamicAnalysis]: 'BevelDifferentialMeshesDynamicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelDifferentialMeshesDynamicAnalysis, constructor.new(_5990.BevelDifferentialGearMeshDynamicAnalysis))
        return value
