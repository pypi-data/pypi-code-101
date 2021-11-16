'''_5663.py

BevelDifferentialSunGearHarmonicAnalysis
'''


from mastapy.system_model.part_model.gears import _2243
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2425
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5659
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_SUN_GEAR_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'BevelDifferentialSunGearHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialSunGearHarmonicAnalysis',)


class BevelDifferentialSunGearHarmonicAnalysis(_5659.BevelDifferentialGearHarmonicAnalysis):
    '''BevelDifferentialSunGearHarmonicAnalysis

    This is a mastapy class.
    '''

    TYPE = _BEVEL_DIFFERENTIAL_SUN_GEAR_HARMONIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BevelDifferentialSunGearHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2243.BevelDifferentialSunGear':
        '''BevelDifferentialSunGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2243.BevelDifferentialSunGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def system_deflection_results(self) -> '_2425.BevelDifferentialSunGearSystemDeflection':
        '''BevelDifferentialSunGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2425.BevelDifferentialSunGearSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None
