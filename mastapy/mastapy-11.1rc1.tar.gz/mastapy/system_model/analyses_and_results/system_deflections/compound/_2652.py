'''_2652.py

PartToPartShearCouplingCompoundSystemDeflection
'''


from typing import List

from mastapy.system_model.part_model.couplings import _2313
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2508
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2608
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_COMPOUND_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'PartToPartShearCouplingCompoundSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('PartToPartShearCouplingCompoundSystemDeflection',)


class PartToPartShearCouplingCompoundSystemDeflection(_2608.CouplingCompoundSystemDeflection):
    '''PartToPartShearCouplingCompoundSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _PART_TO_PART_SHEAR_COUPLING_COMPOUND_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PartToPartShearCouplingCompoundSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2313.PartToPartShearCoupling':
        '''PartToPartShearCoupling: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2313.PartToPartShearCoupling)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def assembly_design(self) -> '_2313.PartToPartShearCoupling':
        '''PartToPartShearCoupling: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2313.PartToPartShearCoupling)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_2508.PartToPartShearCouplingSystemDeflection]':
        '''List[PartToPartShearCouplingSystemDeflection]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCasesReady, constructor.new(_2508.PartToPartShearCouplingSystemDeflection))
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_2508.PartToPartShearCouplingSystemDeflection]':
        '''List[PartToPartShearCouplingSystemDeflection]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCases, constructor.new(_2508.PartToPartShearCouplingSystemDeflection))
        return value
