'''_5916.py

MeasurementComponentCompoundHarmonicAnalysis
'''


from typing import List

from mastapy.system_model.part_model import _2189
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5748
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5962
from mastapy._internal.python_net import python_net_import

_MEASUREMENT_COMPONENT_COMPOUND_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound', 'MeasurementComponentCompoundHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('MeasurementComponentCompoundHarmonicAnalysis',)


class MeasurementComponentCompoundHarmonicAnalysis(_5962.VirtualComponentCompoundHarmonicAnalysis):
    '''MeasurementComponentCompoundHarmonicAnalysis

    This is a mastapy class.
    '''

    TYPE = _MEASUREMENT_COMPONENT_COMPOUND_HARMONIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'MeasurementComponentCompoundHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2189.MeasurementComponent':
        '''MeasurementComponent: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2189.MeasurementComponent)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_5748.MeasurementComponentHarmonicAnalysis]':
        '''List[MeasurementComponentHarmonicAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCasesReady, constructor.new(_5748.MeasurementComponentHarmonicAnalysis))
        return value

    @property
    def component_analysis_cases(self) -> 'List[_5748.MeasurementComponentHarmonicAnalysis]':
        '''List[MeasurementComponentHarmonicAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCases, constructor.new(_5748.MeasurementComponentHarmonicAnalysis))
        return value
