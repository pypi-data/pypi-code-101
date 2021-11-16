'''_6504.py

StaticLoadCase
'''


from typing import List, Optional

from mastapy.system_model.analyses_and_results import (
    _2371, _2366, _2346, _2357,
    _2365, _2349, _2368, _2360,
    _2350, _2367, _2348, _2354,
    _2408, _2345
)
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.gears import _306
from mastapy.system_model.part_model import _2204
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _6977
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5731
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6775
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.load_case_groups import _5371, _5372, _5373
from mastapy.system_model.analyses_and_results.static_loads import _6517, _6503
from mastapy._internal.python_net import python_net_import

_STATIC_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'StaticLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('StaticLoadCase',)


class StaticLoadCase(_6503.LoadCase):
    '''StaticLoadCase

    This is a mastapy class.
    '''

    TYPE = _STATIC_LOAD_CASE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'StaticLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def system_deflection(self) -> '_2371.SystemDeflectionAnalysis':
        '''SystemDeflectionAnalysis: 'SystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2371.SystemDeflectionAnalysis)(self.wrapped.SystemDeflection) if self.wrapped.SystemDeflection is not None else None

    @property
    def power_flow(self) -> '_2366.PowerFlowAnalysis':
        '''PowerFlowAnalysis: 'PowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2366.PowerFlowAnalysis)(self.wrapped.PowerFlow) if self.wrapped.PowerFlow is not None else None

    @property
    def advanced_system_deflection(self) -> '_2346.AdvancedSystemDeflectionAnalysis':
        '''AdvancedSystemDeflectionAnalysis: 'AdvancedSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2346.AdvancedSystemDeflectionAnalysis)(self.wrapped.AdvancedSystemDeflection) if self.wrapped.AdvancedSystemDeflection is not None else None

    @property
    def harmonic_analysis(self) -> '_2357.HarmonicAnalysis':
        '''HarmonicAnalysis: 'HarmonicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2357.HarmonicAnalysis)(self.wrapped.HarmonicAnalysis) if self.wrapped.HarmonicAnalysis is not None else None

    @property
    def parametric_study_tool(self) -> '_2365.ParametricStudyToolAnalysis':
        '''ParametricStudyToolAnalysis: 'ParametricStudyTool' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2365.ParametricStudyToolAnalysis)(self.wrapped.ParametricStudyTool) if self.wrapped.ParametricStudyTool is not None else None

    @property
    def compound_parametric_study_tool(self) -> '_2349.CompoundParametricStudyToolAnalysis':
        '''CompoundParametricStudyToolAnalysis: 'CompoundParametricStudyTool' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2349.CompoundParametricStudyToolAnalysis)(self.wrapped.CompoundParametricStudyTool) if self.wrapped.CompoundParametricStudyTool is not None else None

    @property
    def steady_state_synchronous_response(self) -> '_2368.SteadyStateSynchronousResponseAnalysis':
        '''SteadyStateSynchronousResponseAnalysis: 'SteadyStateSynchronousResponse' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2368.SteadyStateSynchronousResponseAnalysis)(self.wrapped.SteadyStateSynchronousResponse) if self.wrapped.SteadyStateSynchronousResponse is not None else None

    @property
    def modal_analysis(self) -> '_2360.ModalAnalysis':
        '''ModalAnalysis: 'ModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2360.ModalAnalysis)(self.wrapped.ModalAnalysis) if self.wrapped.ModalAnalysis is not None else None

    @property
    def critical_speed_analysis(self) -> '_2350.CriticalSpeedAnalysis':
        '''CriticalSpeedAnalysis: 'CriticalSpeedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2350.CriticalSpeedAnalysis)(self.wrapped.CriticalSpeedAnalysis) if self.wrapped.CriticalSpeedAnalysis is not None else None

    @property
    def stability_analysis(self) -> '_2367.StabilityAnalysis':
        '''StabilityAnalysis: 'StabilityAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2367.StabilityAnalysis)(self.wrapped.StabilityAnalysis) if self.wrapped.StabilityAnalysis is not None else None

    @property
    def advanced_time_stepping_analysis_for_modulation(self) -> '_2348.AdvancedTimeSteppingAnalysisForModulation':
        '''AdvancedTimeSteppingAnalysisForModulation: 'AdvancedTimeSteppingAnalysisForModulation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2348.AdvancedTimeSteppingAnalysisForModulation)(self.wrapped.AdvancedTimeSteppingAnalysisForModulation) if self.wrapped.AdvancedTimeSteppingAnalysisForModulation is not None else None

    @property
    def dynamic_model_for_modal_analysis(self) -> '_2354.DynamicModelForModalAnalysis':
        '''DynamicModelForModalAnalysis: 'DynamicModelForModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2354.DynamicModelForModalAnalysis)(self.wrapped.DynamicModelForModalAnalysis) if self.wrapped.DynamicModelForModalAnalysis is not None else None

    @property
    def design_state(self) -> 'str':
        '''str: 'DesignState' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.DesignState

    @property
    def number_of_stop_start_cycles(self) -> 'int':
        '''int: 'NumberOfStopStartCycles' is the original name of this property.'''

        return self.wrapped.NumberOfStopStartCycles

    @number_of_stop_start_cycles.setter
    def number_of_stop_start_cycles(self, value: 'int'):
        self.wrapped.NumberOfStopStartCycles = int(value) if value else 0

    @property
    def is_stop_start_load_case(self) -> 'bool':
        '''bool: 'IsStopStartLoadCase' is the original name of this property.'''

        return self.wrapped.IsStopStartLoadCase

    @is_stop_start_load_case.setter
    def is_stop_start_load_case(self, value: 'bool'):
        self.wrapped.IsStopStartLoadCase = bool(value) if value else False

    @property
    def power_convergence_tolerance(self) -> 'overridable.Overridable_float':
        '''overridable.Overridable_float: 'PowerConvergenceTolerance' is the original name of this property.'''

        return constructor.new(overridable.Overridable_float)(self.wrapped.PowerConvergenceTolerance) if self.wrapped.PowerConvergenceTolerance is not None else None

    @power_convergence_tolerance.setter
    def power_convergence_tolerance(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.PowerConvergenceTolerance = value

    @property
    def input_shaft_cycles(self) -> 'float':
        '''float: 'InputShaftCycles' is the original name of this property.'''

        return self.wrapped.InputShaftCycles

    @input_shaft_cycles.setter
    def input_shaft_cycles(self, value: 'float'):
        self.wrapped.InputShaftCycles = float(value) if value else 0.0

    @property
    def percentage_of_shaft_torque_alternating(self) -> 'float':
        '''float: 'PercentageOfShaftTorqueAlternating' is the original name of this property.'''

        return self.wrapped.PercentageOfShaftTorqueAlternating

    @percentage_of_shaft_torque_alternating.setter
    def percentage_of_shaft_torque_alternating(self, value: 'float'):
        self.wrapped.PercentageOfShaftTorqueAlternating = float(value) if value else 0.0

    @property
    def planetary_rating_load_sharing_method(self) -> '_306.PlanetaryRatingLoadSharingOption':
        '''PlanetaryRatingLoadSharingOption: 'PlanetaryRatingLoadSharingMethod' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.PlanetaryRatingLoadSharingMethod)
        return constructor.new(_306.PlanetaryRatingLoadSharingOption)(value) if value is not None else None

    @planetary_rating_load_sharing_method.setter
    def planetary_rating_load_sharing_method(self, value: '_306.PlanetaryRatingLoadSharingOption'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.PlanetaryRatingLoadSharingMethod = value

    @property
    def current_time(self) -> 'float':
        '''float: 'CurrentTime' is the original name of this property.'''

        return self.wrapped.CurrentTime

    @current_time.setter
    def current_time(self, value: 'float'):
        self.wrapped.CurrentTime = float(value) if value else 0.0

    @property
    def duration(self) -> 'float':
        '''float: 'Duration' is the original name of this property.'''

        return self.wrapped.Duration

    @duration.setter
    def duration(self, value: 'float'):
        self.wrapped.Duration = float(value) if value else 0.0

    @property
    def unbalanced_mass_inclusion(self) -> 'overridable.Overridable_UnbalancedMassInclusionOption':
        '''overridable.Overridable_UnbalancedMassInclusionOption: 'UnbalancedMassInclusion' is the original name of this property.'''

        value = overridable.Overridable_UnbalancedMassInclusionOption.wrapped_type()
        return enum_with_selected_value_runtime.create(self.wrapped.UnbalancedMassInclusion, value) if self.wrapped.UnbalancedMassInclusion is not None else None

    @unbalanced_mass_inclusion.setter
    def unbalanced_mass_inclusion(self, value: 'overridable.Overridable_UnbalancedMassInclusionOption.implicit_type()'):
        wrapper_type = overridable.Overridable_UnbalancedMassInclusionOption.wrapper_type()
        enclosed_type = overridable.Overridable_UnbalancedMassInclusionOption.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value if value is not None else None, is_overridden)
        self.wrapped.UnbalancedMassInclusion = value

    @property
    def advanced_system_deflection_options(self) -> '_6977.AdvancedSystemDeflectionOptions':
        '''AdvancedSystemDeflectionOptions: 'AdvancedSystemDeflectionOptions' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6977.AdvancedSystemDeflectionOptions)(self.wrapped.AdvancedSystemDeflectionOptions) if self.wrapped.AdvancedSystemDeflectionOptions is not None else None

    @property
    def te_set_up_for_dynamic_analyses_options(self) -> '_2408.TESetUpForDynamicAnalysisOptions':
        '''TESetUpForDynamicAnalysisOptions: 'TESetUpForDynamicAnalysesOptions' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2408.TESetUpForDynamicAnalysisOptions)(self.wrapped.TESetUpForDynamicAnalysesOptions) if self.wrapped.TESetUpForDynamicAnalysesOptions is not None else None

    @property
    def harmonic_analysis_options(self) -> '_5731.HarmonicAnalysisOptions':
        '''HarmonicAnalysisOptions: 'HarmonicAnalysisOptions' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5731.HarmonicAnalysisOptions.TYPE not in self.wrapped.HarmonicAnalysisOptions.__class__.__mro__:
            raise CastException('Failed to cast harmonic_analysis_options to HarmonicAnalysisOptions. Expected: {}.'.format(self.wrapped.HarmonicAnalysisOptions.__class__.__qualname__))

        return constructor.new_override(self.wrapped.HarmonicAnalysisOptions.__class__)(self.wrapped.HarmonicAnalysisOptions) if self.wrapped.HarmonicAnalysisOptions is not None else None

    @property
    def harmonic_analysis_options_for_atsam(self) -> '_5731.HarmonicAnalysisOptions':
        '''HarmonicAnalysisOptions: 'HarmonicAnalysisOptionsForATSAM' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5731.HarmonicAnalysisOptions.TYPE not in self.wrapped.HarmonicAnalysisOptionsForATSAM.__class__.__mro__:
            raise CastException('Failed to cast harmonic_analysis_options_for_atsam to HarmonicAnalysisOptions. Expected: {}.'.format(self.wrapped.HarmonicAnalysisOptionsForATSAM.__class__.__qualname__))

        return constructor.new_override(self.wrapped.HarmonicAnalysisOptionsForATSAM.__class__)(self.wrapped.HarmonicAnalysisOptionsForATSAM) if self.wrapped.HarmonicAnalysisOptionsForATSAM is not None else None

    @property
    def clutch_engagements(self) -> 'List[_5371.ClutchEngagementStatus]':
        '''List[ClutchEngagementStatus]: 'ClutchEngagements' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ClutchEngagements, constructor.new(_5371.ClutchEngagementStatus))
        return value

    @property
    def concept_clutch_engagements(self) -> 'List[_5372.ConceptSynchroGearEngagementStatus]':
        '''List[ConceptSynchroGearEngagementStatus]: 'ConceptClutchEngagements' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptClutchEngagements, constructor.new(_5372.ConceptSynchroGearEngagementStatus))
        return value

    @property
    def design_state_load_case_group(self) -> '_5373.DesignState':
        '''DesignState: 'DesignStateLoadCaseGroup' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5373.DesignState)(self.wrapped.DesignStateLoadCaseGroup) if self.wrapped.DesignStateLoadCaseGroup is not None else None

    def analysis_of(self, analysis_type: '_6517.AnalysisType') -> '_2345.SingleAnalysis':
        ''' 'AnalysisOf' is the original name of this method.

        Args:
            analysis_type (mastapy.system_model.analyses_and_results.static_loads.AnalysisType)

        Returns:
            mastapy.system_model.analyses_and_results.SingleAnalysis
        '''

        analysis_type = conversion.mp_to_pn_enum(analysis_type)
        method_result = self.wrapped.AnalysisOf(analysis_type)
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def run_power_flow(self):
        ''' 'RunPowerFlow' is the original name of this method.'''

        self.wrapped.RunPowerFlow()

    def set_face_widths_for_specified_safety_factors_from_power_flow(self):
        ''' 'SetFaceWidthsForSpecifiedSafetyFactorsFromPowerFlow' is the original name of this method.'''

        self.wrapped.SetFaceWidthsForSpecifiedSafetyFactorsFromPowerFlow()

    def create_time_series_load_case(self):
        ''' 'CreateTimeSeriesLoadCase' is the original name of this method.'''

        self.wrapped.CreateTimeSeriesLoadCase()

    def duplicate(self, new_design_state_group: '_5373.DesignState', name: Optional['str'] = 'None') -> 'StaticLoadCase':
        ''' 'Duplicate' is the original name of this method.

        Args:
            new_design_state_group (mastapy.system_model.analyses_and_results.load_case_groups.DesignState)
            name (str, optional)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.StaticLoadCase
        '''

        name = str(name)
        method_result = self.wrapped.Duplicate(new_design_state_group.wrapped if new_design_state_group else None, name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None
