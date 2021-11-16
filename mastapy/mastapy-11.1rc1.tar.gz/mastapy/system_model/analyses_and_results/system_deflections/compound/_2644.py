'''_2644.py

KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection
'''


from typing import List

from mastapy.system_model.part_model.gears import _2265
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2496
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2638
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_COMPOUND_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection',)


class KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection(_2638.KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection):
    '''KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_COMPOUND_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2265.KlingelnbergCycloPalloidSpiralBevelGear':
        '''KlingelnbergCycloPalloidSpiralBevelGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2265.KlingelnbergCycloPalloidSpiralBevelGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_2496.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection]':
        '''List[KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCasesReady, constructor.new(_2496.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection))
        return value

    @property
    def component_analysis_cases(self) -> 'List[_2496.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection]':
        '''List[KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCases, constructor.new(_2496.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection))
        return value
