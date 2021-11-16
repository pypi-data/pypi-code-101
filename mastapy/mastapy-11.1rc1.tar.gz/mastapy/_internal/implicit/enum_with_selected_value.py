'''enum_with_selected_value.py

Implementations of 'EnumWithSelectedValue' in Python.
As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
'''


from enum import Enum
from typing import List

from mastapy._internal import (
    mixins, enum_with_selected_value_runtime, constructor, conversion
)
from mastapy.shafts import _33, _42
from mastapy._internal.python_net import python_net_import
from mastapy.nodal_analysis import (
    _67, _86, _73, _82,
    _50
)
from mastapy.nodal_analysis.varying_input_components import _93
from mastapy.fe_tools.enums import _1181
from mastapy.materials import _231, _235, _221
from mastapy.gears import _302, _300, _303
from mastapy.math_utility import (
    _1304, _1285, _1284, _1300,
    _1288, _1299, _1297
)
from mastapy.gears.rating.cylindrical import _441, _442
from mastapy.gears.micro_geometry import (
    _530, _529, _528, _527
)
from mastapy.gears.manufacturing.cylindrical import (
    _578, _577, _581, _563
)
from mastapy.gears.manufacturing.cylindrical.plunge_shaving import _600, _599, _597
from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _612
from mastapy.geometry.two_d.curves import _278
from mastapy.gears.gear_designs.cylindrical import _1028, _1000, _1020
from mastapy.gears.gear_designs.conical import _1100, _1099, _1111
from mastapy.gears.gear_set_pareto_optimiser import _857
from mastapy.utility.model_validation import _1556, _1559
from mastapy.gears.ltca import _781
from mastapy.gears.gear_designs.creation_options import _1088
from mastapy.gears.gear_designs.bevel import _1132, _1121
from mastapy.fe_tools.vfx_tools.vfx_enums import _1179, _1178
from mastapy.bearings.tolerances import (
    _1651, _1663, _1644, _1645,
    _1643
)
from mastapy.detailed_rigid_connectors.splines import (
    _1189, _1212, _1198, _1199,
    _1207, _1213, _1190
)
from mastapy.detailed_rigid_connectors.interference_fits import _1243
from mastapy.utility import _1372
from mastapy.utility.report import _1515
from mastapy.bearings import (
    _1633, _1626, _1634, _1637,
    _1614, _1615, _1639, _1621
)
from mastapy.bearings.bearing_results import (
    _1701, _1700, _1703, _1702
)
from mastapy.materials.efficiency import _260
from mastapy.system_model.part_model import _2201
from mastapy.system_model.drawing.options import _1989
from mastapy.utility.enums import _1584, _1585, _1583
from mastapy.system_model.fe import (
    _2093, _2114, _2137, _2124,
    _2090
)
from mastapy.system_model import (
    _1937, _1949, _1944, _1947
)
from mastapy.nodal_analysis.fe_export_utility import _152, _151
from mastapy.system_model.part_model.couplings import _2320, _2316, _2319
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4065
from mastapy.system_model.analyses_and_results.static_loads import (
    _6517, _6680, _6606, _6597,
    _6641, _6681
)
from mastapy.system_model.analyses_and_results.mbd_analyses import (
    _5097, _5149, _5194, _5219
)
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5712, _5730
from mastapy.bearings.bearing_results.rolling.iso_rating_results import _1844
from mastapy.bearings.bearing_results.rolling import _1710
from mastapy.math_utility.hertzian_contact import _1365
from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import _6695

_ARRAY = python_net_import('System', 'Array')
_ENUM_WITH_SELECTED_VALUE = python_net_import('SMT.MastaAPI.Utility.Property', 'EnumWithSelectedValue')


__docformat__ = 'restructuredtext en'
__all__ = (
    'EnumWithSelectedValue_ShaftRatingMethod', 'EnumWithSelectedValue_SurfaceFinishes',
    'EnumWithSelectedValue_IntegrationMethod', 'EnumWithSelectedValue_ValueInputOption',
    'EnumWithSelectedValue_SinglePointSelectionMethod', 'EnumWithSelectedValue_ModeInputType',
    'EnumWithSelectedValue_MaterialPropertyClass', 'EnumWithSelectedValue_LubricantDefinition',
    'EnumWithSelectedValue_LubricantViscosityClassISO', 'EnumWithSelectedValue_MicroGeometryModel',
    'EnumWithSelectedValue_ExtrapolationOptions', 'EnumWithSelectedValue_ScuffingFlashTemperatureRatingMethod',
    'EnumWithSelectedValue_ScuffingIntegralTemperatureRatingMethod', 'EnumWithSelectedValue_CylindricalGearRatingMethods',
    'EnumWithSelectedValue_LocationOfTipReliefEvaluation', 'EnumWithSelectedValue_LocationOfRootReliefEvaluation',
    'EnumWithSelectedValue_LocationOfEvaluationUpperLimit', 'EnumWithSelectedValue_LocationOfEvaluationLowerLimit',
    'EnumWithSelectedValue_CylindricalMftRoughingMethods', 'EnumWithSelectedValue_CylindricalMftFinishingMethods',
    'EnumWithSelectedValue_MicroGeometryDefinitionType', 'EnumWithSelectedValue_MicroGeometryDefinitionMethod',
    'EnumWithSelectedValue_ChartType', 'EnumWithSelectedValue_Flank',
    'EnumWithSelectedValue_ActiveProcessMethod', 'EnumWithSelectedValue_CutterFlankSections',
    'EnumWithSelectedValue_BasicCurveTypes', 'EnumWithSelectedValue_ThicknessType',
    'EnumWithSelectedValue_ConicalManufactureMethods', 'EnumWithSelectedValue_ConicalMachineSettingCalculationMethods',
    'EnumWithSelectedValue_CandidateDisplayChoice', 'EnumWithSelectedValue_Severity',
    'EnumWithSelectedValue_GeometrySpecificationType', 'EnumWithSelectedValue_StatusItemSeverity',
    'EnumWithSelectedValue_LubricationMethods', 'EnumWithSelectedValue_MicropittingCoefficientOfFrictionCalculationMethod',
    'EnumWithSelectedValue_ScuffingCoefficientOfFrictionMethods', 'EnumWithSelectedValue_ContactResultType',
    'EnumWithSelectedValue_StressResultsType', 'EnumWithSelectedValue_CylindricalGearPairCreationOptions_DerivedParameterOption',
    'EnumWithSelectedValue_ToothThicknessSpecificationMethod', 'EnumWithSelectedValue_LoadDistributionFactorMethods',
    'EnumWithSelectedValue_AGMAGleasonConicalGearGeometryMethods', 'EnumWithSelectedValue_ProSolveSolverType',
    'EnumWithSelectedValue_ProSolveMpcType', 'EnumWithSelectedValue_ITDesignation',
    'EnumWithSelectedValue_DudleyEffectiveLengthApproximationOption', 'EnumWithSelectedValue_SplineRatingTypes',
    'EnumWithSelectedValue_Modules', 'EnumWithSelectedValue_PressureAngleTypes',
    'EnumWithSelectedValue_SplineFitClassType', 'EnumWithSelectedValue_SplineToleranceClassTypes',
    'EnumWithSelectedValue_Table4JointInterfaceTypes', 'EnumWithSelectedValue_ExecutableDirectoryCopier_Option',
    'EnumWithSelectedValue_CadPageOrientation', 'EnumWithSelectedValue_RollerBearingProfileTypes',
    'EnumWithSelectedValue_FluidFilmTemperatureOptions', 'EnumWithSelectedValue_SupportToleranceLocationDesignation',
    'EnumWithSelectedValue_LoadedBallElementPropertyType', 'EnumWithSelectedValue_RollingBearingArrangement',
    'EnumWithSelectedValue_RollingBearingRaceType', 'EnumWithSelectedValue_BasicDynamicLoadRatingCalculationMethod',
    'EnumWithSelectedValue_BasicStaticLoadRatingCalculationMethod', 'EnumWithSelectedValue_RotationalDirections',
    'EnumWithSelectedValue_BearingEfficiencyRatingMethod', 'EnumWithSelectedValue_ShaftDiameterModificationDueToRollingBearingRing',
    'EnumWithSelectedValue_ExcitationAnalysisViewOption', 'EnumWithSelectedValue_ThreeDViewContourOptionFirstSelection',
    'EnumWithSelectedValue_ThreeDViewContourOptionSecondSelection', 'EnumWithSelectedValue_ComponentOrientationOption',
    'EnumWithSelectedValue_Axis', 'EnumWithSelectedValue_AlignmentAxis',
    'EnumWithSelectedValue_DesignEntityId', 'EnumWithSelectedValue_FESubstructureType',
    'EnumWithSelectedValue_ThermalExpansionOption', 'EnumWithSelectedValue_FEExportFormat',
    'EnumWithSelectedValue_ThreeDViewContourOption', 'EnumWithSelectedValue_BoundaryConditionType',
    'EnumWithSelectedValue_LinkNodeSource', 'EnumWithSelectedValue_BearingNodeOption',
    'EnumWithSelectedValue_BearingToleranceClass', 'EnumWithSelectedValue_BearingModel',
    'EnumWithSelectedValue_PreloadType', 'EnumWithSelectedValue_RaceRadialMountingType',
    'EnumWithSelectedValue_RaceAxialMountingType', 'EnumWithSelectedValue_BearingToleranceDefinitionOptions',
    'EnumWithSelectedValue_InternalClearanceClass', 'EnumWithSelectedValue_PowerLoadType',
    'EnumWithSelectedValue_RigidConnectorTypes', 'EnumWithSelectedValue_RigidConnectorStiffnessType',
    'EnumWithSelectedValue_FitTypes', 'EnumWithSelectedValue_RigidConnectorToothSpacingType',
    'EnumWithSelectedValue_DoeValueSpecificationOption', 'EnumWithSelectedValue_AnalysisType',
    'EnumWithSelectedValue_BarModelExportType', 'EnumWithSelectedValue_DynamicsResponseType',
    'EnumWithSelectedValue_ComplexPartDisplayOption', 'EnumWithSelectedValue_DynamicsResponseScaling',
    'EnumWithSelectedValue_BearingStiffnessModel', 'EnumWithSelectedValue_GearMeshStiffnessModel',
    'EnumWithSelectedValue_ShaftAndHousingFlexibilityOption', 'EnumWithSelectedValue_ExportOutputType',
    'EnumWithSelectedValue_HarmonicAnalysisFEExportOptions_ComplexNumberOutput', 'EnumWithSelectedValue_StressConcentrationMethod',
    'EnumWithSelectedValue_FrictionModelForGyroscopicMoment', 'EnumWithSelectedValue_MeshStiffnessModel',
    'EnumWithSelectedValue_HertzianContactDeflectionCalculationMethod', 'EnumWithSelectedValue_TorqueRippleInputType',
    'EnumWithSelectedValue_HarmonicLoadDataType', 'EnumWithSelectedValue_HarmonicExcitationType',
    'EnumWithSelectedValue_PointLoadLoadCase_ForceSpecification', 'EnumWithSelectedValue_PowerLoadInputTorqueSpecificationMethod',
    'EnumWithSelectedValue_TorqueSpecificationForSystemDeflection', 'EnumWithSelectedValue_TorqueConverterLockupRule',
    'EnumWithSelectedValue_DegreesOfFreedom', 'EnumWithSelectedValue_DestinationDesignState'
)


class EnumWithSelectedValue_ShaftRatingMethod(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_ShaftRatingMethod

    A specific implementation of 'EnumWithSelectedValue' for 'ShaftRatingMethod' types.
    '''

    __hash__ = None
    __qualname__ = 'ShaftRatingMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_33.ShaftRatingMethod':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _33.ShaftRatingMethod

    @classmethod
    def implicit_type(cls) -> '_33.ShaftRatingMethod.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _33.ShaftRatingMethod.type_()

    @property
    def selected_value(self) -> '_33.ShaftRatingMethod':
        '''ShaftRatingMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_33.ShaftRatingMethod]':
        '''List[ShaftRatingMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_SurfaceFinishes(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_SurfaceFinishes

    A specific implementation of 'EnumWithSelectedValue' for 'SurfaceFinishes' types.
    '''

    __hash__ = None
    __qualname__ = 'SurfaceFinishes'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_42.SurfaceFinishes':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _42.SurfaceFinishes

    @classmethod
    def implicit_type(cls) -> '_42.SurfaceFinishes.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _42.SurfaceFinishes.type_()

    @property
    def selected_value(self) -> '_42.SurfaceFinishes':
        '''SurfaceFinishes: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_42.SurfaceFinishes]':
        '''List[SurfaceFinishes]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_IntegrationMethod(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_IntegrationMethod

    A specific implementation of 'EnumWithSelectedValue' for 'IntegrationMethod' types.
    '''

    __hash__ = None
    __qualname__ = 'IntegrationMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_67.IntegrationMethod':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _67.IntegrationMethod

    @classmethod
    def implicit_type(cls) -> '_67.IntegrationMethod.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _67.IntegrationMethod.type_()

    @property
    def selected_value(self) -> '_67.IntegrationMethod':
        '''IntegrationMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_67.IntegrationMethod]':
        '''List[IntegrationMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_ValueInputOption(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_ValueInputOption

    A specific implementation of 'EnumWithSelectedValue' for 'ValueInputOption' types.
    '''

    __hash__ = None
    __qualname__ = 'ValueInputOption'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_86.ValueInputOption':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _86.ValueInputOption

    @classmethod
    def implicit_type(cls) -> '_86.ValueInputOption.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _86.ValueInputOption.type_()

    @property
    def selected_value(self) -> '_86.ValueInputOption':
        '''ValueInputOption: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_86.ValueInputOption]':
        '''List[ValueInputOption]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_SinglePointSelectionMethod(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_SinglePointSelectionMethod

    A specific implementation of 'EnumWithSelectedValue' for 'SinglePointSelectionMethod' types.
    '''

    __hash__ = None
    __qualname__ = 'SinglePointSelectionMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_93.SinglePointSelectionMethod':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _93.SinglePointSelectionMethod

    @classmethod
    def implicit_type(cls) -> '_93.SinglePointSelectionMethod.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _93.SinglePointSelectionMethod.type_()

    @property
    def selected_value(self) -> '_93.SinglePointSelectionMethod':
        '''SinglePointSelectionMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_93.SinglePointSelectionMethod]':
        '''List[SinglePointSelectionMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_ModeInputType(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_ModeInputType

    A specific implementation of 'EnumWithSelectedValue' for 'ModeInputType' types.
    '''

    __hash__ = None
    __qualname__ = 'ModeInputType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_73.ModeInputType':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _73.ModeInputType

    @classmethod
    def implicit_type(cls) -> '_73.ModeInputType.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _73.ModeInputType.type_()

    @property
    def selected_value(self) -> '_73.ModeInputType':
        '''ModeInputType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_73.ModeInputType]':
        '''List[ModeInputType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_MaterialPropertyClass(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_MaterialPropertyClass

    A specific implementation of 'EnumWithSelectedValue' for 'MaterialPropertyClass' types.
    '''

    __hash__ = None
    __qualname__ = 'MaterialPropertyClass'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1181.MaterialPropertyClass':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _1181.MaterialPropertyClass

    @classmethod
    def implicit_type(cls) -> '_1181.MaterialPropertyClass.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1181.MaterialPropertyClass.type_()

    @property
    def selected_value(self) -> '_1181.MaterialPropertyClass':
        '''MaterialPropertyClass: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_1181.MaterialPropertyClass]':
        '''List[MaterialPropertyClass]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_LubricantDefinition(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_LubricantDefinition

    A specific implementation of 'EnumWithSelectedValue' for 'LubricantDefinition' types.
    '''

    __hash__ = None
    __qualname__ = 'LubricantDefinition'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_231.LubricantDefinition':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _231.LubricantDefinition

    @classmethod
    def implicit_type(cls) -> '_231.LubricantDefinition.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _231.LubricantDefinition.type_()

    @property
    def selected_value(self) -> '_231.LubricantDefinition':
        '''LubricantDefinition: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_231.LubricantDefinition]':
        '''List[LubricantDefinition]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_LubricantViscosityClassISO(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_LubricantViscosityClassISO

    A specific implementation of 'EnumWithSelectedValue' for 'LubricantViscosityClassISO' types.
    '''

    __hash__ = None
    __qualname__ = 'LubricantViscosityClassISO'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_235.LubricantViscosityClassISO':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _235.LubricantViscosityClassISO

    @classmethod
    def implicit_type(cls) -> '_235.LubricantViscosityClassISO.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _235.LubricantViscosityClassISO.type_()

    @property
    def selected_value(self) -> '_235.LubricantViscosityClassISO':
        '''LubricantViscosityClassISO: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_235.LubricantViscosityClassISO]':
        '''List[LubricantViscosityClassISO]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_MicroGeometryModel(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_MicroGeometryModel

    A specific implementation of 'EnumWithSelectedValue' for 'MicroGeometryModel' types.
    '''

    __hash__ = None
    __qualname__ = 'MicroGeometryModel'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_302.MicroGeometryModel':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _302.MicroGeometryModel

    @classmethod
    def implicit_type(cls) -> '_302.MicroGeometryModel.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _302.MicroGeometryModel.type_()

    @property
    def selected_value(self) -> '_302.MicroGeometryModel':
        '''MicroGeometryModel: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_302.MicroGeometryModel]':
        '''List[MicroGeometryModel]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_ExtrapolationOptions(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_ExtrapolationOptions

    A specific implementation of 'EnumWithSelectedValue' for 'ExtrapolationOptions' types.
    '''

    __hash__ = None
    __qualname__ = 'ExtrapolationOptions'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1304.ExtrapolationOptions':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _1304.ExtrapolationOptions

    @classmethod
    def implicit_type(cls) -> '_1304.ExtrapolationOptions.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1304.ExtrapolationOptions.type_()

    @property
    def selected_value(self) -> '_1304.ExtrapolationOptions':
        '''ExtrapolationOptions: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_1304.ExtrapolationOptions]':
        '''List[ExtrapolationOptions]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_ScuffingFlashTemperatureRatingMethod(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_ScuffingFlashTemperatureRatingMethod

    A specific implementation of 'EnumWithSelectedValue' for 'ScuffingFlashTemperatureRatingMethod' types.
    '''

    __hash__ = None
    __qualname__ = 'ScuffingFlashTemperatureRatingMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_441.ScuffingFlashTemperatureRatingMethod':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _441.ScuffingFlashTemperatureRatingMethod

    @classmethod
    def implicit_type(cls) -> '_441.ScuffingFlashTemperatureRatingMethod.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _441.ScuffingFlashTemperatureRatingMethod.type_()

    @property
    def selected_value(self) -> '_441.ScuffingFlashTemperatureRatingMethod':
        '''ScuffingFlashTemperatureRatingMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_441.ScuffingFlashTemperatureRatingMethod]':
        '''List[ScuffingFlashTemperatureRatingMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_ScuffingIntegralTemperatureRatingMethod(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_ScuffingIntegralTemperatureRatingMethod

    A specific implementation of 'EnumWithSelectedValue' for 'ScuffingIntegralTemperatureRatingMethod' types.
    '''

    __hash__ = None
    __qualname__ = 'ScuffingIntegralTemperatureRatingMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_442.ScuffingIntegralTemperatureRatingMethod':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _442.ScuffingIntegralTemperatureRatingMethod

    @classmethod
    def implicit_type(cls) -> '_442.ScuffingIntegralTemperatureRatingMethod.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _442.ScuffingIntegralTemperatureRatingMethod.type_()

    @property
    def selected_value(self) -> '_442.ScuffingIntegralTemperatureRatingMethod':
        '''ScuffingIntegralTemperatureRatingMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_442.ScuffingIntegralTemperatureRatingMethod]':
        '''List[ScuffingIntegralTemperatureRatingMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_CylindricalGearRatingMethods(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_CylindricalGearRatingMethods

    A specific implementation of 'EnumWithSelectedValue' for 'CylindricalGearRatingMethods' types.
    '''

    __hash__ = None
    __qualname__ = 'CylindricalGearRatingMethods'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_221.CylindricalGearRatingMethods':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _221.CylindricalGearRatingMethods

    @classmethod
    def implicit_type(cls) -> '_221.CylindricalGearRatingMethods.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _221.CylindricalGearRatingMethods.type_()

    @property
    def selected_value(self) -> '_221.CylindricalGearRatingMethods':
        '''CylindricalGearRatingMethods: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_221.CylindricalGearRatingMethods]':
        '''List[CylindricalGearRatingMethods]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_LocationOfTipReliefEvaluation(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_LocationOfTipReliefEvaluation

    A specific implementation of 'EnumWithSelectedValue' for 'LocationOfTipReliefEvaluation' types.
    '''

    __hash__ = None
    __qualname__ = 'LocationOfTipReliefEvaluation'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_530.LocationOfTipReliefEvaluation':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _530.LocationOfTipReliefEvaluation

    @classmethod
    def implicit_type(cls) -> '_530.LocationOfTipReliefEvaluation.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _530.LocationOfTipReliefEvaluation.type_()

    @property
    def selected_value(self) -> '_530.LocationOfTipReliefEvaluation':
        '''LocationOfTipReliefEvaluation: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_530.LocationOfTipReliefEvaluation]':
        '''List[LocationOfTipReliefEvaluation]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_LocationOfRootReliefEvaluation(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_LocationOfRootReliefEvaluation

    A specific implementation of 'EnumWithSelectedValue' for 'LocationOfRootReliefEvaluation' types.
    '''

    __hash__ = None
    __qualname__ = 'LocationOfRootReliefEvaluation'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_529.LocationOfRootReliefEvaluation':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _529.LocationOfRootReliefEvaluation

    @classmethod
    def implicit_type(cls) -> '_529.LocationOfRootReliefEvaluation.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _529.LocationOfRootReliefEvaluation.type_()

    @property
    def selected_value(self) -> '_529.LocationOfRootReliefEvaluation':
        '''LocationOfRootReliefEvaluation: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_529.LocationOfRootReliefEvaluation]':
        '''List[LocationOfRootReliefEvaluation]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_LocationOfEvaluationUpperLimit(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_LocationOfEvaluationUpperLimit

    A specific implementation of 'EnumWithSelectedValue' for 'LocationOfEvaluationUpperLimit' types.
    '''

    __hash__ = None
    __qualname__ = 'LocationOfEvaluationUpperLimit'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_528.LocationOfEvaluationUpperLimit':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _528.LocationOfEvaluationUpperLimit

    @classmethod
    def implicit_type(cls) -> '_528.LocationOfEvaluationUpperLimit.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _528.LocationOfEvaluationUpperLimit.type_()

    @property
    def selected_value(self) -> '_528.LocationOfEvaluationUpperLimit':
        '''LocationOfEvaluationUpperLimit: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_528.LocationOfEvaluationUpperLimit]':
        '''List[LocationOfEvaluationUpperLimit]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_LocationOfEvaluationLowerLimit(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_LocationOfEvaluationLowerLimit

    A specific implementation of 'EnumWithSelectedValue' for 'LocationOfEvaluationLowerLimit' types.
    '''

    __hash__ = None
    __qualname__ = 'LocationOfEvaluationLowerLimit'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_527.LocationOfEvaluationLowerLimit':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _527.LocationOfEvaluationLowerLimit

    @classmethod
    def implicit_type(cls) -> '_527.LocationOfEvaluationLowerLimit.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _527.LocationOfEvaluationLowerLimit.type_()

    @property
    def selected_value(self) -> '_527.LocationOfEvaluationLowerLimit':
        '''LocationOfEvaluationLowerLimit: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_527.LocationOfEvaluationLowerLimit]':
        '''List[LocationOfEvaluationLowerLimit]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_CylindricalMftRoughingMethods(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_CylindricalMftRoughingMethods

    A specific implementation of 'EnumWithSelectedValue' for 'CylindricalMftRoughingMethods' types.
    '''

    __hash__ = None
    __qualname__ = 'CylindricalMftRoughingMethods'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_578.CylindricalMftRoughingMethods':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _578.CylindricalMftRoughingMethods

    @classmethod
    def implicit_type(cls) -> '_578.CylindricalMftRoughingMethods.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _578.CylindricalMftRoughingMethods.type_()

    @property
    def selected_value(self) -> '_578.CylindricalMftRoughingMethods':
        '''CylindricalMftRoughingMethods: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_578.CylindricalMftRoughingMethods]':
        '''List[CylindricalMftRoughingMethods]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_CylindricalMftFinishingMethods(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_CylindricalMftFinishingMethods

    A specific implementation of 'EnumWithSelectedValue' for 'CylindricalMftFinishingMethods' types.
    '''

    __hash__ = None
    __qualname__ = 'CylindricalMftFinishingMethods'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_577.CylindricalMftFinishingMethods':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _577.CylindricalMftFinishingMethods

    @classmethod
    def implicit_type(cls) -> '_577.CylindricalMftFinishingMethods.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _577.CylindricalMftFinishingMethods.type_()

    @property
    def selected_value(self) -> '_577.CylindricalMftFinishingMethods':
        '''CylindricalMftFinishingMethods: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_577.CylindricalMftFinishingMethods]':
        '''List[CylindricalMftFinishingMethods]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_MicroGeometryDefinitionType(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_MicroGeometryDefinitionType

    A specific implementation of 'EnumWithSelectedValue' for 'MicroGeometryDefinitionType' types.
    '''

    __hash__ = None
    __qualname__ = 'MicroGeometryDefinitionType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_600.MicroGeometryDefinitionType':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _600.MicroGeometryDefinitionType

    @classmethod
    def implicit_type(cls) -> '_600.MicroGeometryDefinitionType.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _600.MicroGeometryDefinitionType.type_()

    @property
    def selected_value(self) -> '_600.MicroGeometryDefinitionType':
        '''MicroGeometryDefinitionType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_600.MicroGeometryDefinitionType]':
        '''List[MicroGeometryDefinitionType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_MicroGeometryDefinitionMethod(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_MicroGeometryDefinitionMethod

    A specific implementation of 'EnumWithSelectedValue' for 'MicroGeometryDefinitionMethod' types.
    '''

    __hash__ = None
    __qualname__ = 'MicroGeometryDefinitionMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_599.MicroGeometryDefinitionMethod':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _599.MicroGeometryDefinitionMethod

    @classmethod
    def implicit_type(cls) -> '_599.MicroGeometryDefinitionMethod.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _599.MicroGeometryDefinitionMethod.type_()

    @property
    def selected_value(self) -> '_599.MicroGeometryDefinitionMethod':
        '''MicroGeometryDefinitionMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_599.MicroGeometryDefinitionMethod]':
        '''List[MicroGeometryDefinitionMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_ChartType(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_ChartType

    A specific implementation of 'EnumWithSelectedValue' for 'ChartType' types.
    '''

    __hash__ = None
    __qualname__ = 'ChartType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_597.ChartType':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _597.ChartType

    @classmethod
    def implicit_type(cls) -> '_597.ChartType.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _597.ChartType.type_()

    @property
    def selected_value(self) -> '_597.ChartType':
        '''ChartType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_597.ChartType]':
        '''List[ChartType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_Flank(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_Flank

    A specific implementation of 'EnumWithSelectedValue' for 'Flank' types.
    '''

    __hash__ = None
    __qualname__ = 'Flank'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_581.Flank':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _581.Flank

    @classmethod
    def implicit_type(cls) -> '_581.Flank.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _581.Flank.type_()

    @property
    def selected_value(self) -> '_581.Flank':
        '''Flank: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_581.Flank]':
        '''List[Flank]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_ActiveProcessMethod(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_ActiveProcessMethod

    A specific implementation of 'EnumWithSelectedValue' for 'ActiveProcessMethod' types.
    '''

    __hash__ = None
    __qualname__ = 'ActiveProcessMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_612.ActiveProcessMethod':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _612.ActiveProcessMethod

    @classmethod
    def implicit_type(cls) -> '_612.ActiveProcessMethod.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _612.ActiveProcessMethod.type_()

    @property
    def selected_value(self) -> '_612.ActiveProcessMethod':
        '''ActiveProcessMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_612.ActiveProcessMethod]':
        '''List[ActiveProcessMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_CutterFlankSections(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_CutterFlankSections

    A specific implementation of 'EnumWithSelectedValue' for 'CutterFlankSections' types.
    '''

    __hash__ = None
    __qualname__ = 'CutterFlankSections'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_563.CutterFlankSections':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _563.CutterFlankSections

    @classmethod
    def implicit_type(cls) -> '_563.CutterFlankSections.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _563.CutterFlankSections.type_()

    @property
    def selected_value(self) -> '_563.CutterFlankSections':
        '''CutterFlankSections: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_563.CutterFlankSections]':
        '''List[CutterFlankSections]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_BasicCurveTypes(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_BasicCurveTypes

    A specific implementation of 'EnumWithSelectedValue' for 'BasicCurveTypes' types.
    '''

    __hash__ = None
    __qualname__ = 'BasicCurveTypes'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_278.BasicCurveTypes':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _278.BasicCurveTypes

    @classmethod
    def implicit_type(cls) -> '_278.BasicCurveTypes.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _278.BasicCurveTypes.type_()

    @property
    def selected_value(self) -> '_278.BasicCurveTypes':
        '''BasicCurveTypes: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_278.BasicCurveTypes]':
        '''List[BasicCurveTypes]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_ThicknessType(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_ThicknessType

    A specific implementation of 'EnumWithSelectedValue' for 'ThicknessType' types.
    '''

    __hash__ = None
    __qualname__ = 'ThicknessType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1028.ThicknessType':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _1028.ThicknessType

    @classmethod
    def implicit_type(cls) -> '_1028.ThicknessType.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1028.ThicknessType.type_()

    @property
    def selected_value(self) -> '_1028.ThicknessType':
        '''ThicknessType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_1028.ThicknessType]':
        '''List[ThicknessType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_ConicalManufactureMethods(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_ConicalManufactureMethods

    A specific implementation of 'EnumWithSelectedValue' for 'ConicalManufactureMethods' types.
    '''

    __hash__ = None
    __qualname__ = 'ConicalManufactureMethods'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1100.ConicalManufactureMethods':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _1100.ConicalManufactureMethods

    @classmethod
    def implicit_type(cls) -> '_1100.ConicalManufactureMethods.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1100.ConicalManufactureMethods.type_()

    @property
    def selected_value(self) -> '_1100.ConicalManufactureMethods':
        '''ConicalManufactureMethods: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_1100.ConicalManufactureMethods]':
        '''List[ConicalManufactureMethods]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_ConicalMachineSettingCalculationMethods(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_ConicalMachineSettingCalculationMethods

    A specific implementation of 'EnumWithSelectedValue' for 'ConicalMachineSettingCalculationMethods' types.
    '''

    __hash__ = None
    __qualname__ = 'ConicalMachineSettingCalculationMethods'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1099.ConicalMachineSettingCalculationMethods':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _1099.ConicalMachineSettingCalculationMethods

    @classmethod
    def implicit_type(cls) -> '_1099.ConicalMachineSettingCalculationMethods.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1099.ConicalMachineSettingCalculationMethods.type_()

    @property
    def selected_value(self) -> '_1099.ConicalMachineSettingCalculationMethods':
        '''ConicalMachineSettingCalculationMethods: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_1099.ConicalMachineSettingCalculationMethods]':
        '''List[ConicalMachineSettingCalculationMethods]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_CandidateDisplayChoice(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_CandidateDisplayChoice

    A specific implementation of 'EnumWithSelectedValue' for 'CandidateDisplayChoice' types.
    '''

    __hash__ = None
    __qualname__ = 'CandidateDisplayChoice'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_857.CandidateDisplayChoice':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _857.CandidateDisplayChoice

    @classmethod
    def implicit_type(cls) -> '_857.CandidateDisplayChoice.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _857.CandidateDisplayChoice.type_()

    @property
    def selected_value(self) -> '_857.CandidateDisplayChoice':
        '''CandidateDisplayChoice: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_857.CandidateDisplayChoice]':
        '''List[CandidateDisplayChoice]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_Severity(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_Severity

    A specific implementation of 'EnumWithSelectedValue' for 'Severity' types.
    '''

    __hash__ = None
    __qualname__ = 'Severity'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1556.Severity':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _1556.Severity

    @classmethod
    def implicit_type(cls) -> '_1556.Severity.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1556.Severity.type_()

    @property
    def selected_value(self) -> '_1556.Severity':
        '''Severity: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_1556.Severity]':
        '''List[Severity]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_GeometrySpecificationType(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_GeometrySpecificationType

    A specific implementation of 'EnumWithSelectedValue' for 'GeometrySpecificationType' types.
    '''

    __hash__ = None
    __qualname__ = 'GeometrySpecificationType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1000.GeometrySpecificationType':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _1000.GeometrySpecificationType

    @classmethod
    def implicit_type(cls) -> '_1000.GeometrySpecificationType.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1000.GeometrySpecificationType.type_()

    @property
    def selected_value(self) -> '_1000.GeometrySpecificationType':
        '''GeometrySpecificationType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_1000.GeometrySpecificationType]':
        '''List[GeometrySpecificationType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_StatusItemSeverity(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_StatusItemSeverity

    A specific implementation of 'EnumWithSelectedValue' for 'StatusItemSeverity' types.
    '''

    __hash__ = None
    __qualname__ = 'StatusItemSeverity'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1559.StatusItemSeverity':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _1559.StatusItemSeverity

    @classmethod
    def implicit_type(cls) -> '_1559.StatusItemSeverity.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1559.StatusItemSeverity.type_()

    @property
    def selected_value(self) -> '_1559.StatusItemSeverity':
        '''StatusItemSeverity: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_1559.StatusItemSeverity]':
        '''List[StatusItemSeverity]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_LubricationMethods(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_LubricationMethods

    A specific implementation of 'EnumWithSelectedValue' for 'LubricationMethods' types.
    '''

    __hash__ = None
    __qualname__ = 'LubricationMethods'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_300.LubricationMethods':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _300.LubricationMethods

    @classmethod
    def implicit_type(cls) -> '_300.LubricationMethods.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _300.LubricationMethods.type_()

    @property
    def selected_value(self) -> '_300.LubricationMethods':
        '''LubricationMethods: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_300.LubricationMethods]':
        '''List[LubricationMethods]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_MicropittingCoefficientOfFrictionCalculationMethod(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_MicropittingCoefficientOfFrictionCalculationMethod

    A specific implementation of 'EnumWithSelectedValue' for 'MicropittingCoefficientOfFrictionCalculationMethod' types.
    '''

    __hash__ = None
    __qualname__ = 'MicropittingCoefficientOfFrictionCalculationMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_303.MicropittingCoefficientOfFrictionCalculationMethod':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _303.MicropittingCoefficientOfFrictionCalculationMethod

    @classmethod
    def implicit_type(cls) -> '_303.MicropittingCoefficientOfFrictionCalculationMethod.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _303.MicropittingCoefficientOfFrictionCalculationMethod.type_()

    @property
    def selected_value(self) -> '_303.MicropittingCoefficientOfFrictionCalculationMethod':
        '''MicropittingCoefficientOfFrictionCalculationMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_303.MicropittingCoefficientOfFrictionCalculationMethod]':
        '''List[MicropittingCoefficientOfFrictionCalculationMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_ScuffingCoefficientOfFrictionMethods(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_ScuffingCoefficientOfFrictionMethods

    A specific implementation of 'EnumWithSelectedValue' for 'ScuffingCoefficientOfFrictionMethods' types.
    '''

    __hash__ = None
    __qualname__ = 'ScuffingCoefficientOfFrictionMethods'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1020.ScuffingCoefficientOfFrictionMethods':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _1020.ScuffingCoefficientOfFrictionMethods

    @classmethod
    def implicit_type(cls) -> '_1020.ScuffingCoefficientOfFrictionMethods.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1020.ScuffingCoefficientOfFrictionMethods.type_()

    @property
    def selected_value(self) -> '_1020.ScuffingCoefficientOfFrictionMethods':
        '''ScuffingCoefficientOfFrictionMethods: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_1020.ScuffingCoefficientOfFrictionMethods]':
        '''List[ScuffingCoefficientOfFrictionMethods]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_ContactResultType(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_ContactResultType

    A specific implementation of 'EnumWithSelectedValue' for 'ContactResultType' types.
    '''

    __hash__ = None
    __qualname__ = 'ContactResultType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_781.ContactResultType':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _781.ContactResultType

    @classmethod
    def implicit_type(cls) -> '_781.ContactResultType.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _781.ContactResultType.type_()

    @property
    def selected_value(self) -> '_781.ContactResultType':
        '''ContactResultType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_781.ContactResultType]':
        '''List[ContactResultType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_StressResultsType(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_StressResultsType

    A specific implementation of 'EnumWithSelectedValue' for 'StressResultsType' types.
    '''

    __hash__ = None
    __qualname__ = 'StressResultsType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_82.StressResultsType':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _82.StressResultsType

    @classmethod
    def implicit_type(cls) -> '_82.StressResultsType.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _82.StressResultsType.type_()

    @property
    def selected_value(self) -> '_82.StressResultsType':
        '''StressResultsType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_82.StressResultsType]':
        '''List[StressResultsType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_CylindricalGearPairCreationOptions_DerivedParameterOption(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_CylindricalGearPairCreationOptions_DerivedParameterOption

    A specific implementation of 'EnumWithSelectedValue' for 'CylindricalGearPairCreationOptions.DerivedParameterOption' types.
    '''

    __hash__ = None
    __qualname__ = 'CylindricalGearPairCreationOptions.DerivedParameterOption'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1088.CylindricalGearPairCreationOptions.DerivedParameterOption':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _1088.CylindricalGearPairCreationOptions.DerivedParameterOption

    @classmethod
    def implicit_type(cls) -> '_1088.CylindricalGearPairCreationOptions.DerivedParameterOption.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1088.CylindricalGearPairCreationOptions.DerivedParameterOption.type_()

    @property
    def selected_value(self) -> '_1088.CylindricalGearPairCreationOptions.DerivedParameterOption':
        '''CylindricalGearPairCreationOptions.DerivedParameterOption: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_1088.CylindricalGearPairCreationOptions.DerivedParameterOption]':
        '''List[CylindricalGearPairCreationOptions.DerivedParameterOption]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_ToothThicknessSpecificationMethod(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_ToothThicknessSpecificationMethod

    A specific implementation of 'EnumWithSelectedValue' for 'ToothThicknessSpecificationMethod' types.
    '''

    __hash__ = None
    __qualname__ = 'ToothThicknessSpecificationMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1132.ToothThicknessSpecificationMethod':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _1132.ToothThicknessSpecificationMethod

    @classmethod
    def implicit_type(cls) -> '_1132.ToothThicknessSpecificationMethod.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1132.ToothThicknessSpecificationMethod.type_()

    @property
    def selected_value(self) -> '_1132.ToothThicknessSpecificationMethod':
        '''ToothThicknessSpecificationMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_1132.ToothThicknessSpecificationMethod]':
        '''List[ToothThicknessSpecificationMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_LoadDistributionFactorMethods(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_LoadDistributionFactorMethods

    A specific implementation of 'EnumWithSelectedValue' for 'LoadDistributionFactorMethods' types.
    '''

    __hash__ = None
    __qualname__ = 'LoadDistributionFactorMethods'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1111.LoadDistributionFactorMethods':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _1111.LoadDistributionFactorMethods

    @classmethod
    def implicit_type(cls) -> '_1111.LoadDistributionFactorMethods.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1111.LoadDistributionFactorMethods.type_()

    @property
    def selected_value(self) -> '_1111.LoadDistributionFactorMethods':
        '''LoadDistributionFactorMethods: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_1111.LoadDistributionFactorMethods]':
        '''List[LoadDistributionFactorMethods]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_AGMAGleasonConicalGearGeometryMethods(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_AGMAGleasonConicalGearGeometryMethods

    A specific implementation of 'EnumWithSelectedValue' for 'AGMAGleasonConicalGearGeometryMethods' types.
    '''

    __hash__ = None
    __qualname__ = 'AGMAGleasonConicalGearGeometryMethods'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1121.AGMAGleasonConicalGearGeometryMethods':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _1121.AGMAGleasonConicalGearGeometryMethods

    @classmethod
    def implicit_type(cls) -> '_1121.AGMAGleasonConicalGearGeometryMethods.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1121.AGMAGleasonConicalGearGeometryMethods.type_()

    @property
    def selected_value(self) -> '_1121.AGMAGleasonConicalGearGeometryMethods':
        '''AGMAGleasonConicalGearGeometryMethods: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_1121.AGMAGleasonConicalGearGeometryMethods]':
        '''List[AGMAGleasonConicalGearGeometryMethods]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_ProSolveSolverType(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_ProSolveSolverType

    A specific implementation of 'EnumWithSelectedValue' for 'ProSolveSolverType' types.
    '''

    __hash__ = None
    __qualname__ = 'ProSolveSolverType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1179.ProSolveSolverType':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _1179.ProSolveSolverType

    @classmethod
    def implicit_type(cls) -> '_1179.ProSolveSolverType.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1179.ProSolveSolverType.type_()

    @property
    def selected_value(self) -> '_1179.ProSolveSolverType':
        '''ProSolveSolverType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_1179.ProSolveSolverType]':
        '''List[ProSolveSolverType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_ProSolveMpcType(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_ProSolveMpcType

    A specific implementation of 'EnumWithSelectedValue' for 'ProSolveMpcType' types.
    '''

    __hash__ = None
    __qualname__ = 'ProSolveMpcType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1178.ProSolveMpcType':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _1178.ProSolveMpcType

    @classmethod
    def implicit_type(cls) -> '_1178.ProSolveMpcType.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1178.ProSolveMpcType.type_()

    @property
    def selected_value(self) -> '_1178.ProSolveMpcType':
        '''ProSolveMpcType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_1178.ProSolveMpcType]':
        '''List[ProSolveMpcType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_ITDesignation(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_ITDesignation

    A specific implementation of 'EnumWithSelectedValue' for 'ITDesignation' types.
    '''

    __hash__ = None
    __qualname__ = 'ITDesignation'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1651.ITDesignation':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _1651.ITDesignation

    @classmethod
    def implicit_type(cls) -> '_1651.ITDesignation.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1651.ITDesignation.type_()

    @property
    def selected_value(self) -> '_1651.ITDesignation':
        '''ITDesignation: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_1651.ITDesignation]':
        '''List[ITDesignation]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_DudleyEffectiveLengthApproximationOption(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_DudleyEffectiveLengthApproximationOption

    A specific implementation of 'EnumWithSelectedValue' for 'DudleyEffectiveLengthApproximationOption' types.
    '''

    __hash__ = None
    __qualname__ = 'DudleyEffectiveLengthApproximationOption'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1189.DudleyEffectiveLengthApproximationOption':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _1189.DudleyEffectiveLengthApproximationOption

    @classmethod
    def implicit_type(cls) -> '_1189.DudleyEffectiveLengthApproximationOption.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1189.DudleyEffectiveLengthApproximationOption.type_()

    @property
    def selected_value(self) -> '_1189.DudleyEffectiveLengthApproximationOption':
        '''DudleyEffectiveLengthApproximationOption: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_1189.DudleyEffectiveLengthApproximationOption]':
        '''List[DudleyEffectiveLengthApproximationOption]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_SplineRatingTypes(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_SplineRatingTypes

    A specific implementation of 'EnumWithSelectedValue' for 'SplineRatingTypes' types.
    '''

    __hash__ = None
    __qualname__ = 'SplineRatingTypes'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1212.SplineRatingTypes':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _1212.SplineRatingTypes

    @classmethod
    def implicit_type(cls) -> '_1212.SplineRatingTypes.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1212.SplineRatingTypes.type_()

    @property
    def selected_value(self) -> '_1212.SplineRatingTypes':
        '''SplineRatingTypes: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_1212.SplineRatingTypes]':
        '''List[SplineRatingTypes]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_Modules(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_Modules

    A specific implementation of 'EnumWithSelectedValue' for 'Modules' types.
    '''

    __hash__ = None
    __qualname__ = 'Modules'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1198.Modules':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _1198.Modules

    @classmethod
    def implicit_type(cls) -> '_1198.Modules.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1198.Modules.type_()

    @property
    def selected_value(self) -> '_1198.Modules':
        '''Modules: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_1198.Modules]':
        '''List[Modules]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_PressureAngleTypes(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_PressureAngleTypes

    A specific implementation of 'EnumWithSelectedValue' for 'PressureAngleTypes' types.
    '''

    __hash__ = None
    __qualname__ = 'PressureAngleTypes'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1199.PressureAngleTypes':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _1199.PressureAngleTypes

    @classmethod
    def implicit_type(cls) -> '_1199.PressureAngleTypes.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1199.PressureAngleTypes.type_()

    @property
    def selected_value(self) -> '_1199.PressureAngleTypes':
        '''PressureAngleTypes: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_1199.PressureAngleTypes]':
        '''List[PressureAngleTypes]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_SplineFitClassType(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_SplineFitClassType

    A specific implementation of 'EnumWithSelectedValue' for 'SplineFitClassType' types.
    '''

    __hash__ = None
    __qualname__ = 'SplineFitClassType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1207.SplineFitClassType':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _1207.SplineFitClassType

    @classmethod
    def implicit_type(cls) -> '_1207.SplineFitClassType.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1207.SplineFitClassType.type_()

    @property
    def selected_value(self) -> '_1207.SplineFitClassType':
        '''SplineFitClassType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_1207.SplineFitClassType]':
        '''List[SplineFitClassType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_SplineToleranceClassTypes(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_SplineToleranceClassTypes

    A specific implementation of 'EnumWithSelectedValue' for 'SplineToleranceClassTypes' types.
    '''

    __hash__ = None
    __qualname__ = 'SplineToleranceClassTypes'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1213.SplineToleranceClassTypes':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _1213.SplineToleranceClassTypes

    @classmethod
    def implicit_type(cls) -> '_1213.SplineToleranceClassTypes.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1213.SplineToleranceClassTypes.type_()

    @property
    def selected_value(self) -> '_1213.SplineToleranceClassTypes':
        '''SplineToleranceClassTypes: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_1213.SplineToleranceClassTypes]':
        '''List[SplineToleranceClassTypes]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_Table4JointInterfaceTypes(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_Table4JointInterfaceTypes

    A specific implementation of 'EnumWithSelectedValue' for 'Table4JointInterfaceTypes' types.
    '''

    __hash__ = None
    __qualname__ = 'Table4JointInterfaceTypes'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1243.Table4JointInterfaceTypes':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _1243.Table4JointInterfaceTypes

    @classmethod
    def implicit_type(cls) -> '_1243.Table4JointInterfaceTypes.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1243.Table4JointInterfaceTypes.type_()

    @property
    def selected_value(self) -> '_1243.Table4JointInterfaceTypes':
        '''Table4JointInterfaceTypes: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_1243.Table4JointInterfaceTypes]':
        '''List[Table4JointInterfaceTypes]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_ExecutableDirectoryCopier_Option(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_ExecutableDirectoryCopier_Option

    A specific implementation of 'EnumWithSelectedValue' for 'ExecutableDirectoryCopier.Option' types.
    '''

    __hash__ = None
    __qualname__ = 'ExecutableDirectoryCopier.Option'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1372.ExecutableDirectoryCopier.Option':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _1372.ExecutableDirectoryCopier.Option

    @classmethod
    def implicit_type(cls) -> '_1372.ExecutableDirectoryCopier.Option.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1372.ExecutableDirectoryCopier.Option.type_()

    @property
    def selected_value(self) -> '_1372.ExecutableDirectoryCopier.Option':
        '''ExecutableDirectoryCopier.Option: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_1372.ExecutableDirectoryCopier.Option]':
        '''List[ExecutableDirectoryCopier.Option]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_CadPageOrientation(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_CadPageOrientation

    A specific implementation of 'EnumWithSelectedValue' for 'CadPageOrientation' types.
    '''

    __hash__ = None
    __qualname__ = 'CadPageOrientation'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1515.CadPageOrientation':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _1515.CadPageOrientation

    @classmethod
    def implicit_type(cls) -> '_1515.CadPageOrientation.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1515.CadPageOrientation.type_()

    @property
    def selected_value(self) -> '_1515.CadPageOrientation':
        '''CadPageOrientation: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_1515.CadPageOrientation]':
        '''List[CadPageOrientation]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_RollerBearingProfileTypes(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_RollerBearingProfileTypes

    A specific implementation of 'EnumWithSelectedValue' for 'RollerBearingProfileTypes' types.
    '''

    __hash__ = None
    __qualname__ = 'RollerBearingProfileTypes'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1633.RollerBearingProfileTypes':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _1633.RollerBearingProfileTypes

    @classmethod
    def implicit_type(cls) -> '_1633.RollerBearingProfileTypes.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1633.RollerBearingProfileTypes.type_()

    @property
    def selected_value(self) -> '_1633.RollerBearingProfileTypes':
        '''RollerBearingProfileTypes: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_1633.RollerBearingProfileTypes]':
        '''List[RollerBearingProfileTypes]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_FluidFilmTemperatureOptions(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_FluidFilmTemperatureOptions

    A specific implementation of 'EnumWithSelectedValue' for 'FluidFilmTemperatureOptions' types.
    '''

    __hash__ = None
    __qualname__ = 'FluidFilmTemperatureOptions'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1626.FluidFilmTemperatureOptions':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _1626.FluidFilmTemperatureOptions

    @classmethod
    def implicit_type(cls) -> '_1626.FluidFilmTemperatureOptions.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1626.FluidFilmTemperatureOptions.type_()

    @property
    def selected_value(self) -> '_1626.FluidFilmTemperatureOptions':
        '''FluidFilmTemperatureOptions: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_1626.FluidFilmTemperatureOptions]':
        '''List[FluidFilmTemperatureOptions]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_SupportToleranceLocationDesignation(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_SupportToleranceLocationDesignation

    A specific implementation of 'EnumWithSelectedValue' for 'SupportToleranceLocationDesignation' types.
    '''

    __hash__ = None
    __qualname__ = 'SupportToleranceLocationDesignation'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1663.SupportToleranceLocationDesignation':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _1663.SupportToleranceLocationDesignation

    @classmethod
    def implicit_type(cls) -> '_1663.SupportToleranceLocationDesignation.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1663.SupportToleranceLocationDesignation.type_()

    @property
    def selected_value(self) -> '_1663.SupportToleranceLocationDesignation':
        '''SupportToleranceLocationDesignation: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_1663.SupportToleranceLocationDesignation]':
        '''List[SupportToleranceLocationDesignation]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_LoadedBallElementPropertyType(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_LoadedBallElementPropertyType

    A specific implementation of 'EnumWithSelectedValue' for 'LoadedBallElementPropertyType' types.
    '''

    __hash__ = None
    __qualname__ = 'LoadedBallElementPropertyType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1701.LoadedBallElementPropertyType':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _1701.LoadedBallElementPropertyType

    @classmethod
    def implicit_type(cls) -> '_1701.LoadedBallElementPropertyType.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1701.LoadedBallElementPropertyType.type_()

    @property
    def selected_value(self) -> '_1701.LoadedBallElementPropertyType':
        '''LoadedBallElementPropertyType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_1701.LoadedBallElementPropertyType]':
        '''List[LoadedBallElementPropertyType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_RollingBearingArrangement(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_RollingBearingArrangement

    A specific implementation of 'EnumWithSelectedValue' for 'RollingBearingArrangement' types.
    '''

    __hash__ = None
    __qualname__ = 'RollingBearingArrangement'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1634.RollingBearingArrangement':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _1634.RollingBearingArrangement

    @classmethod
    def implicit_type(cls) -> '_1634.RollingBearingArrangement.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1634.RollingBearingArrangement.type_()

    @property
    def selected_value(self) -> '_1634.RollingBearingArrangement':
        '''RollingBearingArrangement: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_1634.RollingBearingArrangement]':
        '''List[RollingBearingArrangement]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_RollingBearingRaceType(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_RollingBearingRaceType

    A specific implementation of 'EnumWithSelectedValue' for 'RollingBearingRaceType' types.
    '''

    __hash__ = None
    __qualname__ = 'RollingBearingRaceType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1637.RollingBearingRaceType':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _1637.RollingBearingRaceType

    @classmethod
    def implicit_type(cls) -> '_1637.RollingBearingRaceType.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1637.RollingBearingRaceType.type_()

    @property
    def selected_value(self) -> '_1637.RollingBearingRaceType':
        '''RollingBearingRaceType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_1637.RollingBearingRaceType]':
        '''List[RollingBearingRaceType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_BasicDynamicLoadRatingCalculationMethod(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_BasicDynamicLoadRatingCalculationMethod

    A specific implementation of 'EnumWithSelectedValue' for 'BasicDynamicLoadRatingCalculationMethod' types.
    '''

    __hash__ = None
    __qualname__ = 'BasicDynamicLoadRatingCalculationMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1614.BasicDynamicLoadRatingCalculationMethod':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _1614.BasicDynamicLoadRatingCalculationMethod

    @classmethod
    def implicit_type(cls) -> '_1614.BasicDynamicLoadRatingCalculationMethod.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1614.BasicDynamicLoadRatingCalculationMethod.type_()

    @property
    def selected_value(self) -> '_1614.BasicDynamicLoadRatingCalculationMethod':
        '''BasicDynamicLoadRatingCalculationMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_1614.BasicDynamicLoadRatingCalculationMethod]':
        '''List[BasicDynamicLoadRatingCalculationMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_BasicStaticLoadRatingCalculationMethod(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_BasicStaticLoadRatingCalculationMethod

    A specific implementation of 'EnumWithSelectedValue' for 'BasicStaticLoadRatingCalculationMethod' types.
    '''

    __hash__ = None
    __qualname__ = 'BasicStaticLoadRatingCalculationMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1615.BasicStaticLoadRatingCalculationMethod':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _1615.BasicStaticLoadRatingCalculationMethod

    @classmethod
    def implicit_type(cls) -> '_1615.BasicStaticLoadRatingCalculationMethod.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1615.BasicStaticLoadRatingCalculationMethod.type_()

    @property
    def selected_value(self) -> '_1615.BasicStaticLoadRatingCalculationMethod':
        '''BasicStaticLoadRatingCalculationMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_1615.BasicStaticLoadRatingCalculationMethod]':
        '''List[BasicStaticLoadRatingCalculationMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_RotationalDirections(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_RotationalDirections

    A specific implementation of 'EnumWithSelectedValue' for 'RotationalDirections' types.
    '''

    __hash__ = None
    __qualname__ = 'RotationalDirections'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1639.RotationalDirections':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _1639.RotationalDirections

    @classmethod
    def implicit_type(cls) -> '_1639.RotationalDirections.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1639.RotationalDirections.type_()

    @property
    def selected_value(self) -> '_1639.RotationalDirections':
        '''RotationalDirections: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_1639.RotationalDirections]':
        '''List[RotationalDirections]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_BearingEfficiencyRatingMethod(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_BearingEfficiencyRatingMethod

    A specific implementation of 'EnumWithSelectedValue' for 'BearingEfficiencyRatingMethod' types.
    '''

    __hash__ = None
    __qualname__ = 'BearingEfficiencyRatingMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_260.BearingEfficiencyRatingMethod':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _260.BearingEfficiencyRatingMethod

    @classmethod
    def implicit_type(cls) -> '_260.BearingEfficiencyRatingMethod.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _260.BearingEfficiencyRatingMethod.type_()

    @property
    def selected_value(self) -> '_260.BearingEfficiencyRatingMethod':
        '''BearingEfficiencyRatingMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_260.BearingEfficiencyRatingMethod]':
        '''List[BearingEfficiencyRatingMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_ShaftDiameterModificationDueToRollingBearingRing(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_ShaftDiameterModificationDueToRollingBearingRing

    A specific implementation of 'EnumWithSelectedValue' for 'ShaftDiameterModificationDueToRollingBearingRing' types.
    '''

    __hash__ = None
    __qualname__ = 'ShaftDiameterModificationDueToRollingBearingRing'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_2201.ShaftDiameterModificationDueToRollingBearingRing':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _2201.ShaftDiameterModificationDueToRollingBearingRing

    @classmethod
    def implicit_type(cls) -> '_2201.ShaftDiameterModificationDueToRollingBearingRing.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _2201.ShaftDiameterModificationDueToRollingBearingRing.type_()

    @property
    def selected_value(self) -> '_2201.ShaftDiameterModificationDueToRollingBearingRing':
        '''ShaftDiameterModificationDueToRollingBearingRing: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_2201.ShaftDiameterModificationDueToRollingBearingRing]':
        '''List[ShaftDiameterModificationDueToRollingBearingRing]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_ExcitationAnalysisViewOption(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_ExcitationAnalysisViewOption

    A specific implementation of 'EnumWithSelectedValue' for 'ExcitationAnalysisViewOption' types.
    '''

    __hash__ = None
    __qualname__ = 'ExcitationAnalysisViewOption'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1989.ExcitationAnalysisViewOption':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _1989.ExcitationAnalysisViewOption

    @classmethod
    def implicit_type(cls) -> '_1989.ExcitationAnalysisViewOption.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1989.ExcitationAnalysisViewOption.type_()

    @property
    def selected_value(self) -> '_1989.ExcitationAnalysisViewOption':
        '''ExcitationAnalysisViewOption: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_1989.ExcitationAnalysisViewOption]':
        '''List[ExcitationAnalysisViewOption]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_ThreeDViewContourOptionFirstSelection(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_ThreeDViewContourOptionFirstSelection

    A specific implementation of 'EnumWithSelectedValue' for 'ThreeDViewContourOptionFirstSelection' types.
    '''

    __hash__ = None
    __qualname__ = 'ThreeDViewContourOptionFirstSelection'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1584.ThreeDViewContourOptionFirstSelection':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _1584.ThreeDViewContourOptionFirstSelection

    @classmethod
    def implicit_type(cls) -> '_1584.ThreeDViewContourOptionFirstSelection.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1584.ThreeDViewContourOptionFirstSelection.type_()

    @property
    def selected_value(self) -> '_1584.ThreeDViewContourOptionFirstSelection':
        '''ThreeDViewContourOptionFirstSelection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_1584.ThreeDViewContourOptionFirstSelection]':
        '''List[ThreeDViewContourOptionFirstSelection]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_ThreeDViewContourOptionSecondSelection(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_ThreeDViewContourOptionSecondSelection

    A specific implementation of 'EnumWithSelectedValue' for 'ThreeDViewContourOptionSecondSelection' types.
    '''

    __hash__ = None
    __qualname__ = 'ThreeDViewContourOptionSecondSelection'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1585.ThreeDViewContourOptionSecondSelection':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _1585.ThreeDViewContourOptionSecondSelection

    @classmethod
    def implicit_type(cls) -> '_1585.ThreeDViewContourOptionSecondSelection.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1585.ThreeDViewContourOptionSecondSelection.type_()

    @property
    def selected_value(self) -> '_1585.ThreeDViewContourOptionSecondSelection':
        '''ThreeDViewContourOptionSecondSelection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_1585.ThreeDViewContourOptionSecondSelection]':
        '''List[ThreeDViewContourOptionSecondSelection]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_ComponentOrientationOption(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_ComponentOrientationOption

    A specific implementation of 'EnumWithSelectedValue' for 'ComponentOrientationOption' types.
    '''

    __hash__ = None
    __qualname__ = 'ComponentOrientationOption'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_2093.ComponentOrientationOption':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _2093.ComponentOrientationOption

    @classmethod
    def implicit_type(cls) -> '_2093.ComponentOrientationOption.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _2093.ComponentOrientationOption.type_()

    @property
    def selected_value(self) -> '_2093.ComponentOrientationOption':
        '''ComponentOrientationOption: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_2093.ComponentOrientationOption]':
        '''List[ComponentOrientationOption]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_Axis(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_Axis

    A specific implementation of 'EnumWithSelectedValue' for 'Axis' types.
    '''

    __hash__ = None
    __qualname__ = 'Axis'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1285.Axis':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _1285.Axis

    @classmethod
    def implicit_type(cls) -> '_1285.Axis.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1285.Axis.type_()

    @property
    def selected_value(self) -> '_1285.Axis':
        '''Axis: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_1285.Axis]':
        '''List[Axis]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_AlignmentAxis(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_AlignmentAxis

    A specific implementation of 'EnumWithSelectedValue' for 'AlignmentAxis' types.
    '''

    __hash__ = None
    __qualname__ = 'AlignmentAxis'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1284.AlignmentAxis':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _1284.AlignmentAxis

    @classmethod
    def implicit_type(cls) -> '_1284.AlignmentAxis.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1284.AlignmentAxis.type_()

    @property
    def selected_value(self) -> '_1284.AlignmentAxis':
        '''AlignmentAxis: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_1284.AlignmentAxis]':
        '''List[AlignmentAxis]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_DesignEntityId(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_DesignEntityId

    A specific implementation of 'EnumWithSelectedValue' for 'DesignEntityId' types.
    '''

    __hash__ = None
    __qualname__ = 'DesignEntityId'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1937.DesignEntityId':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _1937.DesignEntityId

    @classmethod
    def implicit_type(cls) -> '_1937.DesignEntityId.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1937.DesignEntityId.type_()

    @property
    def selected_value(self) -> '_1937.DesignEntityId':
        '''DesignEntityId: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_1937.DesignEntityId]':
        '''List[DesignEntityId]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_FESubstructureType(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_FESubstructureType

    A specific implementation of 'EnumWithSelectedValue' for 'FESubstructureType' types.
    '''

    __hash__ = None
    __qualname__ = 'FESubstructureType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_2114.FESubstructureType':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _2114.FESubstructureType

    @classmethod
    def implicit_type(cls) -> '_2114.FESubstructureType.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _2114.FESubstructureType.type_()

    @property
    def selected_value(self) -> '_2114.FESubstructureType':
        '''FESubstructureType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_2114.FESubstructureType]':
        '''List[FESubstructureType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_ThermalExpansionOption(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_ThermalExpansionOption

    A specific implementation of 'EnumWithSelectedValue' for 'ThermalExpansionOption' types.
    '''

    __hash__ = None
    __qualname__ = 'ThermalExpansionOption'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_2137.ThermalExpansionOption':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _2137.ThermalExpansionOption

    @classmethod
    def implicit_type(cls) -> '_2137.ThermalExpansionOption.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _2137.ThermalExpansionOption.type_()

    @property
    def selected_value(self) -> '_2137.ThermalExpansionOption':
        '''ThermalExpansionOption: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_2137.ThermalExpansionOption]':
        '''List[ThermalExpansionOption]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_FEExportFormat(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_FEExportFormat

    A specific implementation of 'EnumWithSelectedValue' for 'FEExportFormat' types.
    '''

    __hash__ = None
    __qualname__ = 'FEExportFormat'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_152.FEExportFormat':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _152.FEExportFormat

    @classmethod
    def implicit_type(cls) -> '_152.FEExportFormat.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _152.FEExportFormat.type_()

    @property
    def selected_value(self) -> '_152.FEExportFormat':
        '''FEExportFormat: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_152.FEExportFormat]':
        '''List[FEExportFormat]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_ThreeDViewContourOption(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_ThreeDViewContourOption

    A specific implementation of 'EnumWithSelectedValue' for 'ThreeDViewContourOption' types.
    '''

    __hash__ = None
    __qualname__ = 'ThreeDViewContourOption'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1583.ThreeDViewContourOption':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _1583.ThreeDViewContourOption

    @classmethod
    def implicit_type(cls) -> '_1583.ThreeDViewContourOption.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1583.ThreeDViewContourOption.type_()

    @property
    def selected_value(self) -> '_1583.ThreeDViewContourOption':
        '''ThreeDViewContourOption: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_1583.ThreeDViewContourOption]':
        '''List[ThreeDViewContourOption]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_BoundaryConditionType(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_BoundaryConditionType

    A specific implementation of 'EnumWithSelectedValue' for 'BoundaryConditionType' types.
    '''

    __hash__ = None
    __qualname__ = 'BoundaryConditionType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_151.BoundaryConditionType':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _151.BoundaryConditionType

    @classmethod
    def implicit_type(cls) -> '_151.BoundaryConditionType.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _151.BoundaryConditionType.type_()

    @property
    def selected_value(self) -> '_151.BoundaryConditionType':
        '''BoundaryConditionType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_151.BoundaryConditionType]':
        '''List[BoundaryConditionType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_LinkNodeSource(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_LinkNodeSource

    A specific implementation of 'EnumWithSelectedValue' for 'LinkNodeSource' types.
    '''

    __hash__ = None
    __qualname__ = 'LinkNodeSource'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_2124.LinkNodeSource':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _2124.LinkNodeSource

    @classmethod
    def implicit_type(cls) -> '_2124.LinkNodeSource.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _2124.LinkNodeSource.type_()

    @property
    def selected_value(self) -> '_2124.LinkNodeSource':
        '''LinkNodeSource: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_2124.LinkNodeSource]':
        '''List[LinkNodeSource]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_BearingNodeOption(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_BearingNodeOption

    A specific implementation of 'EnumWithSelectedValue' for 'BearingNodeOption' types.
    '''

    __hash__ = None
    __qualname__ = 'BearingNodeOption'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_2090.BearingNodeOption':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _2090.BearingNodeOption

    @classmethod
    def implicit_type(cls) -> '_2090.BearingNodeOption.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _2090.BearingNodeOption.type_()

    @property
    def selected_value(self) -> '_2090.BearingNodeOption':
        '''BearingNodeOption: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_2090.BearingNodeOption]':
        '''List[BearingNodeOption]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_BearingToleranceClass(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_BearingToleranceClass

    A specific implementation of 'EnumWithSelectedValue' for 'BearingToleranceClass' types.
    '''

    __hash__ = None
    __qualname__ = 'BearingToleranceClass'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1644.BearingToleranceClass':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _1644.BearingToleranceClass

    @classmethod
    def implicit_type(cls) -> '_1644.BearingToleranceClass.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1644.BearingToleranceClass.type_()

    @property
    def selected_value(self) -> '_1644.BearingToleranceClass':
        '''BearingToleranceClass: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_1644.BearingToleranceClass]':
        '''List[BearingToleranceClass]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_BearingModel(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_BearingModel

    A specific implementation of 'EnumWithSelectedValue' for 'BearingModel' types.
    '''

    __hash__ = None
    __qualname__ = 'BearingModel'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1621.BearingModel':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _1621.BearingModel

    @classmethod
    def implicit_type(cls) -> '_1621.BearingModel.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1621.BearingModel.type_()

    @property
    def selected_value(self) -> '_1621.BearingModel':
        '''BearingModel: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_1621.BearingModel]':
        '''List[BearingModel]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_PreloadType(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_PreloadType

    A specific implementation of 'EnumWithSelectedValue' for 'PreloadType' types.
    '''

    __hash__ = None
    __qualname__ = 'PreloadType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1700.PreloadType':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _1700.PreloadType

    @classmethod
    def implicit_type(cls) -> '_1700.PreloadType.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1700.PreloadType.type_()

    @property
    def selected_value(self) -> '_1700.PreloadType':
        '''PreloadType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_1700.PreloadType]':
        '''List[PreloadType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_RaceRadialMountingType(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_RaceRadialMountingType

    A specific implementation of 'EnumWithSelectedValue' for 'RaceRadialMountingType' types.
    '''

    __hash__ = None
    __qualname__ = 'RaceRadialMountingType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1703.RaceRadialMountingType':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _1703.RaceRadialMountingType

    @classmethod
    def implicit_type(cls) -> '_1703.RaceRadialMountingType.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1703.RaceRadialMountingType.type_()

    @property
    def selected_value(self) -> '_1703.RaceRadialMountingType':
        '''RaceRadialMountingType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_1703.RaceRadialMountingType]':
        '''List[RaceRadialMountingType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_RaceAxialMountingType(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_RaceAxialMountingType

    A specific implementation of 'EnumWithSelectedValue' for 'RaceAxialMountingType' types.
    '''

    __hash__ = None
    __qualname__ = 'RaceAxialMountingType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1702.RaceAxialMountingType':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _1702.RaceAxialMountingType

    @classmethod
    def implicit_type(cls) -> '_1702.RaceAxialMountingType.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1702.RaceAxialMountingType.type_()

    @property
    def selected_value(self) -> '_1702.RaceAxialMountingType':
        '''RaceAxialMountingType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_1702.RaceAxialMountingType]':
        '''List[RaceAxialMountingType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_BearingToleranceDefinitionOptions(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_BearingToleranceDefinitionOptions

    A specific implementation of 'EnumWithSelectedValue' for 'BearingToleranceDefinitionOptions' types.
    '''

    __hash__ = None
    __qualname__ = 'BearingToleranceDefinitionOptions'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1645.BearingToleranceDefinitionOptions':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _1645.BearingToleranceDefinitionOptions

    @classmethod
    def implicit_type(cls) -> '_1645.BearingToleranceDefinitionOptions.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1645.BearingToleranceDefinitionOptions.type_()

    @property
    def selected_value(self) -> '_1645.BearingToleranceDefinitionOptions':
        '''BearingToleranceDefinitionOptions: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_1645.BearingToleranceDefinitionOptions]':
        '''List[BearingToleranceDefinitionOptions]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_InternalClearanceClass(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_InternalClearanceClass

    A specific implementation of 'EnumWithSelectedValue' for 'InternalClearanceClass' types.
    '''

    __hash__ = None
    __qualname__ = 'InternalClearanceClass'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1643.InternalClearanceClass':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _1643.InternalClearanceClass

    @classmethod
    def implicit_type(cls) -> '_1643.InternalClearanceClass.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1643.InternalClearanceClass.type_()

    @property
    def selected_value(self) -> '_1643.InternalClearanceClass':
        '''InternalClearanceClass: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_1643.InternalClearanceClass]':
        '''List[InternalClearanceClass]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_PowerLoadType(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_PowerLoadType

    A specific implementation of 'EnumWithSelectedValue' for 'PowerLoadType' types.
    '''

    __hash__ = None
    __qualname__ = 'PowerLoadType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1949.PowerLoadType':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _1949.PowerLoadType

    @classmethod
    def implicit_type(cls) -> '_1949.PowerLoadType.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1949.PowerLoadType.type_()

    @property
    def selected_value(self) -> '_1949.PowerLoadType':
        '''PowerLoadType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_1949.PowerLoadType]':
        '''List[PowerLoadType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_RigidConnectorTypes(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_RigidConnectorTypes

    A specific implementation of 'EnumWithSelectedValue' for 'RigidConnectorTypes' types.
    '''

    __hash__ = None
    __qualname__ = 'RigidConnectorTypes'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_2320.RigidConnectorTypes':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _2320.RigidConnectorTypes

    @classmethod
    def implicit_type(cls) -> '_2320.RigidConnectorTypes.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _2320.RigidConnectorTypes.type_()

    @property
    def selected_value(self) -> '_2320.RigidConnectorTypes':
        '''RigidConnectorTypes: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_2320.RigidConnectorTypes]':
        '''List[RigidConnectorTypes]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_RigidConnectorStiffnessType(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_RigidConnectorStiffnessType

    A specific implementation of 'EnumWithSelectedValue' for 'RigidConnectorStiffnessType' types.
    '''

    __hash__ = None
    __qualname__ = 'RigidConnectorStiffnessType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_2316.RigidConnectorStiffnessType':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _2316.RigidConnectorStiffnessType

    @classmethod
    def implicit_type(cls) -> '_2316.RigidConnectorStiffnessType.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _2316.RigidConnectorStiffnessType.type_()

    @property
    def selected_value(self) -> '_2316.RigidConnectorStiffnessType':
        '''RigidConnectorStiffnessType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_2316.RigidConnectorStiffnessType]':
        '''List[RigidConnectorStiffnessType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_FitTypes(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_FitTypes

    A specific implementation of 'EnumWithSelectedValue' for 'FitTypes' types.
    '''

    __hash__ = None
    __qualname__ = 'FitTypes'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1190.FitTypes':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _1190.FitTypes

    @classmethod
    def implicit_type(cls) -> '_1190.FitTypes.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1190.FitTypes.type_()

    @property
    def selected_value(self) -> '_1190.FitTypes':
        '''FitTypes: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_1190.FitTypes]':
        '''List[FitTypes]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_RigidConnectorToothSpacingType(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_RigidConnectorToothSpacingType

    A specific implementation of 'EnumWithSelectedValue' for 'RigidConnectorToothSpacingType' types.
    '''

    __hash__ = None
    __qualname__ = 'RigidConnectorToothSpacingType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_2319.RigidConnectorToothSpacingType':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _2319.RigidConnectorToothSpacingType

    @classmethod
    def implicit_type(cls) -> '_2319.RigidConnectorToothSpacingType.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _2319.RigidConnectorToothSpacingType.type_()

    @property
    def selected_value(self) -> '_2319.RigidConnectorToothSpacingType':
        '''RigidConnectorToothSpacingType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_2319.RigidConnectorToothSpacingType]':
        '''List[RigidConnectorToothSpacingType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_DoeValueSpecificationOption(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_DoeValueSpecificationOption

    A specific implementation of 'EnumWithSelectedValue' for 'DoeValueSpecificationOption' types.
    '''

    __hash__ = None
    __qualname__ = 'DoeValueSpecificationOption'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_4065.DoeValueSpecificationOption':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _4065.DoeValueSpecificationOption

    @classmethod
    def implicit_type(cls) -> '_4065.DoeValueSpecificationOption.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _4065.DoeValueSpecificationOption.type_()

    @property
    def selected_value(self) -> '_4065.DoeValueSpecificationOption':
        '''DoeValueSpecificationOption: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_4065.DoeValueSpecificationOption]':
        '''List[DoeValueSpecificationOption]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_AnalysisType(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_AnalysisType

    A specific implementation of 'EnumWithSelectedValue' for 'AnalysisType' types.
    '''

    __hash__ = None
    __qualname__ = 'AnalysisType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_6517.AnalysisType':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _6517.AnalysisType

    @classmethod
    def implicit_type(cls) -> '_6517.AnalysisType.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _6517.AnalysisType.type_()

    @property
    def selected_value(self) -> '_6517.AnalysisType':
        '''AnalysisType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_6517.AnalysisType]':
        '''List[AnalysisType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_BarModelExportType(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_BarModelExportType

    A specific implementation of 'EnumWithSelectedValue' for 'BarModelExportType' types.
    '''

    __hash__ = None
    __qualname__ = 'BarModelExportType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_50.BarModelExportType':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _50.BarModelExportType

    @classmethod
    def implicit_type(cls) -> '_50.BarModelExportType.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _50.BarModelExportType.type_()

    @property
    def selected_value(self) -> '_50.BarModelExportType':
        '''BarModelExportType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_50.BarModelExportType]':
        '''List[BarModelExportType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_DynamicsResponseType(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_DynamicsResponseType

    A specific implementation of 'EnumWithSelectedValue' for 'DynamicsResponseType' types.
    '''

    __hash__ = None
    __qualname__ = 'DynamicsResponseType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1300.DynamicsResponseType':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _1300.DynamicsResponseType

    @classmethod
    def implicit_type(cls) -> '_1300.DynamicsResponseType.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1300.DynamicsResponseType.type_()

    @property
    def selected_value(self) -> '_1300.DynamicsResponseType':
        '''DynamicsResponseType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_1300.DynamicsResponseType]':
        '''List[DynamicsResponseType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_ComplexPartDisplayOption(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_ComplexPartDisplayOption

    A specific implementation of 'EnumWithSelectedValue' for 'ComplexPartDisplayOption' types.
    '''

    __hash__ = None
    __qualname__ = 'ComplexPartDisplayOption'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1288.ComplexPartDisplayOption':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _1288.ComplexPartDisplayOption

    @classmethod
    def implicit_type(cls) -> '_1288.ComplexPartDisplayOption.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1288.ComplexPartDisplayOption.type_()

    @property
    def selected_value(self) -> '_1288.ComplexPartDisplayOption':
        '''ComplexPartDisplayOption: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_1288.ComplexPartDisplayOption]':
        '''List[ComplexPartDisplayOption]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_DynamicsResponseScaling(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_DynamicsResponseScaling

    A specific implementation of 'EnumWithSelectedValue' for 'DynamicsResponseScaling' types.
    '''

    __hash__ = None
    __qualname__ = 'DynamicsResponseScaling'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1299.DynamicsResponseScaling':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _1299.DynamicsResponseScaling

    @classmethod
    def implicit_type(cls) -> '_1299.DynamicsResponseScaling.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1299.DynamicsResponseScaling.type_()

    @property
    def selected_value(self) -> '_1299.DynamicsResponseScaling':
        '''DynamicsResponseScaling: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_1299.DynamicsResponseScaling]':
        '''List[DynamicsResponseScaling]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_BearingStiffnessModel(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_BearingStiffnessModel

    A specific implementation of 'EnumWithSelectedValue' for 'BearingStiffnessModel' types.
    '''

    __hash__ = None
    __qualname__ = 'BearingStiffnessModel'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_5097.BearingStiffnessModel':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _5097.BearingStiffnessModel

    @classmethod
    def implicit_type(cls) -> '_5097.BearingStiffnessModel.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _5097.BearingStiffnessModel.type_()

    @property
    def selected_value(self) -> '_5097.BearingStiffnessModel':
        '''BearingStiffnessModel: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_5097.BearingStiffnessModel]':
        '''List[BearingStiffnessModel]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_GearMeshStiffnessModel(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_GearMeshStiffnessModel

    A specific implementation of 'EnumWithSelectedValue' for 'GearMeshStiffnessModel' types.
    '''

    __hash__ = None
    __qualname__ = 'GearMeshStiffnessModel'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_5149.GearMeshStiffnessModel':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _5149.GearMeshStiffnessModel

    @classmethod
    def implicit_type(cls) -> '_5149.GearMeshStiffnessModel.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _5149.GearMeshStiffnessModel.type_()

    @property
    def selected_value(self) -> '_5149.GearMeshStiffnessModel':
        '''GearMeshStiffnessModel: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_5149.GearMeshStiffnessModel]':
        '''List[GearMeshStiffnessModel]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_ShaftAndHousingFlexibilityOption(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_ShaftAndHousingFlexibilityOption

    A specific implementation of 'EnumWithSelectedValue' for 'ShaftAndHousingFlexibilityOption' types.
    '''

    __hash__ = None
    __qualname__ = 'ShaftAndHousingFlexibilityOption'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_5194.ShaftAndHousingFlexibilityOption':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _5194.ShaftAndHousingFlexibilityOption

    @classmethod
    def implicit_type(cls) -> '_5194.ShaftAndHousingFlexibilityOption.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _5194.ShaftAndHousingFlexibilityOption.type_()

    @property
    def selected_value(self) -> '_5194.ShaftAndHousingFlexibilityOption':
        '''ShaftAndHousingFlexibilityOption: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_5194.ShaftAndHousingFlexibilityOption]':
        '''List[ShaftAndHousingFlexibilityOption]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_ExportOutputType(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_ExportOutputType

    A specific implementation of 'EnumWithSelectedValue' for 'ExportOutputType' types.
    '''

    __hash__ = None
    __qualname__ = 'ExportOutputType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_5712.ExportOutputType':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _5712.ExportOutputType

    @classmethod
    def implicit_type(cls) -> '_5712.ExportOutputType.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _5712.ExportOutputType.type_()

    @property
    def selected_value(self) -> '_5712.ExportOutputType':
        '''ExportOutputType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_5712.ExportOutputType]':
        '''List[ExportOutputType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_HarmonicAnalysisFEExportOptions_ComplexNumberOutput(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_HarmonicAnalysisFEExportOptions_ComplexNumberOutput

    A specific implementation of 'EnumWithSelectedValue' for 'HarmonicAnalysisFEExportOptions.ComplexNumberOutput' types.
    '''

    __hash__ = None
    __qualname__ = 'HarmonicAnalysisFEExportOptions.ComplexNumberOutput'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_5730.HarmonicAnalysisFEExportOptions.ComplexNumberOutput':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _5730.HarmonicAnalysisFEExportOptions.ComplexNumberOutput

    @classmethod
    def implicit_type(cls) -> '_5730.HarmonicAnalysisFEExportOptions.ComplexNumberOutput.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _5730.HarmonicAnalysisFEExportOptions.ComplexNumberOutput.type_()

    @property
    def selected_value(self) -> '_5730.HarmonicAnalysisFEExportOptions.ComplexNumberOutput':
        '''HarmonicAnalysisFEExportOptions.ComplexNumberOutput: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_5730.HarmonicAnalysisFEExportOptions.ComplexNumberOutput]':
        '''List[HarmonicAnalysisFEExportOptions.ComplexNumberOutput]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_StressConcentrationMethod(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_StressConcentrationMethod

    A specific implementation of 'EnumWithSelectedValue' for 'StressConcentrationMethod' types.
    '''

    __hash__ = None
    __qualname__ = 'StressConcentrationMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1844.StressConcentrationMethod':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _1844.StressConcentrationMethod

    @classmethod
    def implicit_type(cls) -> '_1844.StressConcentrationMethod.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1844.StressConcentrationMethod.type_()

    @property
    def selected_value(self) -> '_1844.StressConcentrationMethod':
        '''StressConcentrationMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_1844.StressConcentrationMethod]':
        '''List[StressConcentrationMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_FrictionModelForGyroscopicMoment(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_FrictionModelForGyroscopicMoment

    A specific implementation of 'EnumWithSelectedValue' for 'FrictionModelForGyroscopicMoment' types.
    '''

    __hash__ = None
    __qualname__ = 'FrictionModelForGyroscopicMoment'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1710.FrictionModelForGyroscopicMoment':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _1710.FrictionModelForGyroscopicMoment

    @classmethod
    def implicit_type(cls) -> '_1710.FrictionModelForGyroscopicMoment.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1710.FrictionModelForGyroscopicMoment.type_()

    @property
    def selected_value(self) -> '_1710.FrictionModelForGyroscopicMoment':
        '''FrictionModelForGyroscopicMoment: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_1710.FrictionModelForGyroscopicMoment]':
        '''List[FrictionModelForGyroscopicMoment]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_MeshStiffnessModel(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_MeshStiffnessModel

    A specific implementation of 'EnumWithSelectedValue' for 'MeshStiffnessModel' types.
    '''

    __hash__ = None
    __qualname__ = 'MeshStiffnessModel'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1944.MeshStiffnessModel':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _1944.MeshStiffnessModel

    @classmethod
    def implicit_type(cls) -> '_1944.MeshStiffnessModel.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1944.MeshStiffnessModel.type_()

    @property
    def selected_value(self) -> '_1944.MeshStiffnessModel':
        '''MeshStiffnessModel: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_1944.MeshStiffnessModel]':
        '''List[MeshStiffnessModel]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_HertzianContactDeflectionCalculationMethod(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_HertzianContactDeflectionCalculationMethod

    A specific implementation of 'EnumWithSelectedValue' for 'HertzianContactDeflectionCalculationMethod' types.
    '''

    __hash__ = None
    __qualname__ = 'HertzianContactDeflectionCalculationMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1365.HertzianContactDeflectionCalculationMethod':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _1365.HertzianContactDeflectionCalculationMethod

    @classmethod
    def implicit_type(cls) -> '_1365.HertzianContactDeflectionCalculationMethod.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1365.HertzianContactDeflectionCalculationMethod.type_()

    @property
    def selected_value(self) -> '_1365.HertzianContactDeflectionCalculationMethod':
        '''HertzianContactDeflectionCalculationMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_1365.HertzianContactDeflectionCalculationMethod]':
        '''List[HertzianContactDeflectionCalculationMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_TorqueRippleInputType(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_TorqueRippleInputType

    A specific implementation of 'EnumWithSelectedValue' for 'TorqueRippleInputType' types.
    '''

    __hash__ = None
    __qualname__ = 'TorqueRippleInputType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_6680.TorqueRippleInputType':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _6680.TorqueRippleInputType

    @classmethod
    def implicit_type(cls) -> '_6680.TorqueRippleInputType.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _6680.TorqueRippleInputType.type_()

    @property
    def selected_value(self) -> '_6680.TorqueRippleInputType':
        '''TorqueRippleInputType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_6680.TorqueRippleInputType]':
        '''List[TorqueRippleInputType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_HarmonicLoadDataType(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_HarmonicLoadDataType

    A specific implementation of 'EnumWithSelectedValue' for 'HarmonicLoadDataType' types.
    '''

    __hash__ = None
    __qualname__ = 'HarmonicLoadDataType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_6606.HarmonicLoadDataType':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _6606.HarmonicLoadDataType

    @classmethod
    def implicit_type(cls) -> '_6606.HarmonicLoadDataType.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _6606.HarmonicLoadDataType.type_()

    @property
    def selected_value(self) -> '_6606.HarmonicLoadDataType':
        '''HarmonicLoadDataType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_6606.HarmonicLoadDataType]':
        '''List[HarmonicLoadDataType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_HarmonicExcitationType(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_HarmonicExcitationType

    A specific implementation of 'EnumWithSelectedValue' for 'HarmonicExcitationType' types.
    '''

    __hash__ = None
    __qualname__ = 'HarmonicExcitationType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_6597.HarmonicExcitationType':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _6597.HarmonicExcitationType

    @classmethod
    def implicit_type(cls) -> '_6597.HarmonicExcitationType.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _6597.HarmonicExcitationType.type_()

    @property
    def selected_value(self) -> '_6597.HarmonicExcitationType':
        '''HarmonicExcitationType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_6597.HarmonicExcitationType]':
        '''List[HarmonicExcitationType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_PointLoadLoadCase_ForceSpecification(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_PointLoadLoadCase_ForceSpecification

    A specific implementation of 'EnumWithSelectedValue' for 'PointLoadLoadCase.ForceSpecification' types.
    '''

    __hash__ = None
    __qualname__ = 'PointLoadLoadCase.ForceSpecification'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_6641.PointLoadLoadCase.ForceSpecification':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _6641.PointLoadLoadCase.ForceSpecification

    @classmethod
    def implicit_type(cls) -> '_6641.PointLoadLoadCase.ForceSpecification.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _6641.PointLoadLoadCase.ForceSpecification.type_()

    @property
    def selected_value(self) -> '_6641.PointLoadLoadCase.ForceSpecification':
        '''PointLoadLoadCase.ForceSpecification: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_6641.PointLoadLoadCase.ForceSpecification]':
        '''List[PointLoadLoadCase.ForceSpecification]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_PowerLoadInputTorqueSpecificationMethod(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_PowerLoadInputTorqueSpecificationMethod

    A specific implementation of 'EnumWithSelectedValue' for 'PowerLoadInputTorqueSpecificationMethod' types.
    '''

    __hash__ = None
    __qualname__ = 'PowerLoadInputTorqueSpecificationMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1947.PowerLoadInputTorqueSpecificationMethod':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _1947.PowerLoadInputTorqueSpecificationMethod

    @classmethod
    def implicit_type(cls) -> '_1947.PowerLoadInputTorqueSpecificationMethod.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1947.PowerLoadInputTorqueSpecificationMethod.type_()

    @property
    def selected_value(self) -> '_1947.PowerLoadInputTorqueSpecificationMethod':
        '''PowerLoadInputTorqueSpecificationMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_1947.PowerLoadInputTorqueSpecificationMethod]':
        '''List[PowerLoadInputTorqueSpecificationMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_TorqueSpecificationForSystemDeflection(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_TorqueSpecificationForSystemDeflection

    A specific implementation of 'EnumWithSelectedValue' for 'TorqueSpecificationForSystemDeflection' types.
    '''

    __hash__ = None
    __qualname__ = 'TorqueSpecificationForSystemDeflection'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_6681.TorqueSpecificationForSystemDeflection':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _6681.TorqueSpecificationForSystemDeflection

    @classmethod
    def implicit_type(cls) -> '_6681.TorqueSpecificationForSystemDeflection.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _6681.TorqueSpecificationForSystemDeflection.type_()

    @property
    def selected_value(self) -> '_6681.TorqueSpecificationForSystemDeflection':
        '''TorqueSpecificationForSystemDeflection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_6681.TorqueSpecificationForSystemDeflection]':
        '''List[TorqueSpecificationForSystemDeflection]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_TorqueConverterLockupRule(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_TorqueConverterLockupRule

    A specific implementation of 'EnumWithSelectedValue' for 'TorqueConverterLockupRule' types.
    '''

    __hash__ = None
    __qualname__ = 'TorqueConverterLockupRule'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_5219.TorqueConverterLockupRule':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _5219.TorqueConverterLockupRule

    @classmethod
    def implicit_type(cls) -> '_5219.TorqueConverterLockupRule.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _5219.TorqueConverterLockupRule.type_()

    @property
    def selected_value(self) -> '_5219.TorqueConverterLockupRule':
        '''TorqueConverterLockupRule: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_5219.TorqueConverterLockupRule]':
        '''List[TorqueConverterLockupRule]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_DegreesOfFreedom(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_DegreesOfFreedom

    A specific implementation of 'EnumWithSelectedValue' for 'DegreesOfFreedom' types.
    '''

    __hash__ = None
    __qualname__ = 'DegreesOfFreedom'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1297.DegreesOfFreedom':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _1297.DegreesOfFreedom

    @classmethod
    def implicit_type(cls) -> '_1297.DegreesOfFreedom.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _1297.DegreesOfFreedom.type_()

    @property
    def selected_value(self) -> '_1297.DegreesOfFreedom':
        '''DegreesOfFreedom: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_1297.DegreesOfFreedom]':
        '''List[DegreesOfFreedom]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None


class EnumWithSelectedValue_DestinationDesignState(mixins.EnumWithSelectedValueMixin, Enum):
    '''EnumWithSelectedValue_DestinationDesignState

    A specific implementation of 'EnumWithSelectedValue' for 'DestinationDesignState' types.
    '''

    __hash__ = None
    __qualname__ = 'DestinationDesignState'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        '''Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_6695.DestinationDesignState':
        '''Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        '''

        return _6695.DestinationDesignState

    @classmethod
    def implicit_type(cls) -> '_6695.DestinationDesignState.type_()':
        '''Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        '''

        return _6695.DestinationDesignState.type_()

    @property
    def selected_value(self) -> '_6695.DestinationDesignState':
        '''DestinationDesignState: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None

    @property
    def available_values(self) -> 'List[_6695.DestinationDesignState]':
        '''List[DestinationDesignState]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return None
