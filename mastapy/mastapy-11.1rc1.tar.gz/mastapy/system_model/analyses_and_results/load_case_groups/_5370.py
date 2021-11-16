'''_5370.py

AbstractStaticLoadCaseGroup
'''


from typing import List

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.system_model.analyses_and_results.load_case_groups import (
    _5380, _5379, _5368, _5378,
    _5369
)
from mastapy.system_model.analyses_and_results.static_loads import (
    _6504, _6519, _6642, _6641,
    _6560, _6562, _6564, _6587,
    _6517
)
from mastapy.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups import _5383, _5386, _5387
from mastapy.system_model.part_model import (
    _2167, _2198, _2197, _2179
)
from mastapy.system_model.part_model.gears import _2251, _2250
from mastapy.system_model.connections_and_sockets.gears import _2036
from mastapy.system_model.analyses_and_results.power_flows.compound import _3932
from mastapy.system_model.analyses_and_results import (
    _2406, _2401, _2383, _2393,
    _2403, _2396, _2386, _2402,
    _2385, _2390, _2344
)
from mastapy._internal.python_net import python_net_import

_ABSTRACT_STATIC_LOAD_CASE_GROUP = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.LoadCaseGroups', 'AbstractStaticLoadCaseGroup')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractStaticLoadCaseGroup',)


class AbstractStaticLoadCaseGroup(_5369.AbstractLoadCaseGroup):
    '''AbstractStaticLoadCaseGroup

    This is a mastapy class.
    '''

    TYPE = _ABSTRACT_STATIC_LOAD_CASE_GROUP

    __hash__ = None

    def __init__(self, instance_to_wrap: 'AbstractStaticLoadCaseGroup.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def max_number_of_load_cases_to_display(self) -> 'int':
        '''int: 'MaxNumberOfLoadCasesToDisplay' is the original name of this property.'''

        return self.wrapped.MaxNumberOfLoadCasesToDisplay

    @max_number_of_load_cases_to_display.setter
    def max_number_of_load_cases_to_display(self, value: 'int'):
        self.wrapped.MaxNumberOfLoadCasesToDisplay = int(value) if value else 0

    @property
    def number_of_possible_system_designs(self) -> 'int':
        '''int: 'NumberOfPossibleSystemDesigns' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.NumberOfPossibleSystemDesigns

    @property
    def system_optimiser_log(self) -> 'str':
        '''str: 'SystemOptimiserLog' is the original name of this property.'''

        return self.wrapped.SystemOptimiserLog

    @system_optimiser_log.setter
    def system_optimiser_log(self, value: 'str'):
        self.wrapped.SystemOptimiserLog = str(value) if value else ''

    @property
    def optimum_tooth_numbers_target(self) -> '_5380.SystemOptimiserTargets':
        '''SystemOptimiserTargets: 'OptimumToothNumbersTarget' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.OptimumToothNumbersTarget)
        return constructor.new(_5380.SystemOptimiserTargets)(value) if value is not None else None

    @optimum_tooth_numbers_target.setter
    def optimum_tooth_numbers_target(self, value: '_5380.SystemOptimiserTargets'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.OptimumToothNumbersTarget = value

    @property
    def gear_set_optimisation(self) -> '_5379.SystemOptimiserGearSetOptimisation':
        '''SystemOptimiserGearSetOptimisation: 'GearSetOptimisation' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.GearSetOptimisation)
        return constructor.new(_5379.SystemOptimiserGearSetOptimisation)(value) if value is not None else None

    @gear_set_optimisation.setter
    def gear_set_optimisation(self, value: '_5379.SystemOptimiserGearSetOptimisation'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.GearSetOptimisation = value

    @property
    def number_of_configurations_to_create(self) -> 'int':
        '''int: 'NumberOfConfigurationsToCreate' is the original name of this property.'''

        return self.wrapped.NumberOfConfigurationsToCreate

    @number_of_configurations_to_create.setter
    def number_of_configurations_to_create(self, value: 'int'):
        self.wrapped.NumberOfConfigurationsToCreate = int(value) if value else 0

    @property
    def static_loads(self) -> 'List[_6504.StaticLoadCase]':
        '''List[StaticLoadCase]: 'StaticLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StaticLoads, constructor.new(_6504.StaticLoadCase))
        return value

    @property
    def static_loads_limited_by_max_number_of_load_cases_to_display(self) -> 'List[_6504.StaticLoadCase]':
        '''List[StaticLoadCase]: 'StaticLoadsLimitedByMaxNumberOfLoadCasesToDisplay' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StaticLoadsLimitedByMaxNumberOfLoadCasesToDisplay, constructor.new(_6504.StaticLoadCase))
        return value

    @property
    def bearings(self) -> 'List[_5383.ComponentStaticLoadCaseGroup[_2167.Bearing, _6519.BearingLoadCase]]':
        '''List[ComponentStaticLoadCaseGroup[Bearing, BearingLoadCase]]: 'Bearings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bearings, constructor.new(_5383.ComponentStaticLoadCaseGroup)[_2167.Bearing, _6519.BearingLoadCase])
        return value

    @property
    def power_loads(self) -> 'List[_5383.ComponentStaticLoadCaseGroup[_2198.PowerLoad, _6642.PowerLoadLoadCase]]':
        '''List[ComponentStaticLoadCaseGroup[PowerLoad, PowerLoadLoadCase]]: 'PowerLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PowerLoads, constructor.new(_5383.ComponentStaticLoadCaseGroup)[_2198.PowerLoad, _6642.PowerLoadLoadCase])
        return value

    @property
    def point_loads(self) -> 'List[_5383.ComponentStaticLoadCaseGroup[_2197.PointLoad, _6641.PointLoadLoadCase]]':
        '''List[ComponentStaticLoadCaseGroup[PointLoad, PointLoadLoadCase]]: 'PointLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PointLoads, constructor.new(_5383.ComponentStaticLoadCaseGroup)[_2197.PointLoad, _6641.PointLoadLoadCase])
        return value

    @property
    def cylindrical_gear_sets(self) -> 'List[_5386.GearSetStaticLoadCaseGroup[_2251.CylindricalGearSet, _2250.CylindricalGear, _6560.CylindricalGearLoadCase, _2036.CylindricalGearMesh, _6562.CylindricalGearMeshLoadCase, _6564.CylindricalGearSetLoadCase]]':
        '''List[GearSetStaticLoadCaseGroup[CylindricalGearSet, CylindricalGear, CylindricalGearLoadCase, CylindricalGearMesh, CylindricalGearMeshLoadCase, CylindricalGearSetLoadCase]]: 'CylindricalGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalGearSets, constructor.new(_5386.GearSetStaticLoadCaseGroup)[_2251.CylindricalGearSet, _2250.CylindricalGear, _6560.CylindricalGearLoadCase, _2036.CylindricalGearMesh, _6562.CylindricalGearMeshLoadCase, _6564.CylindricalGearSetLoadCase])
        return value

    @property
    def parts_with_excitations(self) -> 'List[_5387.PartStaticLoadCaseGroup]':
        '''List[PartStaticLoadCaseGroup]: 'PartsWithExcitations' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PartsWithExcitations, constructor.new(_5387.PartStaticLoadCaseGroup))
        return value

    @property
    def fe_parts(self) -> 'List[_5383.ComponentStaticLoadCaseGroup[_2179.FEPart, _6587.FEPartLoadCase]]':
        '''List[ComponentStaticLoadCaseGroup[FEPart, FEPartLoadCase]]: 'FEParts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FEParts, constructor.new(_5383.ComponentStaticLoadCaseGroup)[_2179.FEPart, _6587.FEPartLoadCase])
        return value

    @property
    def design_states(self) -> 'List[_5368.AbstractDesignStateLoadCaseGroup]':
        '''List[AbstractDesignStateLoadCaseGroup]: 'DesignStates' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.DesignStates, constructor.new(_5368.AbstractDesignStateLoadCaseGroup))
        return value

    @property
    def loaded_gear_sets(self) -> 'List[_3932.CylindricalGearSetCompoundPowerFlow]':
        '''List[CylindricalGearSetCompoundPowerFlow]: 'LoadedGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LoadedGearSets, constructor.new(_3932.CylindricalGearSetCompoundPowerFlow))
        return value

    @property
    def system_optimisation_gear_sets(self) -> 'List[_5378.SystemOptimisationGearSet]':
        '''List[SystemOptimisationGearSet]: 'SystemOptimisationGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SystemOptimisationGearSets, constructor.new(_5378.SystemOptimisationGearSet))
        return value

    @property
    def compound_system_deflection(self) -> '_2406.CompoundSystemDeflectionAnalysis':
        '''CompoundSystemDeflectionAnalysis: 'CompoundSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2406.CompoundSystemDeflectionAnalysis)(self.wrapped.CompoundSystemDeflection) if self.wrapped.CompoundSystemDeflection is not None else None

    @property
    def compound_power_flow(self) -> '_2401.CompoundPowerFlowAnalysis':
        '''CompoundPowerFlowAnalysis: 'CompoundPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2401.CompoundPowerFlowAnalysis)(self.wrapped.CompoundPowerFlow) if self.wrapped.CompoundPowerFlow is not None else None

    @property
    def compound_advanced_system_deflection(self) -> '_2383.CompoundAdvancedSystemDeflectionAnalysis':
        '''CompoundAdvancedSystemDeflectionAnalysis: 'CompoundAdvancedSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2383.CompoundAdvancedSystemDeflectionAnalysis)(self.wrapped.CompoundAdvancedSystemDeflection) if self.wrapped.CompoundAdvancedSystemDeflection is not None else None

    @property
    def compound_harmonic_analysis(self) -> '_2393.CompoundHarmonicAnalysis':
        '''CompoundHarmonicAnalysis: 'CompoundHarmonicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2393.CompoundHarmonicAnalysis)(self.wrapped.CompoundHarmonicAnalysis) if self.wrapped.CompoundHarmonicAnalysis is not None else None

    @property
    def compound_steady_state_synchronous_response(self) -> '_2403.CompoundSteadyStateSynchronousResponseAnalysis':
        '''CompoundSteadyStateSynchronousResponseAnalysis: 'CompoundSteadyStateSynchronousResponse' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2403.CompoundSteadyStateSynchronousResponseAnalysis)(self.wrapped.CompoundSteadyStateSynchronousResponse) if self.wrapped.CompoundSteadyStateSynchronousResponse is not None else None

    @property
    def compound_modal_analysis(self) -> '_2396.CompoundModalAnalysis':
        '''CompoundModalAnalysis: 'CompoundModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2396.CompoundModalAnalysis)(self.wrapped.CompoundModalAnalysis) if self.wrapped.CompoundModalAnalysis is not None else None

    @property
    def compound_critical_speed_analysis(self) -> '_2386.CompoundCriticalSpeedAnalysis':
        '''CompoundCriticalSpeedAnalysis: 'CompoundCriticalSpeedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2386.CompoundCriticalSpeedAnalysis)(self.wrapped.CompoundCriticalSpeedAnalysis) if self.wrapped.CompoundCriticalSpeedAnalysis is not None else None

    @property
    def compound_stability_analysis(self) -> '_2402.CompoundStabilityAnalysis':
        '''CompoundStabilityAnalysis: 'CompoundStabilityAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2402.CompoundStabilityAnalysis)(self.wrapped.CompoundStabilityAnalysis) if self.wrapped.CompoundStabilityAnalysis is not None else None

    @property
    def compound_advanced_time_stepping_analysis_for_modulation(self) -> '_2385.CompoundAdvancedTimeSteppingAnalysisForModulation':
        '''CompoundAdvancedTimeSteppingAnalysisForModulation: 'CompoundAdvancedTimeSteppingAnalysisForModulation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2385.CompoundAdvancedTimeSteppingAnalysisForModulation)(self.wrapped.CompoundAdvancedTimeSteppingAnalysisForModulation) if self.wrapped.CompoundAdvancedTimeSteppingAnalysisForModulation is not None else None

    @property
    def compound_dynamic_model_for_modal_analysis(self) -> '_2390.CompoundDynamicModelForModalAnalysis':
        '''CompoundDynamicModelForModalAnalysis: 'CompoundDynamicModelForModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2390.CompoundDynamicModelForModalAnalysis)(self.wrapped.CompoundDynamicModelForModalAnalysis) if self.wrapped.CompoundDynamicModelForModalAnalysis is not None else None

    def clear_user_specified_excitation_data_for_all_load_cases(self):
        ''' 'ClearUserSpecifiedExcitationDataForAllLoadCases' is the original name of this method.'''

        self.wrapped.ClearUserSpecifiedExcitationDataForAllLoadCases()

    def run_power_flow(self):
        ''' 'RunPowerFlow' is the original name of this method.'''

        self.wrapped.RunPowerFlow()

    def set_face_widths_for_specified_safety_factors_from_power_flow(self):
        ''' 'SetFaceWidthsForSpecifiedSafetyFactorsFromPowerFlow' is the original name of this method.'''

        self.wrapped.SetFaceWidthsForSpecifiedSafetyFactorsFromPowerFlow()

    def calculate_candidates(self):
        ''' 'CalculateCandidates' is the original name of this method.'''

        self.wrapped.CalculateCandidates()

    def perform_system_optimisation(self):
        ''' 'PerformSystemOptimisation' is the original name of this method.'''

        self.wrapped.PerformSystemOptimisation()

    def create_designs(self):
        ''' 'CreateDesigns' is the original name of this method.'''

        self.wrapped.CreateDesigns()

    def optimise_gear_sets_quick(self):
        ''' 'OptimiseGearSetsQuick' is the original name of this method.'''

        self.wrapped.OptimiseGearSetsQuick()

    def analysis_of(self, analysis_type: '_6517.AnalysisType') -> '_2344.CompoundAnalysis':
        ''' 'AnalysisOf' is the original name of this method.

        Args:
            analysis_type (mastapy.system_model.analyses_and_results.static_loads.AnalysisType)

        Returns:
            mastapy.system_model.analyses_and_results.CompoundAnalysis
        '''

        analysis_type = conversion.mp_to_pn_enum(analysis_type)
        method_result = self.wrapped.AnalysisOf(analysis_type)
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None
