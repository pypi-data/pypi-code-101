# This file was generated!
import enum

import construct

from mercury_engine_data_structures import common_types
from mercury_engine_data_structures.object import Object
from mercury_engine_data_structures.pointer_set import PointerSet

Pointer_CAcidBlobsLaunchPattern = PointerSet("CAcidBlobsLaunchPattern")
Pointer_CActor = PointerSet("CActor")
Pointer_CActorComponent = PointerSet("CActorComponent")
Pointer_CAttackPreset = PointerSet("CAttackPreset")
Pointer_CBarelyFrozenIceInfo = PointerSet("CBarelyFrozenIceInfo")
Pointer_CBouncingCreaturesLaunchPattern = PointerSet("CBouncingCreaturesLaunchPattern")
Pointer_CCentralUnitWeightedEdges = PointerSet("CCentralUnitWeightedEdges")
Pointer_CChozoRobotSoldierCannonShotPattern = PointerSet("CChozoRobotSoldierCannonShotPattern")
Pointer_CCooldownXBossFireWallDef = PointerSet("CCooldownXBossFireWallDef")
Pointer_CCooldownXBossLavaCarpetDef = PointerSet("CCooldownXBossLavaCarpetDef")
Pointer_CCooldownXBossLavaDropsDef = PointerSet("CCooldownXBossLavaDropsDef")
Pointer_CEmmyAutoForbiddenEdgesDef = PointerSet("CEmmyAutoForbiddenEdgesDef")
Pointer_CEmmyAutoGlobalSmartLinkDef = PointerSet("CEmmyAutoGlobalSmartLinkDef")
Pointer_CEmmyOverrideDeathPositionDef = PointerSet("CEmmyOverrideDeathPositionDef")
Pointer_CEnvironmentData_SAmbient = PointerSet("CEnvironmentData::SAmbient")
Pointer_CEnvironmentData_SBloom = PointerSet("CEnvironmentData::SBloom")
Pointer_CEnvironmentData_SCubeMap = PointerSet("CEnvironmentData::SCubeMap")
Pointer_CEnvironmentData_SDepthTint = PointerSet("CEnvironmentData::SDepthTint")
Pointer_CEnvironmentData_SFog = PointerSet("CEnvironmentData::SFog")
Pointer_CEnvironmentData_SHemisphericalLight = PointerSet("CEnvironmentData::SHemisphericalLight")
Pointer_CEnvironmentData_SIBLAttenuation = PointerSet("CEnvironmentData::SIBLAttenuation")
Pointer_CEnvironmentData_SMaterialTint = PointerSet("CEnvironmentData::SMaterialTint")
Pointer_CEnvironmentData_SPlayerLight = PointerSet("CEnvironmentData::SPlayerLight")
Pointer_CEnvironmentData_SSSAO = PointerSet("CEnvironmentData::SSSAO")
Pointer_CEnvironmentData_SToneMapping = PointerSet("CEnvironmentData::SToneMapping")
Pointer_CEnvironmentData_SVerticalFog = PointerSet("CEnvironmentData::SVerticalFog")
Pointer_CEnvironmentManager = PointerSet("CEnvironmentManager")
Pointer_CEnvironmentMusicPresets = PointerSet("CEnvironmentMusicPresets")
Pointer_CEnvironmentSoundPresets = PointerSet("CEnvironmentSoundPresets")
Pointer_CEnvironmentVisualPresets = PointerSet("CEnvironmentVisualPresets")
Pointer_CKraidSpinningNailsDef = PointerSet("CKraidSpinningNailsDef")
Pointer_CLightManager = PointerSet("CLightManager")
Pointer_CLogicCamera = PointerSet("CLogicCamera")
Pointer_CPattern = PointerSet("CPattern")
Pointer_CPolypFallPattern = PointerSet("CPolypFallPattern")
Pointer_CScenario = PointerSet("CScenario")
Pointer_CShootDCBones = PointerSet("CShootDCBones")
Pointer_CShotLaunchConfig = PointerSet("CShotLaunchConfig")
Pointer_CShotManager = PointerSet("CShotManager")
Pointer_CSubAreaManager = PointerSet("CSubAreaManager")
Pointer_CSubareaCharclassGroup = PointerSet("CSubareaCharclassGroup")
Pointer_CSubareaInfo = PointerSet("CSubareaInfo")
Pointer_CSubareaSetup = PointerSet("CSubareaSetup")
Pointer_CTentacle = PointerSet("CTentacle")
Pointer_CTriggerComponent_SActivationCondition = PointerSet("CTriggerComponent::SActivationCondition")
Pointer_CTriggerLogicAction = PointerSet("CTriggerLogicAction")
Pointer_CXParasiteBehavior = PointerSet("CXParasiteBehavior")
Pointer_base_global_CFilePathStrId = PointerSet("base::global::CFilePathStrId")
Pointer_base_global_CRntSmallDictionary_base_global_CStrId__CActorComponentPtr_ = PointerSet("base::global::CRntSmallDictionary<base::global::CStrId, CActorComponent*>")
Pointer_base_global_CRntVector_CEnvironmentData_SAmbientTransition_ = PointerSet("base::global::CRntVector<CEnvironmentData::SAmbientTransition>")
Pointer_base_global_CRntVector_CEnvironmentData_SBloomTransition_ = PointerSet("base::global::CRntVector<CEnvironmentData::SBloomTransition>")
Pointer_base_global_CRntVector_CEnvironmentData_SCubeMapTransition_ = PointerSet("base::global::CRntVector<CEnvironmentData::SCubeMapTransition>")
Pointer_base_global_CRntVector_CEnvironmentData_SDepthTintTransition_ = PointerSet("base::global::CRntVector<CEnvironmentData::SDepthTintTransition>")
Pointer_base_global_CRntVector_CEnvironmentData_SFogTransition_ = PointerSet("base::global::CRntVector<CEnvironmentData::SFogTransition>")
Pointer_base_global_CRntVector_CEnvironmentData_SHemisphericalLightTransition_ = PointerSet("base::global::CRntVector<CEnvironmentData::SHemisphericalLightTransition>")
Pointer_base_global_CRntVector_CEnvironmentData_SIBLAttenuationTransition_ = PointerSet("base::global::CRntVector<CEnvironmentData::SIBLAttenuationTransition>")
Pointer_base_global_CRntVector_CEnvironmentData_SMaterialTintTransition_ = PointerSet("base::global::CRntVector<CEnvironmentData::SMaterialTintTransition>")
Pointer_base_global_CRntVector_CEnvironmentData_SPlayerLightTransition_ = PointerSet("base::global::CRntVector<CEnvironmentData::SPlayerLightTransition>")
Pointer_base_global_CRntVector_CEnvironmentData_SSSAOTransition_ = PointerSet("base::global::CRntVector<CEnvironmentData::SSSAOTransition>")
Pointer_base_global_CRntVector_CEnvironmentData_SToneMappingTransition_ = PointerSet("base::global::CRntVector<CEnvironmentData::SToneMappingTransition>")
Pointer_base_global_CRntVector_CEnvironmentData_SVerticalFogTransition_ = PointerSet("base::global::CRntVector<CEnvironmentData::SVerticalFogTransition>")
Pointer_base_global_CRntVector_std_unique_ptr_CSubareaCharclassGroup__ = PointerSet("base::global::CRntVector<std::unique_ptr<CSubareaCharclassGroup>>")
Pointer_base_global_CRntVector_std_unique_ptr_CSubareaSetup__ = PointerSet("base::global::CRntVector<std::unique_ptr<CSubareaSetup>>")
Pointer_base_reflection_CTypedValue = PointerSet("base::reflection::CTypedValue")
Pointer_game_logic_collision_CCollider = PointerSet("game::logic::collision::CCollider")
Pointer_game_logic_collision_CShape = PointerSet("game::logic::collision::CShape")
Pointer_querysystem_CEvaluator = PointerSet("querysystem::CEvaluator")
Pointer_querysystem_CFilter = PointerSet("querysystem::CFilter")
Pointer_sound_CAudioPresets = PointerSet("sound::CAudioPresets")
Pointer_sound_CMusicManager = PointerSet("sound::CMusicManager")
Pointer_sound_CSoundManager = PointerSet("sound::CSoundManager")


base_core_CBaseObject = Object(base_core_CBaseObjectFields := {})

base_core_CAsset = Object(base_core_CAssetFields := base_core_CBaseObjectFields)

base_core_CDefinition = Object(base_core_CDefinitionFields := {
    **base_core_CAssetFields,
    "sLabel": common_types.StrId,
})

CActorDef = Object(CActorDefFields := base_core_CDefinitionFields)

CCharClass = Object(CActorDefFields)

CActorComponentDef = Object(CActorComponentDefFields := {
    **base_core_CBaseObjectFields,
    "bStartEnabled": construct.Flag,
    "bDisabledInEditor": construct.Flag,
    "bPrePhysicsUpdateInEditor": construct.Flag,
    "bPostPhysicsUpdateInEditor": construct.Flag,
})

CCharClassComponent = Object(CCharClassComponentFields := CActorComponentDefFields)

CCharClassWaterNozzleComponent = Object({
    **CCharClassComponentFields,
    "fNozzleHeightOffset": common_types.Float,
})

CCharClassBreakableScenarioComponent = Object({
    **CCharClassComponentFields,
    "vColliderIds": common_types.make_vector(common_types.StrId),
})

CCharClassHecathonPlanktonFXComponent = Object({
    **CCharClassComponentFields,
    "sModelResPath": common_types.StrId,
    "fScale": common_types.Float,
    "fScaleRandom": common_types.Float,
    "vRotation": common_types.CVector3D,
    "vRotationRandom": common_types.CVector3D,
})

CCharClassEventScenarioComponent = Object(CCharClassComponentFields)

CCentralUnitComponentDef = Object(CCentralUnitComponentDefFields := CActorComponentDefFields)

CCharClassTunnelTrapMorphballComponent = Object({
    **CCharClassComponentFields,
    "bEnableFinalCollisionOnClose": construct.Flag,
})

CCharClassWeightActivablePropComponent = Object({
    **CCharClassComponentFields,
    "bDeleteOnOpenAnimationFinished": construct.Flag,
})

CCharClassScorpiusFXComponent = Object(CCharClassComponentFields)

CCharClassGrapplePointComponent = Object(CCharClassGrapplePointComponentFields := {
    **CCharClassComponentFields,
    "bAutoEnableGlow": construct.Flag,
    "sGrappleDragWide": common_types.StrId,
})

CCharClassWeightActivatedPlatformSmartObjectComponent = Object({
    **CCharClassComponentFields,
    "sActionLayer": common_types.StrId,
})


class game_logic_collision_EColMat(enum.IntEnum):
    DEFAULT = 0
    SCENARIO_GENERIC = 1
    FLESH_GENERIC = 2
    DAMAGE_BLOCKED = 3
    METAL = 4
    ENERGY = 5
    DIRT = 6
    ROCK = 7
    ICE = 8
    UNDER_WATER = 9
    UNDER_WATER_SP = 10
    MID_WATER = 11
    MID_WATER_SP = 12
    PUDDLE = 13
    OIL = 14
    END_WORLD = 15
    Invalid = 4294967295


construct_game_logic_collision_EColMat = construct.Enum(construct.Int32ul, game_logic_collision_EColMat)

CCharClassCollisionComponent = Object({
    **CCharClassComponentFields,
    "v3SpawnPointCollisionSizeInc": common_types.CVector3D,
    "eDefaultCollisionMaterial": construct_game_logic_collision_EColMat,
    "bShouldIgnoreSlopeSupport": construct.Flag,
    "bForceSlopeDirectionOnFloorHit": construct.Flag,
    "mExplicitCollisionMaterials": common_types.make_dict(construct_game_logic_collision_EColMat),
})


class EDamageType(enum.IntEnum):
    UNKNOWN = 0
    ELECTRIC = 1
    FIRE = 2
    BLOOD = 3
    STEAM = 4
    NO_DAMAGE = 5
    Invalid = 2147483647


construct_EDamageType = construct.Enum(construct.Int32ul, EDamageType)


class EDamageStrength(enum.IntEnum):
    DEFAULT = 0
    MEDIUM = 1
    MEDIUM_HORIZONTAL = 2
    HARD_WITHOUT_SHAKE = 3
    HARD = 4
    SUPER_HARD = 5
    Invalid = 2147483647


construct_EDamageStrength = construct.Enum(construct.Int32ul, EDamageStrength)

CCharClassAttackComponent = Object(CCharClassAttackComponentFields := {
    **CCharClassComponentFields,
    "sDefaultDamageID": common_types.StrId,
    "sDamageSource": common_types.StrId,
    "bRotateToInstigatorHitCollider": construct.Flag,
    "eDamageType": construct_EDamageType,
    "sSuccessDownDefaultAnim": common_types.StrId,
    "sSuccessUpDefaultAnim": common_types.StrId,
    "sSuccessFrontDefaultAnim": common_types.StrId,
    "sSuccessBackDefaultAnim": common_types.StrId,
    "bIgnoreReaction": construct.Flag,
    "bForceReaction": construct.Flag,
    "eDamageStrengthOnForcedReaction": construct_EDamageStrength,
    "bIgnoreInmune": construct.Flag,
    "dictDamageIDOverrides": common_types.make_dict(common_types.StrId),
    "sIgnoreBumpColliders": common_types.StrId,
})

CCharClassScriptComponent = Object(CCharClassComponentFields)

CCharClassLogicLookAtPlayerComponent = Object({
    **CCharClassComponentFields,
    "sIdNodeName": common_types.StrId,
})

CGameBBPropID = Object({})

CCharClassPersistenceComponent = Object({
    **CCharClassComponentFields,
    "sBoolProperty": CGameBBPropID,
    "sIntProperty": CGameBBPropID,
    "sFloatProperty": CGameBBPropID,
    "sSection": common_types.StrId,
})

CCharClassChozombieFXComponent = Object({
    **CCharClassComponentFields,
    "sModelResPath": common_types.StrId,
    "fScale": common_types.Float,
    "vRotation": common_types.CVector3D,
    "fInstanceLifeTime": common_types.Float,
})

CCharClassPositionalSoundComponent = Object({
    **CCharClassComponentFields,
    "bOverrideDisableInEditor": construct.Flag,
})

CCharClassAudioComponent = Object({
    **CCharClassComponentFields,
    "bDimSounds": construct.Flag,
    "bMuteOutsideCamera": construct.Flag,
})

CCharClassUsableComponent = Object(CCharClassUsableComponentFields := {
    **CCharClassComponentFields,
    "fGrabInterpTime": common_types.Float,
    "fUseTime": common_types.Float,
    "sUseQuestionID": common_types.StrId,
    "sCanNotUseID": common_types.StrId,
    "sUseSuccessMessage": common_types.StrId,
    "sUsePrepareLeftAction": common_types.StrId,
    "sUsePrepareRightAction": common_types.StrId,
    "sUseInitAction": common_types.StrId,
    "sUseAction": common_types.StrId,
    "sUseLevelChangeAction": common_types.StrId,
    "sUseEndAction": common_types.StrId,
    "sUseIdleAction": common_types.StrId,
    "sUsablePrepareToUseAction": common_types.StrId,
    "sUsableInitAction": common_types.StrId,
    "sUsableAction": common_types.StrId,
    "sUsableLevelChangeAction": common_types.StrId,
    "sUsableEndAction": common_types.StrId,
    "sUsableIdleAction": common_types.StrId,
    "sUseDiscoverRightAction": common_types.StrId,
    "sUseDiscoverLeftAction": common_types.StrId,
    "sUsableDiscoverAction": common_types.StrId,
    "sUsableUndiscoverAction": common_types.StrId,
    "sUsePrepareLeftAfterDiscoverAction": common_types.StrId,
    "sUsePrepareRightAfterDiscoverAction": common_types.StrId,
    "sUseReadyToSaveBackgroundAction": common_types.StrId,
    "fDiscoverInterpTime": common_types.Float,
    "fStationUseInterpTime": common_types.Float,
    "fStationNotUsedInterpTime": common_types.Float,
    "sStartLevelMusicID": common_types.StrId,
    "sSaveSoundID": common_types.StrId,
    "fPostponeFadeInTime": common_types.Float,
    "fFadeInTime": common_types.Float,
})

CCharClassPickableComponent = Object({
    **CCharClassComponentFields,
    "sOnPickFX": common_types.StrId,
    "sOnPickCaption": common_types.StrId,
    "sOnPickEnergyFragment1Caption": common_types.StrId,
    "sOnPickEnergyFragment2Caption": common_types.StrId,
    "sOnPickEnergyFragment3Caption": common_types.StrId,
    "sOnPickEnergyFragmentCompleteCaption": common_types.StrId,
    "sOnPickTankUnknownCaption": common_types.StrId,
})

CCharClassAIComponent = Object(CCharClassAIComponentFields := CCharClassComponentFields)

CCharClassShipRechargeComponent = Object({
    **CCharClassUsableComponentFields,
    "sSaveUseQuestionID": common_types.StrId,
    "sSaveUseSuccessMessage": common_types.StrId,
})

CCharClassFusibleBoxComponent = Object(CCharClassComponentFields)

CMagmaCentralUnitComponentDef = Object(CCentralUnitComponentDefFields)

CCharClassAIAttackComponent = Object(CCharClassAIAttackComponentFields := {
    **CCharClassAttackComponentFields,
    "bAllowFloorSlideTunnel": construct.Flag,
})

CCharClassModelUpdaterComponent = Object(CCharClassModelUpdaterComponentFields := {
    **CCharClassComponentFields,
    "vInitPosWorldOffset": common_types.CVector3D,
    "vInitAngWorldOffset": common_types.CVector3D,
    "bOverrideDisableInEditor": construct.Flag,
    "vInitScale": common_types.CVector3D,
})

CCharClassTrainUsableComponent = Object({
    **CCharClassUsableComponentFields,
    "sUsableLeftAction": common_types.StrId,
    "sUsableRightAction": common_types.StrId,
    "sUsableLevelChangeLeftAction": common_types.StrId,
    "sUsableLevelChangeRightAction": common_types.StrId,
    "sUseInitRightAction": common_types.StrId,
    "sUseInitLeftAction": common_types.StrId,
    "sUseLeftAction": common_types.StrId,
    "sUseRightAction": common_types.StrId,
    "sUseLeftLevelChangeAction": common_types.StrId,
    "sUseRightLevelChangeAction": common_types.StrId,
    "sUseLeftEndAction": common_types.StrId,
    "sUseRightEndAction": common_types.StrId,
})

CCharClassAimCameraEnabledVisibleOnlyComponent = Object(CCharClassComponentFields)


class EFollowPathRotationMode(enum.IntEnum):
    NONE = 0
    VerticalRotationToMovement = 1
    InvertVerticalRotationToMovement = 2
    PositiveVerticalRotationToMovement = 3
    NegativeVerticalRotationToMovement = 4
    HorizontalRotationToMovement = 5
    Invalid = 2147483647


construct_EFollowPathRotationMode = construct.Enum(construct.Int32ul, EFollowPathRotationMode)

CCharClassAINavigationComponent = Object({
    **CCharClassComponentFields,
    "eFollowPathRotationMode": construct_EFollowPathRotationMode,
    "fFollowPathVerticalRotationDist": common_types.Float,
    "fFollowPathVerticalRotationFactor": common_types.Float,
    "fFollowPathTargetReachedDistance": common_types.Float,
    "fFollowPathLookAhead": common_types.Float,
    "bFollowPathUpdateDirWhenNotLookingAtDesiredViewDir": construct.Flag,
    "fGotoPointReachedDistance": common_types.Float,
    "fTurnWeightPenalization": common_types.Float,
})

CCharClassAreaSoundEffectsComponent = Object(CCharClassComponentFields)

CCharClassGooplotCapsuleComponent = Object(CCharClassComponentFields)

CCharClassBlockableWarningRadius = Object(CCharClassComponentFields)

CCharClassBillboardComponent = Object({
    **CCharClassComponentFields,
    "fGroupRadius": common_types.Float,
    "fBillboardRadius": common_types.Float,
    "sPath": common_types.StrId,
    "sBgPath": common_types.StrId,
    "iTextureWidth": common_types.Int,
    "iTextureHeight": common_types.Int,
    "vInitialColor": common_types.CVector3D,
    "fUniformColorOffset": common_types.Float,
    "vColorOffset": common_types.CVector3D,
    "fInitialAlpha": common_types.Float,
    "fAlphaOffset": common_types.Float,
    "sBillboardDefaultLoop": common_types.StrId,
    "sBillboardMotionDefaultLoop": common_types.StrId,
    "sGroupMotionDefaultLoop": common_types.StrId,
    "bUseRotation": construct.Flag,
    "fBillboardMotionDefaultScale": common_types.Float,
    "fGroupMotionDefaultScale": common_types.Float,
    "sSoundLoopLot": common_types.StrId,
    "sSoundLoopLit": common_types.StrId,
    "fSoundLoopLotAmountPct": common_types.Float,
    "fSoundLoopAttMinDist": common_types.Float,
    "fSoundLoopAttMaxDist": common_types.Float,
    "sSoundImpactBase": common_types.StrId,
    "iSoundImpactCount": common_types.Int,
    "fSoundImpactRadiusMinAtt": common_types.Float,
    "fSoundImpactRadiusMaxAtt": common_types.Float,
    "iPoolSize": common_types.UInt,
})


class ENavMeshItemType(enum.IntEnum):
    Static = 0
    Dynamic = 1
    Destructible = 2
    Invalid = 2147483647


construct_ENavMeshItemType = construct.Enum(construct.Int32ul, ENavMeshItemType)

CCharClassNavMeshItemComponent = Object(CCharClassNavMeshItemComponentFields := {
    **CCharClassComponentFields,
    "sInitialStage": common_types.StrId,
    "eType": construct_ENavMeshItemType,
    "bConnectSubareas": construct.Flag,
})

CCharClassRumbleComponent = Object(CCharClassComponentFields)

CCharClassCentralUnitCannonAIComponent = Object(CCharClassAIComponentFields)

int = Object(intFields := {})

base_global_timeline_TLayers = Object(intFields)

CCharClassGrabComponent = Object({
    **CCharClassComponentFields,
    "sFireCameraFXPreset": common_types.StrId,
    "oAnimationLayers": base_global_timeline_TLayers,
})

CCharClassSceneModelAnimationComponent = Object(CCharClassComponentFields)

CCharClassAreaMusicComponent = Object(CCharClassComponentFields)

CCharClassAISmartObjectComponent = Object({
    **CCharClassComponentFields,
    "fUseOffset": common_types.Float,
})

CCharClassStartPointComponent = Object(CCharClassStartPointComponentFields := {
    **CCharClassComponentFields,
    "bProjectOnFloor": construct.Flag,
})


class CAnimationPrefix_SPrefix_Enum(enum.IntEnum):
    NONE = 0
    water = 1
    speedbooster = 2
    speedbooster45up = 3
    left = 4
    right = 5
    patrol = 6
    search = 7
    chase = 8
    chase2 = 9
    chasereachable = 10
    combat = 11
    flee = 12
    brokenshield = 13
    grab2 = 14
    grabwater = 15
    protoemmytuto = 16
    preseta = 17
    presetb = 18
    presetc = 19
    Count = 20


construct_CAnimationPrefix_SPrefix_Enum = construct.Enum(construct.Int32ul, CAnimationPrefix_SPrefix_Enum)

CCharClassAnimationComponent = Object({
    **CCharClassComponentFields,
    "bOverrideDisableInEditor": construct.Flag,
    "sInitialAction": common_types.StrId,
    "sDefaultLoop": common_types.StrId,
    "sAnimTree": common_types.StrId,
    "sInitialPrefix": construct_CAnimationPrefix_SPrefix_Enum,
    "iDebugLine": common_types.Int,
    "fInitialFrame": common_types.Float,
})

CCharClassFactionComponent = Object(CCharClassComponentFields)


class engine_utils_EMaterialConstantColor(enum.IntEnum):
    MATERIAL_CONSTANT_COLOR_0 = 0
    MATERIAL_CONSTANT_COLOR_1 = 1
    MATERIAL_CONSTANT_COLOR_2 = 2
    MATERIAL_CONSTANT_COLOR_3 = 3
    MATERIAL_CONSTANT_COLOR_4 = 4
    MATERIAL_CONSTANT_COLOR_5 = 5
    MATERIAL_CONSTANT_COLOR_6 = 6
    MATERIAL_CONSTANT_COLOR_7 = 7
    MATERIAL_CONSTANT_COLOR_8 = 8
    MATERIAL_CONSTANT_COLOR_9 = 9
    EMATERIALCONSTANTCOLOR_COUNT = 10
    Invalid = 2147483647


construct_engine_utils_EMaterialConstantColor = construct.Enum(construct.Int32ul, engine_utils_EMaterialConstantColor)


class msapi_api_shdr_EShaderType(enum.IntEnum):
    E_VERTEX = 0
    E_PIXEL = 1
    E_GEOMETRY = 2
    Invalid = 2147483647


construct_msapi_api_shdr_EShaderType = construct.Enum(construct.Int32ul, msapi_api_shdr_EShaderType)

CCharClassBoneToConstantComponent = Object({
    **CCharClassComponentFields,
    "sNode": common_types.StrId,
    "sMaterialName": common_types.StrId,
    "ePropertyName": construct_engine_utils_EMaterialConstantColor,
    "eStage": construct_msapi_api_shdr_EShaderType,
})

CCharClassAbilityComponent = Object(CCharClassComponentFields)

CCharClassDredhedAttackComponent = Object(CCharClassAIAttackComponentFields)

CCharClassEmmyAttackComponent = Object(CCharClassAIAttackComponentFields)

CCharClassActivatableComponent = Object(CCharClassActivatableComponentFields := CCharClassComponentFields)

CCharClassRinkaAIComponent = Object(CCharClassAIComponentFields)

CCharClassFrozenComponent = Object(CCharClassFrozenComponentFields := {
    **CCharClassComponentFields,
    "fTotalFreezeTime": common_types.Float,
    "fThawingTime": common_types.Float,
    "sTimelineIdOnFrozen": common_types.StrId,
    "sTimelineIdOnThawing": common_types.StrId,
    "sTimelineIdOnUnfreeze": common_types.StrId,
    "sActionFreezeInit": common_types.StrId,
    "sActionFreezeEnd": common_types.StrId,
    "sActionFreezeEndFalling": common_types.StrId,
    "sCustomLayer": common_types.StrId,
    "sCustomLayerMixerNode": common_types.StrId,
})

CCharClassLightingComponent = Object({
    **CCharClassComponentFields,
    "sLightsDefPath": common_types.StrId,
    "bOverrideDisableInEditor": construct.Flag,
})


class CEscapeSequenceExplosionComponent_EExplosionType(enum.IntEnum):
    SMALL = 0
    MEDIUM = 1
    BIG = 2
    Invalid = 2147483647


construct_CEscapeSequenceExplosionComponent_EExplosionType = construct.Enum(construct.Int32ul, CEscapeSequenceExplosionComponent_EExplosionType)

CCharClassEscapeSequenceExplosionComponent = Object({
    **CCharClassComponentFields,
    "eExplosionType": construct_CEscapeSequenceExplosionComponent_EExplosionType,
})

CCharClassMagnetSlidingBlockComponent = Object(CCharClassMagnetSlidingBlockComponentFields := {
    **CCharClassComponentFields,
    "bFreezeOnFinish": construct.Flag,
    "bActiveRailCameraOnFinish": construct.Flag,
    "fMinMovementPercentToForceContinueMovingOnStopHang": common_types.Float,
})

CCharClassEventPropComponent = Object(CCharClassComponentFields)

CCharClassRinkaUnitComponent = Object(CCharClassComponentFields)

CCharClassLifeComponent = Object(CCharClassLifeComponentFields := {
    **CCharClassComponentFields,
    "sLife": common_types.StrId,
    "sImpactAnim": common_types.StrId,
    "sImpactBackAnim": common_types.StrId,
    "sDeadAnim": common_types.StrId,
    "sDeadBackAnim": common_types.StrId,
    "sDeadAirAnim": common_types.StrId,
    "sDeadAirBackAnim": common_types.StrId,
    "sDeadMeleeAnim": common_types.StrId,
    "sDeadNoInstigatorAnim": common_types.StrId,
    "bDisableCollidersOnDead": construct.Flag,
})

CCaveCentralUnitComponentDef = Object(CCentralUnitComponentDefFields)

CGameObject = Object(CGameObjectFields := base_core_CBaseObjectFields)

game_logic_collision_CBroadphaseObject = Object(game_logic_collision_CBroadphaseObjectFields := {
    **CGameObjectFields,
    "sId": common_types.UInt,
    "sStrId": common_types.StrId,
})

game_logic_collision_CShape = Object(game_logic_collision_CShapeFields := {
    "vPos": common_types.CVector3D,
    "bIsSolid": construct.Flag,
})

game_logic_collision_CCollider = Object({
    **game_logic_collision_CBroadphaseObjectFields,
    "pShape": Pointer_game_logic_collision_CShape.create_construct(),
})

CActorComponent = Object(CActorComponentFields := CGameObjectFields)

base_global_CRntSmallDictionary_base_global_CStrId__CActorComponentPtr_ = common_types.make_dict(Pointer_CActorComponent.create_construct())

CActor = Object(CActorFields := {
    **CGameObjectFields,
    "sName": common_types.StrId,
    "oActorDefLink": common_types.StrId,
    "sActorDefName": common_types.StrId,
    "vPos": common_types.CVector3D,
    "vAng": common_types.CVector3D,
    "pComponents": Pointer_base_global_CRntSmallDictionary_base_global_CStrId__CActorComponentPtr_.create_construct(),
    "bEnabled": construct.Flag,
})

CActorSublayer = Object({
    "sName": common_types.StrId,
    "dctActors": common_types.make_dict(Pointer_CActor.create_construct()),
})

CActorLayer = Object({
    "dctSublayers": common_types.make_dict(CActorSublayer),
    "dctActorGroups": common_types.make_dict(common_types.make_vector(common_types.StrId)),
})

CScenario = Object({
    **CGameObjectFields,
    "awpScenarioColliders": common_types.make_vector(Pointer_game_logic_collision_CCollider.create_construct()),
    "sLevelID": common_types.StrId,
    "sScenarioID": common_types.StrId,
    "rEntitiesLayer": CActorLayer,
    "rSoundsLayer": CActorLayer,
    "rLightsLayer": CActorLayer,
    "vLayerFiles": common_types.make_vector(common_types.StrId),
})

CSubareaInfo = Object({
    "sId": common_types.StrId,
    "sSetupId": common_types.StrId,
    "sPackSetId": common_types.StrId,
    "bDisableSubArea": construct.Flag,
    "fCameraZDistance": common_types.Float,
    "bIgnoreMetroidCameraOffsets": construct.Flag,
    "sCharclassGroupId": common_types.StrId,
    "asItemsIds": common_types.make_vector(common_types.StrId),
    "vsCameraCollisionsIds": common_types.make_vector(common_types.StrId),
    "vsCutscenesIds": common_types.make_vector(common_types.StrId),
})

CSubareaSetup = Object({
    "sId": common_types.StrId,
    "vSubareaConfigs": common_types.make_vector(Pointer_CSubareaInfo.create_construct()),
})

base_global_CRntVector_std_unique_ptr_CSubareaSetup__ = common_types.make_vector(Pointer_CSubareaSetup.create_construct())

CSubareaCharclassGroup = Object({
    "sId": common_types.StrId,
    "vsCharClassesIds": common_types.make_vector(common_types.StrId),
})

base_global_CRntVector_std_unique_ptr_CSubareaCharclassGroup__ = common_types.make_vector(Pointer_CSubareaCharclassGroup.create_construct())

CSubAreaManager = Object({
    "vSubareaSetups": Pointer_base_global_CRntVector_std_unique_ptr_CSubareaSetup__.create_construct(),
    "vCharclassGroups": Pointer_base_global_CRntVector_std_unique_ptr_CSubareaCharclassGroup__.create_construct(),
})

CEnvironmentData_SFog = Object({
    "tColor": common_types.CVector4D,
    "fColorInterp": common_types.Float,
    "fScale": common_types.Float,
    "fScaleInterp": common_types.Float,
    "tRange": common_types.CVector2D,
    "fRangeInterp": common_types.Float,
    "fWaveFreq": common_types.Float,
    "fWaveAmp": common_types.Float,
    "fWaveVelocity": common_types.Float,
    "fWaveInterp": common_types.Float,
})

CEnvironmentData_SVerticalFog = Object({
    "bEnabled": construct.Flag,
    "tColor": common_types.CVector4D,
    "fColorInterp": common_types.Float,
    "fBase": common_types.Float,
    "fBaseInterp": common_types.Float,
    "tAttenuation": common_types.CVector2D,
    "fAttInterp": common_types.Float,
    "fNear": common_types.Float,
    "fNearInterp": common_types.Float,
    "fFar": common_types.Float,
    "fFarInterp": common_types.Float,
    "fWaveFreq": common_types.Float,
    "fWaveAmp": common_types.Float,
    "fWaveVelocity": common_types.Float,
    "fWaveInterp": common_types.Float,
})

STransition = Object(STransitionFields := {})

CEnvironmentData_SFogTransition = Object({
    **STransitionFields,
    "sPreset": common_types.StrId,
    "fColorInterp": common_types.Float,
    "fScaleInterp": common_types.Float,
    "fRangeInterp": common_types.Float,
    "fWaveInterp": common_types.Float,
})

base_global_CRntVector_CEnvironmentData_SFogTransition_ = common_types.make_vector(CEnvironmentData_SFogTransition)

CEnvironmentData_SAmbient = Object({
    "tColor": common_types.CVector4D,
    "fColorInterp": common_types.Float,
})

CEnvironmentData_SAmbientTransition = Object({
    **STransitionFields,
    "sPreset": common_types.StrId,
    "fColorInterp": common_types.Float,
})

base_global_CRntVector_CEnvironmentData_SAmbientTransition_ = common_types.make_vector(CEnvironmentData_SAmbientTransition)

CEnvironmentData_SDepthTint = Object({
    "fTintInterp": common_types.Float,
    "fLight": common_types.Float,
    "fCube": common_types.Float,
    "fDepth": common_types.Float,
    "fSaturation": common_types.Float,
    "fLightNear": common_types.Float,
    "fCubeNear": common_types.Float,
    "fDepthNear": common_types.Float,
    "fSaturationNear": common_types.Float,
})

CEnvironmentData_SDepthTintTransition = Object({
    **STransitionFields,
    "sPreset": common_types.StrId,
    "fTintInterp": common_types.Float,
})

base_global_CRntVector_CEnvironmentData_SDepthTintTransition_ = common_types.make_vector(CEnvironmentData_SDepthTintTransition)

CEnvironmentData_SMaterialTint = Object({
    "tColor": common_types.CVector4D,
    "fColorInterp": common_types.Float,
    "fBlend": common_types.Float,
    "fBlendInterp": common_types.Float,
})

CEnvironmentData_SMaterialTintTransition = Object({
    **STransitionFields,
    "sPreset": common_types.StrId,
    "fColorInterp": common_types.Float,
    "fBlendInterp": common_types.Float,
})

base_global_CRntVector_CEnvironmentData_SMaterialTintTransition_ = common_types.make_vector(CEnvironmentData_SMaterialTintTransition)

CEnvironmentData_SPlayerLight = Object({
    "tDiffuse": common_types.CVector4D,
    "tSpecular0": common_types.CVector4D,
    "tSpecular1": common_types.CVector4D,
    "fColorInterp": common_types.Float,
    "tAttenuation": common_types.CVector2D,
    "fAttenuationInterp": common_types.Float,
})

CEnvironmentData_SPlayerLightTransition = Object({
    **STransitionFields,
    "sPreset": common_types.StrId,
    "fColorInterp": common_types.Float,
    "fAttenuationInterp": common_types.Float,
})

base_global_CRntVector_CEnvironmentData_SPlayerLightTransition_ = common_types.make_vector(CEnvironmentData_SPlayerLightTransition)

CEnvironmentData_SHemisphericalLight = Object({
    "tColorUp": common_types.CVector3D,
    "fColorUpInterp": common_types.Float,
    "tColorDown": common_types.CVector3D,
    "fColorDownInterp": common_types.Float,
})

CEnvironmentData_SHemisphericalLightTransition = Object({
    **STransitionFields,
    "sPreset": common_types.StrId,
    "fColorUpInterp": common_types.Float,
    "fColorDownInterp": common_types.Float,
})

base_global_CRntVector_CEnvironmentData_SHemisphericalLightTransition_ = common_types.make_vector(CEnvironmentData_SHemisphericalLightTransition)

CEnvironmentData_SBloom = Object({
    "tBloom": common_types.CVector3D,
    "fBloomInterp": common_types.Float,
})

CEnvironmentData_SBloomTransition = Object({
    **STransitionFields,
    "sPreset": common_types.StrId,
    "fBloomInterp": common_types.Float,
})

base_global_CRntVector_CEnvironmentData_SBloomTransition_ = common_types.make_vector(CEnvironmentData_SBloomTransition)

CEnvironmentData_SVerticalFogTransition = Object({
    **STransitionFields,
    "sPreset": common_types.StrId,
    "fColorInterp": common_types.Float,
    "fBaseInterp": common_types.Float,
    "fNearInterp": common_types.Float,
    "fFarInterp": common_types.Float,
    "fAttInterp": common_types.Float,
    "fWaveInterp": common_types.Float,
})

base_global_CRntVector_CEnvironmentData_SVerticalFogTransition_ = common_types.make_vector(CEnvironmentData_SVerticalFogTransition)

CEnvironmentData_SCubeMap = Object({
    "fInterp": common_types.Float,
    "bEnabled": construct.Flag,
    "sTexturePath": common_types.StrId,
})

CEnvironmentData_SCubeMapTransition = Object({
    **STransitionFields,
    "sPreset": common_types.StrId,
    "fCubeMapInterp": common_types.Float,
})

base_global_CRntVector_CEnvironmentData_SCubeMapTransition_ = common_types.make_vector(CEnvironmentData_SCubeMapTransition)

CEnvironmentData_SSSAO = Object({
    "fFallOff": common_types.Float,
    "fIntensity": common_types.Float,
    "fBias": common_types.Float,
    "fRadius": common_types.Float,
    "fDepthFct": common_types.Float,
    "bEnabled": construct.Flag,
    "fInterp": common_types.Float,
    "fIntensityFactor": common_types.Float,
    "fFogFactor": common_types.Float,
})

CEnvironmentData_SSSAOTransition = Object({
    **STransitionFields,
    "sPreset": common_types.StrId,
    "fInterp": common_types.Float,
})

base_global_CRntVector_CEnvironmentData_SSSAOTransition_ = common_types.make_vector(CEnvironmentData_SSSAOTransition)

CEnvironmentData_SToneMapping = Object({
    "fInterp": common_types.Float,
    "fExposure": common_types.Float,
    "fGamma": common_types.Float,
    "fSaturationColor": common_types.Float,
    "fContrast": common_types.Float,
    "fBrightness": common_types.Float,
    "vColorTint": common_types.CVector4D,
    "fColorVibrance": common_types.Float,
    "bEnabled": construct.Flag,
})

CEnvironmentData_SToneMappingTransition = Object({
    **STransitionFields,
    "sPreset": common_types.StrId,
    "fInterp": common_types.Float,
})

base_global_CRntVector_CEnvironmentData_SToneMappingTransition_ = common_types.make_vector(CEnvironmentData_SToneMappingTransition)

CEnvironmentData_SIBLAttenuation = Object({
    "fInterp": common_types.Float,
    "fCubeAttFactor": common_types.Float,
    "fZDistance": common_types.Float,
    "fGradientSize": common_types.Float,
})

CEnvironmentData_SIBLAttenuationTransition = Object({
    **STransitionFields,
    "sPreset": common_types.StrId,
    "fInterp": common_types.Float,
})

base_global_CRntVector_CEnvironmentData_SIBLAttenuationTransition_ = common_types.make_vector(CEnvironmentData_SIBLAttenuationTransition)

CEnvironmentData = Object({
    "sID": common_types.StrId,
    "tFog": Pointer_CEnvironmentData_SFog.create_construct(),
    "tVerticalFog": Pointer_CEnvironmentData_SVerticalFog.create_construct(),
    "tFogTransitions": Pointer_base_global_CRntVector_CEnvironmentData_SFogTransition_.create_construct(),
    "tAmbient": Pointer_CEnvironmentData_SAmbient.create_construct(),
    "tAmbientTransitions": Pointer_base_global_CRntVector_CEnvironmentData_SAmbientTransition_.create_construct(),
    "tDepthTint": Pointer_CEnvironmentData_SDepthTint.create_construct(),
    "tDepthTintTransitions": Pointer_base_global_CRntVector_CEnvironmentData_SDepthTintTransition_.create_construct(),
    "tMaterialTint": Pointer_CEnvironmentData_SMaterialTint.create_construct(),
    "tMaterialTintTransitions": Pointer_base_global_CRntVector_CEnvironmentData_SMaterialTintTransition_.create_construct(),
    "tPlayerLight": Pointer_CEnvironmentData_SPlayerLight.create_construct(),
    "tPlayerLightTransitions": Pointer_base_global_CRntVector_CEnvironmentData_SPlayerLightTransition_.create_construct(),
    "tHemisphericalLight": Pointer_CEnvironmentData_SHemisphericalLight.create_construct(),
    "tHemisphericalLightTransitions": Pointer_base_global_CRntVector_CEnvironmentData_SHemisphericalLightTransition_.create_construct(),
    "tBloom": Pointer_CEnvironmentData_SBloom.create_construct(),
    "tBloomTransitions": Pointer_base_global_CRntVector_CEnvironmentData_SBloomTransition_.create_construct(),
    "tVerticalFogTransitions": Pointer_base_global_CRntVector_CEnvironmentData_SVerticalFogTransition_.create_construct(),
    "tCubeMap": Pointer_CEnvironmentData_SCubeMap.create_construct(),
    "tCubeMapTransitions": Pointer_base_global_CRntVector_CEnvironmentData_SCubeMapTransition_.create_construct(),
    "tSSAO": Pointer_CEnvironmentData_SSSAO.create_construct(),
    "tSSAOTransitions": Pointer_base_global_CRntVector_CEnvironmentData_SSSAOTransition_.create_construct(),
    "tToneMapping": Pointer_CEnvironmentData_SToneMapping.create_construct(),
    "tToneMappingTransitions": Pointer_base_global_CRntVector_CEnvironmentData_SToneMappingTransition_.create_construct(),
    "tIBLAttenuation": Pointer_CEnvironmentData_SIBLAttenuation.create_construct(),
    "tIBLAttenuationTransitions": Pointer_base_global_CRntVector_CEnvironmentData_SIBLAttenuationTransition_.create_construct(),
})

CEnvironmentVisualPresets = Object({
    "dicPresets": common_types.make_dict(CEnvironmentData),
})


class base_snd_EReverbIntensity(enum.IntEnum):
    NONE = 0
    SMALL_ROOM = 1
    MEDIUM_ROOM = 2
    BIG_ROOM = 3
    CATHEDRAL = 4
    Invalid = 2147483647


construct_base_snd_EReverbIntensity = construct.Enum(construct.Int32ul, base_snd_EReverbIntensity)

CEnvironmentSoundData_SSound = Object({
    "sToPreset": common_types.StrId,
    "fVolume": common_types.Float,
    "fFadeIn": common_types.Float,
    "fFadeOut": common_types.Float,
    "fFadeInDelay": common_types.Float,
    "eReverb": construct_base_snd_EReverbIntensity,
})

CEnvironmentSoundData = Object({
    "sID": common_types.StrId,
    "sSoundID": common_types.StrId,
    "tSound": CEnvironmentSoundData_SSound,
    "dctTransitions": common_types.make_dict(CEnvironmentSoundData_SSound),
})

CEnvironmentSoundPresets = Object({
    "dicPresets": common_types.make_dict(CEnvironmentSoundData),
})

sound_TMusicFile = Object({
    "sWav": common_types.StrId,
    "iLoops": common_types.Int,
    "iLoopStart": common_types.Int,
    "iLoopEnd": common_types.Int,
})


class EMusicFadeType(enum.IntEnum):
    NONE = 0
    DEFAULT = 1
    CROSS_FADE = 2
    Invalid = 2147483647


construct_EMusicFadeType = construct.Enum(construct.Int32ul, EMusicFadeType)

sound_TMusicTrack = Object({
    "iTrack": common_types.Int,
    "vFiles": common_types.make_vector(sound_TMusicFile),
    "fFadeIn": common_types.Float,
    "fFadeOut": common_types.Float,
    "fDelay": common_types.Float,
    "fVol": common_types.Float,
    "iStartPos": common_types.Int,
    "eCrossFade": construct_EMusicFadeType,
    "bPauseOnPop": construct.Flag,
    "fEnvFactor": common_types.Float,
})

sound_TScenarioMusicPreset = Object({
    "sAlias": common_types.StrId,
    "vTracks": common_types.make_vector(sound_TMusicTrack),
})


class SMusicPlayFlag(enum.IntEnum):
    NONE = 0
    FORCE = 1
    CLEAR_STACKS = 2
    CLEAR_TRACKS = 3
    POP_CURRENT = 4
    PAUSE_CURRENT = 5
    IGNORE_PAUSE = 6
    SKIP_TO_LOOP = 7
    PAUSE_ON_POP = 8
    Invalid = 2147483647


construct_SMusicPlayFlag = construct.Enum(construct.Int32ul, SMusicPlayFlag)

CEnvironmentMusicData_SMusicTransition = Object({
    "sPreset": common_types.StrId,
    "fFadeIn": common_types.Float,
    "fFadeOut": common_types.Float,
    "eFadeType": construct_EMusicFadeType,
    "ePlayFlag": construct_SMusicPlayFlag,
})

CEnvironmentMusicData = Object({
    "sID": common_types.StrId,
    "tPreset": sound_TScenarioMusicPreset,
    "ePlayFlag": construct_SMusicPlayFlag,
    "tMusicTransitions": common_types.make_vector(CEnvironmentMusicData_SMusicTransition),
})


class EMusicManagerInGameState(enum.IntEnum):
    NONE = 0
    RELAX = 1
    PATROL = 2
    SEARCH = 3
    PATROL2 = 4
    SEARCH2 = 5
    DEATH = 6
    COMBAT = 7
    Invalid = 2147483647


construct_EMusicManagerInGameState = construct.Enum(construct.Int32ul, EMusicManagerInGameState)

sound_SStateFadeOut = Object({
    "eState": construct_EMusicManagerInGameState,
    "fFadeOut": common_types.Float,
})

sound_TBossMusicTrack = Object({
    "oTrack": sound_TMusicTrack,
    "vFadeOuts": common_types.make_vector(sound_SStateFadeOut),
})

sound_TBossMusicSubStateConfig = Object({
    "eState": common_types.StrId,
    "vTracks": common_types.make_vector(sound_TBossMusicTrack),
})

sound_TBossMusicSpawnGroupConfig = Object({
    "sSpawnGroup": common_types.StrId,
    "dicSubStatePresets": common_types.make_dict(sound_TBossMusicSubStateConfig),
})

sound_TBossMusicPreset = Object({
    "sBoss": common_types.StrId,
    "dicSpawnGroupConfigs": common_types.make_dict(sound_TBossMusicSpawnGroupConfig),
})

CEnvironmentMusicPresets = Object({
    "dicPresets": common_types.make_dict(CEnvironmentMusicData),
    "dicBossPresets": common_types.make_dict(sound_TBossMusicPreset),
})

CEnvironmentManager = Object({
    "pVisualPresets": Pointer_CEnvironmentVisualPresets.create_construct(),
    "pSoundPresets": Pointer_CEnvironmentSoundPresets.create_construct(),
    "pMusicPresets": Pointer_CEnvironmentMusicPresets.create_construct(),
})

sound_CAudioMaterial = Object({
    "vFiles": common_types.make_vector(common_types.StrId),
})


class base_snd_ESndPlayerId(enum.IntEnum):
    SFX = 0
    MUSIC = 1
    SPEECH = 2
    GRUNT = 3
    GUI = 4
    ENVIRONMENT_STREAMS = 5
    SFX_EMMY = 6
    CUTSCENE = 7
    Invalid = 2147483647


construct_base_snd_ESndPlayerId = construct.Enum(construct.Int32ul, base_snd_ESndPlayerId)


class base_snd_ESndLogicId(enum.IntEnum):
    DEFAULT = 0
    SHIELD_IMPACT = 1
    FLESH_IMPACT = 2
    WALL_IMPACT = 3
    DOOR_FAIL = 4
    BOSS_DISCOVER = 5
    PHASEDISPLACEMENT = 6
    ENERSHIELDENTER = 7
    ENERSHIELDEXIT = 8
    SAMUS_MOVEMENT = 9
    EMMY_ALARM = 10
    Invalid = 2147483647


construct_base_snd_ESndLogicId = construct.Enum(construct.Int32ul, base_snd_ESndLogicId)


class base_snd_EAttenuationCurve(enum.IntEnum):
    Logarithmic = 0
    Linear = 1
    Invalid = 2147483647


construct_base_snd_EAttenuationCurve = construct.Enum(construct.Int32ul, base_snd_EAttenuationCurve)


class base_snd_EPositionalType(enum.IntEnum):
    POS_2D = 0
    POS_3D = 1
    Invalid = 2147483647


construct_base_snd_EPositionalType = construct.Enum(construct.Int32ul, base_snd_EPositionalType)

sound_CAudioPreset = Object({
    **base_core_CAssetFields,
    "sUniqueId": common_types.StrId,
    "sNodeToAttach": common_types.StrId,
    "arrMatFiles": common_types.make_vector(sound_CAudioMaterial),
    "ePlayerId": construct_base_snd_ESndPlayerId,
    "eLogicId": construct_base_snd_ESndLogicId,
    "eAttCurve": construct_base_snd_EAttenuationCurve,
    "ePositional": construct_base_snd_EPositionalType,
    "iInstanceLimit": common_types.Int,
    "fInBetweenTime": common_types.Float,
    "fAttMaxRange": common_types.Float,
    "fAttMinRange": common_types.Float,
    "fVolume": common_types.Float,
    "fVolumeRange": common_types.Float,
    "fPitch": common_types.Float,
    "fPitchRange": common_types.Float,
    "fPan": common_types.Float,
    "fPanRange": common_types.Float,
    "fFadeIn": common_types.Float,
    "fFadeOut": common_types.Float,
    "fEmptyPercentage": common_types.Float,
    "fStartDelayed": common_types.Float,
    "bLoop": construct.Flag,
    "bAttachToActor": construct.Flag,
    "bStpChgAnim": construct.Flag,
    "bStpEntDead": construct.Flag,
    "bManaged": construct.Flag,
    "bRumbleSync": construct.Flag,
    "fRumbleGainOverride": common_types.Float,
    "fDimRelativeVolume": common_types.Float,
    "fDimTime": common_types.Float,
    "fDimFadeTime": common_types.Float,
    "fDimRecoverTime": common_types.Float,
})

sound_CAudioPresets = Object({
    "dicPresets": common_types.make_dict(sound_CAudioPreset),
})

sound_CSoundManager = Object({
    "pAudioPresets": Pointer_sound_CAudioPresets.create_construct(),
})

CShotAudioWeaponStates = Object({
    "arrWeaponStateAssets": common_types.make_vector(common_types.StrId),
})

CShotAudioWeaponPresets = Object({
    "arrAudioPresetsSources": common_types.make_vector(CShotAudioWeaponStates),
})

CShotManager = Object({
    "oWeaponAudioPresets": CShotAudioWeaponPresets,
})


class ELightType(enum.IntEnum):
    Directional = 0
    Omni = 1
    Spot = 2
    Seg = 3
    Invalid = 4294967295


construct_ELightType = construct.Enum(construct.Int32ul, ELightType)


class ELightAttachment(enum.IntEnum):
    PosRot3D = 0
    Pos3D = 1
    Rot3D = 2
    PosRot2D = 3
    Pos2D = 4
    Rot2D = 5
    Invalid = 4294967295


construct_ELightAttachment = construct.Enum(construct.Int32ul, ELightAttachment)

CLightInfo = Object({
    **intFields,
    "eType": construct_ELightType,
    "eAttachment": construct_ELightAttachment,
    "sName": common_types.StrId,
    "sNode": common_types.StrId,
    "vPosOffset": common_types.CVector3D,
    "vRotOffset": common_types.CVector3D,
    "vColor": common_types.CVector4D,
    "vAtt": common_types.CVector4D,
    "fAttConstantFactor": common_types.Float,
    "fAttQuadraticFactor": common_types.Float,
    "fIntensity": common_types.Float,
    "bCastShadows": construct.Flag,
    "bUseSpecular": construct.Flag,
    "bEnabled": construct.Flag,
})

CLightsDef = Object({
    **base_core_CAssetFields,
    "sPath": common_types.StrId,
    "vLights": common_types.make_vector(CLightInfo),
})

CLightManager = Object({
    "dicLightDefs": common_types.make_dict(CLightsDef),
})

sound_CMusicManager = Object({
    "dicGlobalMusicPresets": common_types.make_dict(CEnvironmentMusicData),
    "dicGlobalBossMusicPresets": common_types.make_dict(sound_TBossMusicPreset),
})

gameeditor_CGameModelRoot = Object({
    "pScenario": Pointer_CScenario.create_construct(),
    "pSubareaManager": Pointer_CSubAreaManager.create_construct(),
    "pEnvironmentManager": Pointer_CEnvironmentManager.create_construct(),
    "pSoundManager": Pointer_sound_CSoundManager.create_construct(),
    "pShotManager": Pointer_CShotManager.create_construct(),
    "pLightManager": Pointer_CLightManager.create_construct(),
    "pMusicManager": Pointer_sound_CMusicManager.create_construct(),
})

CCharClassAreaFXComponent = Object({
    **CCharClassComponentFields,
    "sModelResPath": common_types.StrId,
    "fScale": common_types.Float,
    "fScaleRandom": common_types.Float,
    "vRotation": common_types.CVector3D,
    "vRotationRandom": common_types.CVector3D,
    "fFXAttackLenght": common_types.Float,
    "bUseInstances": construct.Flag,
})

CCharClassSensorDoorComponent = Object({
    **CCharClassComponentFields,
    "fDelayCloseTime": common_types.Float,
    "fDelayOpenTime": common_types.Float,
})

CCharClassMapAcquisitionComponent = Object({
    **CCharClassUsableComponentFields,
    "sUsePrepareLeftMRNoUsedAction": common_types.StrId,
    "sUsePrepareRightMRNoUsedAction": common_types.StrId,
    "sUseInitMRUsedAction": common_types.StrId,
    "sUseMRUsedAction": common_types.StrId,
    "sUseAfterDownLoadMapAction": common_types.StrId,
    "sUseEndUseAfterDownLoadMapAction": common_types.StrId,
    "sUsableInitMRUsedAction": common_types.StrId,
    "sSaveRingsOpenAction": common_types.StrId,
    "sSaveRingsCloseAction": common_types.StrId,
    "sSaveRingLoopAction": common_types.StrId,
})

CCharClassActionSwitcherComponent = Object({
    **CCharClassActivatableComponentFields,
    "sActivateAction": common_types.StrId,
    "sDeactivateAction": common_types.StrId,
    "bScalePlayRate": construct.Flag,
    "bDisableOnActivatedOnDeattachActor": construct.Flag,
})

CCharClassEnhanceWeakSpotComponent = Object(CCharClassEnhanceWeakSpotComponentFields := {
    **CCharClassComponentFields,
    "sOnWeakSpotAimed": common_types.StrId,
    "sOnWeakSpotNotAimed": common_types.StrId,
})

CProtoCentralUnitComponentDef = Object(CCentralUnitComponentDefFields)

CCharClassMenuAnimationChangeComponent = Object(CCharClassComponentFields)

CCharClassLogicPathNavMeshItemComponent = Object(CCharClassNavMeshItemComponentFields)


class SDropProbabilities_SDir(enum.IntEnum):
    NONE = 0
    Front = 1
    Back = 2
    Up = 3
    Down = 4
    FrontUp = 5
    FrontDown = 6
    BackUp = 7
    BackDown = 8
    Player = 9
    Invalid = 2147483647


construct_SDropProbabilities_SDir = construct.Enum(construct.Int32ul, SDropProbabilities_SDir)


class SDropProbabilities_SType(enum.IntEnum):
    NONE = 0
    Default = 1
    Melee = 2
    Invalid = 2147483647


construct_SDropProbabilities_SType = construct.Enum(construct.Int32ul, SDropProbabilities_SType)

SDropProbabilities = Object({
    "iMinNumOfDroppedItems": common_types.Int,
    "iMaxNumOfDroppedItems": common_types.Int,
    "iMaxItemTypeMin": common_types.Int,
    "iMaxItemTypeMax": common_types.Int,
    "fNothingProbability": common_types.Float,
    "fLifeProbability": common_types.Float,
    "fLifeBigProbability": common_types.Float,
    "fMissileProbability": common_types.Float,
    "fMissileBigProbability": common_types.Float,
    "fPowerBombProbability": common_types.Float,
    "fPowerBombBigProbability": common_types.Float,
    "fXParasiteYellowTypeProbability": common_types.Float,
    "fXParasiteGreenTypeProbability": common_types.Float,
    "fXParasiteRedTypeProbability": common_types.Float,
    "fXParasiteOrangeTypeProbability": common_types.Float,
    "fXParasiteMiniNothingProbability": common_types.Float,
    "fXParasiteMiniYellowTypeProbability": common_types.Float,
    "fXParasiteMiniGreenTypeProbability": common_types.Float,
    "fMinDistance": common_types.Float,
    "fMaxDistance": common_types.Float,
    "fMaxZDisp": common_types.Float,
    "sNodeToDrop": common_types.StrId,
    "vNodeOffset": common_types.CVector3D,
    "vRawOffset": common_types.CVector3D,
    "eDirToDrop": construct_SDropProbabilities_SDir,
    "eType": construct_SDropProbabilities_SType,
    "bStrictDir": construct.Flag,
    "bForceAttract": construct.Flag,
    "bAutomaticGrab": construct.Flag,
    "iXCellsToDrop": common_types.Int,
    "iNumOfItemsToDropWithXCells": common_types.Int,
})

CCharClassDropComponent = Object({
    **CCharClassComponentFields,
    "bDropOnDeath": construct.Flag,
    "bDropItemOnDeath": construct.Flag,
    "bDropItemOnDeathByMelee": construct.Flag,
    "bRestrictFloorSectors": construct.Flag,
    "vDropOffset": common_types.CVector3D,
    "bCanDropXParasite": construct.Flag,
    "fXCellDropInitialSpeed": common_types.Float,
    "fXCellDropEndSpeed": common_types.Float,
    "fXCellDropTime": common_types.Float,
    "fXCellDropRotationAngSpeed": common_types.Float,
    "sXParasiteTypeMask": common_types.StrId,
    "oDropProbabilities": SDropProbabilities,
    "oMeleeChargeShotDropProbabilities": SDropProbabilities,
    "bSkipUsefulItemsRule": construct.Flag,
})

CCharClassPlayerLifeComponent = Object({
    **CCharClassLifeComponentFields,
    "fImpactInvulnerableTime": common_types.Float,
    "fMinImpactInvulnerableTime": common_types.Float,
})

CCharClassPerceptionComponent = Object(CCharClassComponentFields)

CCharClassFXComponent = Object(CCharClassComponentFields)

CCharClassMovementComponent = Object(CCharClassMovementComponentFields := {
    **CCharClassComponentFields,
    "fPhysicsVelocityFriction": common_types.Float,
    "fGravityScalar": common_types.Float,
    "bWantsCheckViewDirInComputeKinematicRotationDelta": construct.Flag,
})

CCharClassXParasiteDropComponent = Object(CCharClassComponentFields)

CCharClassHydrogigaZiplineComponent = Object({
    **CCharClassMagnetSlidingBlockComponentFields,
    "fMovementMultiplierUnderwater": common_types.Float,
    "fWaterLevelToSlowDownBeforeUnderwater": common_types.Float,
    "fWaterLevelToConsiderUnderwater": common_types.Float,
    "fTimeToMatchMovementMultiplierGoingBackToStartUnderwater": common_types.Float,
    "fTimeToMatchMovementMultiplierSlowingDown": common_types.Float,
})

CCharClassMeleeComponent = Object({
    **CCharClassComponentFields,
    "bAutoLockOnMelee": construct.Flag,
    "sMeleeKillFX": common_types.StrId,
    "sMeleeKillSound": common_types.StrId,
})

CCharClassSwarmAttackComponent = Object({
    **CCharClassAttackComponentFields,
    "fMaxDamage": common_types.Float,
})

CCharClassDoorEmmyFXComponent = Object({
    **CCharClassComponentFields,
    "fLockedTime": common_types.Float,
})

CCharClassAnimationNavMeshItemComponent = Object({
    **CCharClassNavMeshItemComponentFields,
    "sAnimationId": common_types.StrId,
})

CCharClassMaterialFXComponent = Object(CCharClassComponentFields)

CCharClassAimComponent = Object({
    **CCharClassComponentFields,
    "fAutoAimWidth": common_types.Float,
    "fAutoAimLength": common_types.Float,
    "fAutoAimConeLength": common_types.Float,
    "fAutoAimInterp": common_types.Float,
    "fAutoAimLockOnInterp": common_types.Float,
    "fAutoAimLockOnPredictionTime": common_types.Float,
    "fAutoAimLockAfterDeadTime": common_types.Float,
    "fMaxTimeMaintainingFront": common_types.Float,
    "fLaserDeactivationTime": common_types.Float,
    "fAnalogModeDefaultInterp": common_types.Float,
    "fForcedFrontTimeAfterFire": common_types.Float,
    "fForcedFrontTimeAfterFireOnAir": common_types.Float,
    "fForcedFrontTimeAfterDiagonal": common_types.Float,
    "fForcedFrontTimeAfterSecondaryWeapon": common_types.Float,
    "fForcedFrontTimeAfterStealthRun": common_types.Float,
    "fForcedFrontTimeAfterParkour": common_types.Float,
    "fForcedFrontTimeAfterFloorSlide45End": common_types.Float,
})

CCharClassPullableGrapplePointComponent = Object(CCharClassPullableGrapplePointComponentFields := {
    **CCharClassGrapplePointComponentFields,
    "sOnDestructionLeftTimeline": common_types.StrId,
    "sOnDestructionRightTimeline": common_types.StrId,
})

CCharClassElevatorUsableComponent = Object(CCharClassElevatorUsableComponentFields := {
    **CCharClassUsableComponentFields,
    "sUsableUpAction": common_types.StrId,
    "sUsableDownAction": common_types.StrId,
    "sUsableLevelChangeUpAction": common_types.StrId,
    "sUsableLevelChangeDownAction": common_types.StrId,
})


class CTimelineComponent_ENextPolicy(enum.IntEnum):
    NEXT = 0
    RANDOM = 1
    RANDOM_DELAY = 2
    Invalid = 2147483647


construct_CTimelineComponent_ENextPolicy = construct.Enum(construct.Int32ul, CTimelineComponent_ENextPolicy)

CCharClassTimelineComponent = Object({
    **CCharClassComponentFields,
    "sInitAction": common_types.StrId,
    "eNextPolicy": construct_CTimelineComponent_ENextPolicy,
    "fMinDelayTime": common_types.Float,
    "fMaxDelayTime": common_types.Float,
    "eLayerInFrustumToLaunchInRandomDelayPolicy": base_global_timeline_TLayers,
})

CDamageSourceFactor = Object({
    "fPowerBeamFactor": common_types.Float,
    "fWideBeamFactor": common_types.Float,
    "fPlasmaBeamFactor": common_types.Float,
    "fWaveBeamFactor": common_types.Float,
    "fGrappleBeamFactor": common_types.Float,
    "fHyperBeamFactor": common_types.Float,
    "fChargePowerBeamFactor": common_types.Float,
    "fChargeWideBeamFactor": common_types.Float,
    "fChargePlasmaBeamFactor": common_types.Float,
    "fChargeWaveBeamFactor": common_types.Float,
    "fMeleeChargePowerBeamFactor": common_types.Float,
    "fMeleeChargeWideBeamFactor": common_types.Float,
    "fMeleeChargePlasmaBeamFactor": common_types.Float,
    "fMeleeChargeWaveBeamFactor": common_types.Float,
    "fMissileFactor": common_types.Float,
    "fSuperMissileFactor": common_types.Float,
    "fIceMissileFactor": common_types.Float,
    "fMultiLockonMissileFactor": common_types.Float,
    "fBombFactor": common_types.Float,
    "fLineBombFactor": common_types.Float,
    "fPowerBombFactor": common_types.Float,
    "fScrewAttackFactor": common_types.Float,
    "fDashMeleeFactor": common_types.Float,
    "fSpeedBoosterFactor": common_types.Float,
    "fShineSparkFactor": common_types.Float,
})


class EDemolitionPhase(enum.IntEnum):
    NONE = 0
    Idle = 1
    StartSwelling = 2
    HeartBeat = 3
    Explosion = 4
    Invalid = 2147483647


construct_EDemolitionPhase = construct.Enum(construct.Int32ul, EDemolitionPhase)

CCharClassDemolitionBlockLifeComponent = Object(CCharClassDemolitionBlockLifeComponentFields := {
    **CCharClassLifeComponentFields,
    "oDamageSourceFactor": CDamageSourceFactor,
    "iHitCount": common_types.Int,
    "fTimeAfterHuskDestroyed": common_types.Float,
    "fTimeAfterFirstHit": common_types.Float,
    "fTimeMaterialExplosive": common_types.Float,
    "fTimeAfterDiffuseHuskDestroyed": common_types.Float,
    "eDemolitionPhase": construct_EDemolitionPhase,
    "bHuskInitiallyRemoved": construct.Flag,
    "sCameraFXPresetHusk": common_types.StrId,
    "sCameraFXPresetOnImpact": common_types.StrId,
    "sCameraFXPresetOnDead": common_types.StrId,
})

CCharClassMorphBallLauncherExitComponent = Object({
    **CCharClassComponentFields,
    "fExpelImpulseSize": common_types.Float,
    "fInputIgnoreTimeAfterExpelling": common_types.Float,
    "fFrictionIgnoreTimeAfterExpelling": common_types.Float,
})

CCharClassEmmyValveComponent = Object(CCharClassComponentFields)

CCharClassFanCoolDownComponent = Object(CCharClassComponentFields)

CCharClassSaveStationUsableComponent = Object({
    **CCharClassUsableComponentFields,
    "sSaveFXID": common_types.StrId,
    "sStartLevelFXID": common_types.StrId,
})

CCharClassInfesterBallAttackComponent = Object(CCharClassAIAttackComponentFields)

CShotLaunchConfig = Object(CShotLaunchConfigFields := {
    "sID": common_types.StrId,
    "fMaxHitVerticalSpeed": common_types.Float,
    "fTrajectorySampleTimeInterval": common_types.Float,
})

CCharClassShotComponent = Object({
    **CCharClassComponentFields,
    "vLaunchShotConfigs": common_types.make_vector(Pointer_CShotLaunchConfig.create_construct()),
})

CCharClassBehaviorTreeAIComponent = Object(CCharClassBehaviorTreeAIComponentFields := {
    **CCharClassAIComponentFields,
    "sBehaviorTreePath": common_types.StrId,
    "fMaxCrazyTime": common_types.Float,
})

CCharClassElectrifyingAreaComponent = Object({
    **CCharClassComponentFields,
    "bShouldUpdateAreaOnStart": construct.Flag,
    "bShouldCoverPlatformsCompletely": construct.Flag,
    "fMinValidYNormal": common_types.Float,
    "fClockwiseDistance": common_types.Float,
    "fCounterClockwiseDistance": common_types.Float,
    "fTriggerHeight": common_types.Float,
    "fTriggerDownwardHeight": common_types.Float,
    "fFXHeight": common_types.Float,
    "fHeightTolerance": common_types.Float,
})

CCharClassMorphBallLauncherComponent = Object({
    **CCharClassComponentFields,
    "fTimeShootSequence": common_types.Float,
    "fTimeRepositioningEntities": common_types.Float,
    "fTimeToAccelerateCannon": common_types.Float,
    "fMinCannonActionPlayRate": common_types.Float,
    "fMaxCannonActionPlayRate": common_types.Float,
    "sCannonActionPlayRateEasingFunction": common_types.StrId,
})

CCharClassChangeStageNavMeshItemComponent = Object({
    **CCharClassComponentFields,
    "sStage": common_types.StrId,
    "sRemovedStage": common_types.StrId,
})

CCharClassMagnetSurfaceHuskComponent = Object({
    **CCharClassComponentFields,
    "sHuskName": common_types.StrId,
    "sBrokenHuskName": common_types.StrId,
})

CCharClassSwarmControllerComponent = Object(CCharClassSwarmControllerComponentFields := {
    **CCharClassComponentFields,
    "fMinTimeInNode": common_types.Float,
    "fTimeInNodeRandomness": common_types.Float,
    "fTargetChangeProbability": common_types.Float,
    "sIndividualLife": common_types.StrId,
    "fAttackPathOffset": common_types.Float,
    "iMaxChangingTargetSimul": common_types.Int,
    "bWantsSpiraling": construct.Flag,
    "bWantsJellyfishMovement": construct.Flag,
    "bWantsFishMovement": construct.Flag,
    "bWantsInternalFlocking": construct.Flag,
    "bWantsMigration": construct.Flag,
    "fMaxDistToMigrate": common_types.Float,
    "bWantsBumpReaction": construct.Flag,
    "iTotalDrops": common_types.Int,
    "fShakeAmplitude": common_types.Float,
    "fShakeSpeed": common_types.Float,
    "iMinHitsForMediumImpact": common_types.Int,
    "iMinHitsForLargeImpact": common_types.Int,
    "sImpactSoundSmallGroup": common_types.StrId,
    "sImpactSoundMediumGroup": common_types.StrId,
    "sImpactSoundLargeGroup": common_types.StrId,
    "sMoveSoundSmallGroup": common_types.StrId,
    "sMoveSoundMediumGroup": common_types.StrId,
    "sMoveSoundLargeGroup": common_types.StrId,
    "iMaxPopulationForSmallGroup": common_types.UInt,
    "iMaxPopulationForMediumGroup": common_types.UInt,
    "fMaxTimeAlive": common_types.Float,
    "fMinTimeAlive": common_types.Float,
    "fMaxDistToLinkNodes": common_types.Float,
    "fMeleeRepelRadius": common_types.Float,
    "fMeleeKillRatio": common_types.Float,
    "iMeleeMinKills": common_types.Int,
    "iMeleeMaxKills": common_types.Int,
    "fMeleeMinRepelDistance": common_types.Float,
    "fMeleeMaxRepelDistance": common_types.Float,
    "fMissileRepelRadius": common_types.Float,
    "fMissileKillRatio": common_types.Float,
    "iMissileMinKills": common_types.Int,
    "iMissileMaxKills": common_types.Int,
    "fMissileMinRepelDistance": common_types.Float,
    "fMissileMaxRepelDistance": common_types.Float,
    "fMigrationCheckMinTime": common_types.Float,
    "fMigrationCheckMaxTime": common_types.Float,
    "fDefaultDiversionTimer": common_types.Float,
    "fMinStunTime": common_types.Float,
    "fMaxStunTime": common_types.Float,
    "fDefaultBeamsRadiusIncrement": common_types.Float,
    "fWideBeamRadiusIncrement": common_types.Float,
    "fPlasmaBeamRadiusIncrement": common_types.Float,
    "oDamageSourceFactor": CDamageSourceFactor,
    "bDiesOfLoneliness": construct.Flag,
    "iLonelinessGroupSize": common_types.Int,
    "bApplyLonelinessToEachGroup": construct.Flag,
    "bWeakToSpinAttack": construct.Flag,
    "bIsWater": construct.Flag,
})

CCharClassEnemyLifeComponent = Object(CCharClassEnemyLifeComponentFields := {
    **CCharClassLifeComponentFields,
    "oDamageSourceFactor": CDamageSourceFactor,
    "bShouldDieWithPowerBomb": construct.Flag,
    "fDamageFXTime": common_types.Float,
    "fMinTimeBetweenDamageSoundCallback": common_types.Float,
    "fMaxTimeBetweenDamageSoundCallback": common_types.Float,
    "bIgnoreRotateToInstigator": construct.Flag,
    "bShowLifeBar": construct.Flag,
    "vLifeBarOffset": common_types.CVector3D,
    "sDamageTimeline": common_types.StrId,
    "sDamageSFXTimeline": common_types.StrId,
    "bDashMeleeAppliesNonLethalDamage": construct.Flag,
})

CCharClassTriggerNavMeshItemComponent = Object(CCharClassNavMeshItemComponentFields)

CCharClassScourgeLifeComponent = Object(CCharClassEnemyLifeComponentFields)


class CCharClassFlockingSwarmControllerComponent_SRotationMode(enum.IntEnum):
    Raw = 0
    Inclinate = 1
    Invalid = 2147483647


construct_CCharClassFlockingSwarmControllerComponent_SRotationMode = construct.Enum(construct.Int32ul, CCharClassFlockingSwarmControllerComponent_SRotationMode)

CCharClassFlockingSwarmControllerComponent = Object(CCharClassFlockingSwarmControllerComponentFields := {
    **CCharClassSwarmControllerComponentFields,
    "fContaimentDist": common_types.Float,
    "eRotationMode": construct_CCharClassFlockingSwarmControllerComponent_SRotationMode,
    "fMaxAngularSpeed": common_types.Float,
    "fCohesion": common_types.Float,
    "fSeparationFactor": common_types.Float,
    "fSeparation": common_types.Float,
    "fToTarget": common_types.Float,
    "fContainment": common_types.Float,
    "bAllowSharpTurns": construct.Flag,
    "bCanFollowTarget": construct.Flag,
    "fPreferredRadius": common_types.Float,
    "fMinRadius": common_types.Float,
    "fPursuitSpeed": common_types.Float,
    "fRecoverySpeed": common_types.Float,
    "fAttackSpeed": common_types.Float,
    "fBillboardScale": common_types.Float,
    "bForceAllowTurn": construct.Flag,
    "fHareDistance": common_types.Float,
    "fMaxQueueSize": common_types.Float,
})

CCharClassXParasiteAIComponent = Object({
    **CCharClassBehaviorTreeAIComponentFields,
    "fAbsorptionDistance": common_types.Float,
    "uMaxSimultaneous": common_types.UInt,
    "fMaxSteeringAcceleration": common_types.Float,
    "fMaxSteeringBrake": common_types.Float,
    "fMaxSteeringChangingDir": common_types.Float,
    "fBrakeDistance": common_types.Float,
    "bLimitSteeringForceAngle": construct.Flag,
    "fMaxSteeringForceAngle": common_types.Float,
    "fWanderRadius": common_types.Float,
    "fInitTime": common_types.Float,
    "fWanderTime": common_types.Float,
    "fOffSetDisplacementNearPowerBomb": common_types.Float,
    "fDistanceArriveEndAttract": common_types.Float,
})

CCharClassHangableGrappleSurfaceComponent = Object(CCharClassHangableGrappleSurfaceComponentFields := {
    **CCharClassGrapplePointComponentFields,
    "fMagnetSurfaceMaxIntensityOnGrappleNotAllowed": common_types.Float,
    "sGrappleHelperColliderId": common_types.StrId,
    "fGrappleHelperMaxSegmentLengthToUseCenter": common_types.Float,
})

CCharClassAutectorLifeComponent = Object(CCharClassEnemyLifeComponentFields)

CCharClassSabotoruLifeComponent = Object(CCharClassEnemyLifeComponentFields)

CCharClassShineonAIComponent = Object({
    **CCharClassBehaviorTreeAIComponentFields,
    "fSteeringAcceleration": common_types.Float,
    "fSteeringSpeed": common_types.Float,
    "fMaxTargetDistanceToAccelerateCloseToTarget": common_types.Float,
    "fCloseToTargetAcceleration": common_types.Float,
    "fMaxDistanceToTurn": common_types.Float,
})

CCharClassArachnusAIComponent = Object(CCharClassBehaviorTreeAIComponentFields)

CCharClassBaseTriggerComponent = Object(CCharClassBaseTriggerComponentFields := CCharClassActivatableComponentFields)

CCharClassFulmiteBellyMineAIComponent = Object({
    **CCharClassBehaviorTreeAIComponentFields,
    "fLifeTime": common_types.Float,
    "fExplosionRadius": common_types.Float,
    "fTimeToExplosion": common_types.Float,
    "fTimeAtMaxRadiusExplosion": common_types.Float,
    "fDamageFulmiteBellyMineExplosion": common_types.Float,
    "fNormalXFactor": common_types.Float,
    "fNormalYFactor": common_types.Float,
    "fUpsideDownXFactor": common_types.Float,
    "fUpsideDownYFactor": common_types.Float,
    "fInWallXFactor": common_types.Float,
    "fInWallYFactor": common_types.Float,
    "uGroundRebounds": common_types.UInt,
    "fWallImpulseXFactor": common_types.Float,
    "fWallImpulseYFactor": common_types.Float,
    "fGroundImpulseXFactor": common_types.Float,
    "fGroundImpulseYFactor": common_types.Float,
    "bPlayReboundActions": construct.Flag,
    "fImpulseVelocityXLimit": common_types.Float,
    "fImpulseVelocityYLimit": common_types.Float,
    "fTimeToShowBeforeExplosionFX": common_types.Float,
    "fMinTimeBetweenBeeps": common_types.Float,
    "fMaxTimeBetweenBeeps": common_types.Float,
    "fMinBeepVolume": common_types.Float,
    "fMaxBeepVolume": common_types.Float,
    "fMinBeepPitch": common_types.Float,
    "fMaxBeepPitch": common_types.Float,
})


class CCharClassHecathonAIComponent_ESubspecies(enum.IntEnum):
    Hecathon = 0
    Omnithon = 1
    Invalid = 2147483647


construct_CCharClassHecathonAIComponent_ESubspecies = construct.Enum(construct.Int32ul, CCharClassHecathonAIComponent_ESubspecies)

CCharClassHecathonAIComponent = Object({
    **CCharClassBehaviorTreeAIComponentFields,
    "eSubspecies": construct_CCharClassHecathonAIComponent_ESubspecies,
})

CAttackPreset = Object({
    "bEnabled": construct.Flag,
    "fMinNextAttackTime": common_types.Float,
    "fMaxNextAttackTime": common_types.Float,
    "fMandatoryMinNextAttackTime": common_types.Float,
    "fMandatoryMaxNextAttackTime": common_types.Float,
    "fRepeatAttackTime": common_types.Float,
    "fShortDistanceProb": common_types.Float,
    "fMediumDistanceProb": common_types.Float,
    "fLongDistanceProb": common_types.Float,
    "fAbuseShortDistanceProb": common_types.Float,
    "fAbuseMediumDistanceProb": common_types.Float,
    "fAbuseLongDistanceProb": common_types.Float,
    "fAbuseTime": common_types.Float,
    "uMaxOccurrencesInLastAttacks": common_types.UInt,
    "uNumOfAttacksToEvaluate": common_types.UInt,
})

CCharClassAttack = Object(CCharClassAttackFields := {
    "tPresets": common_types.make_vector(Pointer_CAttackPreset.create_construct()),
    "sAttackAnim": common_types.StrId,
    "sName": common_types.StrId,
    "bCheckInFrustum": construct.Flag,
    "fMinDistance": common_types.Float,
    "fMaxDistance": common_types.Float,
    "bCheckTargetReachable": construct.Flag,
    "bCheckTargetDetected": construct.Flag,
    "bCheckTargetNotInvulnerable": construct.Flag,
    "bCheckViewDirection": construct.Flag,
    "bCheckNotViewDirection": construct.Flag,
    "bUpdateAttackWhileFrozen": construct.Flag,
    "bFreezeEndsAttack": construct.Flag,
    "sCancelAttackAnim": common_types.StrId,
    "sAttackOnEndTimeline": common_types.StrId,
    "fMinTimeBossInCombatToAttack": common_types.Float,
    "iMaxToRepeat": common_types.Int,
    "iMaxWithoutLaunch": common_types.Int,
    "fMinTimeToReachDesiredAttackPos": common_types.Float,
    "fChaseCenterDistance": common_types.Float,
    "fMinTimeSinceLastGrab": common_types.Float,
    "bCheckTargetOnFloor": construct.Flag,
    "bCheckNotTurning": construct.Flag,
    "fTimeSinceLastFrozen": common_types.Float,
    "bCheckInSubarea": construct.Flag,
})

CCharClassInfesterShootAttack = Object(CCharClassAttackFields)

CCharClassInfesterReloadAttack = Object(CCharClassAttackFields)


class CCharClassInfesterAIComponent_ESubspecies(enum.IntEnum):
    Infester = 0
    Fulmite = 1
    Invalid = 2147483647


construct_CCharClassInfesterAIComponent_ESubspecies = construct.Enum(construct.Int32ul, CCharClassInfesterAIComponent_ESubspecies)

CCharClassInfesterAIComponent = Object({
    **CCharClassBehaviorTreeAIComponentFields,
    "fTimeToReloadBeam": common_types.Float,
    "sProjectileModelName": common_types.StrId,
    "oInfesterShootAttackDef": CCharClassInfesterShootAttack,
    "oInfesterReloadAttackDef": CCharClassInfesterReloadAttack,
    "eSubspecies": construct_CCharClassInfesterAIComponent_ESubspecies,
})

CCharClassProtoEmmyChaseMusicTriggerComponent = Object(CCharClassBaseTriggerComponentFields)

CCharClassDoorGrapplePointComponent = Object({
    **CCharClassPullableGrapplePointComponentFields,
    "sGrappleColliderNames": common_types.make_vector(common_types.StrId),
})

CCharClassWarLotusAIComponent = Object({
    **CCharClassBehaviorTreeAIComponentFields,
    "fImpactToRelaxTime": common_types.Float,
    "fBumpToRelaxTime": common_types.Float,
    "fImpactTime": common_types.Float,
    "fBumpTime": common_types.Float,
})

CCharClassAccessPointComponent = Object({
    **CCharClassUsableComponentFields,
    "sUsePrepareLeftAPNoUsedAction": common_types.StrId,
    "sUsePrepareRightAPNoUsedAction": common_types.StrId,
    "sUseInitAPUsedAction": common_types.StrId,
    "sUseAPUsedAction": common_types.StrId,
    "sUsableInitAPUsedAction": common_types.StrId,
    "sSaveRingsOpenAction": common_types.StrId,
    "sSaveRingsCloseAction": common_types.StrId,
    "sSaveRingLoopAction": common_types.StrId,
    "sUsePrepareLeftAfterDiscoverNoDialogueAction": common_types.StrId,
    "sUsePrepareRightAfterDiscoverNoDialogueAction": common_types.StrId,
})

CCharClassFulmiteBellyMineAttackComponent = Object(CCharClassAIAttackComponentFields)

CCharClassFrozenAsPlatformComponent = Object({
    **CCharClassFrozenComponentFields,
    "sCollisionMaskToFreeze": common_types.StrId,
    "sCollisionTagsExcludedFromFreezing": common_types.StrId,
    "fPlatformDepth": common_types.Float,
    "sIceCubeCharClass": common_types.StrId,
    "vIceCubeSize": common_types.CVector2D,
})

CCharClassAIGrapplePointComponent = Object({
    **CCharClassPullableGrapplePointComponentFields,
    "sGrappleCollider": common_types.StrId,
})

CCharClassGobblerBiteAttack = Object(CCharClassAttackFields)

CCharClassGobblerAIComponent = Object({
    **CCharClassBehaviorTreeAIComponentFields,
    "oGobblerBiteAttackDef": CCharClassGobblerBiteAttack,
    "fMinImpulseFactorX": common_types.Float,
    "fMinImpulseFactorY": common_types.Float,
    "fMaxImpulseFactorX": common_types.Float,
    "fMaxImpulseFactorY": common_types.Float,
    "fDistForMaxImpulse": common_types.Float,
    "fDistForMinImpulse": common_types.Float,
    "fDistanceToBiteAttack": common_types.Float,
    "fMinNervousnessDist": common_types.Float,
    "fMaxNervousnessDist": common_types.Float,
})

CCharClassDummyAIComponent = Object({
    **CCharClassAIComponentFields,
    "bWantsDrawModelPrimitiveSet": construct.Flag,
})

CCharClassLavaPumpComponent = Object(CCharClassActivatableComponentFields)

CCharClassMultiModelUpdaterComponent = Object({
    **CCharClassModelUpdaterComponentFields,
    "dctModels": common_types.make_dict(common_types.StrId),
})

CCharClassItemLifeComponent = Object(CCharClassItemLifeComponentFields := {
    **CCharClassLifeComponentFields,
    "oDamageSourceFactor": CDamageSourceFactor,
    "iHitCount": common_types.Int,
})

CCharClassCapsuleUsableComponent = Object({
    **CCharClassElevatorUsableComponentFields,
    "sCapsuleLeaveAction": common_types.StrId,
    "sCapsuleArriveAction": common_types.StrId,
    "sSkybaseAction": common_types.StrId,
})

CCharClassAutsharpLifeComponent = Object(CCharClassEnemyLifeComponentFields)

CCharClassDemolitionBlockActivatableActorLifeComponent = Object({
    **CCharClassDemolitionBlockLifeComponentFields,
    "sActivatableObjAnim": common_types.StrId,
    "sActivatableObjAnimRelax": common_types.StrId,
})

CCharClassFingSwarmControllerComponent = Object(CCharClassFlockingSwarmControllerComponentFields)

CCharClassMovablePlatformComponent = Object(CCharClassMovablePlatformComponentFields := {
    **CCharClassMovementComponentFields,
    "sMovableColliderId": common_types.StrId,
    "bDisableOnActivatedOnLoadScenario": construct.Flag,
})


class CCharClassRodotukAIComponent_SAbsorbConfig_EType(enum.IntEnum):
    NONE = 0
    Short = 1
    Medium = 2
    Long = 3
    Invalid = 2147483647


construct_CCharClassRodotukAIComponent_SAbsorbConfig_EType = construct.Enum(construct.Int32ul, CCharClassRodotukAIComponent_SAbsorbConfig_EType)

CCharClassRodotukAIComponent_SAbsorbConfig = Object({
    "eType": construct_CCharClassRodotukAIComponent_SAbsorbConfig_EType,
    "fBaseAbsorbDistance": common_types.Float,
    "fAngryAbsorbDistance": common_types.Float,
    "fBombAbsorbExtraHeight": common_types.Float,
    "fBombAbsorbExtraWidth": common_types.Float,
    "fMaxAbsorbAngle": common_types.Float,
    "fAbsorbBaseSpeed": common_types.Float,
    "fAbsorbMaxSpeed": common_types.Float,
    "fAbsorbTimeToLoseControl": common_types.Float,
    "fAbsorbAcceleration": common_types.Float,
    "fBombAbsorbBaseSpeed": common_types.Float,
    "fBombAbsorbAcceleration": common_types.Float,
})

base_global_CRntDictionary_base_global_CStrId__CCharClassRodotukAIComponent_SAbsorbConfig_ = common_types.make_dict(CCharClassRodotukAIComponent_SAbsorbConfig)

CCharClassRodotukAIComponent_TVAbsorbConfigs = base_global_CRntDictionary_base_global_CStrId__CCharClassRodotukAIComponent_SAbsorbConfig_

CCharClassRodotukSuckAttack = Object(CCharClassRodotukSuckAttackFields := CCharClassAttackFields)

CCharClassRodotukAIComponent = Object(CCharClassRodotukAIComponentFields := {
    **CCharClassBehaviorTreeAIComponentFields,
    "fBiteAnticipationDistance": common_types.Float,
    "fBombForceExplosionDistance": common_types.Float,
    "vAbsorbConfigs": CCharClassRodotukAIComponent_TVAbsorbConfigs,
    "oRodotukSuckAttackDef": CCharClassRodotukSuckAttack,
})

CCharClassEmmyAIComponent = Object(CCharClassEmmyAIComponentFields := {
    **CCharClassBehaviorTreeAIComponentFields,
    "bControlsEmmyZoneLight": construct.Flag,
    "bCanUseTunnels": construct.Flag,
    "sInventoryItemOnKilled": common_types.StrId,
})

CCharClassCharacterMovement = Object(CCharClassCharacterMovementFields := {
    **CCharClassMovementComponentFields,
    "fMaxYCollisionNormalToBeFloor": common_types.Float,
    "bStopOnWallMovementCollision": construct.Flag,
})

CCharClassSluggerSpitAttack = Object({
    **CCharClassAttackFields,
    "fBallGravity": common_types.Float,
    "fMaxHitVerticalSpeed": common_types.Float,
    "fTrajectorySampleTimeInterval": common_types.Float,
    "fTimeOutOfFrustumToAbortAttack": common_types.Float,
    "fBallDefaultLaunchAngleDegs": common_types.Float,
    "fBallLaunchSpeed": common_types.Float,
    "fBallMinLaunchAngleDegs": common_types.Float,
    "fBallMaxLaunchAngleDegs": common_types.Float,
    "fHighLaunchFixedAngleDegs": common_types.Float,
    "fHighLaunchMinSpeed": common_types.Float,
    "fHighLaunchMaxSpeed": common_types.Float,
    "fMediumLaunchFixedAngleDegs": common_types.Float,
    "fMediumLaunchMinSpeed": common_types.Float,
    "fMediumLaunchMaxSpeed": common_types.Float,
    "fLowLaunchFixedAngleDegs": common_types.Float,
    "fLowLaunchMinSpeed": common_types.Float,
    "fLowLaunchMaxSpeed": common_types.Float,
})

CCharClassSluggerAIComponent = Object(CCharClassSluggerAIComponentFields := {
    **CCharClassBehaviorTreeAIComponentFields,
    "oSluggerSpitAttackDef": CCharClassSluggerSpitAttack,
    "sAcidBallCharClass": common_types.StrId,
    "fAttackReachableHeight": common_types.Float,
    "fBallTrajectoryCheckRadius": common_types.Float,
})


class CCharClassDropterAIComponent_ESubspecies(enum.IntEnum):
    Dropter = 0
    Sharpaw = 1
    Iceflea = 2
    Invalid = 2147483647


construct_CCharClassDropterAIComponent_ESubspecies = construct.Enum(construct.Int32ul, CCharClassDropterAIComponent_ESubspecies)

CCharClassDropterDiveAttack = Object({
    **CCharClassAttackFields,
    "fStartAttackDistance": common_types.Float,
    "fMaxAttackTravelDistance": common_types.Float,
})

CCharClassDropterAIComponent = Object({
    **CCharClassBehaviorTreeAIComponentFields,
    "bWantsIceExplosion": construct.Flag,
    "fMaxFreezeTime": common_types.Float,
    "fMinFreezeTime": common_types.Float,
    "fFreezeExplosionPreparationTime": common_types.Float,
    "fFreezeExplosionRadius": common_types.Float,
    "fFreezeExplosionDuration": common_types.Float,
    "fFreezeExplosionRemanentDuration": common_types.Float,
    "eSubspecies": construct_CCharClassDropterAIComponent_ESubspecies,
    "oDropterDiveAttackDef": CCharClassDropterDiveAttack,
})

CCharClassRedenkiSwarmControllerComponent = Object(CCharClassRedenkiSwarmControllerComponentFields := {
    **CCharClassFlockingSwarmControllerComponentFields,
    "fDistToStartCharge": common_types.Float,
    "fDistToEndRecovery": common_types.Float,
    "bAlwaysForceRailMovement": construct.Flag,
    "fPathRecalculationTime": common_types.Float,
    "fAttackPathLength": common_types.Float,
    "fDistToForceAttack": common_types.Float,
    "fMinChaos": common_types.Float,
    "fMaxChaos": common_types.Float,
    "fMinMovementAnimSpeed": common_types.Float,
    "fMaxMovementAnimSpeed": common_types.Float,
    "fWallChargeStunDuration": common_types.Float,
    "sCombatSoundSmallGroup": common_types.StrId,
    "sCombatSoundMediumGroup": common_types.StrId,
    "sCombatSoundLargeGroup": common_types.StrId,
    "sPreparationSoundSmallGroup": common_types.StrId,
    "sPreparationSoundMediumGroup": common_types.StrId,
    "sPreparationSoundLargeGroup": common_types.StrId,
    "sStartChargeSoundSmallGroup": common_types.StrId,
    "sStartChargeSoundMediumGroup": common_types.StrId,
    "sStartChargeSoundLargeGroup": common_types.StrId,
    "sCollisionWithWallSoundSmallGroup": common_types.StrId,
    "sCollisionWithWallSoundMediumGroup": common_types.StrId,
    "sCollisionWithWallSoundLargeGroup": common_types.StrId,
    "bPreparationBackAllowed": construct.Flag,
    "fMinPreparationTime": common_types.Float,
    "fBackDistanceLength": common_types.Float,
    "fBackDistanceWidth": common_types.Float,
    "fAttackCooldown": common_types.Float,
    "fAngleLimitDeg": common_types.Float,
    "fMinDistForAngleLimit": common_types.Float,
})

CCharClassEmmyForestAIComponent = Object(CCharClassEmmyAIComponentFields)

CCharClassDummyMovement = Object({
    **CCharClassMovementComponentFields,
    "bCanFall": construct.Flag,
})

base_global_TRntString256 = Object({})

TCheckpointOffset = Object({
    **CCharClassStartPointComponentFields,
    "strCheckpointID": base_global_TRntString256,
    "vOffsetPos": common_types.CVector3D,
    "vOffsetAng": common_types.CVector3D,
})


class CCharClassDredhedAIComponent_ESubspecies(enum.IntEnum):
    Dredhed = 0
    Sakai = 1
    Invalid = 2147483647


construct_CCharClassDredhedAIComponent_ESubspecies = construct.Enum(construct.Int32ul, CCharClassDredhedAIComponent_ESubspecies)

CCharClassDredhedDiveAttack = Object({
    **CCharClassAttackFields,
    "fHightBlendSpeed": common_types.Float,
})

CCharClassDredhedAIComponent = Object({
    **CCharClassBehaviorTreeAIComponentFields,
    "eSubspecies": construct_CCharClassDredhedAIComponent_ESubspecies,
    "fTimeBetweenCharges": common_types.Float,
    "oDredhedDiveAttackDef": CCharClassDredhedDiveAttack,
})

CCharClassSclawkLifeComponent = Object(CCharClassEnemyLifeComponentFields)

CCharClassBeamBoxComponent = Object(CCharClassItemLifeComponentFields)

CCharClassEmmyMagmaAIComponent = Object(CCharClassEmmyAIComponentFields)


class EForcedDamageMode(enum.IntEnum):
    NOT_FORCED = 0
    ONLY_REACTION = 1
    FORCED = 2
    Invalid = 2147483647


construct_EForcedDamageMode = construct.Enum(construct.Int32ul, EForcedDamageMode)

CCharClassWeaponMovement = Object(CCharClassWeaponMovementFields := {
    **CCharClassMovementComponentFields,
    "sDamageID": common_types.StrId,
    "sDamageSource": common_types.StrId,
    "eDamageType": construct_EDamageType,
    "eDamageStrength": construct_EDamageStrength,
    "fSpeed": common_types.Float,
    "sCollisionMask": common_types.StrId,
    "bWantsProcessBreakableTileHit": construct.Flag,
    "eForcedDamageMode": construct_EForcedDamageMode,
    "bSetHitPosOnCollisionProcessed": construct.Flag,
    "bAllowMultipleHitsToSameEntity": construct.Flag,
    "bIgnoreSamusCannonImpactDuringMelee": construct.Flag,
})

CCharClassActionSwitcherOnPullGrapplePointComponent = Object({
    **CCharClassPullableGrapplePointComponentFields,
    "sGrappleCollider": common_types.StrId,
    "fGrappleMinAlignmentX": common_types.Float,
    "sActionOnGrappleAttach": common_types.StrId,
    "sActionOnPullStart": common_types.StrId,
    "sActionOnPullAbort": common_types.StrId,
    "sActionOnGrappleDetach": common_types.StrId,
})

CBarelyFrozenIceInfo = Object({
    "sModel": common_types.StrId,
    "sNode": common_types.StrId,
    "fScale": common_types.Float,
})

CCharClassFrozenAsFrostbiteComponent = Object({
    **CCharClassFrozenComponentFields,
    "iRequiredFrostbiteLevel": common_types.Int,
    "fFrostbiteLevelResetTime": common_types.Float,
    "fAfterHitNoFrostbiteLevelResetTime": common_types.Float,
    "sTimelineIdOnFrostbiteStart": common_types.StrId,
    "sTimelineIdOnFrostbiteStop": common_types.StrId,
    "bShouldDieWithDashMelee": construct.Flag,
    "tBarelyIceInfo": common_types.make_vector(Pointer_CBarelyFrozenIceInfo.create_construct()),
})

CCharClassInfesterBallLifeComponent = Object(CCharClassEnemyLifeComponentFields)

CCharClassMushroomPlatformComponent = Object({
    **CCharClassLifeComponentFields,
    "fTimeToRetract": common_types.Float,
    "fRetractedTime": common_types.Float,
})

CCharClassChozoZombieXPoisonClawsAttack = Object(CCharClassAttackFields)

CCharClassChozoZombieXAIComponent = Object({
    **CCharClassBehaviorTreeAIComponentFields,
    "oChozoZombieXPoisonClawsAttackDef": CCharClassChozoZombieXPoisonClawsAttack,
})

CCharClassDaivoSwarmControllerComponent = Object({
    **CCharClassRedenkiSwarmControllerComponentFields,
    "fVomitSpeed": common_types.Float,
})


class CCharClassGooplotAIComponent_ESubspecies(enum.IntEnum):
    Gooplot = 0
    Gooshocker = 1
    Invalid = 2147483647


construct_CCharClassGooplotAIComponent_ESubspecies = construct.Enum(construct.Int32ul, CCharClassGooplotAIComponent_ESubspecies)

CCharClassGooplotJumpAttack = Object(CCharClassAttackFields)

CCharClassGooplotUndoJumpAttack = Object(CCharClassAttackFields)

CCharClassGooplotAIComponent = Object(CCharClassGooplotAIComponentFields := {
    **CCharClassBehaviorTreeAIComponentFields,
    "eSubspecies": construct_CCharClassGooplotAIComponent_ESubspecies,
    "fExplosionTime": common_types.Float,
    "oGooplotJumpAttackDef": CCharClassGooplotJumpAttack,
    "oGooplotUndoJumpAttackDef": CCharClassGooplotUndoJumpAttack,
})

CCharClassCaterzillaAIComponent = Object({
    **CCharClassBehaviorTreeAIComponentFields,
    "iNumOfCreatures": common_types.Int,
})

CCharClassEmmySancAIComponent = Object(CCharClassEmmyAIComponentFields)

CCharClassBaseGroundShockerAIComponent = Object(CCharClassBaseGroundShockerAIComponentFields := {
    **CCharClassBehaviorTreeAIComponentFields,
    "fDefaultMotionSpeed": common_types.Float,
    "fCombatMotionSpeed": common_types.Float,
    "fFleeMotionSpeed": common_types.Float,
})

CCharClassDizzeanSwarmControllerComponent = Object(CCharClassFlockingSwarmControllerComponentFields)

CCharClassBatalloonAIComponent = Object({
    **CCharClassBaseGroundShockerAIComponentFields,
    "fCallDistMaxDelayTime": common_types.Float,
    "fCallDistLimit": common_types.Float,
    "fCallRandMinDelayTime": common_types.Float,
    "fCallRandMaxDelayTime": common_types.Float,
    "fRandMinTimeForPathUpdate": common_types.Float,
    "fRandMaxTimeForPathUpdate": common_types.Float,
    "fDotNegativeMaxTimeForPathUpdate": common_types.Float,
    "fMovementShakeRadius": common_types.Float,
    "fMovementShakeInterpolationSpeed": common_types.Float,
    "fBrothersDist2Stop": common_types.Float,
})

CCharClassBasicLifeComponent = Object(CCharClassBasicLifeComponentFields := {
    **CCharClassLifeComponentFields,
    "oDamageSourceFactor": CDamageSourceFactor,
    "bDestroyOnDead": construct.Flag,
    "fInitialDamageFactor": common_types.Float,
    "fInitialDamageFactorTime": common_types.Float,
})

CCharClassChozoCommanderXLifeComponent = Object({
    **CCharClassLifeComponentFields,
    "fTimeToWin": common_types.Float,
    "fImpactedPlayRate": common_types.Float,
})

SLaunchPatternStep = Object({
    "fAngleOffsetDegs": common_types.Float,
    "fSpeed": common_types.Float,
    "fGravity": common_types.Float,
    "fTimeForNextBall": common_types.Float,
})

base_global_CRntDictionary_base_global_CStrId__SLaunchPatternStep_ = common_types.make_dict(SLaunchPatternStep)

TLaunchPattern = base_global_CRntDictionary_base_global_CStrId__SLaunchPatternStep_

SLaunchConfig = Object({
    "fCombatMinTimeBetweenBalls": common_types.Float,
    "fCombatMaxTimeBetweenBalls": common_types.Float,
    "tPattern": TLaunchPattern,
    "sName": common_types.StrId,
    "fFloorMinAngleDegs": common_types.Float,
    "fFloorMaxAngleDegs": common_types.Float,
    "fFloorMinAngleDegs2": common_types.Float,
    "fFloorMaxAngleDegs2": common_types.Float,
})

base_global_CRntDictionary_base_global_CStrId__SLaunchConfig_ = common_types.make_dict(SLaunchConfig)

TLaunchConfigs = base_global_CRntDictionary_base_global_CStrId__SLaunchConfig_


class CCharClassVulkranAIComponent_ESubspecies(enum.IntEnum):
    Vulkran = 0
    Spittail = 1
    Invalid = 2147483647


construct_CCharClassVulkranAIComponent_ESubspecies = construct.Enum(construct.Int32ul, CCharClassVulkranAIComponent_ESubspecies)

CCharClassVulkranAIComponent = Object({
    **CCharClassBehaviorTreeAIComponentFields,
    "fFrenzyTime": common_types.Float,
    "fActivationTime": common_types.Float,
    "fPatrolMinTimeBetweenBalls": common_types.Float,
    "fPatrolMaxTimeBetweenBalls": common_types.Float,
    "fCombatMinTimeBetweenBalls": common_types.Float,
    "fCombatMaxTimeBetweenBalls": common_types.Float,
    "fBallGravity": common_types.Float,
    "fLaunchUpAngleRef": common_types.Float,
    "fLaunchUpAngleLowerOffset": common_types.Float,
    "fLaunchUpAngleUpperOffset": common_types.Float,
    "fLaunchRightAngleRef": common_types.Float,
    "fLaunchLeftAngleRef": common_types.Float,
    "fLaunchSideAngleLowerOffset": common_types.Float,
    "fLaunchSideAngleUpperOffset": common_types.Float,
    "fLaunchDownAngleRef": common_types.Float,
    "bMirrorLaunchDown": construct.Flag,
    "fLaunchDownAngleLowerOffset": common_types.Float,
    "fLaunchDownAngleUpperOffset": common_types.Float,
    "fLaunchUpMinInitialSpeed": common_types.Float,
    "fLaunchUpMaxInitialSpeed": common_types.Float,
    "fLaunchSideMinInitialSpeed": common_types.Float,
    "fLaunchSideMaxInitialSpeed": common_types.Float,
    "fLaunchDownMinInitialSpeed": common_types.Float,
    "fLaunchDownMaxInitialSpeed": common_types.Float,
    "sWalkRightLaunchUpConfig": SLaunchConfig,
    "sWalkDownLaunchRightConfig": SLaunchConfig,
    "sWalkLeftLaunchDownConfig": SLaunchConfig,
    "sWalkUpLaunchLeftConfig": SLaunchConfig,
    "tLaunchConfigs": TLaunchConfigs,
    "fMinTimeBetweenAttacks": common_types.Float,
    "fMaxTimeBetweenAttacks": common_types.Float,
    "fMinTimeAttacking": common_types.Float,
    "fMaxTimeAttacking": common_types.Float,
    "fShotHeightOffset": common_types.Float,
    "fTimeInFrustumToStartAttack": common_types.Float,
    "fTimeOutOfFrustumToEndAttack": common_types.Float,
    "fMaxLOSDistanceToChasePoint": common_types.Float,
    "sMagmaBallCharClass": common_types.StrId,
    "eSubspecies": construct_CCharClassVulkranAIComponent_ESubspecies,
})

CCharClassDaivoSpitAttack = Object({
    **CCharClassAttackFields,
    "fAttackCoolDown": common_types.Float,
})

CCharClassDaivoAIComponent = Object({
    **CCharClassSluggerAIComponentFields,
    "oDaivoSpitAttackDef": CCharClassDaivoSpitAttack,
})

CCharClassHeatableShieldEnhanceWeakSpotComponent = Object({
    **CCharClassEnhanceWeakSpotComponentFields,
    "sOnWeakSpotAimedWithMask": common_types.StrId,
    "sOnWeakSpotAimedWithoutMask": common_types.StrId,
    "sOnWeakSpotNotAimedWithMask": common_types.StrId,
    "sOnWeakSpotNotAimedWithoutMask": common_types.StrId,
})

CCharClassGrappleBeamComponent = Object({
    **CCharClassWeaponMovementFields,
    "fDamage": common_types.Float,
})


class CCharClassSabotoruAIComponent_ESubspecies(enum.IntEnum):
    Sabotoru = 0
    Kreep = 1
    Invalid = 2147483647


construct_CCharClassSabotoruAIComponent_ESubspecies = construct.Enum(construct.Int32ul, CCharClassSabotoruAIComponent_ESubspecies)

CCharClassSabotoruTurnInDoorAttack = Object(CCharClassAttackFields)

CCharClassSabotoruAIComponent = Object({
    **CCharClassBehaviorTreeAIComponentFields,
    "eSubspecies": construct_CCharClassSabotoruAIComponent_ESubspecies,
    "oSabotoruTurnInDoorAttackDef": CCharClassSabotoruTurnInDoorAttack,
    "fDoorPlayRate": common_types.Float,
})

CCharClassPlatformTrapGrapplePointComponent = Object({
    **CCharClassPullableGrapplePointComponentFields,
    "sGrappleCollider": common_types.StrId,
})

CCharClassSwifterAIComponent = Object(CCharClassBehaviorTreeAIComponentFields)

CCharClassEmmyCaveAIComponent = Object(CCharClassEmmyAIComponentFields)

CCharClassInfesterBallAIComponent = Object({
    **CCharClassBehaviorTreeAIComponentFields,
    "fLifeTime": common_types.Float,
    "fExplosionRadius": common_types.Float,
    "fTimeToExplosion": common_types.Float,
    "fTimeAtMaxRadiusExplosion": common_types.Float,
    "fDamageInfesterBallExplosion": common_types.Float,
    "bChangeDirOnLand": construct.Flag,
    "fXImpulseInWallSpawn": common_types.Float,
    "bNotExplodeInWallCollision": construct.Flag,
    "iNumCollisionsToExplode": common_types.Int,
    "iNumWallCollisions": common_types.Int,
    "bExplodeInVerticalTunnelCollision": construct.Flag,
    "fTunnelImpulseFactor": common_types.Float,
    "fReboundInWallFactor": common_types.Float,
    "fReboundInGroundFactor": common_types.Float,
    "fReboundInSlopeFactor": common_types.Float,
})

CCharClassChozoCommanderSentenceSphereLifeComponent = Object(CCharClassBasicLifeComponentFields)

CCharClassObsydomithonAttack = Object({
    **CCharClassAttackFields,
    "fBlockableAttackTime": common_types.Float,
    "fBlockableAttackWarningTime": common_types.Float,
})

CCharClassObsydomithonAIComponent = Object({
    **CCharClassBehaviorTreeAIComponentFields,
    "oObsydomithonAttackDef": CCharClassObsydomithonAttack,
})

CCharClassYamplotXBiteAttack = Object(CCharClassAttackFields)

CCharClassYamplotXStepAttack = Object(CCharClassAttackFields)


class CCharClassYamplotXAIComponent_ESubspecies(enum.IntEnum):
    Yampa = 0
    YamplotX = 1
    Invalid = 2147483647


construct_CCharClassYamplotXAIComponent_ESubspecies = construct.Enum(construct.Int32ul, CCharClassYamplotXAIComponent_ESubspecies)

CCharClassYamplotXAIComponent = Object({
    **CCharClassBehaviorTreeAIComponentFields,
    "oYamplotXBiteAttackDef": CCharClassYamplotXBiteAttack,
    "oYamplotXStepAttackDef": CCharClassYamplotXStepAttack,
    "eSubspecies": construct_CCharClassYamplotXAIComponent_ESubspecies,
})

CCharClassSoundTriggerComponent = Object(CCharClassSoundTriggerComponentFields := CCharClassBaseTriggerComponentFields)

CCharClassShelmitPlasmaRayAttack = Object({
    **CCharClassAttackFields,
    "fDistanceToInitShooting": common_types.Float,
    "fDistanceToInitShootingWithGrapple": common_types.Float,
    "fMinYAimForGrappleShootDistance": common_types.Float,
    "fMaxTimeShooting": common_types.Float,
    "fMaxTrackedDistance2ReleaseTurn": common_types.Float,
    "fMaxLaunchedTime2ReleaseTurn": common_types.Float,
})

CCharClassShelmitAIComponent = Object({
    **CCharClassBehaviorTreeAIComponentFields,
    "oShelmitPlasmaRayAttackDef": CCharClassShelmitPlasmaRayAttack,
    "fMinOpenGrappleTimeAfterAttack": common_types.Float,
    "fMaxGrappledTime": common_types.Float,
    "fMinGrapplePullTimeToBreak": common_types.Float,
    "fMinPlatformRotationSpeed": common_types.Float,
    "fMaxPlatformRotationSpeed": common_types.Float,
    "fMinEntitySpeedForMinRotation": common_types.Float,
    "fMaxEntitySpeedForMaxRotation": common_types.Float,
    "fCrystalMinAlbedoEmissiveFactor": common_types.Float,
    "fCrystalMaxAlbedoEmissiveFactor": common_types.Float,
    "fTimeToDisableCrystal": common_types.Float,
    "fChargeLoopTime": common_types.Float,
    "oRegularShelmitMeleeChargeShotDropProbabilities": SDropProbabilities,
})

CCharClassBaseDamageTriggerComponent = Object(CCharClassBaseDamageTriggerComponentFields := CCharClassBaseTriggerComponentFields)


class CCharClassNailongThornsAttack_EDepthornAttackType(enum.IntEnum):
    ClassicShoot = 0
    SequenceShoot = 1
    SineWaveShoot = 2
    Invalid = 2147483647


construct_CCharClassNailongThornsAttack_EDepthornAttackType = construct.Enum(construct.Int32ul, CCharClassNailongThornsAttack_EDepthornAttackType)

CCharClassNailongThornsAttack = Object({
    **CCharClassAttackFields,
    "bAttackInIntervals": construct.Flag,
    "fIntervalMin": common_types.Float,
    "fIntervalMax": common_types.Float,
    "fRepeatAttackTimer": common_types.Float,
    "fTimeToChargeAttack": common_types.Float,
    "sProjectile": common_types.StrId,
    "fBallGravity": common_types.Float,
    "fBallInitialSpeed": common_types.Float,
    "eDepthornAttackType": construct_CCharClassNailongThornsAttack_EDepthornAttackType,
    "fTimeBetweenThornsMin": common_types.Float,
    "fTimeBetweenThornsMax": common_types.Float,
    "bUseSineWavesInSequenceShoot": construct.Flag,
    "uNumSequences": common_types.UInt,
})

CCharClassNailuggerAcidBallsAttack = Object({
    **CCharClassAttackFields,
    "fIntervalMin": common_types.Float,
    "fIntervalMax": common_types.Float,
    "fRepeatAttackTimer": common_types.Float,
    "fTimeToChargeAttack": common_types.Float,
})

CShootDCBones = Object({
    "sName": common_types.StrId,
    "tBoneNames": common_types.make_vector(common_types.StrId),
})

COffset = Object({
    "fOffset": common_types.Float,
    "sBoneName": common_types.StrId,
    "fGravity": common_types.Float,
    "fSpeed": common_types.Float,
    "fTimeToNextOffset": common_types.Float,
})

base_global_CRntDictionary_base_global_CStrId__COffset_ = common_types.make_dict(COffset)

TPatterns = base_global_CRntDictionary_base_global_CStrId__COffset_

CPattern = Object({
    "sPatternName": common_types.StrId,
    "tOffsets": TPatterns,
})

CCharClassNailongAIComponent = Object({
    **CCharClassBehaviorTreeAIComponentFields,
    "oNailongThornsAttackDef": CCharClassNailongThornsAttack,
    "oNailuggerAcidBallsAttackDef": CCharClassNailuggerAcidBallsAttack,
    "fTimeBetweenThornsAttack": common_types.Float,
    "fSteeringTargetReachDistance": common_types.Float,
    "fSteeringCloseToTargetAccel": common_types.Float,
    "fSteeringMaxDistToTurn": common_types.Float,
    "fSteeringLookAheadDistance": common_types.Float,
    "fSteeringAcceleration": common_types.Float,
    "fMaxTargetDistanceToAccelerateCloseToTarget": common_types.Float,
    "fSlowSteeringTargetReachDistance": common_types.Float,
    "fSlowSteeringCloseToTargetAccel": common_types.Float,
    "fSlowSteeringMaxDistToTurn": common_types.Float,
    "fSlowSteeringLookAheadDistance": common_types.Float,
    "fSlowSteeringAcceleration": common_types.Float,
    "fSlowMaxTargetDistanceToAccelerateCloseToTarget": common_types.Float,
    "fSlowMotionSpeed": common_types.Float,
    "tShootDCBones": common_types.make_vector(Pointer_CShootDCBones.create_construct()),
    "tLaunchConfig": common_types.make_vector(Pointer_CPattern.create_construct()),
})

CCharClassGoliathXBurstProjectionBombMovement = Object({
    **CCharClassWeaponMovementFields,
    "fExplosionRadius": common_types.Float,
    "fExplosionGrowthTime": common_types.Float,
    "fExplosionLifeTime": common_types.Float,
    "fSubExplosionLifeTime": common_types.Float,
    "fSubExplosionStepTime": common_types.Float,
    "fClosestAxisSpeedMultiplier": common_types.Float,
    "fDetonationTime": common_types.Float,
})

CCharClassRobotAIComponent = Object(CCharClassRobotAIComponentFields := {
    **CCharClassBehaviorTreeAIComponentFields,
    "sBumpedFX": common_types.StrId,
    "sDeathTimeline": common_types.StrId,
})

CCharClassCentralUnitAIComponent = Object({
    **CCharClassBehaviorTreeAIComponentFields,
    "bPlaceholder": construct.Flag,
    "sArmorLifeTunableId": common_types.StrId,
})

CCharClassScourgeTongueSlashAttack = Object({
    **CCharClassAttackFields,
    "fMinInitTime": common_types.Float,
    "fMinDistanceIfTargetOnPath": common_types.Float,
})

CTentacle = Object({
    "sName": common_types.StrId,
    "fExtraNodeLengthFactor": common_types.Float,
    "tTentacleNodes": common_types.make_vector(common_types.StrId),
    "bAllowTrail": construct.Flag,
})

CCharClassScourgeAIComponent = Object({
    **CCharClassBehaviorTreeAIComponentFields,
    "oScourgeTongueSlashAttackDef": CCharClassScourgeTongueSlashAttack,
    "oTongue": CTentacle,
    "fTentacleWidth": common_types.Float,
    "vTentacleZAxisThreshold": common_types.CVector3D,
    "fTongueCheckWidth": common_types.Float,
    "fTongueArcCheckBigWidth": common_types.Float,
    "fTongueArcCheckSmallWidth": common_types.Float,
    "fTongueScenarioCheckWidth": common_types.Float,
    "fDefaultShootOffset": common_types.Float,
    "fCrouchingShootOffset": common_types.Float,
    "fHangingAboveVerticalShootOffset": common_types.Float,
    "fHangingHorizontalShootOffset": common_types.Float,
})

CCharClassHangableGrappleMagnetSlidingBlockComponent = Object(CCharClassHangableGrappleSurfaceComponentFields)

CCharClassSoundProofTriggerComponent = Object(CCharClassBaseTriggerComponentFields)

CCharClassHecathonLifeComponent = Object(CCharClassEnemyLifeComponentFields)

CCharClassEmmyShipyardAIComponent = Object(CCharClassEmmyAIComponentFields)


class CDoorShieldLifeComponent_EDoorsShieldType(enum.IntEnum):
    MISSILE = 0
    SUPERMISSILE = 1
    POWERBOOM = 2
    PLASMA = 3
    WAVE = 4
    WIDE = 5
    Invalid = 2147483647


construct_CDoorShieldLifeComponent_EDoorsShieldType = construct.Enum(construct.Int32ul, CDoorShieldLifeComponent_EDoorsShieldType)

CCharClassDoorShieldLifeComponent = Object({
    **CCharClassItemLifeComponentFields,
    "bDisolveByMaterial": construct.Flag,
    "fTimeToStartDisolve": common_types.Float,
    "eDoorShieldType": construct_CDoorShieldLifeComponent_EDoorsShieldType,
})


class CCharClassPoisonFlyAIComponent_ESubspecies(enum.IntEnum):
    Poisonfly = 0
    Blindfly = 1
    Invalid = 2147483647


construct_CCharClassPoisonFlyAIComponent_ESubspecies = construct.Enum(construct.Int32ul, CCharClassPoisonFlyAIComponent_ESubspecies)

CCharClassPoisonFlyDiveAttack = Object({
    **CCharClassAttackFields,
    "fAttackDiveDistance": common_types.Float,
    "fAttackPreparationTime": common_types.Float,
})

CCharClassPoisonFlyAIComponent = Object({
    **CCharClassBehaviorTreeAIComponentFields,
    "eSubspecies": construct_CCharClassPoisonFlyAIComponent_ESubspecies,
    "oPoisonFlyDiveAttackDef": CCharClassPoisonFlyDiveAttack,
})

CCharClassRockDiverAIComponent = Object({
    **CCharClassBehaviorTreeAIComponentFields,
    "fCloseWingsStartDistance": common_types.Float,
})

CCharClassAutomperAutomaticIrradiationAttack = Object({
    **CCharClassAttackFields,
    "fAttackDuration": common_types.Float,
    "fChargeDuration": common_types.Float,
})

CCharClassAutomperAIComponent = Object({
    **CCharClassRobotAIComponentFields,
    "oAutomperAutomaticIrradiationAttackDef": CCharClassAutomperAutomaticIrradiationAttack,
})

CCharClassShakernautDoubleGroundShockAttack = Object({
    **CCharClassAttackFields,
    "fTimeToChargeDoubleGroundShock": common_types.Float,
    "uNumShocks": common_types.UInt,
    "fTimeBetweenShockwaves": common_types.Float,
    "fTimeToEndShockwaves": common_types.Float,
})

CCharClassShakernautPiercingLaserAttack = Object({
    **CCharClassAttackFields,
    "fTimeToChargePiercingLaser": common_types.Float,
    "fTimeToChargeSecondLaser": common_types.Float,
    "fTimeToPrepareLaser": common_types.Float,
    "fTimeLaser": common_types.Float,
    "fTimeToRelocateEye": common_types.Float,
})

CCharClassShakernautAIComponent = Object({
    **CCharClassRobotAIComponentFields,
    "oShakernautDoubleGroundShockAttackDef": CCharClassShakernautDoubleGroundShockAttack,
    "oShakernautPiercingLaserAttackDef": CCharClassShakernautPiercingLaserAttack,
    "fMaxDistToMeleeAttack": common_types.Float,
    "fTimeSinceLastRangedAttack": common_types.Float,
    "fExplosionDuration": common_types.Float,
    "fExplosionWidth": common_types.Float,
    "fExplosionHeight": common_types.Float,
})

CCharClassSclawkAIComponent = Object(CCharClassSclawkAIComponentFields := {
    **CCharClassBehaviorTreeAIComponentFields,
    "fMinHiddenTime": common_types.Float,
    "fMaxHiddenTime": common_types.Float,
    "fJumpPreparationTime": common_types.Float,
    "fJumpShortPreparationTime": common_types.Float,
})

CCharClassBossAIComponent = Object(CCharClassBossAIComponentFields := {
    **CCharClassBehaviorTreeAIComponentFields,
    "bUseIsInFrustumForBossCamera": construct.Flag,
    "bUseAngry": construct.Flag,
    "bManuallyRemoveFromTeamManager": construct.Flag,
    "bWantsLifeFeedback": construct.Flag,
    "bRemovePlayerInputOnDeath": construct.Flag,
    "bSetPlayerInvulnerableWithReactionOnDeath": construct.Flag,
    "bOpenDoorWhenDie": construct.Flag,
    "sBossBattleLabel": common_types.StrId,
    "sInventoryItemOnKilled": common_types.StrId,
    "bCheckOrientationInGrab": construct.Flag,
    "bPersistenBossDefeatedPushSetup": construct.Flag,
    "bGiveInventoryItemOnDead": construct.Flag,
})


class EAIAnimationStates(enum.IntEnum):
    NONE = 0
    Idle = 1
    Walking = 2
    WalkingWall = 3
    WalkingCeil = 4
    Flying = 5
    Side = 6
    Invalid = 2147483647


construct_EAIAnimationStates = construct.Enum(construct.Int32ul, EAIAnimationStates)


class CCharClassEnemyMovement_ETurn180Mode(enum.IntEnum):
    AxisX = 0
    AxisY = 1
    Dot = 2
    Invalid = 2147483647


construct_CCharClassEnemyMovement_ETurn180Mode = construct.Enum(construct.Int32ul, CCharClassEnemyMovement_ETurn180Mode)


class EAnimationTag(enum.IntEnum):
    slope = 0
    stealth = 1
    left = 2
    right = 3
    shield = 4
    hiddenshield = 5
    attack = 6
    stage2 = 7
    super = 8
    low = 9
    preseta = 10
    presetb = 11
    presetc = 12
    chozowarriorx_powerbomb = 13
    slope26up = 14


construct_EAnimationTag = construct.Enum(construct.Int32ul, EAnimationTag)

CCharClassEnemyMovement = Object(CCharClassEnemyMovementFields := {
    **CCharClassCharacterMovementFields,
    "bCanFall": construct.Flag,
    "bShouldMakeExtraMove": construct.Flag,
    "eInitialState": construct_EAIAnimationStates,
    "eTurn180Mode": construct_CCharClassEnemyMovement_ETurn180Mode,
    "sIdleAnim": common_types.StrId,
    "sWalkingRelaxAnim": common_types.StrId,
    "sWalkingFrontAnim": common_types.StrId,
    "sWalkingBackAnim": common_types.StrId,
    "sWalkingFrontInitAnim": common_types.StrId,
    "sWalkingBackInitAnim": common_types.StrId,
    "sWalkingFrontEndAnim": common_types.StrId,
    "sWalkingBackEndAnim": common_types.StrId,
    "sFlyingRelaxAnim": common_types.StrId,
    "sFlyingFrontAnim": common_types.StrId,
    "sFlyingBackAnim": common_types.StrId,
    "sFlyingUpAnim": common_types.StrId,
    "sFlyingDownAnim": common_types.StrId,
    "sFlyingFrontInitAnim": common_types.StrId,
    "sFlyingBackInitAnim": common_types.StrId,
    "sFlyingUpInitAnim": common_types.StrId,
    "sFlyingDownInitAnim": common_types.StrId,
    "sFlyingFrontEndAnim": common_types.StrId,
    "sFlyingBackEndAnim": common_types.StrId,
    "sFlyingUpEndAnim": common_types.StrId,
    "sFlyingDownEndAnim": common_types.StrId,
    "fFlyingStateChangeBlendTime": common_types.Float,
    "fFlyingUpStartAng": common_types.Float,
    "fFlyingDownStartAng": common_types.Float,
    "sSideRelaxAnim": common_types.StrId,
    "sSideWalkAnim": common_types.StrId,
    "sSideWalkInitAnim": common_types.StrId,
    "eSideLeftTag": construct_EAnimationTag,
    "eSideRightTag": construct_EAnimationTag,
    "iNumScenarioCollisionSteps": common_types.Int,
    "bOnLastCollisionStepHitResetTickVelocities": construct.Flag,
    "bUseCurrentScenarioCollisionScene": construct.Flag,
    "bRotateWhenMoving": construct.Flag,
    "fMinSpeedToRotate": common_types.Float,
    "fMaxSpeedToRotate": common_types.Float,
    "fMaxAngleRotationY": common_types.Float,
    "fDefaultAngleRotationY": common_types.Float,
    "fMaxAngleRotationZ": common_types.Float,
    "fDefaultAngleRotationZ": common_types.Float,
    "fSpeedToRotateFallingFromPath": common_types.Float,
    "sWalkUpAnim": common_types.StrId,
    "fWalkUpExitBlend": common_types.Float,
    "sWalkDownAnim": common_types.StrId,
    "fWalkDownExitBlend": common_types.Float,
    "fStickyDistanceToAnticipateCornerAnim": common_types.Float,
    "fStickyDistanceToQuitCornerAnim": common_types.Float,
    "bUseDistanceModeToChangeCornerAnim": construct.Flag,
    "bSynchronizeUpAnim": construct.Flag,
    "bSynchronizeDownAnim": construct.Flag,
    "fFlyingAngleAccumulativeInterpolationSpeedFactor": common_types.Float,
    "bUseFlyingAngleAccumulativeInterpolationSpeedFactor": construct.Flag,
    "bInPathMode": construct.Flag,
    "fMaxDistanceToExecuteRule": common_types.Float,
    "bUseBreakableTileBlockerCollidersOnSmartLink": construct.Flag,
    "fSupportedOnFloorTolerance": common_types.Float,
    "bBipedMode": construct.Flag,
    "bIgnoreOpenCorner": construct.Flag,
    "bRelocateOnFrozen": construct.Flag,
    "bForceNextTransformCharClassScale": construct.Flag,
    "fAngularSpeed": common_types.Float,
    "fSteeringAcceleration": common_types.Float,
    "fMaxTargetDistanceToAccelerateCloseToTarget": common_types.Float,
    "fCloseToTargetAcceleration": common_types.Float,
    "bLookAtHorizontalDir": construct.Flag,
})

CCharClassTakumakuDashAttack = Object(CCharClassAttackFields)


class CCharClassTakumakuAIComponent_ESubspecies(enum.IntEnum):
    Takumaku = 0
    Armadigger = 1
    Klaida = 2
    Invalid = 2147483647


construct_CCharClassTakumakuAIComponent_ESubspecies = construct.Enum(construct.Int32ul, CCharClassTakumakuAIComponent_ESubspecies)

CCharClassTakumakuAIComponent = Object({
    **CCharClassBehaviorTreeAIComponentFields,
    "oTakumakuDashAttackDef": CCharClassTakumakuDashAttack,
    "eSubspecies": construct_CCharClassTakumakuAIComponent_ESubspecies,
    "fMinTimeBetweenDigs": common_types.Float,
    "fMaxTimeBetweenDigs": common_types.Float,
    "fMinTimeDigging": common_types.Float,
    "fMaxTimeDigging": common_types.Float,
    "fReachableHeightBeforeAttack": common_types.Float,
    "fReachableHeightOnAttack": common_types.Float,
    "fSpikeTime": common_types.Float,
    "fSpikeActivationInterpolationSpeed": common_types.Float,
    "fSpikeDeactivationInterpolationSpeed": common_types.Float,
    "fSpikeShakeActivationInterpolationSpeed": common_types.Float,
    "fSpikeShakeDeactivationInterpolationSpeed": common_types.Float,
    "fMinChaseDistance": common_types.Float,
    "fMaxChaseDistance": common_types.Float,
    "iChaseMaxNumJumps": common_types.Int,
    "fMinChargeTime": common_types.Float,
    "bWantsAttackPreparationAfterMelee": construct.Flag,
    "bWantsAttackPreparationAfterDetection": construct.Flag,
    "fMaxTargetSeparationBehindToTurn": common_types.Float,
    "fMaxTimeDetectingBehindToTurn": common_types.Float,
    "fMaxTimeMissingToStop": common_types.Float,
})

CCharClassShootActivatorComponent = Object(CCharClassShootActivatorComponentFields := {
    **CCharClassItemLifeComponentFields,
    "fActivationTime": common_types.Float,
    "fTimePerShot": common_types.Float,
})

CCharClassWeightActivableMovablePlatformComponent = Object({
    **CCharClassMovablePlatformComponentFields,
    "sActionOnActivated": common_types.StrId,
})

CCharClassEmmyProtoAIComponent = Object(CCharClassEmmyAIComponentFields)

CCharClassFanComponent = Object({
    **CCharClassBaseTriggerComponentFields,
    "sFX_wind": common_types.StrId,
    "sFX_hurricane": common_types.StrId,
})

CCharClassEmmyLabAIComponent = Object(CCharClassEmmyAIComponentFields)

CCharClassKraidSpikeMovablePlatformComponent = Object({
    **CCharClassMovablePlatformComponentFields,
    "fInitialMotionSpeed": common_types.Float,
    "fMotionSpeed": common_types.Float,
    "fInitialDisplacement": common_types.Float,
    "fPreparationTime": common_types.Float,
    "fShakeDisplacementX": common_types.Float,
    "fShakeSpeedX": common_types.Float,
    "fShakeDisplacementY": common_types.Float,
    "fShakeSpeedY": common_types.Float,
    "fFlyingSpikeStickedWallTime": common_types.Float,
})


class CCharClassProjectileMovement_EProjectileMeleeHitReaction(enum.IntEnum):
    IMPACT = 0
    IMPACT_ATTACKER = 1
    NONE = 2
    Invalid = 2147483647


construct_CCharClassProjectileMovement_EProjectileMeleeHitReaction = construct.Enum(construct.Int32ul, CCharClassProjectileMovement_EProjectileMeleeHitReaction)

CCharClassProjectileMovement = Object(CCharClassProjectileMovementFields := {
    **CCharClassWeaponMovementFields,
    "sCameraFXPresetOnImpact": common_types.StrId,
    "bUseCheckBeforeCast": construct.Flag,
    "fGravity": common_types.Float,
    "bApplyGravityOnInitialSpeed": construct.Flag,
    "sColliderToCheckCollisions": common_types.StrId,
    "sColliderToCheckDamage": common_types.StrId,
    "bDeleteAfterCollisionProcessed": construct.Flag,
    "bAddOwnerVelocityOnBeginPlay": construct.Flag,
    "fOwnerVelocityFactor": common_types.Float,
    "fVelocityHorizontalFriction": common_types.Float,
    "fVelocityVerticalFriction": common_types.Float,
    "bDestroyOnImpactSpeedBooster": construct.Flag,
    "bIgnoreInvulnerableEntities": construct.Flag,
    "eDefaultProjectileMeleeHitReaction": construct_CCharClassProjectileMovement_EProjectileMeleeHitReaction,
    "bAutoCalculateSpeedForParabola": construct.Flag,
    "bIgnoreMovementOnCollision": construct.Flag,
})

CCharClassBaseBigFistAIComponent = Object(CCharClassBaseBigFistAIComponentFields := {
    **CCharClassBossAIComponentFields,
    "fMaxHeightAttackBehindDist": common_types.Float,
    "fMaxHeightAttackFrontalDist": common_types.Float,
})

CCharClassKraidShockerSplashMovementComponent = Object(CCharClassProjectileMovementFields)

CCharClassChozoWarriorXSpitMovementComponent = Object(CCharClassProjectileMovementFields)

CCharClassHydrogigaAttack = Object(CCharClassHydrogigaAttackFields := CCharClassAttackFields)

CCharClassHydrogigaBraidAttack = Object({
    **CCharClassHydrogigaAttackFields,
    "fPrepareTime": common_types.Float,
    "fHitTime": common_types.Float,
})

CCharClassHydrogigaMaelstormAttack = Object(CCharClassHydrogigaAttackFields)

CPolypFallPattern = Object({
    "fFarSpeed": common_types.Float,
    "fMiddleSpeed": common_types.Float,
    "CloseSpeed": common_types.Float,
})

CCharClassHydrogigaPolypsAttack = Object({
    **CCharClassHydrogigaAttackFields,
    "iAttackPattern": common_types.Int,
    "fTimeBetweenWaves": common_types.Float,
    "uMinNumWaves": common_types.UInt,
    "uMaxNumWaves": common_types.UInt,
    "tUnbreakableFarPatterns": common_types.make_vector(Pointer_CPolypFallPattern.create_construct()),
    "tUnbreakableMiddlePatterns": common_types.make_vector(Pointer_CPolypFallPattern.create_construct()),
    "tUnbreakableClosePatterns": common_types.make_vector(Pointer_CPolypFallPattern.create_construct()),
})

CCharClassHydrogigaTentacleBashAttack = Object(CCharClassHydrogigaAttackFields)

CCharClassHydrogigaTongueSwirlAttack = Object(CCharClassHydrogigaAttackFields)

CCharClassHydrogigaAIComponent = Object({
    **CCharClassBossAIComponentFields,
    "tTentacles": common_types.make_vector(Pointer_CTentacle.create_construct()),
    "oHydrogigaBraidAttackDef": CCharClassHydrogigaBraidAttack,
    "oHydrogigaMaelstormAttackDef": CCharClassHydrogigaMaelstormAttack,
    "oHydrogigaPolypsAttackDef": CCharClassHydrogigaPolypsAttack,
    "oHydrogigaTentacleBashAttackDef": CCharClassHydrogigaTentacleBashAttack,
    "oHydrogigaTongueSwirlAttackDef": CCharClassHydrogigaTongueSwirlAttack,
    "fTimeOpened": common_types.Float,
    "fTimeDry": common_types.Float,
    "fTimeStunned": common_types.Float,
    "fUnderwaterZipLineMultiplier": common_types.Float,
    "fTurbineRestoreTime": common_types.Float,
    "bMeleeDestroyPolyps": construct.Flag,
    "fMaxDamageDry": common_types.Float,
    "fMaxDamageStunned": common_types.Float,
    "fDamageStage2": common_types.Float,
    "fDamageFactorFillingPool": common_types.Float,
    "oDamageSourceFactorClose": CDamageSourceFactor,
    "oDamageSourceFactorOpen": CDamageSourceFactor,
    "oDamageSourceFactorDry": CDamageSourceFactor,
    "oDamageSourceFactorPolyps": CDamageSourceFactor,
})

CCharClassAutsniperShootAttack = Object({
    **CCharClassAttackFields,
    "fTimeToReload": common_types.Float,
    "fTimeToChargeRay": common_types.Float,
    "fTimeToUnchargeRay": common_types.Float,
    "fTimeToRelocateCannon": common_types.Float,
    "fTimeBeforeShoot": common_types.Float,
    "fTimeAfterShoot": common_types.Float,
    "fMaxPitch": common_types.Float,
    "fMinPitch": common_types.Float,
    "fMaxVolume": common_types.Float,
    "fMinVolume": common_types.Float,
    "fTimeCannonLocked": common_types.Float,
    "fTimeToGoPatrol": common_types.Float,
    "fTimeToLoseTarget": common_types.Float,
    "fDistToStopCloseToTarget": common_types.Float,
    "fTimeBeforeBlockeableWarning": common_types.Float,
    "fTimeAfterBlockeableWarning": common_types.Float,
})

CCharClassAutsniperAIComponent = Object({
    **CCharClassRobotAIComponentFields,
    "oAutsniperShootAttackDef": CCharClassAutsniperShootAttack,
    "fTimeToChangeLayer": common_types.Float,
    "fMovementFactor": common_types.Float,
})

CCharClassGroundShockerAttack = Object(CCharClassAttackFields)

CCharClassGroundShockerAIComponent = Object({
    **CCharClassBaseGroundShockerAIComponentFields,
    "oGroundShockerAttackDef": CCharClassGroundShockerAttack,
})

CCharClassChozoCommanderEnergyShardsFragmentMovementComponent = Object(CCharClassProjectileMovementFields)

CCharClassInfesterBallMovementComponent = Object(CCharClassProjectileMovementFields)

CCharClassAreaSoundComponent = Object({
    **CCharClassSoundTriggerComponentFields,
    "bOverrideDisableInEditor": construct.Flag,
})

CCharClassNailuggerAcidBallMovementComponent = Object(CCharClassProjectileMovementFields)

CCharClassAutsharpAIComponent = Object({
    **CCharClassRobotAIComponentFields,
    "fExplosionRadius": common_types.Float,
    "fTimeToExplosion": common_types.Float,
    "fTimeAtMaxRadiusExplosion": common_types.Float,
    "fDamageAutsharpExplosion": common_types.Float,
    "fTimeToPrepareExplosion": common_types.Float,
    "fRotationAccelTime": common_types.Float,
    "fRotationMultiplier": common_types.Float,
    "fAccelIncrementation": common_types.Float,
    "fTimeToDecelerate": common_types.Float,
    "fJumpUpImpulse": common_types.Float,
    "fJumpFrontImpulse": common_types.Float,
    "bIncrementRotationInJump": construct.Flag,
})

CCharClassScorpiusPoisonousSpitMovementComponent = Object(CCharClassProjectileMovementFields)

CCharClassCooldownXBossWeakPointLifeComponent = Object(CCharClassBasicLifeComponentFields)

CChozoRobotSoldierCannonShotPattern = Object({
    "fInitialTimeToShot": common_types.Float,
    "fTimeBetweenShot_1_2": common_types.Float,
    "fTimeBetweenShot_2_3": common_types.Float,
})

CCharClassChozoRobotSoldierCannonShotAttack = Object({
    **CCharClassAttackFields,
    "tPatterns": common_types.make_vector(Pointer_CChozoRobotSoldierCannonShotPattern.create_construct()),
})

CCharClassChozoRobotSoldierDashSlashAttack = Object(CCharClassAttackFields)

CCharClassChozoRobotSoldierDisruptionFieldAttack = Object(CCharClassAttackFields)

CCharClassChozoRobotSoldierUppercutAttack = Object({
    **CCharClassAttackFields,
    "fTraveledMaxDistanceToAddToMaxDistance": common_types.Float,
    "fDistanceToReachableTarget": common_types.Float,
    "fDistanceToReachableTargetMB": common_types.Float,
    "fDistanceToNonReachableTarget": common_types.Float,
    "fDistanceToLaunchEnd4m": common_types.Float,
})

CEnemyMovementWalkingAnims = Object({
    "sRelaxAnim": common_types.StrId,
    "sFrontAnim": common_types.StrId,
    "sBackAnim": common_types.StrId,
    "sFrontInitAnim": common_types.StrId,
    "sBackInitAnim": common_types.StrId,
    "sFrontEndAnim": common_types.StrId,
    "sBackEndAnim": common_types.StrId,
})

querysystem_CFilter = Object(querysystem_CFilterFields := {
    "bNegate": construct.Flag,
})

querysystem_CEvaluator = Object(querysystem_CEvaluatorFields := {
    "fWeight": common_types.Float,
    "sFunction": common_types.StrId,
})

querysystem_CQuerySystemDef = Object({
    "tFilters": common_types.make_vector(Pointer_querysystem_CFilter.create_construct()),
    "tEvaluators": common_types.make_vector(Pointer_querysystem_CEvaluator.create_construct()),
})

CCharClassChozoRobotSoldierAIComponent = Object({
    **CCharClassBossAIComponentFields,
    "oChozoRobotSoldierCannonShotAttackDef": CCharClassChozoRobotSoldierCannonShotAttack,
    "oChozoRobotSoldierDashSlashAttackDef": CCharClassChozoRobotSoldierDashSlashAttack,
    "oChozoRobotSoldierDisruptionFieldAttackDef": CCharClassChozoRobotSoldierDisruptionFieldAttack,
    "oChozoRobotSoldierUppercutAttackDef": CCharClassChozoRobotSoldierUppercutAttack,
    "oRunningAnims": CEnemyMovementWalkingAnims,
    "oShootingPositionQuerySystemDef": querysystem_CQuerySystemDef,
    "oSelectedShootingPositionQuerySystemDef": querysystem_CQuerySystemDef,
    "oNoPathFoundShootingPositionQuerySystemDef": querysystem_CQuerySystemDef,
    "oDamageSourceFactorElite": CDamageSourceFactor,
    "oDamageSourceFactorCrazy": CDamageSourceFactor,
    "oDamageSourceFactorCrazyElite": CDamageSourceFactor,
})

CCharClassFulmiteBellyMineMovementComponent = Object(CCharClassProjectileMovementFields)

CCharClassDoorLifeComponent = Object(CCharClassDoorLifeComponentFields := {
    **CCharClassItemLifeComponentFields,
    "fMinTimeClosed": common_types.Float,
    "fMaxDistanceOpened": common_types.Float,
    "bUsesPresenceDetection": construct.Flag,
    "bPresenceOpenEnabled": construct.Flag,
    "bUseDoorLockOnLocked": construct.Flag,
    "vDefaultLightColor": common_types.CVector4D,
    "vBlockLightColor": common_types.CVector4D,
    "bVerticalDimensionInFrustum": construct.Flag,
    "bHorizontalDimensionInFrustum": construct.Flag,
    "bUseHeatDeviceActivation": construct.Flag,
    "bStartOpened": construct.Flag,
})

CCharClassCooldownXBossAttack = Object(CCharClassCooldownXBossAttackFields := {
    **CCharClassAttackFields,
    "fLaserWidth": common_types.Float,
    "sStartLavaTL": common_types.StrId,
    "sEndLavaTL": common_types.StrId,
})


class ELavaCarpetState(enum.IntEnum):
    Init = 0
    ShotInit = 1
    Shot = 2
    StopShot = 3
    Breathe = 4
    End = 5
    Invalid = 2147483647


construct_ELavaCarpetState = construct.Enum(construct.Int32ul, ELavaCarpetState)

CCooldownXBossLavaCarpetDef = Object({
    "eState": construct_ELavaCarpetState,
    "fWidth": common_types.Float,
    "fTime": common_types.Float,
    "fPlayRateFactor": common_types.Float,
    "bChangeDirection": construct.Flag,
})

CCharClassCooldownXBossLavaCarpetAttack = Object({
    **CCharClassCooldownXBossAttackFields,
    "tPatterns": common_types.make_vector(common_types.make_vector(Pointer_CCooldownXBossLavaCarpetDef.create_construct())),
    "fBreatheSpeedFactor": common_types.Float,
    "fTimeToPuddleDamage": common_types.Float,
})


class ELavaDropArmPos(enum.IntEnum):
    A = 0
    B = 1
    Invalid = 2147483647


construct_ELavaDropArmPos = construct.Enum(construct.Int32ul, ELavaDropArmPos)


class ELavaDropArm(enum.IntEnum):
    LeftUp = 0
    LeftDown = 1
    RightUp = 2
    RightDown = 3
    Invalid = 2147483647


construct_ELavaDropArm = construct.Enum(construct.Int32ul, ELavaDropArm)

CCooldownXBossLavaDropsMovementDef = Object({
    "eArmToChange": construct_ELavaDropArm,
    "fDelay": common_types.Float,
    "fAnimSpeed": common_types.Float,
})

CCooldownXBossLavaDropsDef = Object({
    "eLeftUpArmPos": construct_ELavaDropArmPos,
    "eLeftDownArmPos": construct_ELavaDropArmPos,
    "eRightUpArmPos": construct_ELavaDropArmPos,
    "eRightDownArmPos": construct_ELavaDropArmPos,
    "tActions": common_types.make_vector(CCooldownXBossLavaDropsMovementDef),
})

CCharClassCooldownXBossLavaDropsAttack = Object({
    **CCharClassCooldownXBossAttackFields,
    "fTimeInit": common_types.Float,
    "fTimeBetweenShots": common_types.Float,
    "fTimeLocked": common_types.Float,
    "fShotPreparationTime": common_types.Float,
    "fShotTime": common_types.Float,
    "fDamageRadius": common_types.Float,
    "fAimSpeed": common_types.Float,
    "fAimMinSpeed": common_types.Float,
    "fAimMaxSpeed": common_types.Float,
    "fAimMaxSpeedMaxDistance": common_types.Float,
    "tInitialState": CCooldownXBossLavaDropsDef,
    "tPatterns": common_types.make_vector(Pointer_CCooldownXBossLavaDropsDef.create_construct()),
})

CCharClassCooldownXBossReaperAttack = Object(CCharClassCooldownXBossAttackFields)

CCharClassCooldownXBossStrongWhipAttack = Object({
    **CCharClassCooldownXBossAttackFields,
    "fLoopTimeout": common_types.Float,
})

CCooldownXBossFireBallDef = Object({
    "bEnabled": construct.Flag,
    "fPreparationTimeOffset": common_types.Float,
    "bBreakable": construct.Flag,
})

CCooldownXBossFireWallDef = Object({
    "tFireBalls": common_types.make_vector(CCooldownXBossFireBallDef),
    "fDelay": common_types.Float,
    "fHorizontalOffset": common_types.Float,
    "bSpawnWallDamage": construct.Flag,
    "bStartWind": construct.Flag,
    "bStartStun": construct.Flag,
})

CCharClassCooldownXBossWindTunnelAttack = Object({
    **CCharClassCooldownXBossAttackFields,
    "sEndAttackAnim": common_types.StrId,
    "sShotAttackAnim": common_types.StrId,
    "sStunAttackAnim": common_types.StrId,
    "iNumShots": common_types.Int,
    "fTimeToEndAttack": common_types.Float,
    "tLaunchPatterns": common_types.make_vector(common_types.make_vector(Pointer_CCooldownXBossFireWallDef.create_construct())),
})

CCharClassCooldownXBossLaserBiteAttack = Object({
    **CCharClassCooldownXBossAttackFields,
    "fLoopTimeout": common_types.Float,
    "fDistanceToLaunchAttackIfImpacted": common_types.Float,
})

CCharClassCooldownXBossAIComponent = Object({
    **CCharClassBossAIComponentFields,
    "oCooldownXBossLavaCarpetAttackDef": CCharClassCooldownXBossLavaCarpetAttack,
    "oCooldownXBossLavaDropsAttackDef": CCharClassCooldownXBossLavaDropsAttack,
    "oCooldownXBossReaperAttackDef": CCharClassCooldownXBossReaperAttack,
    "oCooldownXBossStrongWhipAttackDef": CCharClassCooldownXBossStrongWhipAttack,
    "oCooldownXBossWindTunnelAttackDef": CCharClassCooldownXBossWindTunnelAttack,
    "oCooldownXBossLaserBiteAttackDef": CCharClassCooldownXBossLaserBiteAttack,
    "tTentacles": common_types.make_vector(Pointer_CTentacle.create_construct()),
    "fMinTimeToRelaxAction": common_types.Float,
    "fMaxTimeToRelaxAction": common_types.Float,
    "fTimeToGoToPhase3After4WPDestroyed": common_types.Float,
    "oGrabDamageSourceFactor": CDamageSourceFactor,
})

CCharClassMissileMovement = Object(CCharClassMissileMovementFields := {
    **CCharClassProjectileMovementFields,
    "fInitialSpeed": common_types.Float,
    "fTimeInInitialSpeed": common_types.Float,
    "fTimeToReachSpeed": common_types.Float,
})

CCharClassEmmyWaveMovementComponent = Object(CCharClassProjectileMovementFields)

CCharClassDoorCentralUnitLifeComponent = Object(CCharClassDoorLifeComponentFields)

CCharClassAutoolAIComponent = Object(CCharClassRobotAIComponentFields)

CCharClassShootActivatorHidrogigaComponent = Object(CCharClassShootActivatorComponentFields)

CCharClassCoreXAIComponent = Object({
    **CCharClassBossAIComponentFields,
    "fAcceleration": common_types.Float,
    "fTurningAcceleration": common_types.Float,
    "fMaxTurningAngle": common_types.Float,
    "fBrakeDistance": common_types.Float,
    "fMinBrakeSpeed": common_types.Float,
    "sBrakeCurve": common_types.StrId,
    "fImpactSpeed": common_types.Float,
    "fImpactTime": common_types.Float,
    "fImpactInvulnerableTime": common_types.Float,
    "fXParasiteDropCooldownTime": common_types.Float,
    "iXParasiteMinDrop": common_types.Int,
    "iXParasiteMaxDrop": common_types.Int,
    "sInventoryItemOnBigXAbsorbed": common_types.StrId,
})

CCharClassDamageTriggerComponent = Object({
    **CCharClassBaseDamageTriggerComponentFields,
    "fDamagePerTime": common_types.Float,
    "sDamagePerTime": common_types.StrId,
    "fInBetweenDamageTime": common_types.Float,
    "fInitTimeDamageIncrease": common_types.Float,
    "fDamageIncreaseAmount": common_types.Float,
    "fMaxDamage": common_types.Float,
    "sDamageSource": common_types.StrId,
    "sDamageID": common_types.StrId,
    "bIgnoreReaction": construct.Flag,
    "bContinuousDamageHit": construct.Flag,
    "eForceDamageModeHit": construct_EForcedDamageMode,
})

CCharClassChozoRobotSoldierBeamMovementComponent = Object({
    **CCharClassProjectileMovementFields,
    "fChargedSpeed": common_types.Float,
})

CCharClassSteamJetComponent = Object({
    **CCharClassBaseDamageTriggerComponentFields,
    "fDefaultDamage": common_types.Float,
    "sFX_init": common_types.StrId,
    "sFX_end": common_types.StrId,
    "sFX_1_1": common_types.StrId,
    "sFX_1_2": common_types.StrId,
    "sFX_1_3": common_types.StrId,
    "sFX_1_4": common_types.StrId,
    "sFX_1_5": common_types.StrId,
    "bSteamOnly": construct.Flag,
})

CCharClassQuetzoaChargeAttack = Object(CCharClassAttackFields)

CCharClassQuetzoaEnergyWaveAttack = Object(CCharClassAttackFields)


class CCharClassQuetzoaAIComponent_ESubspecies(enum.IntEnum):
    Quetzoa = 0
    Quetshocker = 1
    Invalid = 2147483647


construct_CCharClassQuetzoaAIComponent_ESubspecies = construct.Enum(construct.Int32ul, CCharClassQuetzoaAIComponent_ESubspecies)

CCharClassQuetzoaAIComponent = Object(CCharClassQuetzoaAIComponentFields := {
    **CCharClassBossAIComponentFields,
    "oQuetzoaChargeAttackDef": CCharClassQuetzoaChargeAttack,
    "oQuetzoaEnergyWaveAttackDef": CCharClassQuetzoaEnergyWaveAttack,
    "eSubspecies": construct_CCharClassQuetzoaAIComponent_ESubspecies,
})

CCharClassRodomithonXAIComponent_TVFirePillarConfigs = Object(intFields)

CCharClassRodomithonXSuckAttack = Object(CCharClassRodotukSuckAttackFields)

CCharClassRodomithonXAIComponent = Object({
    **CCharClassRodotukAIComponentFields,
    "fFireActiveTime": common_types.Float,
    "fRestTime": common_types.Float,
    "vFirePillarConfigs": CCharClassRodomithonXAIComponent_TVFirePillarConfigs,
    "oRodomithonXSuckAttackDef": CCharClassRodomithonXSuckAttack,
})

CCharClassNailongThornMovementComponent = Object({
    **CCharClassProjectileMovementFields,
    "fAmplitude": common_types.Float,
    "fFrequency": common_types.Float,
})

CCharClassSunnapAIComponent = Object(CCharClassRodotukAIComponentFields)

CCharClassPlayerMovement = Object(CCharClassPlayerMovementFields := {
    **CCharClassCharacterMovementFields,
    "sFrozenStartTimeline": common_types.StrId,
    "sFrozenStopTimeline": common_types.StrId,
    "sFrozenGroundTimeline": common_types.StrId,
    "sFrozenImpactTimeline": common_types.StrId,
    "sFrozenRestoreTimeline": common_types.StrId,
})

CCharClassVulkranMagmaBallMovementComponent = Object(CCharClassVulkranMagmaBallMovementComponentFields := CCharClassProjectileMovementFields)

CCharClassBigkranXMagmaRainAttack = Object({
    **CCharClassAttackFields,
    "fTimeAttacking": common_types.Float,
    "fTargetBehindMaxTime": common_types.Float,
    "fTargetAheadMaxDistance": common_types.Float,
    "fTargetBehindMaxDistance": common_types.Float,
    "fChargeLoopFarDistance": common_types.Float,
    "fChargeLoopFarDistance2": common_types.Float,
})

SBigkranXSpitLaunchPatternStep = Object({
    "fHorizontalOffset": common_types.Float,
    "fVerticalOffset": common_types.Float,
    "fTimeForNextBall": common_types.Float,
})

base_global_CRntDictionary_base_global_CStrId__SBigkranXSpitLaunchPatternStep_ = common_types.make_dict(SBigkranXSpitLaunchPatternStep)

TBigkranXSpitLaunchPattern = base_global_CRntDictionary_base_global_CStrId__SBigkranXSpitLaunchPatternStep_

SBigkranXSpitLaunchConfig = Object({
    "tPattern": TBigkranXSpitLaunchPattern,
    "sName": common_types.StrId,
})

CCharClassBigkranXSpitAttack = Object({
    **CCharClassAttackFields,
    "fTimeAttacking": common_types.Float,
    "fTargetBehindMaxTime": common_types.Float,
    "fTargetAheadMaxDistance": common_types.Float,
    "fTargetBehindMaxDistance": common_types.Float,
    "fTimeOutOfFrustumToAbortAttack": common_types.Float,
    "fBallGravity": common_types.Float,
    "fBallTrajectoryCheckRadius": common_types.Float,
    "fTrajectorySampleTimeInterval": common_types.Float,
    "fMaxHitVerticalSpeed": common_types.Float,
    "fBallDefaultLaunchAngleDegs": common_types.Float,
    "fBallLaunchSpeed": common_types.Float,
    "fBallMinLaunchAngleDegs": common_types.Float,
    "fBallMaxLaunchAngleDegs": common_types.Float,
    "fHighLaunchFixedAngleDegs": common_types.Float,
    "fHighLaunchMinSpeed": common_types.Float,
    "fHighLaunchMaxSpeed": common_types.Float,
    "fMediumLaunchFixedAngleDegs": common_types.Float,
    "fMediumLaunchMinSpeed": common_types.Float,
    "fMediumLaunchMaxSpeed": common_types.Float,
    "fLowLaunchFixedAngleDegs": common_types.Float,
    "fLowLaunchMinSpeed": common_types.Float,
    "fLowLaunchMaxSpeed": common_types.Float,
    "oOffsetPatternConfig": SBigkranXSpitLaunchConfig,
})

CCharClassBigkranXAIComponent = Object({
    **CCharClassBaseBigFistAIComponentFields,
    "oBigkranXMagmaRainAttackDef": CCharClassBigkranXMagmaRainAttack,
    "oBigkranXSpitAttackDef": CCharClassBigkranXSpitAttack,
    "sLaunchConfig": SLaunchConfig,
    "sLaunchConfig2": SLaunchConfig,
    "sLaunchConfig3": SLaunchConfig,
    "fMaxDistance1": common_types.Float,
    "fMaxDistance2": common_types.Float,
    "sMagmaBallCharClass": common_types.StrId,
    "fShotHeightOffset": common_types.Float,
    "fReachableHeightBeforeAttack": common_types.Float,
    "fReachableHeightOnAttack": common_types.Float,
    "fTimeBeforeWarningAttack": common_types.Float,
})

CCharClassKraidBouncingCreaturesMovementComponent = Object({
    **CCharClassProjectileMovementFields,
    "fRotationFactor": common_types.Float,
})

CCharClassGoliathAttack = Object(CCharClassGoliathAttackFields := {
    **CCharClassAttackFields,
    "fPostAttackLoopDuration": common_types.Float,
})

CCharClassGoliathAIComponent = Object(CCharClassGoliathAIComponentFields := {
    **CCharClassBaseBigFistAIComponentFields,
    "oGoliathAttackDef": CCharClassGoliathAttack,
    "fAnimSpeedMultiplier": common_types.Float,
})

CCharClassMorphBallMovement = Object({
    **CCharClassPlayerMovementFields,
    "fSlopeExitFrictionFactorTime": common_types.Float,
    "fSlopeExitFrictionFactor": common_types.Float,
    "sSlopeAccelerationFunction": common_types.StrId,
    "fSlopeTimeToAccelerate": common_types.Float,
    "fSlopeMinImpulse": common_types.Float,
    "fSlopeMaxImpulse": common_types.Float,
    "sMovementAudioPreset": common_types.StrId,
    "fInitialSpeedDiffDecrease": common_types.Float,
    "fMaxInitialSpeedDiff": common_types.Float,
    "fOnAirImpulseFactor": common_types.Float,
    "fXImpulseStrenght": common_types.Float,
})

CCharClassSamusMovement = Object({
    **CCharClassPlayerMovementFields,
    "fMinTimeToSpaceJump": common_types.Float,
    "fMinTimeToDoubleJump": common_types.Float,
    "sFallOilFX": common_types.StrId,
    "fRunningImpulseX": common_types.Float,
    "fImpulseY": common_types.Float,
    "fHighJumpBootImpulseY": common_types.Float,
    "fMinImpulseY": common_types.Float,
    "fMaxImpulseY": common_types.Float,
    "fChangeDirectionOnAirBrakeFactor": common_types.Float,
    "fTimeOnAirAllowingJump": common_types.Float,
    "fNoJumpingDefaultGravityFactor": common_types.Float,
    "fTimeToAimUpAfterRaise": common_types.Float,
    "fTimeToHangClimb": common_types.Float,
    "fRunningFallInitImpulse": common_types.Float,
    "fWalkingFallInitImpulse": common_types.Float,
    "fTimeToAbortSpinJump": common_types.Float,
    "fSpinJumpVelocityX": common_types.Float,
    "fAirRunningVelocityX": common_types.Float,
    "fAirWalkingVelocityX": common_types.Float,
})

CCharClassKraidAcidBlobsMovementComponent = Object({
    **CCharClassProjectileMovementFields,
    "fRotationFactor": common_types.Float,
})

CCharClassKraidAttack = Object(CCharClassKraidAttackFields := CCharClassAttackFields)


class ESpinningNailsState(enum.IntEnum):
    init = 0
    nail1 = 1
    nail2 = 2
    nail3 = 3
    nail4 = 4
    end = 5
    Invalid = 2147483647


construct_ESpinningNailsState = construct.Enum(construct.Int32ul, ESpinningNailsState)


class ESpinningNailsSpeed(enum.IntEnum):
    fast = 0
    medium = 1
    slow = 2
    Invalid = 2147483647


construct_ESpinningNailsSpeed = construct.Enum(construct.Int32ul, ESpinningNailsSpeed)

CKraidSpinningNailsDef = Object({
    "eState": construct_ESpinningNailsState,
    "eSpeed": construct_ESpinningNailsSpeed,
    "fAngle": common_types.Float,
})

CCharClassKraidSpinningNailsAttack = Object({
    **CCharClassKraidAttackFields,
    "tPatternsPhase1": common_types.make_vector(common_types.make_vector(Pointer_CKraidSpinningNailsDef.create_construct())),
    "tPatternsPhase2": common_types.make_vector(common_types.make_vector(Pointer_CKraidSpinningNailsDef.create_construct())),
})

CCharClassKraidBackSlapAttack = Object(CCharClassKraidAttackFields)

CCharClassKraidFierceSwipeAttack = Object(CCharClassKraidAttackFields)

CAcidBlobsLaunchPattern = Object({
    "iDistance": common_types.Int,
    "fTime": common_types.Float,
    "bBreakable": construct.Flag,
})

CCharClassKraidAcidBlobsAttack = Object({
    **CCharClassKraidAttackFields,
    "sEndAttackAnim": common_types.StrId,
    "fDuration": common_types.Float,
    "fUnbreakableGravity": common_types.Float,
    "fBreakableGravity": common_types.Float,
    "fMaxAngle": common_types.Float,
    "fMinAngle": common_types.Float,
    "tLaunchPatterns": common_types.make_vector(common_types.make_vector(Pointer_CAcidBlobsLaunchPattern.create_construct())),
})

CCharClassKraidFlyingSpikesAttack = Object({
    **CCharClassKraidAttackFields,
    "fSpike1VerticalOffset": common_types.Float,
    "fSpike1HorizontalOffset": common_types.Float,
    "fSpike2VerticalOffset": common_types.Float,
    "fSpike2HorizontalOffset": common_types.Float,
    "fSpike3VerticalOffset": common_types.Float,
    "fSpike3HorizontalOffset": common_types.Float,
})

CCharClassKraidTripleFlyingSpikesAttack = Object({
    **CCharClassKraidAttackFields,
    "fSpike1VerticalOffset": common_types.Float,
    "fSpike1HorizontalOffset": common_types.Float,
    "fSpike2VerticalOffset": common_types.Float,
    "fSpike2HorizontalOffset": common_types.Float,
    "fSpike3VerticalOffset": common_types.Float,
    "fSpike3HorizontalOffset": common_types.Float,
})

CBouncingCreaturesLaunchPattern = Object({
    "fAngle": common_types.Float,
    "fSpeed": common_types.Float,
    "fReboundImpulse": common_types.Float,
    "fDelay": common_types.Float,
})

CCharClassKraidBouncingCreaturesAttack = Object({
    **CCharClassKraidAttackFields,
    "sEndAttackAnim": common_types.StrId,
    "tPatterns": common_types.make_vector(common_types.make_vector(Pointer_CBouncingCreaturesLaunchPattern.create_construct())),
})

CCharClassKraidShockerSplashAttack = Object(CCharClassKraidAttackFields)

CCharClassKraidAIComponent = Object({
    **CCharClassBossAIComponentFields,
    "oKraidSpinningNailsAttackDef": CCharClassKraidSpinningNailsAttack,
    "oKraidBackSlapAttackDef": CCharClassKraidBackSlapAttack,
    "oKraidFierceSwipeAttackDef": CCharClassKraidFierceSwipeAttack,
    "oKraidAcidBlobsAttackDef": CCharClassKraidAcidBlobsAttack,
    "oKraidFlyingSpikesAttackDef": CCharClassKraidFlyingSpikesAttack,
    "oKraidTripleFlyingSpikesAttackDef": CCharClassKraidTripleFlyingSpikesAttack,
    "oKraidBouncingCreaturesAttackDef": CCharClassKraidBouncingCreaturesAttack,
    "oKraidShockerSplashAttackDef": CCharClassKraidShockerSplashAttack,
    "fOpenMouthInterpolationSpeed": common_types.Float,
    "fDesiredTimeToCloseMouth": common_types.Float,
    "fDamageToCloseMouth": common_types.Float,
    "fBellyLife": common_types.Float,
    "fMinTimeToRelaxAction": common_types.Float,
    "fMaxTimeToRelaxAction": common_types.Float,
    "fTimeToUncoverBelly": common_types.Float,
    "fIgnoreOpenMouthTimeAfterCloseMouth": common_types.Float,
    "fTimeToBellyDamage": common_types.Float,
    "fBellyButtonRadius": common_types.Float,
    "oGrabDamageSourceFactor": CDamageSourceFactor,
    "oFierceswipeActingDamageSourceFactor": CDamageSourceFactor,
})

CCharClassChozoCommanderSentenceSphereMovementComponent = Object({
    **CCharClassProjectileMovementFields,
    "fRotationSpeedDeg": common_types.Float,
    "fInitialRadius": common_types.Float,
    "fMinRadius": common_types.Float,
    "fMaxRadius": common_types.Float,
    "fTimeToReachMinRadius": common_types.Float,
    "fTimeToReachMaxRadius": common_types.Float,
})

CCharClassChozoCommanderAttack = Object(CCharClassChozoCommanderAttackFields := {
    **CCharClassAttackFields,
    "bCheckAuraNotCharged": construct.Flag,
    "bSyncCapeActionOnStart": construct.Flag,
})

CCharClassChozoCommanderGroundAttack = Object(CCharClassChozoCommanderGroundAttackFields := {
    **CCharClassChozoCommanderAttackFields,
    "fDesiredDistanceToAttack": common_types.Float,
    "fMinHyperDashDistance": common_types.Float,
    "fMaxHyperDashDistance": common_types.Float,
})

CCharClassChozoCommanderTriComboAttack = Object(CCharClassChozoCommanderGroundAttackFields)

CCharClassChozoCommanderKiStrikeAttack = Object({
    **CCharClassChozoCommanderGroundAttackFields,
    "fNoReactionTimeCharging": common_types.Float,
    "fMinTimeCharging": common_types.Float,
    "fMaxTimeCharging": common_types.Float,
    "fSlomo": common_types.Float,
    "fSlomotime": common_types.Float,
    "sSlomoFunction": common_types.StrId,
    "fDistanceToEndCharge": common_types.Float,
})

CCharClassChozoCommanderSentenceSphereAttack = Object({
    **CCharClassChozoCommanderGroundAttackFields,
    "fMinDistanceInSpaceJump": common_types.Float,
})

CCharClassChozoCommanderPowerPulseAttack = Object({
    **CCharClassChozoCommanderGroundAttackFields,
    "fFinalAngleDeg": common_types.Float,
    "fTimeAtFinalAngle": common_types.Float,
    "fTimeToReachFinalAngle": common_types.Float,
    "fMinDistToWall": common_types.Float,
    "sAngleIncrementCurve": common_types.StrId,
})

CCharClassChozoCommanderAuraScratchAttack = Object(CCharClassChozoCommanderGroundAttackFields)

CCharClassChozoCommanderKiCounterAttack = Object({
    **CCharClassChozoCommanderGroundAttackFields,
    "fTimeToLaunchEnd": common_types.Float,
    "fDistToForceMelee": common_types.Float,
    "fDistToLaunchInit": common_types.Float,
    "fBlockableAttackWarningTimeout": common_types.Float,
    "fMinCameraBoundingWidth": common_types.Float,
})

CCharClassChozoCommanderAirAttack = Object(CCharClassChozoCommanderAirAttackFields := CCharClassChozoCommanderAttackFields)

CCharClassChozoCommanderLandingSlamAttack = Object({
    **CCharClassChozoCommanderAirAttackFields,
    "fHeightToSamus": common_types.Float,
    "fTimeTracking": common_types.Float,
    "fMinSpeed": common_types.Float,
    "fMaxSpeed": common_types.Float,
    "fDistToClampMaxSpeed": common_types.Float,
})

CCharClassChozoCommanderAirChargeAttack = Object(CCharClassChozoCommanderAirAttackFields)

CCharClassChozoCommanderZeroLaserAttack = Object({
    **CCharClassChozoCommanderAirAttackFields,
    "fHeight": common_types.Float,
    "fAimingAngle": common_types.Float,
    "fMinTrackingTime": common_types.Float,
    "fMaxTrackingTime": common_types.Float,
    "fChargingTime": common_types.Float,
    "fShootingTime": common_types.Float,
    "fMinXDistToAttack": common_types.Float,
    "fMinYDistToAttack": common_types.Float,
    "fMinXDistToShot": common_types.Float,
})

CCharClassChozoCommanderBeamBurstAttack = Object(CCharClassChozoCommanderAirAttackFields)

CCharClassChozoCommanderHypersparkAttack = Object({
    **CCharClassChozoCommanderGroundAttackFields,
    "fPreparationTime": common_types.Float,
    "fVerticalPreparationTime": common_types.Float,
    "fChangeDirProb": common_types.Float,
})

CCharClassChozoCommanderEnergyShardsAttack = Object({
    **CCharClassChozoCommanderGroundAttackFields,
    "fMinDistanceToWall": common_types.Float,
    "fSphereHeight": common_types.Float,
})

CCharClassChozoCommanderZeroLaserGroundedAttack = Object({
    **CCharClassChozoCommanderGroundAttackFields,
    "fAimingTime": common_types.Float,
    "fChargingTime": common_types.Float,
    "fFiringTime": common_types.Float,
    "fAimAngleInterpSpeedMin": common_types.Float,
    "fAimAngleInterpSpeedMax": common_types.Float,
})

CCharClassChozoCommanderHyperDashAttack = Object({
    **CCharClassChozoCommanderGroundAttackFields,
    "fHeightOverSamus": common_types.Float,
    "fDistanceBehindSamus": common_types.Float,
})

CCharClassChozoCommanderUltimateGrabAttack = Object(CCharClassChozoCommanderAttackFields)

CCharClassChozoCommanderKiGrabAttack = Object(CCharClassChozoCommanderAttackFields)

CCharClassChozoCommanderAIComponent = Object({
    **CCharClassBossAIComponentFields,
    "oChozoCommanderTriComboAttackDef": CCharClassChozoCommanderTriComboAttack,
    "oChozoCommanderKiStrikeAttackDef": CCharClassChozoCommanderKiStrikeAttack,
    "oChozoCommanderSentenceSphereAttackDef": CCharClassChozoCommanderSentenceSphereAttack,
    "oChozoCommanderPowerPulseAttackDef": CCharClassChozoCommanderPowerPulseAttack,
    "oChozoCommanderAuraScratchAttackDef": CCharClassChozoCommanderAuraScratchAttack,
    "oChozoCommanderKiCounterAttackDef": CCharClassChozoCommanderKiCounterAttack,
    "oChozoCommanderLandingSlamAttackDef": CCharClassChozoCommanderLandingSlamAttack,
    "oChozoCommanderAirChargeAttackDef": CCharClassChozoCommanderAirChargeAttack,
    "oChozoCommanderZeroLaserAttackDef": CCharClassChozoCommanderZeroLaserAttack,
    "oChozoCommanderBeamBurstAttackDef": CCharClassChozoCommanderBeamBurstAttack,
    "oChozoCommanderHypersparkAttackDef": CCharClassChozoCommanderHypersparkAttack,
    "oChozoCommanderEnergyShardsAttackDef": CCharClassChozoCommanderEnergyShardsAttack,
    "oChozoCommanderZeroLaserGroundedAttackDef": CCharClassChozoCommanderZeroLaserGroundedAttack,
    "oChozoCommanderHyperDashAttackDef": CCharClassChozoCommanderHyperDashAttack,
    "oChozoCommanderUltimateGrabAttackDef": CCharClassChozoCommanderUltimateGrabAttack,
    "oChozoCommanderKiGrabAttackDef": CCharClassChozoCommanderKiGrabAttack,
    "fAuraLife": common_types.Float,
    "fLifeToRecoverAfterUltimateGrabStage1": common_types.Float,
    "fLifeToRecoverAfterUltimateGrabStage3": common_types.Float,
    "fUltimateGrabDamage": common_types.Float,
    "fTimeBetweenKiStrikeAttacks": common_types.Float,
    "fAttackWaitTimeBetweenPhases": common_types.Float,
    "fMinDistToHyperDash": common_types.Float,
    "fMaxVerticalDiffToAboveHyperDash": common_types.Float,
    "oDamageSourceFactorShortShootingGrab": CDamageSourceFactor,
    "oDamageSourceFactorLongShootingGrab": CDamageSourceFactor,
})

CCharClassSpitclawkAIComponent = Object({
    **CCharClassSclawkAIComponentFields,
    "fAcidRadius": common_types.Float,
    "fAcidGrowthTime": common_types.Float,
    "fTimeAtMaxRadius": common_types.Float,
    "fWidthMax": common_types.Float,
    "fWidthMin": common_types.Float,
})

CCharClassLiquidPoolComponent = Object(CCharClassLiquidPoolComponentFields := {
    **CCharClassBaseDamageTriggerComponentFields,
    "sLiquidMaterial0": common_types.StrId,
    "sLiquidMaterial1": common_types.StrId,
    "sSolidMaterial0": common_types.StrId,
    "sSolidMaterial1": common_types.StrId,
})

CCharClassGoliathXBurstProjectionBombsAttack = Object({
    **CCharClassAttackFields,
    "fChargingTime": common_types.Float,
    "fTimeBetweenWaves": common_types.Float,
    "uNumWaves": common_types.UInt,
})

CCharClassGoliathXSlamAttack = Object(CCharClassGoliathAttackFields)

CCharClassGoliathXAIComponent = Object({
    **CCharClassGoliathAIComponentFields,
    "oGoliathXBurstProjectionBombsAttackDef": CCharClassGoliathXBurstProjectionBombsAttack,
    "oGoliathXSlamAttackDef": CCharClassGoliathXSlamAttack,
})

CCharClassSluggerAcidBallMovementComponent = Object({
    **CCharClassProjectileMovementFields,
    "fTimeMeleeable": common_types.Float,
    "fTimeAbortable": common_types.Float,
})

CCharClassLockOnMissileMovement = Object(CCharClassLockOnMissileMovementFields := CCharClassMissileMovementFields)

CCharClassChozoCommanderEnergyShardsSphereMovementComponent = Object({
    **CCharClassProjectileMovementFields,
    "fAngleDispersion": common_types.Float,
    "fPositionDispersion": common_types.Float,
    "iNumExplosions": common_types.Int,
    "fTimeBetweenExplosions": common_types.Float,
    "fInitialTimeBetweenExplosions": common_types.Float,
    "fMaxLifeTime": common_types.Float,
})

CCharClassSpittailMagmaBallMovementComponent = Object({
    **CCharClassVulkranMagmaBallMovementComponentFields,
    "fWidthMax": common_types.Float,
    "fWidthMin": common_types.Float,
    "fYOffset": common_types.Float,
    "fTimeToGrow": common_types.Float,
    "fTimeAtMaxSize": common_types.Float,
})

CCharClassGooshockerAIComponent = Object({
    **CCharClassGooplotAIComponentFields,
    "fShockAttackDuration": common_types.Float,
})

CCharClassEmmyMovement = Object({
    **CCharClassEnemyMovementFields,
    "sWalkingWallUpRelaxAnim": common_types.StrId,
    "sWalkingWallUpFrontAnim": common_types.StrId,
    "sWalkingWallUpBackAnim": common_types.StrId,
    "sWalkingWallUpFrontInitAnim": common_types.StrId,
    "sWalkingWallUpBackInitAnim": common_types.StrId,
    "sWalkingWallUpFrontEndAnim": common_types.StrId,
    "sWalkingWallUpBackEndAnim": common_types.StrId,
    "sWalkingWallDownRelaxAnim": common_types.StrId,
    "sWalkingWallDownFrontAnim": common_types.StrId,
    "sWalkingWallDownBackAnim": common_types.StrId,
    "sWalkingWallDownFrontInitAnim": common_types.StrId,
    "sWalkingWallDownBackInitAnim": common_types.StrId,
    "sWalkingWallDownFrontEndAnim": common_types.StrId,
    "sWalkingWallDownBackEndAnim": common_types.StrId,
    "sWalkingCeilRelaxAnim": common_types.StrId,
    "sWalkingCeilFrontAnim": common_types.StrId,
    "sWalkingCeilBackAnim": common_types.StrId,
    "sWalkingCeilFrontInitAnim": common_types.StrId,
    "sWalkingCeilBackInitAnim": common_types.StrId,
    "sWalkingCeilFrontEndAnim": common_types.StrId,
    "sWalkingCeilBackEndAnim": common_types.StrId,
    "sWalkingPatrolRelaxAnim": common_types.StrId,
    "sWalkingPatrolFrontAnim": common_types.StrId,
    "sWalkingPatrolBackAnim": common_types.StrId,
    "sWalkingPatrolFrontInitAnim": common_types.StrId,
    "sWalkingPatrolBackInitAnim": common_types.StrId,
    "sWalkingPatrolFrontEndAnim": common_types.StrId,
    "sWalkingPatrolBackEndAnim": common_types.StrId,
    "sWalkingWallUpPatrolRelaxAnim": common_types.StrId,
    "sWalkingWallUpPatrolFrontAnim": common_types.StrId,
    "sWalkingWallUpPatrolBackAnim": common_types.StrId,
    "sWalkingWallUpPatrolFrontInitAnim": common_types.StrId,
    "sWalkingWallUpPatrolBackInitAnim": common_types.StrId,
    "sWalkingWallUpPatrolFrontEndAnim": common_types.StrId,
    "sWalkingWallUpPatrolBackEndAnim": common_types.StrId,
    "sWalkingWallDownPatrolRelaxAnim": common_types.StrId,
    "sWalkingWallDownPatrolFrontAnim": common_types.StrId,
    "sWalkingWallDownPatrolBackAnim": common_types.StrId,
    "sWalkingWallDownPatrolFrontInitAnim": common_types.StrId,
    "sWalkingWallDownPatrolBackInitAnim": common_types.StrId,
    "sWalkingWallDownPatrolFrontEndAnim": common_types.StrId,
    "sWalkingWallDownPatrolBackEndAnim": common_types.StrId,
    "sWalkingCeilPatrolRelaxAnim": common_types.StrId,
    "sWalkingCeilPatrolFrontAnim": common_types.StrId,
    "sWalkingCeilPatrolBackAnim": common_types.StrId,
    "sWalkingCeilPatrolFrontInitAnim": common_types.StrId,
    "sWalkingCeilPatrolBackInitAnim": common_types.StrId,
    "sWalkingCeilPatrolFrontEndAnim": common_types.StrId,
    "sWalkingCeilPatrolBackEndAnim": common_types.StrId,
    "sWalkingTunnelRelaxAnim": common_types.StrId,
    "sWalkingTunnelFrontAnim": common_types.StrId,
    "sWalkingTunnelBackAnim": common_types.StrId,
    "sWalkingTunnelFrontInitAnim": common_types.StrId,
    "sWalkingTunnelBackInitAnim": common_types.StrId,
    "sWalkingTunnelFrontEndAnim": common_types.StrId,
    "sWalkingTunnelBackEndAnim": common_types.StrId,
})

CCharClassAutectorAIComponent = Object(CCharClassRobotAIComponentFields)

CCharClassCentralUnitCannonBeamMovementComponent = Object(CCharClassProjectileMovementFields)

CCharClassHomingMovement = Object(CCharClassProjectileMovementFields)

CCharClassQuetzoaEnergyWaveMovementComponent = Object(CCharClassProjectileMovementFields)

CCharClassBigFistAttack = Object(CCharClassAttackFields)

CCharClassBigFistAIComponent = Object({
    **CCharClassBaseBigFistAIComponentFields,
    "oBigFistAttackDef": CCharClassBigFistAttack,
})

CCharClassKraidNailMovementComponent = Object({
    **CCharClassProjectileMovementFields,
    "fRotationFactor": common_types.Float,
    "fPhase1LeftHandCloseSpeed": common_types.Float,
    "fPhase1LeftHandFarSpeed": common_types.Float,
    "fPhase1RightHandCloseSpeed": common_types.Float,
    "fPhase1RightHandFarSpeed": common_types.Float,
    "fPhase2LeftHandSpeed": common_types.Float,
    "fPhase2RightHandSpeed": common_types.Float,
})

CCharClassCooldownXBossFireBallMovementComponent = Object({
    **CCharClassProjectileMovementFields,
    "fPreparationTime": common_types.Float,
    "fMovingSpeed": common_types.Float,
})

CCharClassChozoWarriorAttack = Object(CCharClassChozoWarriorAttackFields := CCharClassAttackFields)

CCharClassChozoWarriorGlaiveSpinAttack = Object(CCharClassChozoWarriorGlaiveSpinAttackFields := CCharClassChozoWarriorAttackFields)

CCharClassChozoWarriorGlaiveWalljumpAttack = Object(CCharClassChozoWarriorAttackFields)

CCharClassChozoWarriorDeflectorShieldAttack = Object(CCharClassChozoWarriorAttackFields)

CCharClassChozoWarriorAIComponent = Object(CCharClassChozoWarriorAIComponentFields := {
    **CCharClassBossAIComponentFields,
    "oChozoWarriorGlaiveSpinAttackDef": CCharClassChozoWarriorGlaiveSpinAttack,
    "oChozoWarriorGlaiveWalljumpAttackDef": CCharClassChozoWarriorGlaiveWalljumpAttack,
    "oChozoWarriorDeflectorShieldAttackDef": CCharClassChozoWarriorDeflectorShieldAttack,
    "bUsesShield": construct.Flag,
    "fTargetMinDistanceToFloorToForceGlaiveSpinAttack": common_types.Float,
    "fGlaiveSpinAttackOffsetDistanceIfTargetOnAir": common_types.Float,
})

CCharClassScorpiusAttack = Object(CCharClassScorpiusAttackFields := {
    **CCharClassAttackFields,
    "bAnimateTail": construct.Flag,
    "fTailBlendTime": common_types.Float,
})

CCharClassScorpiusWhiplashAttack = Object(CCharClassScorpiusAttackFields)

CCharClassScorpiusSpikeBallPrickAttack = Object({
    **CCharClassScorpiusAttackFields,
    "sMagnetAttackAnim": common_types.StrId,
})

CCharClassScorpiusPoisonousSpitAttack = Object(CCharClassScorpiusAttackFields)

CCharClassScorpiusDefensiveSpikeBallPrickAttack = Object(CCharClassScorpiusAttackFields)

CCharClassScorpiusTailSmashAttack = Object(CCharClassScorpiusAttackFields)

CCharClassScorpiusPoisonousGasAttack = Object(CCharClassScorpiusPoisonousGasAttackFields := {
    **CCharClassScorpiusAttackFields,
    "sChargeAttackAnim": common_types.StrId,
    "sAfterChargeAttackAnim": common_types.StrId,
})

CCharClassScorpiusMovingPoisonousGasAttack = Object(CCharClassScorpiusPoisonousGasAttackFields)

CCharClassScorpiusDraggedBallPrickAttack = Object(CCharClassScorpiusAttackFields)

CCharClassScorpiusAIComponent = Object({
    **CCharClassBossAIComponentFields,
    "oWhiplashAttackDef": CCharClassScorpiusWhiplashAttack,
    "oSpikeBallPrickAttackDef": CCharClassScorpiusSpikeBallPrickAttack,
    "oPoisonousSpitAttackDef": CCharClassScorpiusPoisonousSpitAttack,
    "oDefensiveSpikeBallPrickAttackDef": CCharClassScorpiusDefensiveSpikeBallPrickAttack,
    "oTailSmashAttackDef": CCharClassScorpiusTailSmashAttack,
    "oPoisonousGasAttackDef": CCharClassScorpiusPoisonousGasAttack,
    "oMovingPoisonousGasAttackDef": CCharClassScorpiusMovingPoisonousGasAttack,
    "oDraggedBallPrickAttackDef": CCharClassScorpiusDraggedBallPrickAttack,
    "sHeadMovementFunction": common_types.StrId,
    "sTailMovementFunction": common_types.StrId,
    "fTailMinTimeToChange": common_types.Float,
    "fTailMaxTimeToChange": common_types.Float,
    "fRegenTailMaxAnimSpeed": common_types.Float,
    "sRegenTailAnimSpeedFunc": common_types.StrId,
    "fTimeRegenTailSlowMovement": common_types.Float,
    "fTimeRegenTailFastMovement": common_types.Float,
    "fTimeRegenTailMovementTransitionFactor": common_types.Float,
    "fTailHeightInterpolationSpeed": common_types.Float,
    "oGrabDamageSourceFactor": CDamageSourceFactor,
    "fHeadMaxSpeed": common_types.Float,
    "fHeadMinSpeed": common_types.Float,
})

CCharClassAutclastChargeAttack = Object(CCharClassAttackFields)

CCharClassAutclastAIComponent = Object({
    **CCharClassRobotAIComponentFields,
    "oAutclastChargeAttackDef": CCharClassAutclastChargeAttack,
})

CCharClassQuetzoaMultiTargetProjectileMovementComponent = Object({
    **CCharClassLockOnMissileMovementFields,
    "fLaunchAngle": common_types.Float,
    "fLaunchDist": common_types.Float,
    "fSteeringSpeed": common_types.Float,
    "fMaxDistanceFromGuide": common_types.Float,
})

CCharClassQuetzoaXMultiTargetAttack = Object({
    **CCharClassAttackFields,
    "uNumProjectiles": common_types.UInt,
    "fTimeBetweenShots": common_types.Float,
})

CCharClassQuetzoaXAIComponent = Object({
    **CCharClassQuetzoaAIComponentFields,
    "oQuetzoaXMultiTargetAttackDef": CCharClassQuetzoaXMultiTargetAttack,
    "fVulnerabilityTime": common_types.Float,
})

CCharClassWaterPoolComponent = Object({
    **CCharClassLiquidPoolComponentFields,
    "fDamagePerTime": common_types.Float,
    "fInBetweenDamageTime": common_types.Float,
    "fInitTimeDamageIncrease": common_types.Float,
    "fDamageIncreaseAmount": common_types.Float,
    "fMaxDamage": common_types.Float,
})

CCharClassLavaPoolComponent = Object({
    **CCharClassLiquidPoolComponentFields,
    "fDamagePerTime": common_types.Float,
    "fInBetweenDamageTime": common_types.Float,
    "fInitTimeDamageIncrease": common_types.Float,
    "fDamageIncreaseAmount": common_types.Float,
    "fMaxDamage": common_types.Float,
    "sLevelChangeEasingFunction": common_types.StrId,
})

CCharClassChozoWarriorXGlaiveSpinAttack = Object(CCharClassChozoWarriorGlaiveSpinAttackFields)

CCharClassChozoWarriorXWallClimbAttack = Object(CCharClassChozoWarriorAttackFields)

CCharClassChozoWarriorXLandAttack = Object(CCharClassChozoWarriorAttackFields)

CCharClassChozoWarriorXChangeWallAttack = Object(CCharClassChozoWarriorAttackFields)

CCharClassChozoWarriorXSpitAttack = Object(CCharClassChozoWarriorAttackFields)

CCharClassChozoWarriorXUltimateGrabAttack = Object({
    **CCharClassChozoWarriorAttackFields,
    "fUltimateGrabDamage": common_types.Float,
})

CCharClassChozoWarriorXAIComponent = Object(CCharClassChozoWarriorXAIComponentFields := {
    **CCharClassChozoWarriorAIComponentFields,
    "oChozoWarriorXGlaiveSpinAttackDef": CCharClassChozoWarriorXGlaiveSpinAttack,
    "oChozoWarriorXWallClimbAttackDef": CCharClassChozoWarriorXWallClimbAttack,
    "oChozoWarriorXLandAttackDef": CCharClassChozoWarriorXLandAttack,
    "oChozoWarriorXChangeWallAttackDef": CCharClassChozoWarriorXChangeWallAttack,
    "oChozoWarriorXSpitAttackDef": CCharClassChozoWarriorXSpitAttack,
    "oChozoWarriorXUltimateGrabAttackDef": CCharClassChozoWarriorXUltimateGrabAttack,
})

CCharClassChozoWarriorEliteAIComponent = Object(CCharClassChozoWarriorAIComponentFields)

CCharClassChozoWarriorXEliteAIComponent = Object(CCharClassChozoWarriorXAIComponentFields)

base_spatial_CAABox = Object({
    "Min": common_types.CVector3D,
    "Max": common_types.CVector3D,
})

CEntity = Object({
    **CActorFields,
    "oBBox": base_spatial_CAABox,
    "bIsInFrustum": construct.Flag,
})

CComponent = Object(CComponentFields := {
    **CActorComponentFields,
    "bEnabled": construct.Flag,
    "bWantsEnabled": construct.Flag,
    "bUseDefaultValues": construct.Flag,
})

CAttackComponent = Object(CAttackComponentFields := {
    **CComponentFields,
    "bRotateToDamagedEntity": construct.Flag,
    "fRotateToDamagedEntityMaxAngle": common_types.Float,
    "fRotateToDamagedEntityMinAngle": common_types.Float,
})

CAIAttackComponent = Object(CAIAttackComponentFields := CAttackComponentFields)


class IPath_EType(enum.IntEnum):
    NONE = 0
    Once = 1
    PingPong = 2
    Loop = 3
    Invalid = 2147483647


construct_IPath_EType = construct.Enum(construct.Int32ul, IPath_EType)

SFallBackPath = Object({
    "wpPath": common_types.StrId,
    "ePathType": construct_IPath_EType,
})

CAIComponent = Object(CAIComponentFields := {
    **CComponentFields,
    "sForcedAttack": common_types.StrId,
    "iForcedAttackPreset": common_types.Int,
    "fTimeSinceTargetLastSeen": common_types.Float,
    "fTimeSinceLastDamage": common_types.Float,
    "fTimeSinceLastFrozen": common_types.Float,
    "fPathLeftCut": common_types.Float,
    "fPathRightCut": common_types.Float,
    "fCutDistanceClockwise": common_types.Float,
    "fCutDistanceCounterClockwise": common_types.Float,
    "wpPathToFollow": common_types.StrId,
    "tFallbackPaths": common_types.make_vector(SFallBackPath),
    "ePathType": construct_IPath_EType,
    "bIndividualRequiresActivationPerception": construct.Flag,
    "bIgnoreAttack": construct.Flag,
    "bInBlindAttack": construct.Flag,
})

CGrapplePointComponent = Object(CGrapplePointComponentFields := CComponentFields)

CPullableGrapplePointComponent = Object(CPullableGrapplePointComponentFields := CGrapplePointComponentFields)

CAIGrapplePointComponent = Object(CPullableGrapplePointComponentFields)

CAINavigationComponent = Object(CComponentFields)

CAISmartObjectComponent = Object({
    **CComponentFields,
    "fResetTime": common_types.Float,
    "fUseTime": common_types.Float,
    "iSpawnDirection": common_types.Int,
})

CAbilityComponent = Object({
    **CComponentFields,
    "bAccurateAiming": construct.Flag,
    "sBlockSyncFX": common_types.StrId,
})

CUsableComponent = Object(CUsableComponentFields := {
    **CComponentFields,
    "bFadeInActived": construct.Flag,
})

CAccessPointComponent = Object(CAccessPointComponentFields := {
    **CUsableComponentFields,
    "vDoorsToChange": common_types.make_vector(common_types.StrId),
    "sInteractionLiteralID": common_types.StrId,
    "tCaptionList": common_types.make_dict(common_types.make_vector(common_types.StrId)),
    "wpThermalDevice": common_types.StrId,
})

CAccessPointCommanderComponent = Object({
    **CAccessPointComponentFields,
    "wpAfterFirstDialogueScenePlayer": common_types.StrId,
})

CActivatableComponent = Object(CActivatableComponentFields := CComponentFields)

CActionSwitcherComponent = Object(CActivatableComponentFields)

CActionSwitcherOnPullGrapplePointComponent = Object({
    **CPullableGrapplePointComponentFields,
    "sActionOnPull": common_types.StrId,
})

CActivatableByProjectileComponent = Object(CActivatableByProjectileComponentFields := CComponentFields)

CAimCameraEnabledVisibleOnlyComponent = Object(CComponentFields)

CAimComponent = Object({
    **CComponentFields,
    "sLaserFX": common_types.StrId,
    "sAutoAimLaserFX": common_types.StrId,
    "bAutoAimActive": construct.Flag,
    "bLockOnSoundAllowed": construct.Flag,
    "fCurrentAutoAimWidth": common_types.Float,
    "fCurrentAutoAimConeLength": common_types.Float,
})

CAlternativeActionPlayerComponent = Object(CAlternativeActionPlayerComponentFields := CComponentFields)

CAmmoRechargeComponent = Object({
    **CUsableComponentFields,
    "sRechargeFX": common_types.StrId,
    "sEyeRFX": common_types.StrId,
    "sEyeLFX": common_types.StrId,
})

CAnimationComponent = Object(CAnimationComponentFields := CComponentFields)

CNavMeshItemComponent = Object(CNavMeshItemComponentFields := {
    **CComponentFields,
    "tForbiddenEdgesSpawnPoints": common_types.make_vector(common_types.StrId),
})

CAnimationNavMeshItemComponent = Object(CNavMeshItemComponentFields)

CBehaviorTreeAIComponent = Object(CBehaviorTreeAIComponentFields := CAIComponentFields)

CArachnusAIComponent = Object(CBehaviorTreeAIComponentFields)

CSceneComponent = Object(CSceneComponentFields := CComponentFields)

CAreaFXComponent = Object({
    **CSceneComponentFields,
    "sModelResPath": common_types.StrId,
})

CBaseTriggerComponent = Object(CBaseTriggerComponentFields := {
    **CActivatableComponentFields,
    "bCheckAllEntities": construct.Flag,
})


class base_snd_ELowPassFilter(enum.IntEnum):
    LPF_DISABLED = 0
    LPF_80HZ = 1
    LPF_100HZ = 2
    LPF_128HZ = 3
    LPF_160HZ = 4
    LPF_200HZ = 5
    LPF_256HZ = 6
    LPF_320HZ = 7
    LPF_400HZ = 8
    LPF_500HZ = 9
    LPF_640HZ = 10
    LPF_800HZ = 11
    LPF_1000HZ = 12
    LPF_1280HZ = 13
    LPF_1600HZ = 14
    LPF_2000HZ = 15
    LPF_2560HZ = 16
    LPF_3200HZ = 17
    LPF_4000HZ = 18
    LPF_5120HZ = 19
    LPF_6400HZ = 20
    LPF_8000HZ = 21
    LPF_10240HZ = 22
    LPF_12800HZ = 23
    LPF_16000HZ = 24
    Invalid = 2147483647


construct_base_snd_ELowPassFilter = construct.Enum(construct.Int32ul, base_snd_ELowPassFilter)

CSoundTrigger = Object(CSoundTriggerFields := {
    **CBaseTriggerComponentFields,
    "eReverb": construct_base_snd_EReverbIntensity,
    "iLowPassFilter": construct_base_snd_ELowPassFilter,
})

CAreaMusicComponent = Object({
    **CSoundTriggerFields,
    "fEnterFadeIn": common_types.Float,
    "fEnterFadeOut": common_types.Float,
    "fExitFadeIn": common_types.Float,
    "fExitFadeOut": common_types.Float,
    "sPreset": common_types.StrId,
    "eEnterFadeType": construct_EMusicFadeType,
    "eExitFadeType": construct_EMusicFadeType,
})


class base_snd_ESndType(enum.IntEnum):
    SFX = 0
    MUSIC = 1
    SPEECH = 2
    GRUNT = 3
    GUI = 4
    ENVIRONMENT_STREAMS = 5
    SFX_EMMY = 6
    CUTSCENE = 7
    Invalid = 2147483647


construct_base_snd_ESndType = construct.Enum(construct.Int32ul, base_snd_ESndType)

CAreaSoundComponent = Object({
    **CSoundTriggerFields,
    "sOnEnterSound": common_types.StrId,
    "eOnEnterSoundType": construct_base_snd_ESndType,
    "fEnterVol": common_types.Float,
    "fEnterPitch": common_types.Float,
    "fEnterFadeInTime": common_types.Float,
    "fEnterFadeOutTime": common_types.Float,
    "eOnEnterPositional": construct_base_snd_EPositionalType,
    "sLoopSound": common_types.StrId,
    "eLoopSoundType": construct_base_snd_ESndType,
    "fLoopVol": common_types.Float,
    "fLoopPitch": common_types.Float,
    "fLoopPan": common_types.Float,
    "fLoopFadeInTime": common_types.Float,
    "fLoopFadeOutTime": common_types.Float,
    "sOnExitSound": common_types.StrId,
    "eOnExitSoundType": construct_base_snd_ESndType,
    "fExitVol": common_types.Float,
    "fExitPitch": common_types.Float,
    "fExitFadeInTime": common_types.Float,
    "fExitFadeOutTime": common_types.Float,
    "eOnExitPositional": construct_base_snd_EPositionalType,
})

CAudioComponent = Object(CComponentFields)

CRobotAIComponent = Object(CRobotAIComponentFields := CBehaviorTreeAIComponentFields)

CAutclastAIComponent = Object(CRobotAIComponentFields)


class EJumpType(enum.IntEnum):
    Short = 0
    Large = 1
    Invalid = 2147483647


construct_EJumpType = construct.Enum(construct.Int32ul, EJumpType)

CAutectorAIComponent = Object({
    **CRobotAIComponentFields,
    "eJumpType": construct_EJumpType,
})

CLifeComponent = Object(CLifeComponentFields := {
    **CComponentFields,
    "bWantsCameraFXPreset": construct.Flag,
    "fMaxLife": common_types.Float,
    "fCurrentLife": common_types.Float,
    "bCurrentLifeLocked": construct.Flag,
})

CCharacterLifeComponent = Object(CCharacterLifeComponentFields := {
    **CLifeComponentFields,
    "sImpactAnim": common_types.StrId,
    "sDeadAnim": common_types.StrId,
})

CEnemyLifeComponent = Object(CEnemyLifeComponentFields := {
    **CCharacterLifeComponentFields,
    "sImpactBackAnim": common_types.StrId,
    "sDeadBackAnim": common_types.StrId,
    "sDeadAirAnim": common_types.StrId,
    "sDeadAirBackAnim": common_types.StrId,
})

CAutectorLifeComponent = Object(CEnemyLifeComponentFields)

CAutomperAIComponent = Object(CRobotAIComponentFields)

CAutoolAIComponent = Object({
    **CRobotAIComponentFields,
    "vAISmartObjects": common_types.make_vector(common_types.StrId),
})

CAutsharpAIComponent = Object(CRobotAIComponentFields)

CAutsharpLifeComponent = Object(CEnemyLifeComponentFields)


class CSpawnPointComponent_EXCellSpawnPositionMode(enum.IntEnum):
    FarthestToSpawnPoint = 0
    ClosestToSpawnPoint = 1
    Invalid = 2147483647


construct_CSpawnPointComponent_EXCellSpawnPositionMode = construct.Enum(construct.Int32ul, CSpawnPointComponent_EXCellSpawnPositionMode)


class CSpawnPointComponent_EDynamicSpawnPositionMode(enum.IntEnum):
    ClosestToPlayer = 0
    FarthestToPlayer = 1
    Random = 2
    Invalid = 2147483647


construct_CSpawnPointComponent_EDynamicSpawnPositionMode = construct.Enum(construct.Int32ul, CSpawnPointComponent_EDynamicSpawnPositionMode)

CSpawnerActorBlueprint = Object({
    "InnerValue": Pointer_base_reflection_CTypedValue.create_construct(),
})

CSpawnPointComponent = Object(CSpawnPointComponentFields := {
    **CComponentFields,
    "sOnBeforeGenerate": common_types.StrId,
    "sOnEntityGenerated": common_types.StrId,
    "sStartAnimation": common_types.StrId,
    "bSpawnOnFloor": construct.Flag,
    "bEntityCheckFloor": construct.Flag,
    "bCheckCollisions": construct.Flag,
    "fTimeToActivate": common_types.Float,
    "iMaxNumToGenerate": common_types.Int,
    "bAllowSpawnInFrustum": construct.Flag,
    "bStartEnabled": construct.Flag,
    "bAutomanaged": construct.Flag,
    "wpSceneShapeId": common_types.StrId,
    "wpCollisionSceneShapeId": common_types.StrId,
    "wpNavigableShape": common_types.StrId,
    "wpAreaOfInterest": common_types.StrId,
    "wpAreaOfInterestEnd": common_types.StrId,
    "fTimeOnAOIEndToUseAsMainAOI": common_types.Float,
    "fSpawnFromXCellProbability": common_types.Float,
    "fSpawnFromXCellProbabilityAfterFirst": common_types.Float,
    "eXCellSpawnPositionMode": construct_CSpawnPointComponent_EXCellSpawnPositionMode,
    "bUseDynamicSpawnPosition": construct.Flag,
    "eDynamicSpawnPositionMode": construct_CSpawnPointComponent_EDynamicSpawnPositionMode,
    "tDynamicSpawnPositions": common_types.make_vector(common_types.StrId),
    "tXCellTransformTargets": common_types.make_vector(common_types.StrId),
    "wpXCellActivationAreaShape": common_types.StrId,
    "sCharClass": common_types.StrId,
    "voActorBlueprint": common_types.make_vector(CSpawnerActorBlueprint),
})


class EAutsharpSpawnPointDir(enum.IntEnum):
    Left = 0
    Right = 1
    Both = 2
    Invalid = 2147483647


construct_EAutsharpSpawnPointDir = construct.Enum(construct.Int32ul, EAutsharpSpawnPointDir)

CAutsharpSpawnPointComponent = Object({
    **CSpawnPointComponentFields,
    "eSpawnDir": construct_EAutsharpSpawnPointDir,
    "wpSpawnShape": common_types.StrId,
})

CAutsniperAIComponent = Object(CRobotAIComponentFields)


class EAutsniperSpawnPointDir(enum.IntEnum):
    Clockwise = 0
    Counterclockwise = 1
    Invalid = 2147483647


construct_EAutsniperSpawnPointDir = construct.Enum(construct.Int32ul, EAutsniperSpawnPointDir)

CAutsniperSpawnPointComponent = Object({
    **CSpawnPointComponentFields,
    "eSpawnDir": construct_EAutsniperSpawnPointDir,
})

CBTObserverComponent = Object(CActorComponentFields)

CBossAIComponent = Object(CBossAIComponentFields := {
    **CBehaviorTreeAIComponentFields,
    "sArenaLeftLandmark": common_types.StrId,
    "sArenaRightLandmark": common_types.StrId,
    "fArenaLimitDist": common_types.Float,
    "tDoors": common_types.make_vector(common_types.StrId),
    "wpBossCamera": common_types.StrId,
    "wpBossCameraFloorLandmark": common_types.StrId,
    "wpBossCameraCeilingLandmark": common_types.StrId,
    "wpStartCombatCheckpointStartPoint": common_types.StrId,
    "sStartCombatCheckpointSnapshotId": common_types.StrId,
    "wpDeadCheckpointStartPoint": common_types.StrId,
    "bSaveGameOnAfterDead": construct.Flag,
})

CBaseBigFistAIComponent = Object(CBaseBigFistAIComponentFields := {
    **CBossAIComponentFields,
    "fMinTimeBetweenDigs": common_types.Float,
    "fMaxTimeBetweenDigs": common_types.Float,
    "fMinTimeDigging": common_types.Float,
    "fMaxTimeDigging": common_types.Float,
})

CBaseDamageTriggerComponent = Object(CBaseDamageTriggerComponentFields := {
    **CBaseTriggerComponentFields,
    "sContinuousDamageSound": common_types.StrId,
})

CBaseGroundShockerAIComponent = Object(CBaseGroundShockerAIComponentFields := CBehaviorTreeAIComponentFields)


class engine_utils_ELightPreset(enum.IntEnum):
    E_LIGHT_PRESET_NONE = 0
    E_LIGHT_PRESET_PULSE = 1
    E_LIGHT_PRESET_BLINK = 2
    E_LIGHT_PRESET_LIGHTNING = 3
    ELIGHT_PRESET_COUNT = 4
    ELIGHT_PRESET_INVALID = 5
    Invalid = 2147483647


construct_engine_utils_ELightPreset = construct.Enum(construct.Int32ul, engine_utils_ELightPreset)

CBaseLightComponent = Object(CBaseLightComponentFields := {
    **CComponentFields,
    "vLightPos": common_types.CVector3D,
    "fIntensity": common_types.Float,
    "fVIntensity": common_types.Float,
    "fFIntensity": common_types.Float,
    "vAmbient": common_types.CVector4D,
    "vDiffuse": common_types.CVector4D,
    "vSpecular0": common_types.CVector4D,
    "vSpecular1": common_types.CVector4D,
    "bVertexLight": construct.Flag,
    "eLightPreset": construct_engine_utils_ELightPreset,
    "vLightPresetParams": common_types.CVector4D,
    "bSubstractive": construct.Flag,
    "bUseFaceCull": construct.Flag,
    "bUseSpecular": construct.Flag,
})

CBasicLifeComponent = Object(CBasicLifeComponentFields := CLifeComponentFields)

CBatalloonAIComponent = Object({
    **CBaseGroundShockerAIComponentFields,
    "bReceivingCall": construct.Flag,
})

CItemLifeComponent = Object(CItemLifeComponentFields := CLifeComponentFields)

SBeamBoxActivatable = Object({
    "oActivatableObj": common_types.StrId,
    "sState": common_types.StrId,
})

CBeamBoxComponent = Object({
    **CItemLifeComponentFields,
    "fDisplaceDist": common_types.Float,
    "vActivatables": common_types.make_vector(SBeamBoxActivatable),
    "sAnimationId": common_types.StrId,
})


class CDoorShieldLifeComponent_EColor(enum.IntEnum):
    NONE = 0
    RED = 1
    GREEN = 2
    YELLOW = 3
    Invalid = 2147483647


construct_CDoorShieldLifeComponent_EColor = construct.Enum(construct.Int32ul, CDoorShieldLifeComponent_EColor)

CDoorShieldLifeComponent = Object(CDoorShieldLifeComponentFields := {
    **CItemLifeComponentFields,
    "fDamageFXTime": common_types.Float,
    "sDamageSound": common_types.StrId,
    "sKillSound": common_types.StrId,
    "eColor": construct_CDoorShieldLifeComponent_EColor,
})

CBeamDoorLifeComponent = Object(CDoorShieldLifeComponentFields)

CBigFistAIComponent = Object({
    **CBaseBigFistAIComponentFields,
    "timeForNextDig": common_types.Float,
})

CBigkranXAIComponent = Object(CBaseBigFistAIComponentFields)

CCollisionComponent = Object(CCollisionComponentFields := CComponentFields)

CBillboardCollisionComponent = Object(CCollisionComponentFields)

CBillboardComponent = Object({
    **CComponentFields,
    "iNumGroups": common_types.Int,
    "iMaxInhabitantsPerGroup": common_types.Int,
    "iMinInhabitantsPerGroup": common_types.Int,
})

CBillboardLifeComponent = Object(CLifeComponentFields)

CMovementComponent = Object(CMovementComponentFields := {
    **CComponentFields,
    "bIsFlying": construct.Flag,
})

CWeaponMovement = Object(CWeaponMovementFields := CMovementComponentFields)

CBombMovement = Object(CBombMovementFields := {
    **CWeaponMovementFields,
    "sCollisionFX": common_types.StrId,
})

CBoneToConstantComponent = Object(CSceneComponentFields)

CBossLifeComponent = Object(CEnemyLifeComponentFields)

CSpawnGroupComponent = Object(CSpawnGroupComponentFields := {
    **CComponentFields,
    "bIsGenerator": construct.Flag,
    "bIsInfinite": construct.Flag,
    "iMaxToGenerate": common_types.Int,
    "iMaxSimultaneous": common_types.Int,
    "fGenerateEvery": common_types.Float,
    "sOnBeforeGenerateEntity": common_types.StrId,
    "sOnEntityGenerated": common_types.StrId,
    "sOnEnable": common_types.StrId,
    "sOnDisable": common_types.StrId,
    "sOnMaxSimultaneous": common_types.StrId,
    "sOnMaxGenerated": common_types.StrId,
    "sOnEntityDead": common_types.StrId,
    "sOnEntityDamaged": common_types.StrId,
    "sOnAllEntitiesDead": common_types.StrId,
    "bAutomanaged": construct.Flag,
    "bDisableOnAllDead": construct.Flag,
    "bAutoenabled": construct.Flag,
    "bSpawnPointsNotInFrustrum": construct.Flag,
    "bGenerateEntitiesByOrder": construct.Flag,
    "sLogicCollisionShapeID": common_types.StrId,
    "wpAreaOfInterest": common_types.StrId,
    "wpAreaOfInterestEnd": common_types.StrId,
    "fDropAmmoProb": common_types.Float,
    "iInitToGenerate": common_types.Int,
    "sArenaId": common_types.StrId,
    "bCheckActiveDrops": construct.Flag,
    "iNumDeaths": common_types.Int,
    "vectSpawnPoints": common_types.make_vector(common_types.StrId),
})

CBossSpawnGroupComponent = Object({
    **CSpawnGroupComponentFields,
    "sBossBattleLabel": common_types.StrId,
})

CLogicShapeComponent = Object(CLogicShapeComponentFields := {
    **CActorComponentFields,
    "pLogicShape": Pointer_game_logic_collision_CShape.create_construct(),
    "bWantsToGenerateNavMeshEdges": construct.Flag,
})

CBreakableHintComponent = Object(CLogicShapeComponentFields)

CBreakableScenarioComponent = Object({
    **CComponentFields,
    "aVignettes": common_types.make_vector(common_types.StrId),
})


class EBreakableTileType(enum.IntEnum):
    UNDEFINED = 0
    POWERBEAM = 1
    BOMB = 2
    MISSILE = 3
    SUPERMISSILE = 4
    POWERBOMB = 5
    SCREWATTACK = 6
    WEIGHT = 7
    BABYHATCHLING = 8
    SPEEDBOOST = 9
    Invalid = 2147483647


construct_EBreakableTileType = construct.Enum(construct.Int32ul, EBreakableTileType)

CBreakableTileGroupComponent_STileInfo = Object({
    "eTileType": construct_EBreakableTileType,
    "vGridCoords": common_types.CVector2D,
    "sHiddenSG": common_types.StrId,
    "bIsHidingSecret": construct.Flag,
    "aVignettes": common_types.make_vector(common_types.StrId),
})

CBreakableTileGroupComponent = Object({
    **CSceneComponentFields,
    "uGroupId": common_types.UInt,
    "aGridTiles": common_types.make_vector(CBreakableTileGroupComponent_STileInfo),
    "bFakeHusks": construct.Flag,
    "eCollisionMaterial": construct_game_logic_collision_EColMat,
})

CSonarTargetComponent = Object(CSonarTargetComponentFields := CComponentFields)

CBreakableTileGroupSonarTargetComponent = Object(CSonarTargetComponentFields)

CBreakableVignetteComponent = Object({
    **CLogicShapeComponentFields,
    "sVignetteSG": common_types.StrId,
    "bUnhideWhenPlayerInside": construct.Flag,
    "bPreventVisibilityOnly": construct.Flag,
    "bForceNotVisible": construct.Flag,
})

CCameraComponent = Object({
    **CComponentFields,
    "fCurrentInterp": common_types.Float,
    "vCurrentPos": common_types.CVector3D,
    "vCurrentDir": common_types.CVector3D,
    "fDefaultInterp": common_types.Float,
    "fCurrentInterpChangeSpeed": common_types.Float,
    "fDefaultNear": common_types.Float,
    "fDefaultFar": common_types.Float,
    "bIgnoreSlomo": construct.Flag,
})

IPath = Object(IPathFields := {})

ISubPath = Object(ISubPathFields := {})

IPathNode = Object(IPathNodeFields := {})

SCameraRailNode = Object({
    **IPathNodeFields,
    "vPos": common_types.CVector3D,
    "wpLogicCamera": common_types.StrId,
})

SCameraSubRail = Object({
    **ISubPathFields,
    "tNodes": common_types.make_vector(SCameraRailNode),
})

SCameraRail = Object({
    **IPathFields,
    "tSubRails": common_types.make_vector(SCameraSubRail),
    "fMaxRailSpeed": common_types.Float,
    "fMinRailSpeed": common_types.Float,
    "fMaxRailDistance": common_types.Float,
})

CCameraRailComponent = Object({
    **CActorComponentFields,
    "oCameraRail": SCameraRail,
})


class EElevatorDirection(enum.IntEnum):
    UP = 0
    DOWN = 1
    Invalid = 2147483647


construct_EElevatorDirection = construct.Enum(construct.Int32ul, EElevatorDirection)


class ELoadingScreen(enum.IntEnum):
    E_LOADINGSCREEN_GUI_2D = 0
    E_LOADINGSCREEN_VIDEO = 1
    E_LOADINGSCREEN_ELEVATOR_UP = 2
    E_LOADINGSCREEN_ELEVATOR_DOWN = 3
    E_LOADINGSCREEN_MAIN_ELEVATOR_UP = 4
    E_LOADINGSCREEN_MAIN_ELEVATOR_DOWN = 5
    E_LOADINGSCREEN_TELEPORTER = 6
    E_LOADINGSCREEN_TRAIN_LEFT = 7
    E_LOADINGSCREEN_TRAIN_LEFT_AQUA = 8
    E_LOADINGSCREEN_TRAIN_RIGHT = 9
    E_LOADINGSCREEN_TRAIN_RIGHT_AQUA = 10
    Invalid = 2147483647


construct_ELoadingScreen = construct.Enum(construct.Int32ul, ELoadingScreen)

CElevatorUsableComponent = Object(CElevatorUsableComponentFields := {
    **CUsableComponentFields,
    "eDirection": construct_EElevatorDirection,
    "eLoadingScreen": construct_ELoadingScreen,
    "sLevelName": common_types.StrId,
    "sScenarioName": common_types.StrId,
    "sTargetSpawnPoint": common_types.StrId,
    "sMapConnectionId": common_types.StrId,
    "fMinTimeLoad": common_types.Float,
})

CCapsuleUsableComponent = Object({
    **CElevatorUsableComponentFields,
    "wpCapsule": common_types.StrId,
    "wpSkybase": common_types.StrId,
})

CCaterzillaAIComponent = Object(CBehaviorTreeAIComponentFields)


class ECaterzillaSpawnPointDir(enum.IntEnum):
    Front = 0
    Side = 1
    Invalid = 2147483647


construct_ECaterzillaSpawnPointDir = construct.Enum(construct.Int32ul, ECaterzillaSpawnPointDir)


class ECaterzillaSpawnPointOrder(enum.IntEnum):
    First = 0
    Second = 1
    InFrustrum = 2
    Invalid = 2147483647


construct_ECaterzillaSpawnPointOrder = construct.Enum(construct.Int32ul, ECaterzillaSpawnPointOrder)

CCaterzillaSpawnPointComponent = Object({
    **CSpawnPointComponentFields,
    "eSpawnDir": construct_ECaterzillaSpawnPointDir,
    "eSpawnOrder": construct_ECaterzillaSpawnPointOrder,
    "NumCaterzillas": common_types.UInt,
    "fTimeToGenerateNextWave": common_types.Float,
    "wpSpawnPointLinked": common_types.StrId,
    "fTimeToRespawnAllCaterzillas": common_types.Float,
    "aHomeLandmarks": common_types.make_vector(common_types.StrId),
    "bInOutSpawnPoint": construct.Flag,
})


class CCentralUnitComponent_ECentralUnitMode(enum.IntEnum):
    Default = 0
    Decayed = 1
    Cave = 2
    Shipyard = 3
    Invalid = 2147483647


construct_CCentralUnitComponent_ECentralUnitMode = construct.Enum(construct.Int32ul, CCentralUnitComponent_ECentralUnitMode)

CCentralUnitComponent_SStartPointInfo = Object({
    "wpStartPoint": common_types.StrId,
    "wpEmmyLandmark": common_types.StrId,
})

CCentralUnitWeightedEdges = Object({
    "sId": common_types.StrId,
    "pLogicShape": common_types.StrId,
    "fFactorToAdd": common_types.Float,
    "fFactorToMultiply": common_types.Float,
})

CCentralUnitComponent = Object(CCentralUnitComponentFields := {
    **CActorComponentFields,
    "eMode": construct_CCentralUnitComponent_ECentralUnitMode,
    "bStartEnabled": construct.Flag,
    "wpBossSpawnPoint": common_types.StrId,
    "wpCentralUnitAI": common_types.StrId,
    "wpBossAlive": common_types.StrId,
    "wpBossDestroyed": common_types.StrId,
    "wpBossDoor": common_types.StrId,
    "sBossCollisionCameraID": common_types.StrId,
    "wpEmmySpawnPoint": common_types.StrId,
    "tEmmyStartPointsInfo": common_types.make_vector(CCentralUnitComponent_SStartPointInfo),
    "wpEmmyZoneShape": common_types.StrId,
    "wpDestroySearchLandmark": common_types.StrId,
    "tEmmyForbiddenShapes": common_types.make_vector(common_types.StrId),
    "tEmmyWeightedShapes": common_types.make_vector(Pointer_CCentralUnitWeightedEdges.create_construct()),
    "bUnlockDoorsOnEmmyDead": construct.Flag,
    "tEmmyLockedDoors": common_types.make_vector(common_types.StrId),
    "tEmmyPhase2DeactivatedActors": common_types.make_vector(common_types.StrId),
    "wpStartCombatCheckpointStartPoint": common_types.StrId,
    "sStartCombatCheckpointSnapshotId": common_types.StrId,
    "wpDeadCheckpointStartPoint": common_types.StrId,
})

CCaveCentralUnitComponent = Object({
    **CCentralUnitComponentFields,
    "wpGate": common_types.StrId,
})


class CRinkaUnitComponent_ECentralUnitType(enum.IntEnum):
    Caves = 0
    Magma = 1
    Lab = 2
    Forest = 3
    Sanc = 4
    Invalid = 2147483647


construct_CRinkaUnitComponent_ECentralUnitType = construct.Enum(construct.Int32ul, CRinkaUnitComponent_ECentralUnitType)

CCentralUnitAIComponent = Object({
    **CBehaviorTreeAIComponentFields,
    "vSpawnPointActors": common_types.make_vector(common_types.StrId),
    "eType": construct_CRinkaUnitComponent_ECentralUnitType,
    "wpDoorCentralUnit": common_types.StrId,
    "wpDeadCutScenePlayer": common_types.StrId,
})

CCentralUnitCannonAIComponent = Object(CAIComponentFields)

CProjectileMovement = Object(CProjectileMovementFields := {
    **CWeaponMovementFields,
    "fMaxDist": common_types.Float,
    "fMaxLifeTime": common_types.Float,
    "sCollisionFX": common_types.StrId,
    "fFXAngZOffset": common_types.Float,
    "fFXScl": common_types.Float,
    "sNoDamageFX": common_types.StrId,
    "sEnergyCollisionFX": common_types.StrId,
})

CCentralUnitCannonBeamMovementComponent = Object(CProjectileMovementFields)

CChainReactionActionSwitcherComponent = Object(CComponentFields)

CChangeStageNavMeshItemComponent = Object(CComponentFields)

CCharacterMovement = Object(CCharacterMovementFields := CMovementComponentFields)

CChozoCommanderAIComponent = Object({
    **CBossAIComponentFields,
    "bUltimateGrabTestMode": construct.Flag,
    "wpUltimateGrabLandmark": common_types.StrId,
    "wpDeadCutScenePlayer": common_types.StrId,
    "wpPhase2CutscenePlayer": common_types.StrId,
    "wpPhase3CutscenePlayer": common_types.StrId,
    "wpPhase3EndLeftCutscenePlayer": common_types.StrId,
    "wpPhase3EndRightCutscenePlayer": common_types.StrId,
})

CChozoCommanderEnergyShardsFragmentMovementComponent = Object(CProjectileMovementFields)

CChozoCommanderEnergyShardsSphereMovementComponent = Object(CProjectileMovementFields)

CChozoCommanderSentenceSphereLifeComponent = Object(CBasicLifeComponentFields)

CChozoCommanderSentenceSphereMovementComponent = Object(CProjectileMovementFields)

CChozoCommanderXLifeComponent = Object({
    **CLifeComponentFields,
    "wpIntroductionCutScenePlayer": common_types.StrId,
    "wpDeathCutScenePlayer": common_types.StrId,
})

CChozoRobotSoldierAIComponent = Object({
    **CBossAIComponentFields,
    "bAlternativeSkin": construct.Flag,
    "wpPatrolPath": common_types.StrId,
    "tShootingPositions": common_types.make_vector(common_types.StrId),
})

CChozoRobotSoldierBeamMovementComponent = Object(CProjectileMovementFields)


class CChozoWarriorAIComponent_ETransformationType(enum.IntEnum):
    NONE = 0
    Quick = 1
    Full = 2
    Quick_without_init = 3
    Invalid = 2147483647


construct_CChozoWarriorAIComponent_ETransformationType = construct.Enum(construct.Int32ul, CChozoWarriorAIComponent_ETransformationType)

CChozoWarriorAIComponent = Object(CChozoWarriorAIComponentFields := {
    **CBossAIComponentFields,
    "wpChozoWarrioXSpawnPoint": common_types.StrId,
    "eTransformationType": construct_CChozoWarriorAIComponent_ETransformationType,
})

CChozoWarriorEliteAIComponent = Object(CChozoWarriorAIComponentFields)

CChozoWarriorXAIComponent = Object(CChozoWarriorXAIComponentFields := CChozoWarriorAIComponentFields)

CChozoWarriorXEliteAIComponent = Object(CChozoWarriorXAIComponentFields)

CChozoWarriorXSpitMovementComponent = Object(CProjectileMovementFields)

CChozoZombieXAIComponent = Object(CBehaviorTreeAIComponentFields)

CChozoZombieXSpawnPointComponent = Object(CSpawnPointComponentFields)

CChozombieFXComponent = Object(CSceneComponentFields)


class CTriggerComponent_EEvent(enum.IntEnum):
    OnEnter = 0
    OnExit = 1
    OnAllExit = 2
    OnStay = 3
    OnEnable = 4
    OnDisable = 5
    TE_COUNT = 6
    Invalid = 2147483647


construct_CTriggerComponent_EEvent = construct.Enum(construct.Int32ul, CTriggerComponent_EEvent)

CTriggerLogicAction = Object(CTriggerLogicActionFields := {})

CTriggerComponent_SActivationCondition = Object({
    "sID": common_types.StrId,
    "sCharclasses": common_types.StrId,
    "bEnabled": construct.Flag,
    "bAlways": construct.Flag,
    "bDone": construct.Flag,
    "fExecutesEvery": common_types.Float,
    "fExecutesEveryRandomRange": common_types.Float,
    "fLastExecution": common_types.Float,
    "eEvent": construct_CTriggerComponent_EEvent,
    "vLogicActions": common_types.make_vector(Pointer_CTriggerLogicAction.create_construct()),
})

CTriggerComponent = Object(CTriggerComponentFields := {
    **CComponentFields,
    "bCallEntityLuaCallback": construct.Flag,
    "iReverb": common_types.Int,
    "iLowPassFilter": common_types.Int,
    "sOnEnable": common_types.StrId,
    "sOnDisable": common_types.StrId,
    "bOnEnableAlways": construct.Flag,
    "bOnDisableAlways": construct.Flag,
    "bStartEnabled": construct.Flag,
    "bCheckAllEntities": construct.Flag,
    "bPersistentState": construct.Flag,
    "sSfxType": common_types.StrId,
    "lstActivationConditions": common_types.make_vector(Pointer_CTriggerComponent_SActivationCondition.create_construct()),
})

CColliderTriggerComponent = Object({
    **CTriggerComponentFields,
    "lnkShape": common_types.StrId,
})

CCollisionMaterialCacheComponent = Object(CComponentFields)

CConstantMovement = Object(CCharacterMovementFields)

CCooldownXBossAIComponent = Object({
    **CBossAIComponentFields,
    "wpWindTunnelDamageTrigger": common_types.StrId,
    "wpLavaCarpetFloorFX": common_types.StrId,
    "wpCoolShinesparkTrigger": common_types.StrId,
    "wpDeathCutscenePlayer": common_types.StrId,
    "wpDeathFromGrabCutscenePlayer": common_types.StrId,
})

CCooldownXBossFireBallMovementComponent = Object(CProjectileMovementFields)

CCooldownXBossWeakPointLifeComponent = Object(CBasicLifeComponentFields)

CCoreXAIComponent = Object(CBossAIComponentFields)

CCubeMapComponent = Object({
    **CComponentFields,
    "vCubePos": common_types.CVector3D,
    "fAttMin": common_types.Float,
    "fAttMax": common_types.Float,
    "vBoxBounds": common_types.CVector3D,
    "fIntensity": common_types.Float,
    "bEnableCulling": construct.Flag,
    "sTexturePathSpecular": common_types.StrId,
    "sTexturePathDiffuse": common_types.StrId,
})

CCutsceneComponent_SActorInfo = Object(CCutsceneComponent_SActorInfoFields := {
    "sId": common_types.StrId,
    "lnkActor": common_types.StrId,
    "bStartingVisibleState": construct.Flag,
    "bReceiveLogicUpdate": construct.Flag,
    "vctVisibilityPerTake": common_types.make_vector(construct.Flag),
})

CCutsceneComponent = Object({
    **CActorComponentFields,
    "sCutsceneName": common_types.StrId,
    "bDisableScenarioEntitiesOnPlay": construct.Flag,
    "vOriginalPos": common_types.CVector3D,
    "vctCutscenesOffsets": common_types.make_vector(common_types.CVector3D),
    "vctExtraInvolvedSubareas": common_types.make_vector(common_types.StrId),
    "vctExtraInvolvedActors": common_types.make_vector(CCutsceneComponent_SActorInfo),
    "vctOnBeforeCutsceneStartsLA": common_types.make_vector(Pointer_CTriggerLogicAction.create_construct()),
    "vctOnAfterCutsceneEndsLA": common_types.make_vector(Pointer_CTriggerLogicAction.create_construct()),
    "bHasSamusAsExtraActor": construct.Flag,
})

CCutsceneTriggerComponent = Object({
    **CBaseTriggerComponentFields,
    "lnkTargetCutsceneActor": common_types.StrId,
    "bOneShot": construct.Flag,
})

CSluggerAIComponent = Object(CSluggerAIComponentFields := CBehaviorTreeAIComponentFields)

CDaivoAIComponent = Object({
    **CSluggerAIComponentFields,
    "wpSwarmActor": common_types.StrId,
    "wpSwarmAOIBegin": common_types.StrId,
    "wpSwarmAOIEnd": common_types.StrId,
    "fChaseForcedDistanceToWall": common_types.Float,
})

CSwarmControllerComponent = Object(CSwarmControllerComponentFields := {
    **CComponentFields,
    "wpPathToFollow": common_types.StrId,
    "ePathType": construct_IPath_EType,
    "fGroupVelocity": common_types.Float,
})

CFlockingSwarmControllerComponent = Object(CFlockingSwarmControllerComponentFields := CSwarmControllerComponentFields)

CRedenkiSwarmControllerComponent = Object(CRedenkiSwarmControllerComponentFields := CFlockingSwarmControllerComponentFields)

CDaivoSwarmControllerComponent = Object(CRedenkiSwarmControllerComponentFields)

CDamageComponent = Object(CComponentFields)

CDamageTriggerConfig = Object({
    "fDamagePerTime": common_types.Float,
    "fInBetweenDamageTime": common_types.Float,
    "fInitTimeDamageIncrease": common_types.Float,
    "fDamageIncreaseAmount": common_types.Float,
    "fMaxDamage": common_types.Float,
})

CDamageTriggerComponent = Object({
    **CBaseDamageTriggerComponentFields,
    "oConfig": CDamageTriggerConfig,
})

CDemolitionBlockLifeComponent = Object(CDemolitionBlockLifeComponentFields := {
    **CLifeComponentFields,
    "wpOtherBlock": common_types.StrId,
})

CDemolitionBlockActivatableActorLifeComponent = Object({
    **CDemolitionBlockLifeComponentFields,
    "oActivatableObjController": common_types.StrId,
})

CDemolitionBlockComponent = Object({
    **CActivatableComponentFields,
    "vObjsToEnable": common_types.make_vector(common_types.StrId),
    "vObjsToDisable": common_types.make_vector(common_types.StrId),
})

CDemolitionBlockSonarTargetComponent = Object(CSonarTargetComponentFields)

CDirLightComponent = Object({
    **CBaseLightComponentFields,
    "vDir": common_types.CVector3D,
    "fAnimFrame": common_types.Float,
    "bCastShadows": construct.Flag,
})

CDizzeanSwarmControllerComponent = Object(CFlockingSwarmControllerComponentFields)

CDoorLifeComponent = Object(CDoorLifeComponentFields := {
    **CItemLifeComponentFields,
    "fMaxDistanceOpened": common_types.Float,
    "wpLeftDoorShieldEntity": common_types.StrId,
    "wpRightDoorShieldEntity": common_types.StrId,
    "fMinTimeOpened": common_types.Float,
    "bStayOpen": construct.Flag,
    "bStartOpened": construct.Flag,
    "bOnBlackOutOpened": construct.Flag,
    "bDoorIsWet": construct.Flag,
    "bFrozenDuringColdown": construct.Flag,
    "iAreaLeft": common_types.Int,
    "iAreaRight": common_types.Int,
    "aVignettes": common_types.make_vector(common_types.StrId),
    "sShieldEntity": common_types.StrId,
})

CDoorCentralUnitLifeComponent = Object({
    **CDoorLifeComponentFields,
    "eMode": construct_CCentralUnitComponent_ECentralUnitMode,
})

CDoorEmmyFXComponent = Object(CComponentFields)

CDoorGrapplePointComponent = Object(CPullableGrapplePointComponentFields)

CDredhedAIComponent = Object(CBehaviorTreeAIComponentFields)

CDredhedAttackComponent = Object(CAIAttackComponentFields)

CDropComponent = Object(CComponentFields)

CDroppableComponent = Object(CDroppableComponentFields := {
    **CComponentFields,
    "fMaxTimeAlive": common_types.Float,
})

CDroppableLifeComponent = Object({
    **CDroppableComponentFields,
    "fAmount": common_types.Float,
})

CDroppableMissileComponent = Object({
    **CDroppableComponentFields,
    "sItemMax": common_types.StrId,
    "sItemCurrent": common_types.StrId,
})

CDroppablePowerBombComponent = Object({
    **CDroppableComponentFields,
    "sItemMax": common_types.StrId,
    "sItemCurrent": common_types.StrId,
})

CDroppableSpecialEnergyComponent = Object({
    **CDroppableComponentFields,
    "fAmount": common_types.Float,
})

CDropterAIComponent = Object(CBehaviorTreeAIComponentFields)

CDummyAIComponent = Object(CAIComponentFields)

CDummyMovement = Object(CMovementComponentFields)

CDummyPullableGrapplePointComponent = Object(CPullableGrapplePointComponentFields)


class CElectricGeneratorComponent_EBlackOutZone(enum.IntEnum):
    Zone1 = 0
    Zone2 = 1
    Unknown = 2
    Invalid = 2147483647


construct_CElectricGeneratorComponent_EBlackOutZone = construct.Enum(construct.Int32ul, CElectricGeneratorComponent_EBlackOutZone)

CElectricGeneratorComponent = Object({
    **CUsableComponentFields,
    "eBlackOutZone": construct_CElectricGeneratorComponent_EBlackOutZone,
    "sOnEnterUseLuaCallback": common_types.StrId,
    "vAffectedSubAreas": common_types.make_vector(common_types.StrId),
})

CElectricReactionComponent = Object(CElectricReactionComponentFields := CComponentFields)

CElectrifyingAreaComponent = Object({
    **CComponentFields,
    "bShouldUpdateAreaOnStart": construct.Flag,
})

CElevatorCommanderUsableComponent = Object({
    **CUsableComponentFields,
    "sTargetSpawnPoint": common_types.StrId,
})

CEmergencyLightElectricReactionComponent = Object(CElectricReactionComponentFields)

CEmmyOverrideDeathPositionDef = Object({
    "wpLandmark": common_types.StrId,
    "wpLogicShape": common_types.StrId,
})

CEmmyAutoForbiddenEdgesDef = Object({
    "wpCheckSamusLogicShape": common_types.StrId,
    "wpCheckEmmyLogicShape": common_types.StrId,
    "tForbiddenLogicShapes": common_types.make_vector(common_types.StrId),
    "tWeightedLogicShapeIDs": common_types.make_vector(common_types.StrId),
})

CEmmyAutoGlobalSmartLinkDef = Object({
    "wpStartLandmark": common_types.StrId,
    "tEndLandmarks": common_types.make_vector(common_types.StrId),
    "wpActivateLogicShape": common_types.StrId,
})

CEmmyAIComponent = Object(CEmmyAIComponentFields := {
    **CBehaviorTreeAIComponentFields,
    "sCurrentPatrol": common_types.StrId,
    "bPerceptionFeedbackEnabled": construct.Flag,
    "bShowBehaviorDebug": construct.Flag,
    "fPhaseDisplacementFactor": common_types.Float,
    "fGrabQTEFailTime": common_types.Float,
    "bPlayerNoiseEnabled": construct.Flag,
    "fPatrolSearchMaxTime": common_types.Float,
    "fGrabZoomOffset": common_types.Float,
    "fGrabZoomTime": common_types.Float,
    "bTargetDetectionEnabled": construct.Flag,
    "bTargetInsideEmmyZone": construct.Flag,
    "tOverrideGrabPosition": common_types.make_vector(Pointer_CEmmyOverrideDeathPositionDef.create_construct()),
    "tOverrideDeathPosition": common_types.make_vector(Pointer_CEmmyOverrideDeathPositionDef.create_construct()),
    "tAutoForbiddenEdges": common_types.make_vector(Pointer_CEmmyAutoForbiddenEdgesDef.create_construct()),
    "tAutoGlobalSmartLinks": common_types.make_vector(Pointer_CEmmyAutoGlobalSmartLinkDef.create_construct()),
    "tLogicShapesToAvoidCornerReposition": common_types.make_vector(common_types.StrId),
})

CEmmyAttackComponent = Object(CAIAttackComponentFields)

CEmmyCaveAIComponent = Object(CEmmyAIComponentFields)

CEmmyForestAIComponent = Object(CEmmyAIComponentFields)

CEmmyLabAIComponent = Object(CEmmyAIComponentFields)

CEmmyMagmaAIComponent = Object(CEmmyAIComponentFields)

CEnemyMovement = Object(CEnemyMovementFields := CCharacterMovementFields)

CEmmyMovement = Object(CEnemyMovementFields)

CEmmyProtoAIComponent = Object({
    **CEmmyAIComponentFields,
    "sDirtMaterialConstantId": common_types.StrId,
})

CEmmySancAIComponent = Object({
    **CEmmyAIComponentFields,
    "tFast4LegTransformationMagnet": common_types.make_vector(common_types.StrId),
    "wpForceEmmyPerceptionVisionConeOffShape": common_types.StrId,
    "bZipLine004Behavior": construct.Flag,
    "wpPhase2HeatEnabledLogicShape": common_types.StrId,
})

CEmmyShipyardAIComponent = Object(CEmmyAIComponentFields)

CEmmySpawnPointComponent = Object(CSpawnPointComponentFields)

CEmmyValveComponent = Object(CComponentFields)

CEventPropComponent = Object(CEventPropComponentFields := CComponentFields)

CEmmyWakeUpComponent = Object({
    **CEventPropComponentFields,
    "wpCentralUnit": common_types.StrId,
})

CEmmyWaveMovementComponent = Object(CProjectileMovementFields)

CEnhanceWeakSpotComponent = Object(CEnhanceWeakSpotComponentFields := CComponentFields)

CEscapeSequenceExplosionComponent = Object(CComponentFields)

CEvacuationCountDown = Object({
    **CEventPropComponentFields,
    "vEntitiesToPowerOff": common_types.make_vector(common_types.StrId),
})

CEventScenarioComponent = Object({
    **CComponentFields,
    "vEventActors": common_types.make_vector(common_types.StrId),
    "sIdleAction": common_types.StrId,
    "sReactionAction": common_types.StrId,
    "sFinishedAction": common_types.StrId,
    "sRecoveryAction": common_types.StrId,
    "bPersistent": construct.Flag,
    "bDisableOnXParasite": construct.Flag,
    "bDisableOnCoolDown": construct.Flag,
    "bReactOnFireOnly": construct.Flag,
    "bReactOnEnemies": construct.Flag,
    "bReactToSamus": construct.Flag,
    "bIgnoreSamusWithOC": construct.Flag,
    "bReactToSamusFiring": construct.Flag,
    "bReactToFireImpact": construct.Flag,
    "fTimeForRecoveryOnStay": common_types.Float,
    "fTimeForRecoveryOnExit": common_types.Float,
    "fInitRelaxFrame": common_types.Float,
})

CFXComponent = Object({
    **CSceneComponentFields,
    "fSelectedHighRadius": common_types.Float,
    "fSelectedLowRadius": common_types.Float,
})

CFactionComponent = Object(CComponentFields)

CFakePhysicsMovement = Object(CMovementComponentFields)

CFanComponent = Object({
    **CBaseTriggerComponentFields,
    "fWindLength": common_types.Float,
    "fHurricaneLength": common_types.Float,
    "fBarrierLength": common_types.Float,
    "fWidth": common_types.Float,
    "fParticleScale": common_types.Float,
})

CFanCoolDownComponent = Object(CComponentFields)

CFingSwarmControllerComponent = Object(CFlockingSwarmControllerComponentFields)

CFireComponent = Object(CComponentFields)

CFloatingPropActingComponent = Object(CComponentFields)

CShockWaveComponent = Object(CShockWaveComponentFields := CComponentFields)

CFloorShockWaveComponent = Object(CShockWaveComponentFields)

CFootstepPlatformComponent = Object({
    **CComponentFields,
    "wpActivableEntity": common_types.StrId,
    "wpPartnerFootStepPlatformEntity": common_types.StrId,
    "sCallbackOnOpened": common_types.StrId,
    "sCallbackOnClosed": common_types.StrId,
})


class CForcedMovementAreaComponent_EForcedDirection(enum.IntEnum):
    NONE = 0
    Right = 1
    Left = 2
    Invalid = 2147483647


construct_CForcedMovementAreaComponent_EForcedDirection = construct.Enum(construct.Int32ul, CForcedMovementAreaComponent_EForcedDirection)

CForcedMovementAreaComponent = Object({
    **CActorComponentFields,
    "bForcedAreaOnce": construct.Flag,
    "eForcedDirection": construct_CForcedMovementAreaComponent_EForcedDirection,
})

CFreezeRoomConfig = Object({
    "fActivationDelayTime": common_types.Float,
    "fDamagePerTime": common_types.Float,
    "fInBetweenDamageTime": common_types.Float,
    "fInitTimeDamageIncrease": common_types.Float,
    "fDamageIncreaseAmount": common_types.Float,
    "fMaxDamage": common_types.Float,
})

CFreezeRoomCoolConfig = Object({
    "fActivationDelayTime": common_types.Float,
    "fDamagePerTime": common_types.Float,
    "fInBetweenDamageTime": common_types.Float,
    "fInitTimeDamageIncrease": common_types.Float,
    "fDamageIncreaseAmount": common_types.Float,
    "fMaxDamage": common_types.Float,
})

CFreezeRoomComponent = Object({
    **CBaseDamageTriggerComponentFields,
    "oFreezeConfig": CFreezeRoomConfig,
    "oCoolConfig": CFreezeRoomCoolConfig,
    "sEnterZoneSound": common_types.StrId,
    "sVisualPresetOverride": common_types.StrId,
})

CFrozenComponent = Object(CFrozenComponentFields := CComponentFields)

CFrozenAsFrostbiteComponent = Object(CFrozenComponentFields)

CFrozenAsPlatformComponent = Object(CFrozenComponentFields)

CFrozenPlatformComponent = Object({
    **CComponentFields,
    "wpWeightPlatform": common_types.StrId,
})

CFulmiteBellyMineAIComponent = Object(CBehaviorTreeAIComponentFields)

CFulmiteBellyMineAttackComponent = Object(CAIAttackComponentFields)

CFulmiteBellyMineMovementComponent = Object(CProjectileMovementFields)

CFusibleBoxComponent = Object(CComponentFields)

CGobblerAIComponent = Object(CBehaviorTreeAIComponentFields)

CGobblerSpawnPointComponent = Object({
    **CSpawnPointComponentFields,
    "wpDoor": common_types.StrId,
    "wpWeb": common_types.StrId,
})

CGoliathAIComponent = Object(CGoliathAIComponentFields := CBaseBigFistAIComponentFields)

CGoliathXAIComponent = Object({
    **CGoliathAIComponentFields,
    "wpCoreXSpawnPoint": common_types.StrId,
})

CGoliathXBurstProjectionBombMovement = Object(CBombMovementFields)

CGooplotAIComponent = Object(CGooplotAIComponentFields := CBehaviorTreeAIComponentFields)

CGooshockerAIComponent = Object(CGooplotAIComponentFields)


class CGrabComponent_ELinkMode(enum.IntEnum):
    NONE = 0
    RootToDC_Grab = 1
    FeetToRoot = 2
    Invalid = 2147483647


construct_CGrabComponent_ELinkMode = construct.Enum(construct.Int32ul, CGrabComponent_ELinkMode)

CGrabComponent = Object({
    **CComponentFields,
    "bIsInGrab": construct.Flag,
    "eLinkModeAsGrabber": construct_CGrabComponent_ELinkMode,
})

CGrappleBeamComponent = Object({
    **CWeaponMovementFields,
    "sIniFXId": common_types.StrId,
    "sEndFXId": common_types.StrId,
    "sGrappleFX": common_types.StrId,
})

CGroundShockerAIComponent = Object(CBaseGroundShockerAIComponentFields)

CGunComponent = Object(CGunComponentFields := CComponentFields)

CHangableGrappleSurfaceComponent = Object(CHangableGrappleSurfaceComponentFields := CGrapplePointComponentFields)

CHangableGrappleMagnetSlidingBlockComponent = Object(CHangableGrappleSurfaceComponentFields)

CHangableGrapplePointComponent = Object(CGrapplePointComponentFields)

CHeatRoomConfig = Object({
    "fActivationDelayTime": common_types.Float,
    "fDamagePerTime": common_types.Float,
    "fInBetweenDamageTime": common_types.Float,
    "fInitTimeDamageIncrease": common_types.Float,
    "fDamageIncreaseAmount": common_types.Float,
    "fMaxDamage": common_types.Float,
    "bActivationDelayTimeOnlyForFirstTime": construct.Flag,
})

CHeatRoomCoolConfig = Object({
    "fActivationDelayTime": common_types.Float,
    "fDamagePerTime": common_types.Float,
    "fInBetweenDamageTime": common_types.Float,
    "fInitTimeDamageIncrease": common_types.Float,
    "fDamageIncreaseAmount": common_types.Float,
    "fMaxDamage": common_types.Float,
    "bActivationDelayTimeOnlyForFirstTime": construct.Flag,
})

CHeatRoomComponent = Object({
    **CBaseDamageTriggerComponentFields,
    "oHeatConfig": CHeatRoomConfig,
    "oCoolConfig": CHeatRoomCoolConfig,
    "sEnterZoneSound": common_types.StrId,
    "sVisualPresetOverride": common_types.StrId,
    "pEnvironmentFXActor": common_types.StrId,
    "vEnvironmentFXActors": common_types.make_vector(common_types.StrId),
})

CHeatableShieldComponent = Object(CComponentFields)

CHeatableShieldEnhanceWeakSpotComponent = Object(CEnhanceWeakSpotComponentFields)

CHecathonAIComponent = Object({
    **CBehaviorTreeAIComponentFields,
    "wpPatrolPath": common_types.StrId,
    "ePatrolPathType": construct_IPath_EType,
    "wpHarassPath": common_types.StrId,
    "eHarassPathType": construct_IPath_EType,
    "fTimeToGoPatrol": common_types.Float,
    "fSpeed": common_types.Float,
    "bIsEating": construct.Flag,
    "bCanEat": construct.Flag,
    "fPatrolEatDuration": common_types.Float,
    "fPatrolEatCooldown": common_types.Float,
    "uMask": common_types.UInt,
})

CHecathonLifeComponent = Object(CEnemyLifeComponentFields)

CHecathonPlanktonFXComponent = Object({
    **CSceneComponentFields,
    "sModelResPath": common_types.StrId,
})

CHomingMovement = Object(CProjectileMovementFields)

CHydrogigaAIComponent = Object({
    **CBossAIComponentFields,
    "wpPresentationCutscenePlayer": common_types.StrId,
    "wpDeadCutScenePlayer": common_types.StrId,
})

CMagnetSlidingBlockComponent = Object(CMagnetSlidingBlockComponentFields := {
    **CComponentFields,
    "fTimePreparingToOpen": common_types.Float,
    "fTimeToCompleteMovementTowardsEnd": common_types.Float,
    "fTimeToCompleteMovementTowardsStart": common_types.Float,
    "bContinueMovingOnStopHang": construct.Flag,
    "wpRail": common_types.StrId,
    "wpDoorOpeningOnAnimatedCamera": common_types.StrId,
    "fTotalMetersToMoveY": common_types.Float,
    "fTimeToOpen": common_types.Float,
    "bAutoOpenAfterPreparing": construct.Flag,
})

CHydrogigaZiplineComponent = Object({
    **CMagnetSlidingBlockComponentFields,
    "lstLinkedMagnetSlidingBlocks": common_types.make_vector(common_types.StrId),
})

CHydrogigaZiplineRailComponent = Object({
    **CComponentFields,
    "lstAttachedZiplines": common_types.make_vector(common_types.StrId),
})

CHyperBeamBlockLifeComponent = Object(CItemLifeComponentFields)

CMissileMovement = Object(CMissileMovementFields := {
    **CProjectileMovementFields,
    "sTrailFX": common_types.StrId,
    "sBurstFX": common_types.StrId,
    "sIgnitionFX": common_types.StrId,
    "sSPRNoDamageFX": common_types.StrId,
})

CIceMissileMovement = Object(CMissileMovementFields)

CInfesterAIComponent = Object(CBehaviorTreeAIComponentFields)

CInfesterBallAIComponent = Object(CBehaviorTreeAIComponentFields)

CInfesterBallAttackComponent = Object(CAIAttackComponentFields)

CInfesterBallLifeComponent = Object(CEnemyLifeComponentFields)

CInfesterBallMovementComponent = Object(CProjectileMovementFields)

CInputComponent = Object({
    **CComponentFields,
    "bInputIgnored": construct.Flag,
})

CInterpolationComponent = Object(CComponentFields)

CInventoryComponent = Object(CComponentFields)

CKraidAIComponent = Object({
    **CBossAIComponentFields,
    "wpStage1ArenaShape": common_types.StrId,
    "wpStage2ArenaShape": common_types.StrId,
    "wpPhase2CutScenePlayer": common_types.StrId,
    "wpDeadCutScenePlayer": common_types.StrId,
    "wpDeadFromZiplineOrMBCutscenePlayer": common_types.StrId,
})

CKraidAcidBlobsMovementComponent = Object(CProjectileMovementFields)

CKraidBouncingCreaturesMovementComponent = Object(CProjectileMovementFields)

CKraidNailMovementComponent = Object(CProjectileMovementFields)

CKraidShockerSplashMovementComponent = Object(CProjectileMovementFields)

CMovablePlatformComponent = Object(CMovablePlatformComponentFields := CMovementComponentFields)

CKraidSpikeMovablePlatformComponent = Object(CMovablePlatformComponentFields)

CLandmarkComponent = Object({
    **CActorComponentFields,
    "sLandmarkID": common_types.StrId,
})

CLiquidPoolBaseComponent = Object(CLiquidPoolBaseComponentFields := {
    **CBaseDamageTriggerComponentFields,
    "sModelPath": common_types.StrId,
    "eLowPassFilter": construct_base_snd_ELowPassFilter,
    "eReverb": construct_base_snd_EReverbIntensity,
})

CLavaPoolConfig = Object({
    "fDamagePerTime": common_types.Float,
    "fInBetweenDamageTime": common_types.Float,
    "fInitTimeDamageIncrease": common_types.Float,
    "fDamageIncreaseAmount": common_types.Float,
    "fMaxDamage": common_types.Float,
})

CLavaPoolComponent = Object({
    **CLiquidPoolBaseComponentFields,
    "oConfig": CLavaPoolConfig,
    "fChangeTime": common_types.Float,
})

CLavaPumpComponent = Object(CActivatableComponentFields)

CThermalReactionComponent = Object(CThermalReactionComponentFields := CComponentFields)

CLavapumpThermalReactionComponent = Object(CThermalReactionComponentFields)

CLifeRechargeComponent = Object({
    **CUsableComponentFields,
    "sRechargeFX": common_types.StrId,
    "sEyeRFX": common_types.StrId,
    "sEyeLFX": common_types.StrId,
})

CLightingComponent = Object(CComponentFields)

CLineBombMovement = Object(CBombMovementFields)

CLiquidSimulationComponent = Object(CComponentFields)

CLockOnMissileMovement = Object(CMissileMovementFields)

CLogicActionTriggerComponent = Object({
    **CComponentFields,
    "vLogicActions": common_types.make_vector(Pointer_CTriggerLogicAction.create_construct()),
})

CLogicCamera = Object({
    **CGameObjectFields,
    "sID": common_types.StrId,
    "sControllerID": common_types.StrId,
    "bStatic": construct.Flag,
    "v3Position": common_types.CVector3D,
    "v3Dir": common_types.CVector3D,
    "fFovX": common_types.Float,
    "fMinExtraZDist": common_types.Float,
    "fMaxExtraZDist": common_types.Float,
    "fDefaultInterp": common_types.Float,
})

CLogicCameraComponent = Object({
    **CActorComponentFields,
    "rLogicCamera": Pointer_CLogicCamera.create_construct(),
})

CLogicLookAtPlayerComponent = Object(CComponentFields)

SLogicPathNode = Object({
    **IPathNodeFields,
    "vPos": common_types.CVector3D,
    "fSwarmRadius": common_types.Float,
    "fDiversionChance": common_types.Float,
})

SLogicSubPath = Object({
    **ISubPathFields,
    "tNodes": common_types.make_vector(SLogicPathNode),
})

SLogicPath = Object({
    **IPathFields,
    "tSubPaths": common_types.make_vector(SLogicSubPath),
})

CLogicPathComponent = Object({
    **CActorComponentFields,
    "logicPath": SLogicPath,
})

CLogicPathNavMeshItemComponent = Object(CNavMeshItemComponentFields)

CMagmaCentralUnitComponent = Object({
    **CCentralUnitComponentFields,
    "wpGate": common_types.StrId,
})

CMagmaKraidPistonPlatformComponent = Object(CComponentFields)

CMagmaKraidScenarioControllerComponent = Object({
    **CComponentFields,
    "wpBackGorundPipesEntity": common_types.StrId,
    "wpPistonEntity": common_types.StrId,
})

CMagmaKraidSpikeComponent = Object(CComponentFields)

CMagnetMovablePlatformComponent = Object(CMagnetMovablePlatformComponentFields := CMovablePlatformComponentFields)

CMagnetSlidingBlockCounterWeightMovablePlatformComponent = Object({
    **CMagnetMovablePlatformComponentFields,
    "wpReferenceEntity": common_types.StrId,
})

CMagnetSlidingBlockRailComponent = Object(CComponentFields)

CMagnetSlidingBlockWithCollisionsComponent = Object(CMagnetSlidingBlockComponentFields)

CMagnetSurfaceComponent = Object(CActorComponentFields)

CMagnetSurfaceHuskComponent = Object(CComponentFields)

CMapAcquisitionComponent = Object({
    **CUsableComponentFields,
    "sLiteralID": common_types.StrId,
})

CMassiveCaterzillaSpawnGroupComponent = Object({
    **CSpawnGroupComponentFields,
    "fTimeToSpawn": common_types.Float,
    "fTimeToSpawnAfterDespawn": common_types.Float,
    "iNumCaterzillas": common_types.Int,
})

CMaterialFXComponent = Object(CSceneComponentFields)

CMeleeComponent = Object({
    **CComponentFields,
    "sBlockSyncFX": common_types.StrId,
})

CMenuAnimationChangeComponent = Object(CComponentFields)

CModelInstanceComponent = Object({
    **CSceneComponentFields,
    "sModelPath": common_types.StrId,
    "vScale": common_types.CVector3D,
})

CModelUpdaterComponent = Object(CModelUpdaterComponentFields := {
    **CSceneComponentFields,
    "sDefaultModelPath": common_types.StrId,
})

CMorphBallLauncherComponent = Object({
    **CComponentFields,
    "wpLauncherExit": common_types.StrId,
    "sTravellingAction": common_types.StrId,
    "bManualActivation": construct.Flag,
})

CMorphBallLauncherExitComponent = Object({
    **CComponentFields,
    "vExpelDirection": common_types.CVector2D,
    "fExpelImpulseSize": common_types.Float,
    "fInputIgnoreTimeAfterExpelling": common_types.Float,
    "fFrictionIgnoreTimeAfterExpelling": common_types.Float,
    "bWantsRelocationAndExpelImpulse": construct.Flag,
    "bWantsAutomaticOpenOnStartLaunchProcess": construct.Flag,
})

CPlayerMovement = Object(CPlayerMovementFields := {
    **CCharacterMovementFields,
    "bForcedAnalogInput": construct.Flag,
    "fImpactImpulseX": common_types.Float,
    "fImpactImpulseY": common_types.Float,
    "fImpactAirImpulseY": common_types.Float,
    "fImpactHardImpulseX": common_types.Float,
    "fImpactHardImpulseY": common_types.Float,
    "fImpactHardAirImpulseY": common_types.Float,
})

CMorphBallMovement = Object({
    **CPlayerMovementFields,
    "bIsMorphBall": construct.Flag,
    "bIsSamus": construct.Flag,
    "fRunningSpeedX": common_types.Float,
    "fSpiderRunningSpeedX": common_types.Float,
    "fSpiderImpulseSpeedX": common_types.Float,
    "fAirRunningSpeedX": common_types.Float,
    "fSpeedY": common_types.Float,
    "fHighJumpBootSpeedY": common_types.Float,
    "fMinSpeedY": common_types.Float,
    "fMaxSpeedY": common_types.Float,
    "fTimeOnAirAllowingJump": common_types.Float,
    "fNoJumpingGravityFactor": common_types.Float,
    "fImpactIgnoreInputTime": common_types.Float,
    "fImpactIgnoreFrictionTime": common_types.Float,
    "sMovingFX": common_types.StrId,
    "sMovingOilFX": common_types.StrId,
    "sMovingOilSlidingFX": common_types.StrId,
    "sTransformationCustomMaterialFX": common_types.StrId,
    "sTransformationParticlesFX": common_types.StrId,
    "sImpulseFX": common_types.StrId,
    "sFallDustFX": common_types.StrId,
    "sFallOilFX": common_types.StrId,
    "fMinTimeInOilState": common_types.Float,
    "fTotalTimeIgnoringGoToSpider": common_types.Float,
    "sSpiderImpulseEndShake": common_types.StrId,
})

CMovableGrapplePointComponent = Object(CPullableGrapplePointComponentFields)

CMultiLockOnBlockComponent = Object({
    **CComponentFields,
    "vMultiLockOnPoints": common_types.make_vector(common_types.StrId),
})

CMultiLockOnPointComponent = Object({
    **CActivatableByProjectileComponentFields,
    "wpMultiLockOnBlock": common_types.StrId,
})

CMultiModelUpdaterComponent = Object(CMultiModelUpdaterComponentFields := {
    **CModelUpdaterComponentFields,
    "sModelAlias": common_types.StrId,
})

CMushroomPlatformComponent = Object({
    **CLifeComponentFields,
    "fAlertTimeToRetract": common_types.Float,
    "fRetractedTimeToRelax": common_types.Float,
})

CNailongAIComponent = Object({
    **CBehaviorTreeAIComponentFields,
    "wpPatrolPath": common_types.StrId,
    "ePatrolPathType": construct_IPath_EType,
})

CNailongThornMovementComponent = Object(CProjectileMovementFields)

CNailuggerAcidBallMovementComponent = Object(CProjectileMovementFields)

CNoFreezeRoomComponent = Object(CLogicShapeComponentFields)

CObsydomithonAIComponent = Object(CBehaviorTreeAIComponentFields)

COmniLightComponent = Object({
    **CBaseLightComponentFields,
    "fAttMin": common_types.Float,
    "fAttMax": common_types.Float,
    "fAttConstantFactor": common_types.Float,
    "fAttQuadraticFactor": common_types.Float,
    "bCastShadows": construct.Flag,
    "bStaticShadows": construct.Flag,
    "fShadowScl": common_types.Float,
})

CPerceptionComponent = Object(CComponentFields)

CPersistenceComponent = Object(CComponentFields)

CPickableComponent = Object(CPickableComponentFields := {
    **CComponentFields,
    "sOnPickFX": common_types.StrId,
})

CPickableItemComponent = Object(CPickableItemComponentFields := {
    **CPickableComponentFields,
    "sBTType": common_types.StrId,
    "sBTHiddenSceneGroup": common_types.StrId,
    "fTimeToCanBePicked": common_types.Float,
    "sStartPoint": common_types.StrId,
})

CPickableSpringBallComponent = Object(CPickableItemComponentFields)

CPickableSuitComponent = Object(CPickableItemComponentFields)

CPlatformTrapGrapplePointComponent = Object(CPullableGrapplePointComponentFields)

CPlayerLifeComponent = Object({
    **CCharacterLifeComponentFields,
    "fImpactInvulnerableTime": common_types.Float,
    "sImpactHardAnim": common_types.StrId,
    "sHardImpactFX": common_types.StrId,
    "fLifeShards": common_types.Float,
})

CPoisonFlyAIComponent = Object(CBehaviorTreeAIComponentFields)

base_global_CFilePathStrId = common_types.StrId

CPositionalSoundComponent = Object({
    **CComponentFields,
    "fMinAtt": common_types.Float,
    "fMaxAtt": common_types.Float,
    "fVol": common_types.Float,
    "fPitch": common_types.Float,
    "fLaunchEvery": common_types.Float,
    "fHorizontalMult": common_types.Float,
    "fVerticalMult": common_types.Float,
    "bLoop": construct.Flag,
    "fFadeInTime": common_types.Float,
    "fFadeOutTime": common_types.Float,
    "sSound1": Pointer_base_global_CFilePathStrId.create_construct(),
    "sSound2": Pointer_base_global_CFilePathStrId.create_construct(),
    "sSound3": Pointer_base_global_CFilePathStrId.create_construct(),
    "sSound4": Pointer_base_global_CFilePathStrId.create_construct(),
})

CPowerBombBlockLifeComponent = Object(CLifeComponentFields)

CPowerBombMovement = Object({
    **CBombMovementFields,
    "fRadiusToAlertMorphball": common_types.Float,
})

CPowerGeneratorComponent = Object({
    **CActivatableComponentFields,
    "wpPowerGeneratorUsable": common_types.StrId,
    "wpPowerGeneratorUsablePlatform": common_types.StrId,
})

CPowerUpLifeComponent = Object({
    **CItemLifeComponentFields,
    "wpCheckPointEntity": common_types.StrId,
    "sPowerupNameLabelID": common_types.StrId,
})

CProfessorDoorComponent = Object(CEventPropComponentFields)

CProtoCentralUnitComponent = Object({
    **CCentralUnitComponentFields,
    "wpGate": common_types.StrId,
})

CProtoEmmyChaseMusicTriggerComponent = Object(CBaseTriggerComponentFields)

CPullOffGrapplePointComponent = Object({
    **CPullableGrapplePointComponentFields,
    "oActivatableObj": common_types.StrId,
})

CQuarentineDoorComponent = Object(CEventPropComponentFields)

CQuetzoaAIComponent = Object(CQuetzoaAIComponentFields := {
    **CBossAIComponentFields,
    "wpShortRangePath": common_types.StrId,
    "eShortRangePathType": construct_IPath_EType,
    "wpLongRangePath": common_types.StrId,
    "eLongRangePathType": construct_IPath_EType,
})

CQuetzoaEnergyWaveMovementComponent = Object(CProjectileMovementFields)

CQuetzoaMultiTargetProjectileMovementComponent = Object(CProjectileMovementFields)

CQuetzoaXAIComponent = Object({
    **CQuetzoaAIComponentFields,
    "wpCoreXSpawnPoint": common_types.StrId,
})

CSmartObjectComponent = Object(CSmartObjectComponentFields := {
    **CComponentFields,
    "sOnUseStart": common_types.StrId,
    "sOnUseFailure": common_types.StrId,
    "sOnUseSuccess": common_types.StrId,
    "sUsableEntity": common_types.StrId,
    "sDefaultUseAction": common_types.StrId,
    "sDefaultAbortAction": common_types.StrId,
    "bStartEnabled": construct.Flag,
    "fInterpolationTime": common_types.Float,
})

CReturnAreaSmartObjectComponent = Object(CSmartObjectComponentFields)

CRinkaAIComponent = Object(CAIComponentFields)


class CRinkaUnitComponent_ERinkaType(enum.IntEnum):
    A = 0
    B = 1
    C = 2
    Invalid = 2147483647


construct_CRinkaUnitComponent_ERinkaType = construct.Enum(construct.Int32ul, CRinkaUnitComponent_ERinkaType)

CRinkaUnitComponent = Object({
    **CComponentFields,
    "eRinkaType": construct_CRinkaUnitComponent_ERinkaType,
})

CRockDiverAIComponent = Object(CBehaviorTreeAIComponentFields)

CRockDiverSpawnPointComponent = Object({
    **CSpawnPointComponentFields,
    "fTimeToSpawn": common_types.Float,
})

CRodotukAIComponent = Object(CRodotukAIComponentFields := {
    **CBehaviorTreeAIComponentFields,
    "eType": construct_CCharClassRodotukAIComponent_SAbsorbConfig_EType,
})


class CCharClassRodomithonXAIComponent_SFirePillarConfig_EType(enum.IntEnum):
    NONE = 0
    Short = 1
    Medium = 2
    Long = 3
    Invalid = 2147483647


construct_CCharClassRodomithonXAIComponent_SFirePillarConfig_EType = construct.Enum(construct.Int32ul, CCharClassRodomithonXAIComponent_SFirePillarConfig_EType)

CRodomithonXAIComponent = Object({
    **CRodotukAIComponentFields,
    "eFirePillarType": construct_CCharClassRodomithonXAIComponent_SFirePillarConfig_EType,
})


class ERotationDirection(enum.IntEnum):
    RIGHT = 0
    LEFT = 1
    Invalid = 2147483647


construct_ERotationDirection = construct.Enum(construct.Int32ul, ERotationDirection)

CRotationalPlatformComponent = Object({
    **CComponentFields,
    "wpDestructibleBlock": common_types.StrId,
    "eRotationDirection": construct_ERotationDirection,
})

CRumbleComponent = Object(CComponentFields)

CSabotoruAIComponent = Object({
    **CBehaviorTreeAIComponentFields,
    "fMinTimeBetweenSearch": common_types.Float,
    "fMaxTimeBetweenSearch": common_types.Float,
    "fMinTimeSearching": common_types.Float,
    "fMaxTimeSearching": common_types.Float,
})

CSabotoruLifeComponent = Object(CEnemyLifeComponentFields)

CSabotoruSpawnPointComponent = Object({
    **CSpawnPointComponentFields,
    "wpDoor": common_types.StrId,
    "wpHomeLandmark": common_types.StrId,
    "bRightSideDoor": construct.Flag,
})

CSamusAlternativeActionPlayerComponent = Object(CAlternativeActionPlayerComponentFields)

CSamusAnimationComponent = Object(CAnimationComponentFields)

CSamusGunComponent = Object({
    **CGunComponentFields,
    "sSpinAttackFX": common_types.StrId,
    "sScrewAttackFX": common_types.StrId,
})

CSamusModelUpdaterComponent = Object(CMultiModelUpdaterComponentFields)

CSamusMovement = Object({
    **CPlayerMovementFields,
    "bIsMorphBall": construct.Flag,
    "bIsSamus": construct.Flag,
    "fFixedModelOffsetYGoingUp": common_types.Float,
    "fFixedModelOffsetYGoingDown": common_types.Float,
    "fFixedRightLegSwivelAngleOffsetGoingUp": common_types.Float,
    "fFixedLeftLegSwivelAngleOffsetGoingUp": common_types.Float,
    "fFixedRightLegSwivelAngleOffsetGoingDown": common_types.Float,
    "fFixedLeftLegSwivelAngleOffsetGoingDown": common_types.Float,
    "fFixedRightLegOffsetGoingUp": common_types.CVector3D,
    "fFixedLeftLegOffsetGoingUp": common_types.CVector3D,
    "fFixedRightLegOffsetGoingDown": common_types.CVector3D,
    "fFixedLeftLegOffsetGoingDown": common_types.CVector3D,
    "fModelOffsetYGoingUp": common_types.Float,
    "fModelOffsetYGoingDown": common_types.Float,
    "fRightLegSwivelAngleOffsetGoingUp": common_types.Float,
    "fLeftLegSwivelAngleOffsetGoingUp": common_types.Float,
    "fRightLegSwivelAngleOffsetGoingDown": common_types.Float,
    "fLeftLegSwivelAngleOffsetGoingDown": common_types.Float,
    "fRightLegOffsetGoingUp": common_types.CVector3D,
    "fLeftLegOffsetGoingUp": common_types.CVector3D,
    "fRightLegOffsetGoingDown": common_types.CVector3D,
    "fLeftLegOffsetGoingDown": common_types.CVector3D,
    "s_fModelOffsetRunningYGoingUp": common_types.Float,
    "s_fModelOffsetRunningYGoingDown": common_types.Float,
    "s_fModelOffsetRunningYOCGoingUp": common_types.Float,
    "s_fModelOffsetRunningYOCGoingDown": common_types.Float,
    "s_fModelOffsetRunningYSlowDownGoingUp": common_types.Float,
    "s_fModelOffsetRunningYSlowDownGoingDown": common_types.Float,
})

CSaveStationUsableComponent = Object(CUsableComponentFields)

CSceneModelAnimationComponent = Object({
    **CComponentFields,
    "sModelAnim": common_types.StrId,
})

CSclawkAIComponent = Object(CSclawkAIComponentFields := CBehaviorTreeAIComponentFields)

CSclawkLifeComponent = Object(CEnemyLifeComponentFields)

CScorpiusAIComponent = Object({
    **CBossAIComponentFields,
    "wpPhase2CutScenePlayer": common_types.StrId,
    "wpPhase3CutScenePlayer": common_types.StrId,
    "wpDeadCutScenePlayer": common_types.StrId,
})

CScorpiusFXComponent = Object(CSceneComponentFields)

CScorpiusPoisonousSpitMovementComponent = Object(CProjectileMovementFields)

CScourgeAIComponent = Object(CBehaviorTreeAIComponentFields)

CScourgeLifeComponent = Object(CEnemyLifeComponentFields)

CScriptComponent = Object(CComponentFields)

CSegmentLightComponent = Object({
    **CBaseLightComponentFields,
    "vDir": common_types.CVector3D,
    "fSegmentLength": common_types.Float,
    "fAttMin": common_types.Float,
    "fAttMax": common_types.Float,
    "fAttConstantFactor": common_types.Float,
    "fAttQuadraticFactor": common_types.Float,
})

CSensorDoorComponent = Object(CComponentFields)

CShakernautAIComponent = Object(CRobotAIComponentFields)


class EShellState(enum.IntEnum):
    SHELTERED = 0
    UNSHELTERED = 1
    Invalid = 2147483647


construct_EShellState = construct.Enum(construct.Int32ul, EShellState)

CShelmitAIComponent = Object({
    **CBehaviorTreeAIComponentFields,
    "eShellState": construct_EShellState,
})

CShineonAIComponent = Object(CBehaviorTreeAIComponentFields)

CShipRechargeComponent = Object(CUsableComponentFields)

CShockWavePoolComponent = Object(CComponentFields)

SActivatabledOnEventInfo = Object({
    "pActivatable": common_types.StrId,
    "sIdActivation": common_types.StrId,
})

CShootActivatorComponent = Object(CShootActivatorComponentFields := {
    **CItemLifeComponentFields,
    "fInitialAccumulatedTime": common_types.Float,
    "fActivationTime": common_types.Float,
    "fTimePerShot": common_types.Float,
    "vTargetsToActivate": common_types.make_vector(common_types.StrId),
    "vTargetsToDeactivate": common_types.make_vector(common_types.StrId),
    "sOnUseEntityTimeline": common_types.StrId,
    "wpAtmosphereEntity": common_types.StrId,
    "vEntitiesActivatabledOnEvent": common_types.make_vector(SActivatabledOnEventInfo),
    "vEntitiesDeactivatabledOnEvent": common_types.make_vector(SActivatabledOnEventInfo),
})

CShootActivatorHidrogigaComponent = Object({
    **CShootActivatorComponentFields,
    "wpOtherActivator": common_types.StrId,
    "wpWaterNozzle": common_types.StrId,
})

CShotComponent = Object(CComponentFields)


class CSideEnemyMovement_EDir(enum.IntEnum):
    left = 0
    right = 1
    Invalid = 2147483647


construct_CSideEnemyMovement_EDir = construct.Enum(construct.Int32ul, CSideEnemyMovement_EDir)

CSideEnemyMovement = Object({
    **CEnemyMovementFields,
    "eInitialDir": construct_CSideEnemyMovement_EDir,
})


class ESlidleOutSpawnPointDir(enum.IntEnum):
    ByDot = 0
    Front = 1
    Side = 2
    Invalid = 2147483647


construct_ESlidleOutSpawnPointDir = construct.Enum(construct.Int32ul, ESlidleOutSpawnPointDir)

CSlidleSpawnPointComponent = Object({
    **CComponentFields,
    "eDespawnDir": construct_ESlidleOutSpawnPointDir,
})

CSlowNailongSpawnPointComponent = Object(CSpawnPointComponentFields)

CSluggerAcidBallMovementComponent = Object(CProjectileMovementFields)

CSoundListenerComponent = Object({
    **CComponentFields,
    "vLookAt": common_types.CVector3D,
})

CSoundProofTriggerComponent = Object({
    **CBaseTriggerComponentFields,
    "eLowPassFilterToApply": construct_base_snd_ELowPassFilter,
    "fFadeInTime": common_types.Float,
    "fFadeOutTime": common_types.Float,
    "bMuteActors": construct.Flag,
    "bFilterSpecificActors": construct.Flag,
    "vActorsToIgnore": common_types.make_vector(common_types.StrId),
})

CSpbSprActivator = Object({
    **CActivatableByProjectileComponentFields,
    "wpSpbSprpPlatform": common_types.StrId,
    "vTargetsToActivate": common_types.make_vector(common_types.StrId),
    "vTargetsToDeactivate": common_types.make_vector(common_types.StrId),
    "wpPoolPlatform": common_types.StrId,
})

CSpecialEnergyComponent = Object({
    **CComponentFields,
    "fMaxEnergy": common_types.Float,
    "fEnergy": common_types.Float,
    "bSpecialEnergyLocked": construct.Flag,
})

CSpitclawkAIComponent = Object(CSclawkAIComponentFields)

CVulkranMagmaBallMovementComponent = Object(CVulkranMagmaBallMovementComponentFields := CProjectileMovementFields)

CSpittailMagmaBallMovementComponent = Object(CVulkranMagmaBallMovementComponentFields)

CSpotLightComponent = Object({
    **CBaseLightComponentFields,
    "fAttMin": common_types.Float,
    "fAttMax": common_types.Float,
    "fAttIn": common_types.Float,
    "fAttOut": common_types.Float,
    "fAttConstantFactor": common_types.Float,
    "fAttQuadraticFactor": common_types.Float,
    "vDir": common_types.CVector3D,
    "fAnimFrame": common_types.Float,
    "bCastShadows": construct.Flag,
    "vShadowNearFar": common_types.CVector2D,
    "fShadowBias": common_types.Float,
    "bStaticShadows": construct.Flag,
    "fShadowScl": common_types.Float,
    "bHasProjectorTexture": construct.Flag,
    "sTexturePath": common_types.StrId,
    "vProjectorUVScroll": common_types.CVector4D,
})

SFXInstanceData = Object({
    "sFXPath": common_types.StrId,
    "v3Position": common_types.CVector3D,
    "v3Rotation": common_types.CVector3D,
    "v3Scale": common_types.CVector3D,
})

CStandaloneFXComponent = Object({
    **CSceneComponentFields,
    "vctFXInstances": common_types.make_vector(SFXInstanceData),
    "uPoolSize": common_types.UInt,
    "vScale": common_types.CVector3D,
    "sFXPath": common_types.StrId,
})

CStartPointComponent = Object({
    **CComponentFields,
    "sOnTeleport": common_types.StrId,
    "sOnTeleportLogicCamera": common_types.StrId,
    "bOnTeleportLogicCameraRaw": construct.Flag,
    "bProjectOnFloor": construct.Flag,
    "bMorphballMode": construct.Flag,
    "bSaveGameToCheckpoint": construct.Flag,
    "bIsBossStartPoint": construct.Flag,
})

CSteamJetComponent = Object({
    **CBaseDamageTriggerComponentFields,
    "fDelayStart": common_types.Float,
    "fDamage": common_types.Float,
    "fLength": common_types.Float,
    "fWidth": common_types.Float,
    "fOnTime": common_types.Float,
    "fOffTime": common_types.Float,
    "fOnOffTime": common_types.Float,
    "fParticleScale": common_types.Float,
    "bCrossingAllowed": construct.Flag,
    "bForceReactionDirection": construct.Flag,
    "vReactionDirection": common_types.CVector2D,
    "wpNextSteamJet": common_types.StrId,
})

CSteeringMovement = Object(CMovementComponentFields)

CSunnapAIComponent = Object(CRodotukAIComponentFields)

CSuperMissileMovement = Object(CMissileMovementFields)

CSwarmAttackComponent = Object(CAttackComponentFields)

CSwifterAIComponent = Object(CBehaviorTreeAIComponentFields)


class ESwifterSpawnGroupDirection(enum.IntEnum):
    Left = 0
    Right = 1
    Invalid = 2147483647


construct_ESwifterSpawnGroupDirection = construct.Enum(construct.Int32ul, ESwifterSpawnGroupDirection)


class ESwifterSpawnGroupSpawnMode(enum.IntEnum):
    Water = 0
    Surface = 1
    Invalid = 2147483647


construct_ESwifterSpawnGroupSpawnMode = construct.Enum(construct.Int32ul, ESwifterSpawnGroupSpawnMode)

CSwifterSpawnGroupComponent = Object({
    **CSpawnGroupComponentFields,
    "eDirection": construct_ESwifterSpawnGroupDirection,
    "eMode": construct_ESwifterSpawnGroupSpawnMode,
    "fTimeToSpawn": common_types.Float,
})

CSwingableGrapplePointComponent = Object(CGrapplePointComponentFields)

CTakumakuAIComponent = Object(CBehaviorTreeAIComponentFields)

CTargetComponent = Object(CComponentFields)


class ETeleporterColorSphere(enum.IntEnum):
    BLUE = 0
    DARKBLUE = 1
    GREEN = 2
    ORANGE = 3
    PINK = 4
    PURPLE = 5
    RED = 6
    YELLOW = 7
    Invalid = 2147483647


construct_ETeleporterColorSphere = construct.Enum(construct.Int32ul, ETeleporterColorSphere)

CTeleporterUsableComponent = Object({
    **CUsableComponentFields,
    "eLoadingScreen": construct_ELoadingScreen,
    "sLevelName": common_types.StrId,
    "sScenarioName": common_types.StrId,
    "sTargetSpawnPoint": common_types.StrId,
    "eTeleporterColorSphere": construct_ETeleporterColorSphere,
    "wpFrozenPlatform": common_types.StrId,
})


class CDoorLifeComponent_SState(enum.IntEnum):
    NONE = 0
    Opened = 1
    Closed = 2
    Locked = 3
    Invalid = 2147483647


construct_CDoorLifeComponent_SState = construct.Enum(construct.Int32ul, CDoorLifeComponent_SState)

SDoorInfo = Object({
    "wpThermalDoor": common_types.StrId,
    "sDoorState": construct_CDoorLifeComponent_SState,
})


class CThermalDeviceComponent_EPipeGroup(enum.IntEnum):
    Group0 = 0
    Group1 = 1
    Group2 = 2
    Group3 = 3
    Group4 = 4
    Group5 = 5
    Group6 = 6
    Group7 = 7
    Invalid = 2147483647


construct_CThermalDeviceComponent_EPipeGroup = construct.Enum(construct.Int32ul, CThermalDeviceComponent_EPipeGroup)

CThermalDeviceComponent = Object({
    **CUsableComponentFields,
    "vThermalDoors": common_types.make_vector(SDoorInfo),
    "sOnEnterUseLuaCallback": common_types.StrId,
    "sOnSetupInitialStateLuaCallback": common_types.StrId,
    "sOnSetupUseStateLuaCallback": common_types.StrId,
    "sUseEndActionOverride": common_types.StrId,
    "bCheckpointBeforeUsage": construct.Flag,
    "ePipeGroup1": construct_CThermalDeviceComponent_EPipeGroup,
    "ePipeGroup2": construct_CThermalDeviceComponent_EPipeGroup,
})

CThermalRoomConnectionFX = Object({
    **CActivatableComponentFields,
    "vTargetToLink": common_types.StrId,
    "vHidderLink": common_types.StrId,
})

CThermalRoomFX = Object(CActivatableComponentFields)

CTimelineComponent = Object({
    **CComponentFields,
    "sInitAction": common_types.StrId,
    "eNextPolicy": construct_CTimelineComponent_ENextPolicy,
    "fMinDelayTime": common_types.Float,
    "fMaxDelayTime": common_types.Float,
})

CTimerComponent = Object(CComponentFields)

CTotalRechargeComponent = Object({
    **CUsableComponentFields,
    "sRechargeFX": common_types.StrId,
    "sEyeRFX": common_types.StrId,
    "sEyeLFX": common_types.StrId,
})


class ETrainDirection(enum.IntEnum):
    LEFT = 0
    RIGHT = 1
    Invalid = 2147483647


construct_ETrainDirection = construct.Enum(construct.Int32ul, ETrainDirection)

CTrainUsableComponent = Object(CTrainUsableComponentFields := {
    **CUsableComponentFields,
    "eDirection": construct_ETrainDirection,
    "eLoadingScreen": construct_ELoadingScreen,
    "sLevelName": common_types.StrId,
    "sScenarioName": common_types.StrId,
    "sTargetSpawnPoint": common_types.StrId,
    "sMapConnectionId": common_types.StrId,
    "bAquaLoadingScreen": construct.Flag,
})

CTrainUsableComponentCutScene = Object({
    **CTrainUsableComponentFields,
    "wpCutScenePlayer": common_types.StrId,
})

CTrainWithPortalUsableComponent = Object({
    **CTrainUsableComponentFields,
    "wpPortal": common_types.StrId,
})

CTriggerNavMeshItemComponent = Object(CNavMeshItemComponentFields)

CTunnelTrapMorphballComponent = Object({
    **CComponentFields,
    "aVignettes": common_types.make_vector(common_types.StrId),
    "bDisableCloseTrapSensor": construct.Flag,
})

CUnlockAreaSmartObjectComponent = Object(CSmartObjectComponentFields)

CVideoManagerComponent = Object({
    **CComponentFields,
    "sVideo_1_Path": common_types.StrId,
    "sVideo_2_Path": common_types.StrId,
    "sVideoAux_1_Path": common_types.StrId,
    "sVideoAux_2_Path": common_types.StrId,
})

CVulkranAIComponent = Object(CBehaviorTreeAIComponentFields)

CWarLotusAIComponent = Object(CBehaviorTreeAIComponentFields)

CWaterNozzleComponent = Object({
    **CComponentFields,
    "wpWaterPool": common_types.StrId,
})

CWaterPlatformUsableComponent = Object({
    **CUsableComponentFields,
    "fTotalMetersToFill": common_types.Float,
    "fSnapToMeters": common_types.Float,
    "fMetersToBreakValve": common_types.Float,
    "fTimeToBreakValve": common_types.Float,
    "fTimeToFillAfterValveBreaks": common_types.Float,
    "fPlatformMovementDelaySinceUseStart": common_types.Float,
})

CWaterPoolComponent_FloatingEntitiesInfo = Object({
    "wpFloatingEntity": common_types.StrId,
    "fLevelStopFloating": common_types.Float,
})

CWaterPoolComponent = Object({
    **CLiquidPoolBaseComponentFields,
    "vWaterLevelChanges": common_types.make_vector(common_types.Float),
    "tFloatingEntities": common_types.make_vector(CWaterPoolComponent_FloatingEntitiesInfo),
    "sOnActivatedLuaCallback": common_types.StrId,
    "bChangedLevelOnCooldownEvent": construct.Flag,
    "vFloatingEntities": common_types.make_vector(common_types.StrId),
})

CWaterTriggerChangeComponent = Object({
    **CComponentFields,
    "wpOriginWaterTrigger": common_types.StrId,
    "wpTargetWaterTrigger": common_types.StrId,
    "fChangeTime": common_types.Float,
    "fDelay": common_types.Float,
    "bDeactivateOnFinished": construct.Flag,
    "wpOtherWaterTriggerChange": common_types.StrId,
    "fOriginChange": common_types.Float,
    "fTargetChange": common_types.Float,
    "sOnActivatedLuaCallback": common_types.StrId,
})

CWeightActivableMovablePlatformComponent = Object({
    **CMovablePlatformComponentFields,
    "sOnActivatedLuaCallback": common_types.StrId,
})

CWeightActivablePropComponent = Object(CComponentFields)

CWeightActivatedPlatformSmartObjectComponent = Object({
    **CSmartObjectComponentFields,
    "sDustFX": common_types.StrId,
    "bDisableWhenEmmyNearby": construct.Flag,
    "bDisableWhenUsed": construct.Flag,
})

SWorldGraphNode = Object({
    "vPos": common_types.CVector3D,
    "sID": common_types.StrId,
    "bDeadEnd": construct.Flag,
    "tNeighboursIds": common_types.make_vector(common_types.StrId),
})

CWorldGraph = Object({
    **CActorComponentFields,
    "tNodes": common_types.make_vector(SWorldGraphNode),
})

CXParasiteAIComponent = Object(CBehaviorTreeAIComponentFields)

CXParasiteBehavior = Object(CXParasiteBehaviorFields := {
    "bCanBeAbsorbed": construct.Flag,
    "fBehaviorProbability": common_types.Float,
    "fOverrideGreenTypeProbability": common_types.Float,
    "fOverrideYellowTypeProbability": common_types.Float,
    "fOverrideOrangeTypeProbability": common_types.Float,
    "fOverrideRedTypeProbability": common_types.Float,
})

CXParasiteDropComponent = Object({
    **CComponentFields,
    "vectBehaviors": common_types.make_vector(Pointer_CXParasiteBehavior.create_construct()),
})

CYamplotXAIComponent = Object(CBehaviorTreeAIComponentFields)

CShotVariableAngleLaunchConfig = Object({
    **CShotLaunchConfigFields,
    "fGravity": common_types.Float,
    "fLaunchSpeed": common_types.Float,
    "fMinLaunchAngleDegs": common_types.Float,
    "fMaxLaunchAngleDegs": common_types.Float,
    "bMakeLaunchSpeedProportionalToDistance": construct.Flag,
    "fLaunchSpeedAtMinDistance": common_types.Float,
    "fDist4MinLaunchSpeed": common_types.Float,
    "fDist4MaxLaunchSpeed": common_types.Float,
})

CShotVariableSpeedLaunchConfig = Object({
    **CShotLaunchConfigFields,
    "fGravity": common_types.Float,
    "fLaunchFixedAngleDegs": common_types.Float,
    "fLaunchMinSpeed": common_types.Float,
    "fLaunchMaxSpeed": common_types.Float,
})

game_logic_collision_CAABoxShape2D = Object({
    **game_logic_collision_CShapeFields,
    "v2Min": common_types.CVector2D,
    "v2Max": common_types.CVector2D,
    "bOutwardsNormal": construct.Flag,
})

game_logic_collision_CCapsuleShape2D = Object({
    **game_logic_collision_CShapeFields,
    "fRadius": common_types.Float,
    "fHalfHeight": common_types.Float,
    "bOutwardsNormal": construct.Flag,
})

game_logic_collision_CCircleShape2D = Object({
    **game_logic_collision_CShapeFields,
    "fRadius": common_types.Float,
    "bOutwardsNormal": construct.Flag,
})

game_logic_collision_COBoxShape2D = Object({
    **game_logic_collision_CShapeFields,
    "v2Extent": common_types.CVector2D,
    "fDegrees": common_types.Float,
    "bOutwardsNormal": construct.Flag,
})

base_spatial_SSegmentData = Object({
    "vPos": common_types.CVector3D,
})

base_spatial_CPolygon2D = Object({
    "bClosed": construct.Flag,
    "oSegmentData": common_types.make_vector(base_spatial_SSegmentData),
    "bOutwardsNormal": construct.Flag,
})

base_spatial_CPolygonCollection2D = Object({
    "vPolys": common_types.make_vector(base_spatial_CPolygon2D),
})

game_logic_collision_CPolygonCollectionShape = Object({
    **game_logic_collision_CShapeFields,
    "oPolyCollection": base_spatial_CPolygonCollection2D,
})

querysystem_CChozoRobotSoldierHeightEvaluator = Object(querysystem_CEvaluatorFields)

querysystem_CCurrentEvaluator = Object(querysystem_CEvaluatorFields)

querysystem_CDistanceEvaluator = Object({
    **querysystem_CEvaluatorFields,
    "fMinDistance": common_types.Float,
    "fMaxDistance": common_types.Float,
})

querysystem_CDistanceToTargetEvaluator = Object({
    **querysystem_CEvaluatorFields,
    "fMinDistance": common_types.Float,
    "fMaxDistance": common_types.Float,
})

querysystem_CFilterToEvaluator = Object({
    **querysystem_CEvaluatorFields,
    "pFilter": Pointer_querysystem_CFilter.create_construct(),
    "fEvaluation": common_types.Float,
})

querysystem_CChozoRobotSoldierIsInFrustumFilter = Object(querysystem_CFilterFields)

querysystem_CChozoRobotSoldierIsInMeleePathFilter = Object(querysystem_CFilterFields)

querysystem_CChozoRobotSoldierIsInShootingPositionPathFilter = Object(querysystem_CFilterFields)

querysystem_CChozoRobotSoldierLineOfFireFilter = Object(querysystem_CFilterFields)

querysystem_CMinTargetDistanceFilter = Object(querysystem_CMinTargetDistanceFilterFields := {
    **querysystem_CFilterFields,
    "fMinDistance": common_types.Float,
})

querysystem_CChozoRobotSoldierMinTargetDistanceFilter = Object(querysystem_CMinTargetDistanceFilterFields)

querysystem_CIsInFrustumFilter = Object({
    **querysystem_CFilterFields,
    "vOffset": common_types.CVector3D,
})

querysystem_CIsInNavigablePathFilter = Object({
    **querysystem_CFilterFields,
    "vOffset": common_types.CVector3D,
})

querysystem_CLookAtTargetFilter = Object({
    **querysystem_CFilterFields,
    "vOffset": common_types.CVector3D,
})

querysystem_CMaxDistanceFilter = Object({
    **querysystem_CFilterFields,
    "fMaxDistance": common_types.Float,
})

querysystem_CMaxTargetDistanceFilter = Object({
    **querysystem_CFilterFields,
    "fMaxTargetDistance": common_types.Float,
})

querysystem_CMinDistanceFilter = Object({
    **querysystem_CFilterFields,
    "fMinDistance": common_types.Float,
})

querysystem_CSameEntitySideFilter = Object({
    **querysystem_CFilterFields,
    "vOffset": common_types.CVector3D,
})


class EShinesparkTravellingDirection(enum.IntEnum):
    No_Direction = 0
    Up = 1
    UpRight = 2
    UpLeft = 3
    Right = 4
    Left = 5
    DownRight = 6
    DownLeft = 7
    Down = 8


construct_EShinesparkTravellingDirection = construct.Enum(construct.Int32ul, EShinesparkTravellingDirection)


class ECoolShinesparkSituation(enum.IntEnum):
    Default = 0
    CooldownX = 1


construct_ECoolShinesparkSituation = construct.Enum(construct.Int32ul, ECoolShinesparkSituation)

CAllowCoolShinesparkLogicAction = Object({
    **CTriggerLogicActionFields,
    "lstAllowedDirections": common_types.make_vector(construct_EShinesparkTravellingDirection),
    "lstAllowedSituations": common_types.make_vector(construct_ECoolShinesparkSituation),
    "sCoolShinesparkId": common_types.StrId,
    "bAllow": construct.Flag,
    "bForce": construct.Flag,
})

CCameraToRailLogicAction = Object({
    **CTriggerLogicActionFields,
    "bCameraToRail": construct.Flag,
})

CChangeSetupLogicAction = Object({
    **CTriggerLogicActionFields,
    "sSetupID": common_types.StrId,
    "bPersistent": construct.Flag,
    "bForceChange": construct.Flag,
    "bPush": construct.Flag,
})


class eDoorStateLogicAction(enum.IntEnum):
    Open = 0
    Close = 1
    Lock = 2
    Unlock = 3
    Invalid = 2147483647


construct_eDoorStateLogicAction = construct.Enum(construct.Int32ul, eDoorStateLogicAction)

DoorStateInfo = Object({
    "pDoor": common_types.StrId,
    "eDoorState": construct_eDoorStateLogicAction,
})

CChangeStateDoorsLogicAction = Object({
    **CTriggerLogicActionFields,
    "vDoorStateInfo": common_types.make_vector(DoorStateInfo),
    "bEnabled": construct.Flag,
})

CCheckCoolShinesparkSuccessfullyCompletedLogicAction = Object(CTriggerLogicActionFields)

CMarkMinimapLogicAction = Object(CMarkMinimapLogicActionFields := {
    **CTriggerLogicActionFields,
    "wpVisibleLogicShape": common_types.StrId,
    "wpVisitedLogicShape": common_types.StrId,
})

CCoolShinesparkMarkMinimapLogicAction = Object(CMarkMinimapLogicActionFields)


class CEmmyStateOverrideLogicAction_EMode(enum.IntEnum):
    ShowVisualCone = 0
    HideVisualCone = 1
    Invalid = 2147483647


construct_CEmmyStateOverrideLogicAction_EMode = construct.Enum(construct.Int32ul, CEmmyStateOverrideLogicAction_EMode)

CEmmyStateOverrideLogicAction = Object({
    **CTriggerLogicActionFields,
    "eMode": construct_CEmmyStateOverrideLogicAction_EMode,
})


class navmesh_ENavMeshGroup(enum.IntEnum):
    DEFAULT = 0
    EMMY = 1
    EMMY_PROTO = 2
    EMMY_CAVE = 3
    EMMY_MAGMA = 4
    Invalid = 2147483647


construct_navmesh_ENavMeshGroup = construct.Enum(construct.Int32ul, navmesh_ENavMeshGroup)


class CForbiddenEdgesLogicAction_EState(enum.IntEnum):
    Allowed = 0
    Forbidden = 1
    Invalid = 2147483647


construct_CForbiddenEdgesLogicAction_EState = construct.Enum(construct.Int32ul, CForbiddenEdgesLogicAction_EState)

CForbiddenEdgesLogicAction = Object({
    **CTriggerLogicActionFields,
    "eNavMeshGroup": construct_navmesh_ENavMeshGroup,
    "wpSpawnPoint": common_types.StrId,
    "wpLogicShape": common_types.StrId,
    "eState": construct_CForbiddenEdgesLogicAction_EState,
})

CForceMovementLogicAction = Object({
    **CTriggerLogicActionFields,
    "bMovePlayer": construct.Flag,
    "v2Direction": common_types.CVector2D,
})

CFreeAimTutoLogicAction = Object({
    **CTriggerLogicActionFields,
    "wpItemToDestroy": common_types.StrId,
})

CHoldPlayerDirectionOnSubAreaChangeLogicAction = Object({
    **CTriggerLogicActionFields,
    "bForce": construct.Flag,
})

CIgnoreFloorSlideUpperBodySubmergedLogicAction = Object({
    **CTriggerLogicActionFields,
    "bActive": construct.Flag,
    "sId": common_types.StrId,
})

CItemDestructionLogicAction = Object({
    **CTriggerLogicActionFields,
    "wpItemToDestroy": common_types.StrId,
    "wpObserver": common_types.StrId,
})

CLockRoomLogicAction = Object({
    **CTriggerLogicActionFields,
    "wpAccessPoint": common_types.StrId,
    "sDoorsLockedLiteralID": common_types.StrId,
    "bInstantLock": construct.Flag,
})

CLuaCallsLogicAction = Object({
    **CTriggerLogicActionFields,
    "sCallbackEntityName": common_types.StrId,
    "sCallback": common_types.StrId,
    "bCallbackEntity": construct.Flag,
    "bCallbackPersistent": construct.Flag,
})


class CPerceptionModifierLogicAction_EMode(enum.IntEnum):
    Add = 0
    Remove = 1
    Invalid = 2147483647


construct_CPerceptionModifierLogicAction_EMode = construct.Enum(construct.Int32ul, CPerceptionModifierLogicAction_EMode)


class CAIManager_EAIGroup(enum.IntEnum):
    Emmy = 0
    Invalid = 2147483647


construct_CAIManager_EAIGroup = construct.Enum(construct.Int32ul, CAIManager_EAIGroup)

CPerceptionModifierLogicAction = Object({
    **CTriggerLogicActionFields,
    "eMode": construct_CPerceptionModifierLogicAction_EMode,
    "wpPerceivedPosition": common_types.StrId,
    "eGroup": construct_CAIManager_EAIGroup,
})

CSPBTutoLogicAction = Object({
    **CTriggerLogicActionFields,
    "wpCentralUnitDoor": common_types.StrId,
    "wpCentralUnit": common_types.StrId,
    "oSPRTuto.m_vAfterTutoLogicActions": common_types.make_vector(Pointer_CTriggerLogicAction.create_construct()),
})

CSPRTutoLogicAction = Object({
    **CTriggerLogicActionFields,
    "wpCentralUnitDoor": common_types.StrId,
    "wpCentralUnit": common_types.StrId,
    "vAfterTutoLogicActions": common_types.make_vector(Pointer_CTriggerLogicAction.create_construct()),
})

CSamusOverrideDistanceToBorderLogicAction = Object({
    **CTriggerLogicActionFields,
    "sId": common_types.StrId,
    "fLeftForwardDistance": common_types.Float,
    "fLeftBackwardDistance": common_types.Float,
    "fRightForwardDistance": common_types.Float,
    "fRightBackwardDistance": common_types.Float,
})

CSaveGameFromEmmyDoorLogicAction = Object({
    **CTriggerLogicActionFields,
    "wpEmmyDoorActor": common_types.StrId,
    "bForce": construct.Flag,
    "bRestoreOriginalValue": construct.Flag,
})


class CSaveGameLogicAction_EDestination(enum.IntEnum):
    savedata = 0
    checkpoint = 1
    Invalid = 2147483647


construct_CSaveGameLogicAction_EDestination = construct.Enum(construct.Int32ul, CSaveGameLogicAction_EDestination)

CSaveGameLogicAction = Object({
    **CTriggerLogicActionFields,
    "eDestination": construct_CSaveGameLogicAction_EDestination,
    "sCheckpointKey": common_types.StrId,
    "wpStartPoint": common_types.StrId,
    "bForce": construct.Flag,
})

CSaveGameToSnapshotLogicAction = Object({
    **CTriggerLogicActionFields,
    "sSnapshotId": common_types.StrId,
})

CSaveSnapshotToCheckpointLogicAction = Object({
    **CTriggerLogicActionFields,
    "sSnapshotId": common_types.StrId,
    "sCheckpointKey": common_types.StrId,
    "wpStartPoint": common_types.StrId,
    "bForce": construct.Flag,
})

CSetActorEnabledLogicAction = Object({
    **CTriggerLogicActionFields,
    "wpActor": common_types.StrId,
    "bEnabled": construct.Flag,
})

CShowPopUpCompositionLogicAction = Object({
    **CTriggerLogicActionFields,
    "vtexts": common_types.make_vector(common_types.StrId),
})

CStartCentralUnitCombatLogicAction = Object({
    **CTriggerLogicActionFields,
    "wpCentralUnit": common_types.StrId,
})


class CSubAreaManager_ETransitionType(enum.IntEnum):
    NONE = 0
    Camera = 1
    Fade = 2
    FakeFade = 3
    Invalid = 2147483647


construct_CSubAreaManager_ETransitionType = construct.Enum(construct.Int32ul, CSubAreaManager_ETransitionType)

CSubareaTransitionTypeLogicAction = Object({
    **CTriggerLogicActionFields,
    "eTransitionType": construct_CSubAreaManager_ETransitionType,
})

CTutoEnterLogicAction = Object({
    **CTriggerLogicActionFields,
    "sLiteralID": common_types.StrId,
    "bShowMessage": construct.Flag,
    "bWaitForInput": construct.Flag,
    "wpObserver": common_types.StrId,
    "sLuaCallbackOnMessageClosed": common_types.StrId,
    "sMissionLogTutoId": common_types.StrId,
})

CTutoExitLogicAction = Object({
    **CTriggerLogicActionFields,
    "sMissionLogTutoId": common_types.StrId,
    "wpTriggerToDisable": common_types.StrId,
})

CXParasiteGoSpawnBehavior = Object({
    **CXParasiteBehaviorFields,
    "tSpawnPoints": common_types.make_vector(common_types.StrId),
})

CXParasiteGoTransformBehavior = Object({
    **CXParasiteBehaviorFields,
    "wpFromSpawnPoint": common_types.StrId,
    "tToSpawnPoints": common_types.make_vector(common_types.StrId),
})

CXParasiteStayOnPlaceBehavior = Object({
    **CXParasiteBehaviorFields,
    "wpStayPosLandmark": common_types.StrId,
})

CXParasiteWanderThenFleeBehavior = Object(CXParasiteBehaviorFields)

base_global_CRntFile = construct.Prefixed(construct.Int32ul, construct.GreedyBytes)

Pointer_CAcidBlobsLaunchPattern.add_option("CAcidBlobsLaunchPattern", CAcidBlobsLaunchPattern)

Pointer_CActor.add_option("CActor", CActor)
Pointer_CActor.add_option("CEntity", CEntity)

Pointer_CActorComponent.add_option("CActorComponent", CActorComponent)
Pointer_CActorComponent.add_option("CAIAttackComponent", CAIAttackComponent)
Pointer_CActorComponent.add_option("CAIComponent", CAIComponent)
Pointer_CActorComponent.add_option("CAIGrapplePointComponent", CAIGrapplePointComponent)
Pointer_CActorComponent.add_option("CAINavigationComponent", CAINavigationComponent)
Pointer_CActorComponent.add_option("CAISmartObjectComponent", CAISmartObjectComponent)
Pointer_CActorComponent.add_option("CAbilityComponent", CAbilityComponent)
Pointer_CActorComponent.add_option("CAccessPointCommanderComponent", CAccessPointCommanderComponent)
Pointer_CActorComponent.add_option("CAccessPointComponent", CAccessPointComponent)
Pointer_CActorComponent.add_option("CActionSwitcherComponent", CActionSwitcherComponent)
Pointer_CActorComponent.add_option("CActionSwitcherOnPullGrapplePointComponent", CActionSwitcherOnPullGrapplePointComponent)
Pointer_CActorComponent.add_option("CActivatableByProjectileComponent", CActivatableByProjectileComponent)
Pointer_CActorComponent.add_option("CActivatableComponent", CActivatableComponent)
Pointer_CActorComponent.add_option("CAimCameraEnabledVisibleOnlyComponent", CAimCameraEnabledVisibleOnlyComponent)
Pointer_CActorComponent.add_option("CAimComponent", CAimComponent)
Pointer_CActorComponent.add_option("CAlternativeActionPlayerComponent", CAlternativeActionPlayerComponent)
Pointer_CActorComponent.add_option("CAmmoRechargeComponent", CAmmoRechargeComponent)
Pointer_CActorComponent.add_option("CAnimationComponent", CAnimationComponent)
Pointer_CActorComponent.add_option("CAnimationNavMeshItemComponent", CAnimationNavMeshItemComponent)
Pointer_CActorComponent.add_option("CArachnusAIComponent", CArachnusAIComponent)
Pointer_CActorComponent.add_option("CAreaFXComponent", CAreaFXComponent)
Pointer_CActorComponent.add_option("CAreaMusicComponent", CAreaMusicComponent)
Pointer_CActorComponent.add_option("CAreaSoundComponent", CAreaSoundComponent)
Pointer_CActorComponent.add_option("CAttackComponent", CAttackComponent)
Pointer_CActorComponent.add_option("CAudioComponent", CAudioComponent)
Pointer_CActorComponent.add_option("CAutclastAIComponent", CAutclastAIComponent)
Pointer_CActorComponent.add_option("CAutectorAIComponent", CAutectorAIComponent)
Pointer_CActorComponent.add_option("CAutectorLifeComponent", CAutectorLifeComponent)
Pointer_CActorComponent.add_option("CAutomperAIComponent", CAutomperAIComponent)
Pointer_CActorComponent.add_option("CAutoolAIComponent", CAutoolAIComponent)
Pointer_CActorComponent.add_option("CAutsharpAIComponent", CAutsharpAIComponent)
Pointer_CActorComponent.add_option("CAutsharpLifeComponent", CAutsharpLifeComponent)
Pointer_CActorComponent.add_option("CAutsharpSpawnPointComponent", CAutsharpSpawnPointComponent)
Pointer_CActorComponent.add_option("CAutsniperAIComponent", CAutsniperAIComponent)
Pointer_CActorComponent.add_option("CAutsniperSpawnPointComponent", CAutsniperSpawnPointComponent)
Pointer_CActorComponent.add_option("CBTObserverComponent", CBTObserverComponent)
Pointer_CActorComponent.add_option("CBaseBigFistAIComponent", CBaseBigFistAIComponent)
Pointer_CActorComponent.add_option("CBaseDamageTriggerComponent", CBaseDamageTriggerComponent)
Pointer_CActorComponent.add_option("CBaseGroundShockerAIComponent", CBaseGroundShockerAIComponent)
Pointer_CActorComponent.add_option("CBaseLightComponent", CBaseLightComponent)
Pointer_CActorComponent.add_option("CBaseTriggerComponent", CBaseTriggerComponent)
Pointer_CActorComponent.add_option("CBasicLifeComponent", CBasicLifeComponent)
Pointer_CActorComponent.add_option("CBatalloonAIComponent", CBatalloonAIComponent)
Pointer_CActorComponent.add_option("CBeamBoxComponent", CBeamBoxComponent)
Pointer_CActorComponent.add_option("CBeamDoorLifeComponent", CBeamDoorLifeComponent)
Pointer_CActorComponent.add_option("CBehaviorTreeAIComponent", CBehaviorTreeAIComponent)
Pointer_CActorComponent.add_option("CBigFistAIComponent", CBigFistAIComponent)
Pointer_CActorComponent.add_option("CBigkranXAIComponent", CBigkranXAIComponent)
Pointer_CActorComponent.add_option("CBillboardCollisionComponent", CBillboardCollisionComponent)
Pointer_CActorComponent.add_option("CBillboardComponent", CBillboardComponent)
Pointer_CActorComponent.add_option("CBillboardLifeComponent", CBillboardLifeComponent)
Pointer_CActorComponent.add_option("CBombMovement", CBombMovement)
Pointer_CActorComponent.add_option("CBoneToConstantComponent", CBoneToConstantComponent)
Pointer_CActorComponent.add_option("CBossAIComponent", CBossAIComponent)
Pointer_CActorComponent.add_option("CBossLifeComponent", CBossLifeComponent)
Pointer_CActorComponent.add_option("CBossSpawnGroupComponent", CBossSpawnGroupComponent)
Pointer_CActorComponent.add_option("CBreakableHintComponent", CBreakableHintComponent)
Pointer_CActorComponent.add_option("CBreakableScenarioComponent", CBreakableScenarioComponent)
Pointer_CActorComponent.add_option("CBreakableTileGroupComponent", CBreakableTileGroupComponent)
Pointer_CActorComponent.add_option("CBreakableTileGroupSonarTargetComponent", CBreakableTileGroupSonarTargetComponent)
Pointer_CActorComponent.add_option("CBreakableVignetteComponent", CBreakableVignetteComponent)
Pointer_CActorComponent.add_option("CCameraComponent", CCameraComponent)
Pointer_CActorComponent.add_option("CCameraRailComponent", CCameraRailComponent)
Pointer_CActorComponent.add_option("CCapsuleUsableComponent", CCapsuleUsableComponent)
Pointer_CActorComponent.add_option("CCaterzillaAIComponent", CCaterzillaAIComponent)
Pointer_CActorComponent.add_option("CCaterzillaSpawnPointComponent", CCaterzillaSpawnPointComponent)
Pointer_CActorComponent.add_option("CCaveCentralUnitComponent", CCaveCentralUnitComponent)
Pointer_CActorComponent.add_option("CCentralUnitAIComponent", CCentralUnitAIComponent)
Pointer_CActorComponent.add_option("CCentralUnitCannonAIComponent", CCentralUnitCannonAIComponent)
Pointer_CActorComponent.add_option("CCentralUnitCannonBeamMovementComponent", CCentralUnitCannonBeamMovementComponent)
Pointer_CActorComponent.add_option("CCentralUnitComponent", CCentralUnitComponent)
Pointer_CActorComponent.add_option("CChainReactionActionSwitcherComponent", CChainReactionActionSwitcherComponent)
Pointer_CActorComponent.add_option("CChangeStageNavMeshItemComponent", CChangeStageNavMeshItemComponent)
Pointer_CActorComponent.add_option("CCharacterLifeComponent", CCharacterLifeComponent)
Pointer_CActorComponent.add_option("CCharacterMovement", CCharacterMovement)
Pointer_CActorComponent.add_option("CChozoCommanderAIComponent", CChozoCommanderAIComponent)
Pointer_CActorComponent.add_option("CChozoCommanderEnergyShardsFragmentMovementComponent", CChozoCommanderEnergyShardsFragmentMovementComponent)
Pointer_CActorComponent.add_option("CChozoCommanderEnergyShardsSphereMovementComponent", CChozoCommanderEnergyShardsSphereMovementComponent)
Pointer_CActorComponent.add_option("CChozoCommanderSentenceSphereLifeComponent", CChozoCommanderSentenceSphereLifeComponent)
Pointer_CActorComponent.add_option("CChozoCommanderSentenceSphereMovementComponent", CChozoCommanderSentenceSphereMovementComponent)
Pointer_CActorComponent.add_option("CChozoCommanderXLifeComponent", CChozoCommanderXLifeComponent)
Pointer_CActorComponent.add_option("CChozoRobotSoldierAIComponent", CChozoRobotSoldierAIComponent)
Pointer_CActorComponent.add_option("CChozoRobotSoldierBeamMovementComponent", CChozoRobotSoldierBeamMovementComponent)
Pointer_CActorComponent.add_option("CChozoWarriorAIComponent", CChozoWarriorAIComponent)
Pointer_CActorComponent.add_option("CChozoWarriorEliteAIComponent", CChozoWarriorEliteAIComponent)
Pointer_CActorComponent.add_option("CChozoWarriorXAIComponent", CChozoWarriorXAIComponent)
Pointer_CActorComponent.add_option("CChozoWarriorXEliteAIComponent", CChozoWarriorXEliteAIComponent)
Pointer_CActorComponent.add_option("CChozoWarriorXSpitMovementComponent", CChozoWarriorXSpitMovementComponent)
Pointer_CActorComponent.add_option("CChozoZombieXAIComponent", CChozoZombieXAIComponent)
Pointer_CActorComponent.add_option("CChozoZombieXSpawnPointComponent", CChozoZombieXSpawnPointComponent)
Pointer_CActorComponent.add_option("CChozombieFXComponent", CChozombieFXComponent)
Pointer_CActorComponent.add_option("CColliderTriggerComponent", CColliderTriggerComponent)
Pointer_CActorComponent.add_option("CCollisionComponent", CCollisionComponent)
Pointer_CActorComponent.add_option("CCollisionMaterialCacheComponent", CCollisionMaterialCacheComponent)
Pointer_CActorComponent.add_option("CComponent", CComponent)
Pointer_CActorComponent.add_option("CConstantMovement", CConstantMovement)
Pointer_CActorComponent.add_option("CCooldownXBossAIComponent", CCooldownXBossAIComponent)
Pointer_CActorComponent.add_option("CCooldownXBossFireBallMovementComponent", CCooldownXBossFireBallMovementComponent)
Pointer_CActorComponent.add_option("CCooldownXBossWeakPointLifeComponent", CCooldownXBossWeakPointLifeComponent)
Pointer_CActorComponent.add_option("CCoreXAIComponent", CCoreXAIComponent)
Pointer_CActorComponent.add_option("CCubeMapComponent", CCubeMapComponent)
Pointer_CActorComponent.add_option("CCutsceneComponent", CCutsceneComponent)
Pointer_CActorComponent.add_option("CCutsceneTriggerComponent", CCutsceneTriggerComponent)
Pointer_CActorComponent.add_option("CDaivoAIComponent", CDaivoAIComponent)
Pointer_CActorComponent.add_option("CDaivoSwarmControllerComponent", CDaivoSwarmControllerComponent)
Pointer_CActorComponent.add_option("CDamageComponent", CDamageComponent)
Pointer_CActorComponent.add_option("CDamageTriggerComponent", CDamageTriggerComponent)
Pointer_CActorComponent.add_option("CDemolitionBlockActivatableActorLifeComponent", CDemolitionBlockActivatableActorLifeComponent)
Pointer_CActorComponent.add_option("CDemolitionBlockComponent", CDemolitionBlockComponent)
Pointer_CActorComponent.add_option("CDemolitionBlockLifeComponent", CDemolitionBlockLifeComponent)
Pointer_CActorComponent.add_option("CDemolitionBlockSonarTargetComponent", CDemolitionBlockSonarTargetComponent)
Pointer_CActorComponent.add_option("CDirLightComponent", CDirLightComponent)
Pointer_CActorComponent.add_option("CDizzeanSwarmControllerComponent", CDizzeanSwarmControllerComponent)
Pointer_CActorComponent.add_option("CDoorCentralUnitLifeComponent", CDoorCentralUnitLifeComponent)
Pointer_CActorComponent.add_option("CDoorEmmyFXComponent", CDoorEmmyFXComponent)
Pointer_CActorComponent.add_option("CDoorGrapplePointComponent", CDoorGrapplePointComponent)
Pointer_CActorComponent.add_option("CDoorLifeComponent", CDoorLifeComponent)
Pointer_CActorComponent.add_option("CDoorShieldLifeComponent", CDoorShieldLifeComponent)
Pointer_CActorComponent.add_option("CDredhedAIComponent", CDredhedAIComponent)
Pointer_CActorComponent.add_option("CDredhedAttackComponent", CDredhedAttackComponent)
Pointer_CActorComponent.add_option("CDropComponent", CDropComponent)
Pointer_CActorComponent.add_option("CDroppableComponent", CDroppableComponent)
Pointer_CActorComponent.add_option("CDroppableLifeComponent", CDroppableLifeComponent)
Pointer_CActorComponent.add_option("CDroppableMissileComponent", CDroppableMissileComponent)
Pointer_CActorComponent.add_option("CDroppablePowerBombComponent", CDroppablePowerBombComponent)
Pointer_CActorComponent.add_option("CDroppableSpecialEnergyComponent", CDroppableSpecialEnergyComponent)
Pointer_CActorComponent.add_option("CDropterAIComponent", CDropterAIComponent)
Pointer_CActorComponent.add_option("CDummyAIComponent", CDummyAIComponent)
Pointer_CActorComponent.add_option("CDummyMovement", CDummyMovement)
Pointer_CActorComponent.add_option("CDummyPullableGrapplePointComponent", CDummyPullableGrapplePointComponent)
Pointer_CActorComponent.add_option("CElectricGeneratorComponent", CElectricGeneratorComponent)
Pointer_CActorComponent.add_option("CElectricReactionComponent", CElectricReactionComponent)
Pointer_CActorComponent.add_option("CElectrifyingAreaComponent", CElectrifyingAreaComponent)
Pointer_CActorComponent.add_option("CElevatorCommanderUsableComponent", CElevatorCommanderUsableComponent)
Pointer_CActorComponent.add_option("CElevatorUsableComponent", CElevatorUsableComponent)
Pointer_CActorComponent.add_option("CEmergencyLightElectricReactionComponent", CEmergencyLightElectricReactionComponent)
Pointer_CActorComponent.add_option("CEmmyAIComponent", CEmmyAIComponent)
Pointer_CActorComponent.add_option("CEmmyAttackComponent", CEmmyAttackComponent)
Pointer_CActorComponent.add_option("CEmmyCaveAIComponent", CEmmyCaveAIComponent)
Pointer_CActorComponent.add_option("CEmmyForestAIComponent", CEmmyForestAIComponent)
Pointer_CActorComponent.add_option("CEmmyLabAIComponent", CEmmyLabAIComponent)
Pointer_CActorComponent.add_option("CEmmyMagmaAIComponent", CEmmyMagmaAIComponent)
Pointer_CActorComponent.add_option("CEmmyMovement", CEmmyMovement)
Pointer_CActorComponent.add_option("CEmmyProtoAIComponent", CEmmyProtoAIComponent)
Pointer_CActorComponent.add_option("CEmmySancAIComponent", CEmmySancAIComponent)
Pointer_CActorComponent.add_option("CEmmyShipyardAIComponent", CEmmyShipyardAIComponent)
Pointer_CActorComponent.add_option("CEmmySpawnPointComponent", CEmmySpawnPointComponent)
Pointer_CActorComponent.add_option("CEmmyValveComponent", CEmmyValveComponent)
Pointer_CActorComponent.add_option("CEmmyWakeUpComponent", CEmmyWakeUpComponent)
Pointer_CActorComponent.add_option("CEmmyWaveMovementComponent", CEmmyWaveMovementComponent)
Pointer_CActorComponent.add_option("CEnemyLifeComponent", CEnemyLifeComponent)
Pointer_CActorComponent.add_option("CEnemyMovement", CEnemyMovement)
Pointer_CActorComponent.add_option("CEnhanceWeakSpotComponent", CEnhanceWeakSpotComponent)
Pointer_CActorComponent.add_option("CEscapeSequenceExplosionComponent", CEscapeSequenceExplosionComponent)
Pointer_CActorComponent.add_option("CEvacuationCountDown", CEvacuationCountDown)
Pointer_CActorComponent.add_option("CEventPropComponent", CEventPropComponent)
Pointer_CActorComponent.add_option("CEventScenarioComponent", CEventScenarioComponent)
Pointer_CActorComponent.add_option("CFXComponent", CFXComponent)
Pointer_CActorComponent.add_option("CFactionComponent", CFactionComponent)
Pointer_CActorComponent.add_option("CFakePhysicsMovement", CFakePhysicsMovement)
Pointer_CActorComponent.add_option("CFanComponent", CFanComponent)
Pointer_CActorComponent.add_option("CFanCoolDownComponent", CFanCoolDownComponent)
Pointer_CActorComponent.add_option("CFingSwarmControllerComponent", CFingSwarmControllerComponent)
Pointer_CActorComponent.add_option("CFireComponent", CFireComponent)
Pointer_CActorComponent.add_option("CFloatingPropActingComponent", CFloatingPropActingComponent)
Pointer_CActorComponent.add_option("CFlockingSwarmControllerComponent", CFlockingSwarmControllerComponent)
Pointer_CActorComponent.add_option("CFloorShockWaveComponent", CFloorShockWaveComponent)
Pointer_CActorComponent.add_option("CFootstepPlatformComponent", CFootstepPlatformComponent)
Pointer_CActorComponent.add_option("CForcedMovementAreaComponent", CForcedMovementAreaComponent)
Pointer_CActorComponent.add_option("CFreezeRoomComponent", CFreezeRoomComponent)
Pointer_CActorComponent.add_option("CFrozenAsFrostbiteComponent", CFrozenAsFrostbiteComponent)
Pointer_CActorComponent.add_option("CFrozenAsPlatformComponent", CFrozenAsPlatformComponent)
Pointer_CActorComponent.add_option("CFrozenComponent", CFrozenComponent)
Pointer_CActorComponent.add_option("CFrozenPlatformComponent", CFrozenPlatformComponent)
Pointer_CActorComponent.add_option("CFulmiteBellyMineAIComponent", CFulmiteBellyMineAIComponent)
Pointer_CActorComponent.add_option("CFulmiteBellyMineAttackComponent", CFulmiteBellyMineAttackComponent)
Pointer_CActorComponent.add_option("CFulmiteBellyMineMovementComponent", CFulmiteBellyMineMovementComponent)
Pointer_CActorComponent.add_option("CFusibleBoxComponent", CFusibleBoxComponent)
Pointer_CActorComponent.add_option("CGobblerAIComponent", CGobblerAIComponent)
Pointer_CActorComponent.add_option("CGobblerSpawnPointComponent", CGobblerSpawnPointComponent)
Pointer_CActorComponent.add_option("CGoliathAIComponent", CGoliathAIComponent)
Pointer_CActorComponent.add_option("CGoliathXAIComponent", CGoliathXAIComponent)
Pointer_CActorComponent.add_option("CGoliathXBurstProjectionBombMovement", CGoliathXBurstProjectionBombMovement)
Pointer_CActorComponent.add_option("CGooplotAIComponent", CGooplotAIComponent)
Pointer_CActorComponent.add_option("CGooshockerAIComponent", CGooshockerAIComponent)
Pointer_CActorComponent.add_option("CGrabComponent", CGrabComponent)
Pointer_CActorComponent.add_option("CGrappleBeamComponent", CGrappleBeamComponent)
Pointer_CActorComponent.add_option("CGrapplePointComponent", CGrapplePointComponent)
Pointer_CActorComponent.add_option("CGroundShockerAIComponent", CGroundShockerAIComponent)
Pointer_CActorComponent.add_option("CGunComponent", CGunComponent)
Pointer_CActorComponent.add_option("CHangableGrappleMagnetSlidingBlockComponent", CHangableGrappleMagnetSlidingBlockComponent)
Pointer_CActorComponent.add_option("CHangableGrapplePointComponent", CHangableGrapplePointComponent)
Pointer_CActorComponent.add_option("CHangableGrappleSurfaceComponent", CHangableGrappleSurfaceComponent)
Pointer_CActorComponent.add_option("CHeatRoomComponent", CHeatRoomComponent)
Pointer_CActorComponent.add_option("CHeatableShieldComponent", CHeatableShieldComponent)
Pointer_CActorComponent.add_option("CHeatableShieldEnhanceWeakSpotComponent", CHeatableShieldEnhanceWeakSpotComponent)
Pointer_CActorComponent.add_option("CHecathonAIComponent", CHecathonAIComponent)
Pointer_CActorComponent.add_option("CHecathonLifeComponent", CHecathonLifeComponent)
Pointer_CActorComponent.add_option("CHecathonPlanktonFXComponent", CHecathonPlanktonFXComponent)
Pointer_CActorComponent.add_option("CHomingMovement", CHomingMovement)
Pointer_CActorComponent.add_option("CHydrogigaAIComponent", CHydrogigaAIComponent)
Pointer_CActorComponent.add_option("CHydrogigaZiplineComponent", CHydrogigaZiplineComponent)
Pointer_CActorComponent.add_option("CHydrogigaZiplineRailComponent", CHydrogigaZiplineRailComponent)
Pointer_CActorComponent.add_option("CHyperBeamBlockLifeComponent", CHyperBeamBlockLifeComponent)
Pointer_CActorComponent.add_option("CIceMissileMovement", CIceMissileMovement)
Pointer_CActorComponent.add_option("CInfesterAIComponent", CInfesterAIComponent)
Pointer_CActorComponent.add_option("CInfesterBallAIComponent", CInfesterBallAIComponent)
Pointer_CActorComponent.add_option("CInfesterBallAttackComponent", CInfesterBallAttackComponent)
Pointer_CActorComponent.add_option("CInfesterBallLifeComponent", CInfesterBallLifeComponent)
Pointer_CActorComponent.add_option("CInfesterBallMovementComponent", CInfesterBallMovementComponent)
Pointer_CActorComponent.add_option("CInputComponent", CInputComponent)
Pointer_CActorComponent.add_option("CInterpolationComponent", CInterpolationComponent)
Pointer_CActorComponent.add_option("CInventoryComponent", CInventoryComponent)
Pointer_CActorComponent.add_option("CItemLifeComponent", CItemLifeComponent)
Pointer_CActorComponent.add_option("CKraidAIComponent", CKraidAIComponent)
Pointer_CActorComponent.add_option("CKraidAcidBlobsMovementComponent", CKraidAcidBlobsMovementComponent)
Pointer_CActorComponent.add_option("CKraidBouncingCreaturesMovementComponent", CKraidBouncingCreaturesMovementComponent)
Pointer_CActorComponent.add_option("CKraidNailMovementComponent", CKraidNailMovementComponent)
Pointer_CActorComponent.add_option("CKraidShockerSplashMovementComponent", CKraidShockerSplashMovementComponent)
Pointer_CActorComponent.add_option("CKraidSpikeMovablePlatformComponent", CKraidSpikeMovablePlatformComponent)
Pointer_CActorComponent.add_option("CLandmarkComponent", CLandmarkComponent)
Pointer_CActorComponent.add_option("CLavaPoolComponent", CLavaPoolComponent)
Pointer_CActorComponent.add_option("CLavaPumpComponent", CLavaPumpComponent)
Pointer_CActorComponent.add_option("CLavapumpThermalReactionComponent", CLavapumpThermalReactionComponent)
Pointer_CActorComponent.add_option("CLifeComponent", CLifeComponent)
Pointer_CActorComponent.add_option("CLifeRechargeComponent", CLifeRechargeComponent)
Pointer_CActorComponent.add_option("CLightingComponent", CLightingComponent)
Pointer_CActorComponent.add_option("CLineBombMovement", CLineBombMovement)
Pointer_CActorComponent.add_option("CLiquidPoolBaseComponent", CLiquidPoolBaseComponent)
Pointer_CActorComponent.add_option("CLiquidSimulationComponent", CLiquidSimulationComponent)
Pointer_CActorComponent.add_option("CLockOnMissileMovement", CLockOnMissileMovement)
Pointer_CActorComponent.add_option("CLogicActionTriggerComponent", CLogicActionTriggerComponent)
Pointer_CActorComponent.add_option("CLogicCameraComponent", CLogicCameraComponent)
Pointer_CActorComponent.add_option("CLogicLookAtPlayerComponent", CLogicLookAtPlayerComponent)
Pointer_CActorComponent.add_option("CLogicPathComponent", CLogicPathComponent)
Pointer_CActorComponent.add_option("CLogicPathNavMeshItemComponent", CLogicPathNavMeshItemComponent)
Pointer_CActorComponent.add_option("CLogicShapeComponent", CLogicShapeComponent)
Pointer_CActorComponent.add_option("CMagmaCentralUnitComponent", CMagmaCentralUnitComponent)
Pointer_CActorComponent.add_option("CMagmaKraidPistonPlatformComponent", CMagmaKraidPistonPlatformComponent)
Pointer_CActorComponent.add_option("CMagmaKraidScenarioControllerComponent", CMagmaKraidScenarioControllerComponent)
Pointer_CActorComponent.add_option("CMagmaKraidSpikeComponent", CMagmaKraidSpikeComponent)
Pointer_CActorComponent.add_option("CMagnetMovablePlatformComponent", CMagnetMovablePlatformComponent)
Pointer_CActorComponent.add_option("CMagnetSlidingBlockComponent", CMagnetSlidingBlockComponent)
Pointer_CActorComponent.add_option("CMagnetSlidingBlockCounterWeightMovablePlatformComponent", CMagnetSlidingBlockCounterWeightMovablePlatformComponent)
Pointer_CActorComponent.add_option("CMagnetSlidingBlockRailComponent", CMagnetSlidingBlockRailComponent)
Pointer_CActorComponent.add_option("CMagnetSlidingBlockWithCollisionsComponent", CMagnetSlidingBlockWithCollisionsComponent)
Pointer_CActorComponent.add_option("CMagnetSurfaceComponent", CMagnetSurfaceComponent)
Pointer_CActorComponent.add_option("CMagnetSurfaceHuskComponent", CMagnetSurfaceHuskComponent)
Pointer_CActorComponent.add_option("CMapAcquisitionComponent", CMapAcquisitionComponent)
Pointer_CActorComponent.add_option("CMassiveCaterzillaSpawnGroupComponent", CMassiveCaterzillaSpawnGroupComponent)
Pointer_CActorComponent.add_option("CMaterialFXComponent", CMaterialFXComponent)
Pointer_CActorComponent.add_option("CMeleeComponent", CMeleeComponent)
Pointer_CActorComponent.add_option("CMenuAnimationChangeComponent", CMenuAnimationChangeComponent)
Pointer_CActorComponent.add_option("CMissileMovement", CMissileMovement)
Pointer_CActorComponent.add_option("CModelInstanceComponent", CModelInstanceComponent)
Pointer_CActorComponent.add_option("CModelUpdaterComponent", CModelUpdaterComponent)
Pointer_CActorComponent.add_option("CMorphBallLauncherComponent", CMorphBallLauncherComponent)
Pointer_CActorComponent.add_option("CMorphBallLauncherExitComponent", CMorphBallLauncherExitComponent)
Pointer_CActorComponent.add_option("CMorphBallMovement", CMorphBallMovement)
Pointer_CActorComponent.add_option("CMovableGrapplePointComponent", CMovableGrapplePointComponent)
Pointer_CActorComponent.add_option("CMovablePlatformComponent", CMovablePlatformComponent)
Pointer_CActorComponent.add_option("CMovementComponent", CMovementComponent)
Pointer_CActorComponent.add_option("CMultiLockOnBlockComponent", CMultiLockOnBlockComponent)
Pointer_CActorComponent.add_option("CMultiLockOnPointComponent", CMultiLockOnPointComponent)
Pointer_CActorComponent.add_option("CMultiModelUpdaterComponent", CMultiModelUpdaterComponent)
Pointer_CActorComponent.add_option("CMushroomPlatformComponent", CMushroomPlatformComponent)
Pointer_CActorComponent.add_option("CNailongAIComponent", CNailongAIComponent)
Pointer_CActorComponent.add_option("CNailongThornMovementComponent", CNailongThornMovementComponent)
Pointer_CActorComponent.add_option("CNailuggerAcidBallMovementComponent", CNailuggerAcidBallMovementComponent)
Pointer_CActorComponent.add_option("CNavMeshItemComponent", CNavMeshItemComponent)
Pointer_CActorComponent.add_option("CNoFreezeRoomComponent", CNoFreezeRoomComponent)
Pointer_CActorComponent.add_option("CObsydomithonAIComponent", CObsydomithonAIComponent)
Pointer_CActorComponent.add_option("COmniLightComponent", COmniLightComponent)
Pointer_CActorComponent.add_option("CPerceptionComponent", CPerceptionComponent)
Pointer_CActorComponent.add_option("CPersistenceComponent", CPersistenceComponent)
Pointer_CActorComponent.add_option("CPickableComponent", CPickableComponent)
Pointer_CActorComponent.add_option("CPickableItemComponent", CPickableItemComponent)
Pointer_CActorComponent.add_option("CPickableSpringBallComponent", CPickableSpringBallComponent)
Pointer_CActorComponent.add_option("CPickableSuitComponent", CPickableSuitComponent)
Pointer_CActorComponent.add_option("CPlatformTrapGrapplePointComponent", CPlatformTrapGrapplePointComponent)
Pointer_CActorComponent.add_option("CPlayerLifeComponent", CPlayerLifeComponent)
Pointer_CActorComponent.add_option("CPlayerMovement", CPlayerMovement)
Pointer_CActorComponent.add_option("CPoisonFlyAIComponent", CPoisonFlyAIComponent)
Pointer_CActorComponent.add_option("CPositionalSoundComponent", CPositionalSoundComponent)
Pointer_CActorComponent.add_option("CPowerBombBlockLifeComponent", CPowerBombBlockLifeComponent)
Pointer_CActorComponent.add_option("CPowerBombMovement", CPowerBombMovement)
Pointer_CActorComponent.add_option("CPowerGeneratorComponent", CPowerGeneratorComponent)
Pointer_CActorComponent.add_option("CPowerUpLifeComponent", CPowerUpLifeComponent)
Pointer_CActorComponent.add_option("CProfessorDoorComponent", CProfessorDoorComponent)
Pointer_CActorComponent.add_option("CProjectileMovement", CProjectileMovement)
Pointer_CActorComponent.add_option("CProtoCentralUnitComponent", CProtoCentralUnitComponent)
Pointer_CActorComponent.add_option("CProtoEmmyChaseMusicTriggerComponent", CProtoEmmyChaseMusicTriggerComponent)
Pointer_CActorComponent.add_option("CPullOffGrapplePointComponent", CPullOffGrapplePointComponent)
Pointer_CActorComponent.add_option("CPullableGrapplePointComponent", CPullableGrapplePointComponent)
Pointer_CActorComponent.add_option("CQuarentineDoorComponent", CQuarentineDoorComponent)
Pointer_CActorComponent.add_option("CQuetzoaAIComponent", CQuetzoaAIComponent)
Pointer_CActorComponent.add_option("CQuetzoaEnergyWaveMovementComponent", CQuetzoaEnergyWaveMovementComponent)
Pointer_CActorComponent.add_option("CQuetzoaMultiTargetProjectileMovementComponent", CQuetzoaMultiTargetProjectileMovementComponent)
Pointer_CActorComponent.add_option("CQuetzoaXAIComponent", CQuetzoaXAIComponent)
Pointer_CActorComponent.add_option("CRedenkiSwarmControllerComponent", CRedenkiSwarmControllerComponent)
Pointer_CActorComponent.add_option("CReturnAreaSmartObjectComponent", CReturnAreaSmartObjectComponent)
Pointer_CActorComponent.add_option("CRinkaAIComponent", CRinkaAIComponent)
Pointer_CActorComponent.add_option("CRinkaUnitComponent", CRinkaUnitComponent)
Pointer_CActorComponent.add_option("CRobotAIComponent", CRobotAIComponent)
Pointer_CActorComponent.add_option("CRockDiverAIComponent", CRockDiverAIComponent)
Pointer_CActorComponent.add_option("CRockDiverSpawnPointComponent", CRockDiverSpawnPointComponent)
Pointer_CActorComponent.add_option("CRodomithonXAIComponent", CRodomithonXAIComponent)
Pointer_CActorComponent.add_option("CRodotukAIComponent", CRodotukAIComponent)
Pointer_CActorComponent.add_option("CRotationalPlatformComponent", CRotationalPlatformComponent)
Pointer_CActorComponent.add_option("CRumbleComponent", CRumbleComponent)
Pointer_CActorComponent.add_option("CSabotoruAIComponent", CSabotoruAIComponent)
Pointer_CActorComponent.add_option("CSabotoruLifeComponent", CSabotoruLifeComponent)
Pointer_CActorComponent.add_option("CSabotoruSpawnPointComponent", CSabotoruSpawnPointComponent)
Pointer_CActorComponent.add_option("CSamusAlternativeActionPlayerComponent", CSamusAlternativeActionPlayerComponent)
Pointer_CActorComponent.add_option("CSamusAnimationComponent", CSamusAnimationComponent)
Pointer_CActorComponent.add_option("CSamusGunComponent", CSamusGunComponent)
Pointer_CActorComponent.add_option("CSamusModelUpdaterComponent", CSamusModelUpdaterComponent)
Pointer_CActorComponent.add_option("CSamusMovement", CSamusMovement)
Pointer_CActorComponent.add_option("CSaveStationUsableComponent", CSaveStationUsableComponent)
Pointer_CActorComponent.add_option("CSceneComponent", CSceneComponent)
Pointer_CActorComponent.add_option("CSceneModelAnimationComponent", CSceneModelAnimationComponent)
Pointer_CActorComponent.add_option("CSclawkAIComponent", CSclawkAIComponent)
Pointer_CActorComponent.add_option("CSclawkLifeComponent", CSclawkLifeComponent)
Pointer_CActorComponent.add_option("CScorpiusAIComponent", CScorpiusAIComponent)
Pointer_CActorComponent.add_option("CScorpiusFXComponent", CScorpiusFXComponent)
Pointer_CActorComponent.add_option("CScorpiusPoisonousSpitMovementComponent", CScorpiusPoisonousSpitMovementComponent)
Pointer_CActorComponent.add_option("CScourgeAIComponent", CScourgeAIComponent)
Pointer_CActorComponent.add_option("CScourgeLifeComponent", CScourgeLifeComponent)
Pointer_CActorComponent.add_option("CScriptComponent", CScriptComponent)
Pointer_CActorComponent.add_option("CSegmentLightComponent", CSegmentLightComponent)
Pointer_CActorComponent.add_option("CSensorDoorComponent", CSensorDoorComponent)
Pointer_CActorComponent.add_option("CShakernautAIComponent", CShakernautAIComponent)
Pointer_CActorComponent.add_option("CShelmitAIComponent", CShelmitAIComponent)
Pointer_CActorComponent.add_option("CShineonAIComponent", CShineonAIComponent)
Pointer_CActorComponent.add_option("CShipRechargeComponent", CShipRechargeComponent)
Pointer_CActorComponent.add_option("CShockWaveComponent", CShockWaveComponent)
Pointer_CActorComponent.add_option("CShockWavePoolComponent", CShockWavePoolComponent)
Pointer_CActorComponent.add_option("CShootActivatorComponent", CShootActivatorComponent)
Pointer_CActorComponent.add_option("CShootActivatorHidrogigaComponent", CShootActivatorHidrogigaComponent)
Pointer_CActorComponent.add_option("CShotComponent", CShotComponent)
Pointer_CActorComponent.add_option("CSideEnemyMovement", CSideEnemyMovement)
Pointer_CActorComponent.add_option("CSlidleSpawnPointComponent", CSlidleSpawnPointComponent)
Pointer_CActorComponent.add_option("CSlowNailongSpawnPointComponent", CSlowNailongSpawnPointComponent)
Pointer_CActorComponent.add_option("CSluggerAIComponent", CSluggerAIComponent)
Pointer_CActorComponent.add_option("CSluggerAcidBallMovementComponent", CSluggerAcidBallMovementComponent)
Pointer_CActorComponent.add_option("CSmartObjectComponent", CSmartObjectComponent)
Pointer_CActorComponent.add_option("CSonarTargetComponent", CSonarTargetComponent)
Pointer_CActorComponent.add_option("CSoundListenerComponent", CSoundListenerComponent)
Pointer_CActorComponent.add_option("CSoundProofTriggerComponent", CSoundProofTriggerComponent)
Pointer_CActorComponent.add_option("CSoundTrigger", CSoundTrigger)
Pointer_CActorComponent.add_option("CSpawnGroupComponent", CSpawnGroupComponent)
Pointer_CActorComponent.add_option("CSpawnPointComponent", CSpawnPointComponent)
Pointer_CActorComponent.add_option("CSpbSprActivator", CSpbSprActivator)
Pointer_CActorComponent.add_option("CSpecialEnergyComponent", CSpecialEnergyComponent)
Pointer_CActorComponent.add_option("CSpitclawkAIComponent", CSpitclawkAIComponent)
Pointer_CActorComponent.add_option("CSpittailMagmaBallMovementComponent", CSpittailMagmaBallMovementComponent)
Pointer_CActorComponent.add_option("CSpotLightComponent", CSpotLightComponent)
Pointer_CActorComponent.add_option("CStandaloneFXComponent", CStandaloneFXComponent)
Pointer_CActorComponent.add_option("CStartPointComponent", CStartPointComponent)
Pointer_CActorComponent.add_option("CSteamJetComponent", CSteamJetComponent)
Pointer_CActorComponent.add_option("CSteeringMovement", CSteeringMovement)
Pointer_CActorComponent.add_option("CSunnapAIComponent", CSunnapAIComponent)
Pointer_CActorComponent.add_option("CSuperMissileMovement", CSuperMissileMovement)
Pointer_CActorComponent.add_option("CSwarmAttackComponent", CSwarmAttackComponent)
Pointer_CActorComponent.add_option("CSwarmControllerComponent", CSwarmControllerComponent)
Pointer_CActorComponent.add_option("CSwifterAIComponent", CSwifterAIComponent)
Pointer_CActorComponent.add_option("CSwifterSpawnGroupComponent", CSwifterSpawnGroupComponent)
Pointer_CActorComponent.add_option("CSwingableGrapplePointComponent", CSwingableGrapplePointComponent)
Pointer_CActorComponent.add_option("CTakumakuAIComponent", CTakumakuAIComponent)
Pointer_CActorComponent.add_option("CTargetComponent", CTargetComponent)
Pointer_CActorComponent.add_option("CTeleporterUsableComponent", CTeleporterUsableComponent)
Pointer_CActorComponent.add_option("CThermalDeviceComponent", CThermalDeviceComponent)
Pointer_CActorComponent.add_option("CThermalReactionComponent", CThermalReactionComponent)
Pointer_CActorComponent.add_option("CThermalRoomConnectionFX", CThermalRoomConnectionFX)
Pointer_CActorComponent.add_option("CThermalRoomFX", CThermalRoomFX)
Pointer_CActorComponent.add_option("CTimelineComponent", CTimelineComponent)
Pointer_CActorComponent.add_option("CTimerComponent", CTimerComponent)
Pointer_CActorComponent.add_option("CTotalRechargeComponent", CTotalRechargeComponent)
Pointer_CActorComponent.add_option("CTrainUsableComponent", CTrainUsableComponent)
Pointer_CActorComponent.add_option("CTrainUsableComponentCutScene", CTrainUsableComponentCutScene)
Pointer_CActorComponent.add_option("CTrainWithPortalUsableComponent", CTrainWithPortalUsableComponent)
Pointer_CActorComponent.add_option("CTriggerComponent", CTriggerComponent)
Pointer_CActorComponent.add_option("CTriggerNavMeshItemComponent", CTriggerNavMeshItemComponent)
Pointer_CActorComponent.add_option("CTunnelTrapMorphballComponent", CTunnelTrapMorphballComponent)
Pointer_CActorComponent.add_option("CUnlockAreaSmartObjectComponent", CUnlockAreaSmartObjectComponent)
Pointer_CActorComponent.add_option("CUsableComponent", CUsableComponent)
Pointer_CActorComponent.add_option("CVideoManagerComponent", CVideoManagerComponent)
Pointer_CActorComponent.add_option("CVulkranAIComponent", CVulkranAIComponent)
Pointer_CActorComponent.add_option("CVulkranMagmaBallMovementComponent", CVulkranMagmaBallMovementComponent)
Pointer_CActorComponent.add_option("CWarLotusAIComponent", CWarLotusAIComponent)
Pointer_CActorComponent.add_option("CWaterNozzleComponent", CWaterNozzleComponent)
Pointer_CActorComponent.add_option("CWaterPlatformUsableComponent", CWaterPlatformUsableComponent)
Pointer_CActorComponent.add_option("CWaterPoolComponent", CWaterPoolComponent)
Pointer_CActorComponent.add_option("CWaterTriggerChangeComponent", CWaterTriggerChangeComponent)
Pointer_CActorComponent.add_option("CWeaponMovement", CWeaponMovement)
Pointer_CActorComponent.add_option("CWeightActivableMovablePlatformComponent", CWeightActivableMovablePlatformComponent)
Pointer_CActorComponent.add_option("CWeightActivablePropComponent", CWeightActivablePropComponent)
Pointer_CActorComponent.add_option("CWeightActivatedPlatformSmartObjectComponent", CWeightActivatedPlatformSmartObjectComponent)
Pointer_CActorComponent.add_option("CWorldGraph", CWorldGraph)
Pointer_CActorComponent.add_option("CXParasiteAIComponent", CXParasiteAIComponent)
Pointer_CActorComponent.add_option("CXParasiteDropComponent", CXParasiteDropComponent)
Pointer_CActorComponent.add_option("CYamplotXAIComponent", CYamplotXAIComponent)

Pointer_CAttackPreset.add_option("CAttackPreset", CAttackPreset)

Pointer_CBarelyFrozenIceInfo.add_option("CBarelyFrozenIceInfo", CBarelyFrozenIceInfo)

Pointer_CBouncingCreaturesLaunchPattern.add_option("CBouncingCreaturesLaunchPattern", CBouncingCreaturesLaunchPattern)

Pointer_CCentralUnitWeightedEdges.add_option("CCentralUnitWeightedEdges", CCentralUnitWeightedEdges)

Pointer_CChozoRobotSoldierCannonShotPattern.add_option("CChozoRobotSoldierCannonShotPattern", CChozoRobotSoldierCannonShotPattern)

Pointer_CCooldownXBossFireWallDef.add_option("CCooldownXBossFireWallDef", CCooldownXBossFireWallDef)

Pointer_CCooldownXBossLavaCarpetDef.add_option("CCooldownXBossLavaCarpetDef", CCooldownXBossLavaCarpetDef)

Pointer_CCooldownXBossLavaDropsDef.add_option("CCooldownXBossLavaDropsDef", CCooldownXBossLavaDropsDef)

Pointer_CEmmyAutoForbiddenEdgesDef.add_option("CEmmyAutoForbiddenEdgesDef", CEmmyAutoForbiddenEdgesDef)

Pointer_CEmmyAutoGlobalSmartLinkDef.add_option("CEmmyAutoGlobalSmartLinkDef", CEmmyAutoGlobalSmartLinkDef)

Pointer_CEmmyOverrideDeathPositionDef.add_option("CEmmyOverrideDeathPositionDef", CEmmyOverrideDeathPositionDef)

Pointer_CEnvironmentData_SAmbient.add_option("CEnvironmentData::SAmbient", CEnvironmentData_SAmbient)

Pointer_CEnvironmentData_SBloom.add_option("CEnvironmentData::SBloom", CEnvironmentData_SBloom)

Pointer_CEnvironmentData_SCubeMap.add_option("CEnvironmentData::SCubeMap", CEnvironmentData_SCubeMap)

Pointer_CEnvironmentData_SDepthTint.add_option("CEnvironmentData::SDepthTint", CEnvironmentData_SDepthTint)

Pointer_CEnvironmentData_SFog.add_option("CEnvironmentData::SFog", CEnvironmentData_SFog)

Pointer_CEnvironmentData_SHemisphericalLight.add_option("CEnvironmentData::SHemisphericalLight", CEnvironmentData_SHemisphericalLight)

Pointer_CEnvironmentData_SIBLAttenuation.add_option("CEnvironmentData::SIBLAttenuation", CEnvironmentData_SIBLAttenuation)

Pointer_CEnvironmentData_SMaterialTint.add_option("CEnvironmentData::SMaterialTint", CEnvironmentData_SMaterialTint)

Pointer_CEnvironmentData_SPlayerLight.add_option("CEnvironmentData::SPlayerLight", CEnvironmentData_SPlayerLight)

Pointer_CEnvironmentData_SSSAO.add_option("CEnvironmentData::SSSAO", CEnvironmentData_SSSAO)

Pointer_CEnvironmentData_SToneMapping.add_option("CEnvironmentData::SToneMapping", CEnvironmentData_SToneMapping)

Pointer_CEnvironmentData_SVerticalFog.add_option("CEnvironmentData::SVerticalFog", CEnvironmentData_SVerticalFog)

Pointer_CEnvironmentManager.add_option("CEnvironmentManager", CEnvironmentManager)

Pointer_CEnvironmentMusicPresets.add_option("CEnvironmentMusicPresets", CEnvironmentMusicPresets)

Pointer_CEnvironmentSoundPresets.add_option("CEnvironmentSoundPresets", CEnvironmentSoundPresets)

Pointer_CEnvironmentVisualPresets.add_option("CEnvironmentVisualPresets", CEnvironmentVisualPresets)

Pointer_CKraidSpinningNailsDef.add_option("CKraidSpinningNailsDef", CKraidSpinningNailsDef)

Pointer_CLightManager.add_option("CLightManager", CLightManager)

Pointer_CLogicCamera.add_option("CLogicCamera", CLogicCamera)

Pointer_CPattern.add_option("CPattern", CPattern)

Pointer_CPolypFallPattern.add_option("CPolypFallPattern", CPolypFallPattern)

Pointer_CScenario.add_option("CScenario", CScenario)

Pointer_CShootDCBones.add_option("CShootDCBones", CShootDCBones)

Pointer_CShotLaunchConfig.add_option("CShotLaunchConfig", CShotLaunchConfig)
Pointer_CShotLaunchConfig.add_option("CShotVariableAngleLaunchConfig", CShotVariableAngleLaunchConfig)
Pointer_CShotLaunchConfig.add_option("CShotVariableSpeedLaunchConfig", CShotVariableSpeedLaunchConfig)

Pointer_CShotManager.add_option("CShotManager", CShotManager)

Pointer_CSubAreaManager.add_option("CSubAreaManager", CSubAreaManager)

Pointer_CSubareaCharclassGroup.add_option("CSubareaCharclassGroup", CSubareaCharclassGroup)

Pointer_CSubareaInfo.add_option("CSubareaInfo", CSubareaInfo)

Pointer_CSubareaSetup.add_option("CSubareaSetup", CSubareaSetup)

Pointer_CTentacle.add_option("CTentacle", CTentacle)

Pointer_CTriggerComponent_SActivationCondition.add_option("CTriggerComponent::SActivationCondition", CTriggerComponent_SActivationCondition)

Pointer_CTriggerLogicAction.add_option("CTriggerLogicAction", CTriggerLogicAction)
Pointer_CTriggerLogicAction.add_option("CAllowCoolShinesparkLogicAction", CAllowCoolShinesparkLogicAction)
Pointer_CTriggerLogicAction.add_option("CCameraToRailLogicAction", CCameraToRailLogicAction)
Pointer_CTriggerLogicAction.add_option("CChangeSetupLogicAction", CChangeSetupLogicAction)
Pointer_CTriggerLogicAction.add_option("CChangeStateDoorsLogicAction", CChangeStateDoorsLogicAction)
Pointer_CTriggerLogicAction.add_option("CCheckCoolShinesparkSuccessfullyCompletedLogicAction", CCheckCoolShinesparkSuccessfullyCompletedLogicAction)
Pointer_CTriggerLogicAction.add_option("CCoolShinesparkMarkMinimapLogicAction", CCoolShinesparkMarkMinimapLogicAction)
Pointer_CTriggerLogicAction.add_option("CEmmyStateOverrideLogicAction", CEmmyStateOverrideLogicAction)
Pointer_CTriggerLogicAction.add_option("CForbiddenEdgesLogicAction", CForbiddenEdgesLogicAction)
Pointer_CTriggerLogicAction.add_option("CForceMovementLogicAction", CForceMovementLogicAction)
Pointer_CTriggerLogicAction.add_option("CFreeAimTutoLogicAction", CFreeAimTutoLogicAction)
Pointer_CTriggerLogicAction.add_option("CHoldPlayerDirectionOnSubAreaChangeLogicAction", CHoldPlayerDirectionOnSubAreaChangeLogicAction)
Pointer_CTriggerLogicAction.add_option("CIgnoreFloorSlideUpperBodySubmergedLogicAction", CIgnoreFloorSlideUpperBodySubmergedLogicAction)
Pointer_CTriggerLogicAction.add_option("CItemDestructionLogicAction", CItemDestructionLogicAction)
Pointer_CTriggerLogicAction.add_option("CLockRoomLogicAction", CLockRoomLogicAction)
Pointer_CTriggerLogicAction.add_option("CLuaCallsLogicAction", CLuaCallsLogicAction)
Pointer_CTriggerLogicAction.add_option("CMarkMinimapLogicAction", CMarkMinimapLogicAction)
Pointer_CTriggerLogicAction.add_option("CPerceptionModifierLogicAction", CPerceptionModifierLogicAction)
Pointer_CTriggerLogicAction.add_option("CSPBTutoLogicAction", CSPBTutoLogicAction)
Pointer_CTriggerLogicAction.add_option("CSPRTutoLogicAction", CSPRTutoLogicAction)
Pointer_CTriggerLogicAction.add_option("CSamusOverrideDistanceToBorderLogicAction", CSamusOverrideDistanceToBorderLogicAction)
Pointer_CTriggerLogicAction.add_option("CSaveGameFromEmmyDoorLogicAction", CSaveGameFromEmmyDoorLogicAction)
Pointer_CTriggerLogicAction.add_option("CSaveGameLogicAction", CSaveGameLogicAction)
Pointer_CTriggerLogicAction.add_option("CSaveGameToSnapshotLogicAction", CSaveGameToSnapshotLogicAction)
Pointer_CTriggerLogicAction.add_option("CSaveSnapshotToCheckpointLogicAction", CSaveSnapshotToCheckpointLogicAction)
Pointer_CTriggerLogicAction.add_option("CSetActorEnabledLogicAction", CSetActorEnabledLogicAction)
Pointer_CTriggerLogicAction.add_option("CShowPopUpCompositionLogicAction", CShowPopUpCompositionLogicAction)
Pointer_CTriggerLogicAction.add_option("CStartCentralUnitCombatLogicAction", CStartCentralUnitCombatLogicAction)
Pointer_CTriggerLogicAction.add_option("CSubareaTransitionTypeLogicAction", CSubareaTransitionTypeLogicAction)
Pointer_CTriggerLogicAction.add_option("CTutoEnterLogicAction", CTutoEnterLogicAction)
Pointer_CTriggerLogicAction.add_option("CTutoExitLogicAction", CTutoExitLogicAction)

Pointer_CXParasiteBehavior.add_option("CXParasiteBehavior", CXParasiteBehavior)
Pointer_CXParasiteBehavior.add_option("CXParasiteGoSpawnBehavior", CXParasiteGoSpawnBehavior)
Pointer_CXParasiteBehavior.add_option("CXParasiteGoTransformBehavior", CXParasiteGoTransformBehavior)
Pointer_CXParasiteBehavior.add_option("CXParasiteStayOnPlaceBehavior", CXParasiteStayOnPlaceBehavior)
Pointer_CXParasiteBehavior.add_option("CXParasiteWanderThenFleeBehavior", CXParasiteWanderThenFleeBehavior)

Pointer_base_global_CFilePathStrId.add_option("base::global::CFilePathStrId", base_global_CFilePathStrId)

Pointer_base_global_CRntSmallDictionary_base_global_CStrId__CActorComponentPtr_.add_option("base::global::CRntSmallDictionary<base::global::CStrId, CActorComponent*>", base_global_CRntSmallDictionary_base_global_CStrId__CActorComponentPtr_)

Pointer_base_global_CRntVector_CEnvironmentData_SAmbientTransition_.add_option("base::global::CRntVector<CEnvironmentData::SAmbientTransition>", base_global_CRntVector_CEnvironmentData_SAmbientTransition_)

Pointer_base_global_CRntVector_CEnvironmentData_SBloomTransition_.add_option("base::global::CRntVector<CEnvironmentData::SBloomTransition>", base_global_CRntVector_CEnvironmentData_SBloomTransition_)

Pointer_base_global_CRntVector_CEnvironmentData_SCubeMapTransition_.add_option("base::global::CRntVector<CEnvironmentData::SCubeMapTransition>", base_global_CRntVector_CEnvironmentData_SCubeMapTransition_)

Pointer_base_global_CRntVector_CEnvironmentData_SDepthTintTransition_.add_option("base::global::CRntVector<CEnvironmentData::SDepthTintTransition>", base_global_CRntVector_CEnvironmentData_SDepthTintTransition_)

Pointer_base_global_CRntVector_CEnvironmentData_SFogTransition_.add_option("base::global::CRntVector<CEnvironmentData::SFogTransition>", base_global_CRntVector_CEnvironmentData_SFogTransition_)

Pointer_base_global_CRntVector_CEnvironmentData_SHemisphericalLightTransition_.add_option("base::global::CRntVector<CEnvironmentData::SHemisphericalLightTransition>", base_global_CRntVector_CEnvironmentData_SHemisphericalLightTransition_)

Pointer_base_global_CRntVector_CEnvironmentData_SIBLAttenuationTransition_.add_option("base::global::CRntVector<CEnvironmentData::SIBLAttenuationTransition>", base_global_CRntVector_CEnvironmentData_SIBLAttenuationTransition_)

Pointer_base_global_CRntVector_CEnvironmentData_SMaterialTintTransition_.add_option("base::global::CRntVector<CEnvironmentData::SMaterialTintTransition>", base_global_CRntVector_CEnvironmentData_SMaterialTintTransition_)

Pointer_base_global_CRntVector_CEnvironmentData_SPlayerLightTransition_.add_option("base::global::CRntVector<CEnvironmentData::SPlayerLightTransition>", base_global_CRntVector_CEnvironmentData_SPlayerLightTransition_)

Pointer_base_global_CRntVector_CEnvironmentData_SSSAOTransition_.add_option("base::global::CRntVector<CEnvironmentData::SSSAOTransition>", base_global_CRntVector_CEnvironmentData_SSSAOTransition_)

Pointer_base_global_CRntVector_CEnvironmentData_SToneMappingTransition_.add_option("base::global::CRntVector<CEnvironmentData::SToneMappingTransition>", base_global_CRntVector_CEnvironmentData_SToneMappingTransition_)

Pointer_base_global_CRntVector_CEnvironmentData_SVerticalFogTransition_.add_option("base::global::CRntVector<CEnvironmentData::SVerticalFogTransition>", base_global_CRntVector_CEnvironmentData_SVerticalFogTransition_)

Pointer_base_global_CRntVector_std_unique_ptr_CSubareaCharclassGroup__.add_option("base::global::CRntVector<std::unique_ptr<CSubareaCharclassGroup>>", base_global_CRntVector_std_unique_ptr_CSubareaCharclassGroup__)

Pointer_base_global_CRntVector_std_unique_ptr_CSubareaSetup__.add_option("base::global::CRntVector<std::unique_ptr<CSubareaSetup>>", base_global_CRntVector_std_unique_ptr_CSubareaSetup__)

Pointer_base_reflection_CTypedValue.add_option("base::global::CRntFile", base_global_CRntFile)

Pointer_game_logic_collision_CCollider.add_option("game::logic::collision::CCollider", game_logic_collision_CCollider)

Pointer_game_logic_collision_CShape.add_option("game::logic::collision::CShape", game_logic_collision_CShape)
Pointer_game_logic_collision_CShape.add_option("game::logic::collision::CAABoxShape2D", game_logic_collision_CAABoxShape2D)
Pointer_game_logic_collision_CShape.add_option("game::logic::collision::CCapsuleShape2D", game_logic_collision_CCapsuleShape2D)
Pointer_game_logic_collision_CShape.add_option("game::logic::collision::CCircleShape2D", game_logic_collision_CCircleShape2D)
Pointer_game_logic_collision_CShape.add_option("game::logic::collision::COBoxShape2D", game_logic_collision_COBoxShape2D)
Pointer_game_logic_collision_CShape.add_option("game::logic::collision::CPolygonCollectionShape", game_logic_collision_CPolygonCollectionShape)

Pointer_querysystem_CEvaluator.add_option("querysystem::CEvaluator", querysystem_CEvaluator)
Pointer_querysystem_CEvaluator.add_option("querysystem::CChozoRobotSoldierHeightEvaluator", querysystem_CChozoRobotSoldierHeightEvaluator)
Pointer_querysystem_CEvaluator.add_option("querysystem::CCurrentEvaluator", querysystem_CCurrentEvaluator)
Pointer_querysystem_CEvaluator.add_option("querysystem::CDistanceEvaluator", querysystem_CDistanceEvaluator)
Pointer_querysystem_CEvaluator.add_option("querysystem::CDistanceToTargetEvaluator", querysystem_CDistanceToTargetEvaluator)
Pointer_querysystem_CEvaluator.add_option("querysystem::CFilterToEvaluator", querysystem_CFilterToEvaluator)

Pointer_querysystem_CFilter.add_option("querysystem::CFilter", querysystem_CFilter)
Pointer_querysystem_CFilter.add_option("querysystem::CChozoRobotSoldierIsInFrustumFilter", querysystem_CChozoRobotSoldierIsInFrustumFilter)
Pointer_querysystem_CFilter.add_option("querysystem::CChozoRobotSoldierIsInMeleePathFilter", querysystem_CChozoRobotSoldierIsInMeleePathFilter)
Pointer_querysystem_CFilter.add_option("querysystem::CChozoRobotSoldierIsInShootingPositionPathFilter", querysystem_CChozoRobotSoldierIsInShootingPositionPathFilter)
Pointer_querysystem_CFilter.add_option("querysystem::CChozoRobotSoldierLineOfFireFilter", querysystem_CChozoRobotSoldierLineOfFireFilter)
Pointer_querysystem_CFilter.add_option("querysystem::CChozoRobotSoldierMinTargetDistanceFilter", querysystem_CChozoRobotSoldierMinTargetDistanceFilter)
Pointer_querysystem_CFilter.add_option("querysystem::CIsInFrustumFilter", querysystem_CIsInFrustumFilter)
Pointer_querysystem_CFilter.add_option("querysystem::CIsInNavigablePathFilter", querysystem_CIsInNavigablePathFilter)
Pointer_querysystem_CFilter.add_option("querysystem::CLookAtTargetFilter", querysystem_CLookAtTargetFilter)
Pointer_querysystem_CFilter.add_option("querysystem::CMaxDistanceFilter", querysystem_CMaxDistanceFilter)
Pointer_querysystem_CFilter.add_option("querysystem::CMaxTargetDistanceFilter", querysystem_CMaxTargetDistanceFilter)
Pointer_querysystem_CFilter.add_option("querysystem::CMinDistanceFilter", querysystem_CMinDistanceFilter)
Pointer_querysystem_CFilter.add_option("querysystem::CMinTargetDistanceFilter", querysystem_CMinTargetDistanceFilter)
Pointer_querysystem_CFilter.add_option("querysystem::CSameEntitySideFilter", querysystem_CSameEntitySideFilter)

Pointer_sound_CAudioPresets.add_option("sound::CAudioPresets", sound_CAudioPresets)

Pointer_sound_CMusicManager.add_option("sound::CMusicManager", sound_CMusicManager)

Pointer_sound_CSoundManager.add_option("sound::CSoundManager", sound_CSoundManager)

