'''_2846.py

BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft
'''


from typing import List

from mastapy.system_model.part_model.gears import _2241
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _2844, _2845, _2851
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _2715
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound', 'BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft',)


class BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft(_2851.BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft):
    '''BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    '''

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2241.BevelDifferentialGearSet':
        '''BevelDifferentialGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2241.BevelDifferentialGearSet)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def assembly_design(self) -> '_2241.BevelDifferentialGearSet':
        '''BevelDifferentialGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2241.BevelDifferentialGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def bevel_differential_gears_compound_steady_state_synchronous_response_on_a_shaft(self) -> 'List[_2844.BevelDifferentialGearCompoundSteadyStateSynchronousResponseOnAShaft]':
        '''List[BevelDifferentialGearCompoundSteadyStateSynchronousResponseOnAShaft]: 'BevelDifferentialGearsCompoundSteadyStateSynchronousResponseOnAShaft' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelDifferentialGearsCompoundSteadyStateSynchronousResponseOnAShaft, constructor.new(_2844.BevelDifferentialGearCompoundSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def bevel_differential_meshes_compound_steady_state_synchronous_response_on_a_shaft(self) -> 'List[_2845.BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseOnAShaft]':
        '''List[BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseOnAShaft]: 'BevelDifferentialMeshesCompoundSteadyStateSynchronousResponseOnAShaft' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelDifferentialMeshesCompoundSteadyStateSynchronousResponseOnAShaft, constructor.new(_2845.BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_2715.BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft]':
        '''List[BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCasesReady, constructor.new(_2715.BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_2715.BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft]':
        '''List[BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCases, constructor.new(_2715.BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft))
        return value
