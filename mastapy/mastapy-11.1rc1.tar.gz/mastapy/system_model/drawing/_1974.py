'''_1974.py

DynamicAnalysisViewable
'''


from mastapy.system_model.drawing import _1972, _1979
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2546
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3328
from mastapy.system_model.analyses_and_results.stability_analyses import _3589
from mastapy.system_model.analyses_and_results.rotor_dynamics import _3744
from mastapy.system_model.analyses_and_results.modal_analyses import _4885
from mastapy.system_model.analyses_and_results.mbd_analyses import _5171
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5728
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6030
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6283
from mastapy._internal.python_net import python_net_import

_DYNAMIC_ANALYSIS_VIEWABLE = python_net_import('SMT.MastaAPI.SystemModel.Drawing', 'DynamicAnalysisViewable')


__docformat__ = 'restructuredtext en'
__all__ = ('DynamicAnalysisViewable',)


class DynamicAnalysisViewable(_1979.PartAnalysisCaseWithContourViewable):
    '''DynamicAnalysisViewable

    This is a mastapy class.
    '''

    TYPE = _DYNAMIC_ANALYSIS_VIEWABLE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'DynamicAnalysisViewable.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def contour_draw_style(self) -> '_1972.ContourDrawStyle':
        '''ContourDrawStyle: 'ContourDrawStyle' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1972.ContourDrawStyle.TYPE not in self.wrapped.ContourDrawStyle.__class__.__mro__:
            raise CastException('Failed to cast contour_draw_style to ContourDrawStyle. Expected: {}.'.format(self.wrapped.ContourDrawStyle.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ContourDrawStyle.__class__)(self.wrapped.ContourDrawStyle) if self.wrapped.ContourDrawStyle is not None else None

    @property
    def contour_draw_style_of_type_system_deflection_draw_style(self) -> '_2546.SystemDeflectionDrawStyle':
        '''SystemDeflectionDrawStyle: 'ContourDrawStyle' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2546.SystemDeflectionDrawStyle.TYPE not in self.wrapped.ContourDrawStyle.__class__.__mro__:
            raise CastException('Failed to cast contour_draw_style to SystemDeflectionDrawStyle. Expected: {}.'.format(self.wrapped.ContourDrawStyle.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ContourDrawStyle.__class__)(self.wrapped.ContourDrawStyle) if self.wrapped.ContourDrawStyle is not None else None

    @property
    def contour_draw_style_of_type_steady_state_synchronous_response_draw_style(self) -> '_3328.SteadyStateSynchronousResponseDrawStyle':
        '''SteadyStateSynchronousResponseDrawStyle: 'ContourDrawStyle' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _3328.SteadyStateSynchronousResponseDrawStyle.TYPE not in self.wrapped.ContourDrawStyle.__class__.__mro__:
            raise CastException('Failed to cast contour_draw_style to SteadyStateSynchronousResponseDrawStyle. Expected: {}.'.format(self.wrapped.ContourDrawStyle.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ContourDrawStyle.__class__)(self.wrapped.ContourDrawStyle) if self.wrapped.ContourDrawStyle is not None else None

    @property
    def contour_draw_style_of_type_stability_analysis_draw_style(self) -> '_3589.StabilityAnalysisDrawStyle':
        '''StabilityAnalysisDrawStyle: 'ContourDrawStyle' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _3589.StabilityAnalysisDrawStyle.TYPE not in self.wrapped.ContourDrawStyle.__class__.__mro__:
            raise CastException('Failed to cast contour_draw_style to StabilityAnalysisDrawStyle. Expected: {}.'.format(self.wrapped.ContourDrawStyle.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ContourDrawStyle.__class__)(self.wrapped.ContourDrawStyle) if self.wrapped.ContourDrawStyle is not None else None

    @property
    def contour_draw_style_of_type_rotor_dynamics_draw_style(self) -> '_3744.RotorDynamicsDrawStyle':
        '''RotorDynamicsDrawStyle: 'ContourDrawStyle' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _3744.RotorDynamicsDrawStyle.TYPE not in self.wrapped.ContourDrawStyle.__class__.__mro__:
            raise CastException('Failed to cast contour_draw_style to RotorDynamicsDrawStyle. Expected: {}.'.format(self.wrapped.ContourDrawStyle.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ContourDrawStyle.__class__)(self.wrapped.ContourDrawStyle) if self.wrapped.ContourDrawStyle is not None else None

    @property
    def contour_draw_style_of_type_modal_analysis_draw_style(self) -> '_4885.ModalAnalysisDrawStyle':
        '''ModalAnalysisDrawStyle: 'ContourDrawStyle' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4885.ModalAnalysisDrawStyle.TYPE not in self.wrapped.ContourDrawStyle.__class__.__mro__:
            raise CastException('Failed to cast contour_draw_style to ModalAnalysisDrawStyle. Expected: {}.'.format(self.wrapped.ContourDrawStyle.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ContourDrawStyle.__class__)(self.wrapped.ContourDrawStyle) if self.wrapped.ContourDrawStyle is not None else None

    @property
    def contour_draw_style_of_type_mbd_analysis_draw_style(self) -> '_5171.MBDAnalysisDrawStyle':
        '''MBDAnalysisDrawStyle: 'ContourDrawStyle' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5171.MBDAnalysisDrawStyle.TYPE not in self.wrapped.ContourDrawStyle.__class__.__mro__:
            raise CastException('Failed to cast contour_draw_style to MBDAnalysisDrawStyle. Expected: {}.'.format(self.wrapped.ContourDrawStyle.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ContourDrawStyle.__class__)(self.wrapped.ContourDrawStyle) if self.wrapped.ContourDrawStyle is not None else None

    @property
    def contour_draw_style_of_type_harmonic_analysis_draw_style(self) -> '_5728.HarmonicAnalysisDrawStyle':
        '''HarmonicAnalysisDrawStyle: 'ContourDrawStyle' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5728.HarmonicAnalysisDrawStyle.TYPE not in self.wrapped.ContourDrawStyle.__class__.__mro__:
            raise CastException('Failed to cast contour_draw_style to HarmonicAnalysisDrawStyle. Expected: {}.'.format(self.wrapped.ContourDrawStyle.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ContourDrawStyle.__class__)(self.wrapped.ContourDrawStyle) if self.wrapped.ContourDrawStyle is not None else None

    @property
    def contour_draw_style_of_type_dynamic_analysis_draw_style(self) -> '_6030.DynamicAnalysisDrawStyle':
        '''DynamicAnalysisDrawStyle: 'ContourDrawStyle' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _6030.DynamicAnalysisDrawStyle.TYPE not in self.wrapped.ContourDrawStyle.__class__.__mro__:
            raise CastException('Failed to cast contour_draw_style to DynamicAnalysisDrawStyle. Expected: {}.'.format(self.wrapped.ContourDrawStyle.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ContourDrawStyle.__class__)(self.wrapped.ContourDrawStyle) if self.wrapped.ContourDrawStyle is not None else None

    @property
    def contour_draw_style_of_type_critical_speed_analysis_draw_style(self) -> '_6283.CriticalSpeedAnalysisDrawStyle':
        '''CriticalSpeedAnalysisDrawStyle: 'ContourDrawStyle' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _6283.CriticalSpeedAnalysisDrawStyle.TYPE not in self.wrapped.ContourDrawStyle.__class__.__mro__:
            raise CastException('Failed to cast contour_draw_style to CriticalSpeedAnalysisDrawStyle. Expected: {}.'.format(self.wrapped.ContourDrawStyle.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ContourDrawStyle.__class__)(self.wrapped.ContourDrawStyle) if self.wrapped.ContourDrawStyle is not None else None

    @property
    def dynamic_analysis_draw_style(self) -> '_6030.DynamicAnalysisDrawStyle':
        '''DynamicAnalysisDrawStyle: 'DynamicAnalysisDrawStyle' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _6030.DynamicAnalysisDrawStyle.TYPE not in self.wrapped.DynamicAnalysisDrawStyle.__class__.__mro__:
            raise CastException('Failed to cast dynamic_analysis_draw_style to DynamicAnalysisDrawStyle. Expected: {}.'.format(self.wrapped.DynamicAnalysisDrawStyle.__class__.__qualname__))

        return constructor.new_override(self.wrapped.DynamicAnalysisDrawStyle.__class__)(self.wrapped.DynamicAnalysisDrawStyle) if self.wrapped.DynamicAnalysisDrawStyle is not None else None

    @property
    def dynamic_analysis_draw_style_of_type_modal_analysis_draw_style(self) -> '_4885.ModalAnalysisDrawStyle':
        '''ModalAnalysisDrawStyle: 'DynamicAnalysisDrawStyle' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4885.ModalAnalysisDrawStyle.TYPE not in self.wrapped.DynamicAnalysisDrawStyle.__class__.__mro__:
            raise CastException('Failed to cast dynamic_analysis_draw_style to ModalAnalysisDrawStyle. Expected: {}.'.format(self.wrapped.DynamicAnalysisDrawStyle.__class__.__qualname__))

        return constructor.new_override(self.wrapped.DynamicAnalysisDrawStyle.__class__)(self.wrapped.DynamicAnalysisDrawStyle) if self.wrapped.DynamicAnalysisDrawStyle is not None else None

    @property
    def dynamic_analysis_draw_style_of_type_harmonic_analysis_draw_style(self) -> '_5728.HarmonicAnalysisDrawStyle':
        '''HarmonicAnalysisDrawStyle: 'DynamicAnalysisDrawStyle' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5728.HarmonicAnalysisDrawStyle.TYPE not in self.wrapped.DynamicAnalysisDrawStyle.__class__.__mro__:
            raise CastException('Failed to cast dynamic_analysis_draw_style to HarmonicAnalysisDrawStyle. Expected: {}.'.format(self.wrapped.DynamicAnalysisDrawStyle.__class__.__qualname__))

        return constructor.new_override(self.wrapped.DynamicAnalysisDrawStyle.__class__)(self.wrapped.DynamicAnalysisDrawStyle) if self.wrapped.DynamicAnalysisDrawStyle is not None else None

    def fe_results(self):
        ''' 'FEResults' is the original name of this method.'''

        self.wrapped.FEResults()
