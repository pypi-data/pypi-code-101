'''_4026.py

BevelDifferentialPlanetGearParametricStudyTool
'''


from mastapy.system_model.part_model.gears import _2242
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4024
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_PLANET_GEAR_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'BevelDifferentialPlanetGearParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialPlanetGearParametricStudyTool',)


class BevelDifferentialPlanetGearParametricStudyTool(_4024.BevelDifferentialGearParametricStudyTool):
    '''BevelDifferentialPlanetGearParametricStudyTool

    This is a mastapy class.
    '''

    TYPE = _BEVEL_DIFFERENTIAL_PLANET_GEAR_PARAMETRIC_STUDY_TOOL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BevelDifferentialPlanetGearParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2242.BevelDifferentialPlanetGear':
        '''BevelDifferentialPlanetGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2242.BevelDifferentialPlanetGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None
