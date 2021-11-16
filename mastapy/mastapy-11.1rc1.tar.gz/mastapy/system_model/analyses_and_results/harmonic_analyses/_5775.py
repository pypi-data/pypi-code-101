'''_5775.py

SpiralBevelGearMeshHarmonicAnalysis
'''


from mastapy.system_model.connections_and_sockets.gears import _2050
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6658
from mastapy.system_model.analyses_and_results.system_deflections import _2527
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5665
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_MESH_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'SpiralBevelGearMeshHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('SpiralBevelGearMeshHarmonicAnalysis',)


class SpiralBevelGearMeshHarmonicAnalysis(_5665.BevelGearMeshHarmonicAnalysis):
    '''SpiralBevelGearMeshHarmonicAnalysis

    This is a mastapy class.
    '''

    TYPE = _SPIRAL_BEVEL_GEAR_MESH_HARMONIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpiralBevelGearMeshHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2050.SpiralBevelGearMesh':
        '''SpiralBevelGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2050.SpiralBevelGearMesh)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign is not None else None

    @property
    def connection_load_case(self) -> '_6658.SpiralBevelGearMeshLoadCase':
        '''SpiralBevelGearMeshLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6658.SpiralBevelGearMeshLoadCase)(self.wrapped.ConnectionLoadCase) if self.wrapped.ConnectionLoadCase is not None else None

    @property
    def system_deflection_results(self) -> '_2527.SpiralBevelGearMeshSystemDeflection':
        '''SpiralBevelGearMeshSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2527.SpiralBevelGearMeshSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None
