'''_5717.py

FEPartHarmonicAnalysis
'''


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses import _4862
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5730, _5650
from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import _5818
from mastapy.system_model.part_model import _2179
from mastapy.system_model.analyses_and_results.static_loads import _6587
from mastapy.system_model.analyses_and_results.system_deflections import _2477
from mastapy._internal.python_net import python_net_import

_FE_PART_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'FEPartHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('FEPartHarmonicAnalysis',)


class FEPartHarmonicAnalysis(_5650.AbstractShaftOrHousingHarmonicAnalysis):
    '''FEPartHarmonicAnalysis

    This is a mastapy class.
    '''

    TYPE = _FE_PART_HARMONIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FEPartHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def export_displacements(self) -> 'str':
        '''str: 'ExportDisplacements' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.ExportDisplacements

    @property
    def export_velocities(self) -> 'str':
        '''str: 'ExportVelocities' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.ExportVelocities

    @property
    def export_accelerations(self) -> 'str':
        '''str: 'ExportAccelerations' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.ExportAccelerations

    @property
    def export_forces(self) -> 'str':
        '''str: 'ExportForces' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.ExportForces

    @property
    def coupled_modal_analysis(self) -> '_4862.FEPartModalAnalysis':
        '''FEPartModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_4862.FEPartModalAnalysis)(self.wrapped.CoupledModalAnalysis) if self.wrapped.CoupledModalAnalysis is not None else None

    @property
    def export(self) -> '_5730.HarmonicAnalysisFEExportOptions':
        '''HarmonicAnalysisFEExportOptions: 'Export' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5730.HarmonicAnalysisFEExportOptions)(self.wrapped.Export) if self.wrapped.Export is not None else None

    @property
    def results(self) -> '_5818.FEPartHarmonicAnalysisResultsPropertyAccessor':
        '''FEPartHarmonicAnalysisResultsPropertyAccessor: 'Results' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5818.FEPartHarmonicAnalysisResultsPropertyAccessor)(self.wrapped.Results) if self.wrapped.Results is not None else None

    @property
    def component_design(self) -> '_2179.FEPart':
        '''FEPart: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2179.FEPart)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6587.FEPartLoadCase':
        '''FEPartLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6587.FEPartLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None

    @property
    def system_deflection_results(self) -> '_2477.FEPartSystemDeflection':
        '''FEPartSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2477.FEPartSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def planetaries(self) -> 'List[FEPartHarmonicAnalysis]':
        '''List[FEPartHarmonicAnalysis]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Planetaries, constructor.new(FEPartHarmonicAnalysis))
        return value
