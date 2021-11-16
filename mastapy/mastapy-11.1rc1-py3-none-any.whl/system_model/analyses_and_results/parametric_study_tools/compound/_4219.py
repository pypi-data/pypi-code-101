'''_4219.py

GearSetCompoundParametricStudyTool
'''


from typing import List

from mastapy.gears.rating import _327
from mastapy._internal import constructor, conversion
from mastapy.gears.rating.worm import _340
from mastapy._internal.cast_exception import CastException
from mastapy.gears.rating.face import _414
from mastapy.gears.rating.cylindrical import _426
from mastapy.gears.rating.conical import _495
from mastapy.gears.rating.concept import _506
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4079
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4257
from mastapy._internal.python_net import python_net_import

_GEAR_SET_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound', 'GearSetCompoundParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('GearSetCompoundParametricStudyTool',)


class GearSetCompoundParametricStudyTool(_4257.SpecialisedAssemblyCompoundParametricStudyTool):
    '''GearSetCompoundParametricStudyTool

    This is a mastapy class.
    '''

    TYPE = _GEAR_SET_COMPOUND_PARAMETRIC_STUDY_TOOL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'GearSetCompoundParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_set_duty_cycle_results(self) -> '_327.GearSetDutyCycleRating':
        '''GearSetDutyCycleRating: 'GearSetDutyCycleResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _327.GearSetDutyCycleRating.TYPE not in self.wrapped.GearSetDutyCycleResults.__class__.__mro__:
            raise CastException('Failed to cast gear_set_duty_cycle_results to GearSetDutyCycleRating. Expected: {}.'.format(self.wrapped.GearSetDutyCycleResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.GearSetDutyCycleResults.__class__)(self.wrapped.GearSetDutyCycleResults) if self.wrapped.GearSetDutyCycleResults is not None else None

    @property
    def gear_set_duty_cycle_results_of_type_worm_gear_set_duty_cycle_rating(self) -> '_340.WormGearSetDutyCycleRating':
        '''WormGearSetDutyCycleRating: 'GearSetDutyCycleResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _340.WormGearSetDutyCycleRating.TYPE not in self.wrapped.GearSetDutyCycleResults.__class__.__mro__:
            raise CastException('Failed to cast gear_set_duty_cycle_results to WormGearSetDutyCycleRating. Expected: {}.'.format(self.wrapped.GearSetDutyCycleResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.GearSetDutyCycleResults.__class__)(self.wrapped.GearSetDutyCycleResults) if self.wrapped.GearSetDutyCycleResults is not None else None

    @property
    def gear_set_duty_cycle_results_of_type_face_gear_set_duty_cycle_rating(self) -> '_414.FaceGearSetDutyCycleRating':
        '''FaceGearSetDutyCycleRating: 'GearSetDutyCycleResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _414.FaceGearSetDutyCycleRating.TYPE not in self.wrapped.GearSetDutyCycleResults.__class__.__mro__:
            raise CastException('Failed to cast gear_set_duty_cycle_results to FaceGearSetDutyCycleRating. Expected: {}.'.format(self.wrapped.GearSetDutyCycleResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.GearSetDutyCycleResults.__class__)(self.wrapped.GearSetDutyCycleResults) if self.wrapped.GearSetDutyCycleResults is not None else None

    @property
    def gear_set_duty_cycle_results_of_type_cylindrical_gear_set_duty_cycle_rating(self) -> '_426.CylindricalGearSetDutyCycleRating':
        '''CylindricalGearSetDutyCycleRating: 'GearSetDutyCycleResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _426.CylindricalGearSetDutyCycleRating.TYPE not in self.wrapped.GearSetDutyCycleResults.__class__.__mro__:
            raise CastException('Failed to cast gear_set_duty_cycle_results to CylindricalGearSetDutyCycleRating. Expected: {}.'.format(self.wrapped.GearSetDutyCycleResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.GearSetDutyCycleResults.__class__)(self.wrapped.GearSetDutyCycleResults) if self.wrapped.GearSetDutyCycleResults is not None else None

    @property
    def gear_set_duty_cycle_results_of_type_conical_gear_set_duty_cycle_rating(self) -> '_495.ConicalGearSetDutyCycleRating':
        '''ConicalGearSetDutyCycleRating: 'GearSetDutyCycleResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _495.ConicalGearSetDutyCycleRating.TYPE not in self.wrapped.GearSetDutyCycleResults.__class__.__mro__:
            raise CastException('Failed to cast gear_set_duty_cycle_results to ConicalGearSetDutyCycleRating. Expected: {}.'.format(self.wrapped.GearSetDutyCycleResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.GearSetDutyCycleResults.__class__)(self.wrapped.GearSetDutyCycleResults) if self.wrapped.GearSetDutyCycleResults is not None else None

    @property
    def gear_set_duty_cycle_results_of_type_concept_gear_set_duty_cycle_rating(self) -> '_506.ConceptGearSetDutyCycleRating':
        '''ConceptGearSetDutyCycleRating: 'GearSetDutyCycleResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _506.ConceptGearSetDutyCycleRating.TYPE not in self.wrapped.GearSetDutyCycleResults.__class__.__mro__:
            raise CastException('Failed to cast gear_set_duty_cycle_results to ConceptGearSetDutyCycleRating. Expected: {}.'.format(self.wrapped.GearSetDutyCycleResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.GearSetDutyCycleResults.__class__)(self.wrapped.GearSetDutyCycleResults) if self.wrapped.GearSetDutyCycleResults is not None else None

    @property
    def assembly_analysis_cases(self) -> 'List[_4079.GearSetParametricStudyTool]':
        '''List[GearSetParametricStudyTool]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCases, constructor.new(_4079.GearSetParametricStudyTool))
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_4079.GearSetParametricStudyTool]':
        '''List[GearSetParametricStudyTool]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCasesReady, constructor.new(_4079.GearSetParametricStudyTool))
        return value
