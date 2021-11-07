''' Waters
    MassLynx Python SDK
'''

from enum import IntEnum

class MassLynxBaseType(IntEnum):
    SCAN = 1
    INFO = 2
    CHROM = 3
    ANALOG = 4
    LOCKMASS = 5
    CENTRIOD = 6
    DDA = 7
    MSE = 8
    UNINITALISED = 99

class MassLynxIonMode(IntEnum):
    EI_POS = 100
    EI_NEG = EI_POS + 1
    CI_POS = EI_POS + 2
    CI_NEG = EI_POS + 3
    FB_POS = EI_POS + 4
    FB_NEG = EI_POS + 5
    TS_POS = EI_POS + 6
    TS_NEG = EI_POS + 7
    ES_POS = EI_POS + 8
    ES_NEG = EI_POS + 9
    AI_POS = EI_POS + 10
    AI_NEG = EI_POS + 11
    LD_POS = EI_POS + 12
    LD_NEG = EI_POS + 13
    UNINITIALISED = EI_POS + 99

class MassLynxFunctionType(IntEnum):
    MS = 200
    SIR = 1 + MS
    DLY = 2 + MS
    CAT = 3 + MS
    OFF = 4 + MS
    PAR = 5 + MS
    DAU = 6 + MS
    NL = 7 + MS
    NG = 8 + MS
    MRM = 9 + MS
    Q1F = 10 + MS
    MS2 = 11 + MS
    DAD = 12 + MS
    TOF = 13 + MS
    PSD = 14 + MS
    TOFS = 15 + MS
    TOFD = 16 + MS
    MTOF = 17 + MS
    TOFM = 18 + MS
    TOFP = 19 + MS
    ASVS = 20 + MS
    ASMS = 21 + MS
    ASVSIR = 22 + MS
    ASMSIR = 23 + MS
    QUADD = 24 + MS
    ASBE = 25 + MS
    ASB2E = 26 + MS
    ASCNL = 27 + MS
    ASMIKES = 28 + MS
    ASMRM = 29 + MS
    ASNRMS = 30 + MS
    ASMRMQ = 31 + MS
    UNINITIALISED = MS + 99

class MassLynxHeaderItem(IntEnum):
    VERSION = 300
    ACQUIRED_NAME = 1 + VERSION
    ACQUIRED_DATE = 2 + VERSION
    ACQUIRED_TIME = 3 + VERSION
    JOB_CODE = 4 + VERSION
    TASK_CODE = 5 + VERSION
    USER_NAME = 6 + VERSION
    INSTRUMENT = 7 + VERSION
    CONDITIONS = 8 + VERSION
    LAB_NAME = 9 + VERSION
    SAMPLE_DESCRIPTION = 10 + VERSION
    SOLVENT_DELAY = 11 + VERSION
    SUBMITTER = 12 + VERSION
    SAMPLE_ID = 13 + VERSION
    BOTTLE_NUMBER = 14 + VERSION
    ANALOG_CH1_OFFSET = 15 + VERSION
    ANALOG_CH2_OFFSET = 16 + VERSION
    ANALOG_CH3_OFFSET = 17 + VERSION
    ANALOG_CH4_OFFSET = 18 + VERSION
    CAL_MS1_STATIC = 19 + VERSION
    CAL_MS2_STATIC = 20 + VERSION
    CAL_MS1_STATIC_PARAMS = 21 + VERSION
    CAL_MS1_DYNAMIC_PARAMS = 22 + VERSION
    CAL_MS2_STATIC_PARAMS = 23 + VERSION
    CAL_MS2_DYNAMIC_PARAMS = 24 + VERSION
    CAL_MS1_FAST_PARAMS = 25 + VERSION
    CAL_MS2_FAST_PARAMS = 26 + VERSION
    CAL_TIME = 27 + VERSION
    CAL_DATE = 28 + VERSION
    CAL_TEMPERATURE = 29 + VERSION
    INLET_METHOD = 30 + VERSION
    SPARE1 = 31 + VERSION
    SPARE2 = 32 + VERSION
    SPARE3 = 33 + VERSION
    SPARE4 = 34 + VERSION
    SPARE5 = 35 + VERSION


class MassLynxScanItem(IntEnum):
    LINEAR_DETECTOR_VOLTAGE = 401
    LINEAR_SENSITIVITY = LINEAR_DETECTOR_VOLTAGE + 1
    REFLECTRON_LENS_VOLTAGE = LINEAR_DETECTOR_VOLTAGE + 2
    REFLECTRON_DETECTOR_VOLTAGE = LINEAR_DETECTOR_VOLTAGE + 3
    REFLECTRON_SENSITIVITY = LINEAR_DETECTOR_VOLTAGE + 4
    LASER_REPETITION_RATE = LINEAR_DETECTOR_VOLTAGE + 5
    COURSE_LASER_CONTROL = LINEAR_DETECTOR_VOLTAGE + 6
    FINE_LASER_CONTROL = LINEAR_DETECTOR_VOLTAGE + 7
    LASERAIM_XPOS = LINEAR_DETECTOR_VOLTAGE + 8
    LASERAIM_YPOS = LINEAR_DETECTOR_VOLTAGE + 9
    NUM_SHOTS_SUMMED = LINEAR_DETECTOR_VOLTAGE + 10
    NUM_SHOTS_PERFORMED = LINEAR_DETECTOR_VOLTAGE + 11
    SEGMENT_NUMBER = LINEAR_DETECTOR_VOLTAGE + 12
    LCMP_TFM_WELL = LINEAR_DETECTOR_VOLTAGE + 13
    SEGMENT_TYPE = LINEAR_DETECTOR_VOLTAGE + 14
    SOURCE_REGION1 = LINEAR_DETECTOR_VOLTAGE + 15
    SOURCE_REGION2 = LINEAR_DETECTOR_VOLTAGE + 16
    REFLECTRON_FIELD_LENGTH = LINEAR_DETECTOR_VOLTAGE + 17
    REFLECTRON_LENGTH = LINEAR_DETECTOR_VOLTAGE + 18
    REFLECTRON_VOLT = LINEAR_DETECTOR_VOLTAGE + 19
    SAMPLE_PLATE_VOLT = LINEAR_DETECTOR_VOLTAGE + 20
    REFLECTRON_FIELD_LENGTH_ALT = LINEAR_DETECTOR_VOLTAGE + 21
    REFLECTRON_LENGTH_ALT = LINEAR_DETECTOR_VOLTAGE + 22
    PSD_STEP_MAJOR = LINEAR_DETECTOR_VOLTAGE + 23
    PSD_STEP_MINOR = LINEAR_DETECTOR_VOLTAGE + 24
    PSD_FACTOR_1 = LINEAR_DETECTOR_VOLTAGE + 25
    NEEDLE = LINEAR_DETECTOR_VOLTAGE + 49
    COUNTER_ELECTRODE_VOLTAGE = LINEAR_DETECTOR_VOLTAGE + 50
    SAMPLING_CONE_VOLTAGE = LINEAR_DETECTOR_VOLTAGE + 51
    SKIMMER_LENS = LINEAR_DETECTOR_VOLTAGE + 52
    SKIMMER = LINEAR_DETECTOR_VOLTAGE + 53
    PROBE_TEMPERATURE = LINEAR_DETECTOR_VOLTAGE + 54
    SOURCE_TEMPERATURE = LINEAR_DETECTOR_VOLTAGE + 55
    RF_VOLTAGE = LINEAR_DETECTOR_VOLTAGE + 56
    SOURCE_APERTURE = LINEAR_DETECTOR_VOLTAGE + 57
    SOURCE_CODE = LINEAR_DETECTOR_VOLTAGE + 58
    LM_RESOLUTION = LINEAR_DETECTOR_VOLTAGE + 59
    HM_RESOLUTION = LINEAR_DETECTOR_VOLTAGE + 60
    COLLISION_ENERGY = LINEAR_DETECTOR_VOLTAGE + 61
    ION_ENERGY = LINEAR_DETECTOR_VOLTAGE + 62
    MULTIPLIER1 = LINEAR_DETECTOR_VOLTAGE + 63
    MULTIPLIER2 = LINEAR_DETECTOR_VOLTAGE + 64
    TRANSPORTDC = LINEAR_DETECTOR_VOLTAGE + 65
    TOF_APERTURE = LINEAR_DETECTOR_VOLTAGE + 66
    ACC_VOLTAGE = LINEAR_DETECTOR_VOLTAGE + 67
    STEERING = LINEAR_DETECTOR_VOLTAGE + 68
    FOCUS = LINEAR_DETECTOR_VOLTAGE + 69
    ENTRANCE = LINEAR_DETECTOR_VOLTAGE + 70
    GUARD = LINEAR_DETECTOR_VOLTAGE + 71
    TOF = LINEAR_DETECTOR_VOLTAGE + 72
    REFLECTRON = LINEAR_DETECTOR_VOLTAGE + 73
    COLLISION_RF = LINEAR_DETECTOR_VOLTAGE + 74
    TRANSPORT_RF = LINEAR_DETECTOR_VOLTAGE + 75
    SET_MASS = LINEAR_DETECTOR_VOLTAGE + 76,
    COLLISION_ENERGY2 = LINEAR_DETECTOR_VOLTAGE + 77
    SET_MASS_CALL_SUPPORTED = LINEAR_DETECTOR_VOLTAGE + 78
    SET_MASS_CALIBRATED = LINEAR_DETECTOR_VOLTAGE + 79
    SONAR_ENABLED = LINEAR_DETECTOR_VOLTAGE + 80
    QUAD_START_MASS = LINEAR_DETECTOR_VOLTAGE + 81
    QUAD_STOP_MASS = LINEAR_DETECTOR_VOLTAGE + 82
    QUAD_PEAK_WIDTH = LINEAR_DETECTOR_VOLTAGE + 83
    REFERENCE_SCAN = LINEAR_DETECTOR_VOLTAGE + 99
    USE_LOCKMASS_CORRECTION = LINEAR_DETECTOR_VOLTAGE + 100
    LOCKMASS_CORRECTION = LINEAR_DETECTOR_VOLTAGE + 101
    USETEMP_CORRECTION = LINEAR_DETECTOR_VOLTAGE + 102
    TEMP_CORRECTION = LINEAR_DETECTOR_VOLTAGE + 103
    TEMP_COEFFICIENT = LINEAR_DETECTOR_VOLTAGE + 104
    FAIMS_COMPENSATION_VOLTAGE = LINEAR_DETECTOR_VOLTAGE + 105
    TIC_TRACE_A = LINEAR_DETECTOR_VOLTAGE + 106
    TIC_TRACE_B = LINEAR_DETECTOR_VOLTAGE + 107
    RAW_EE_CV = LINEAR_DETECTOR_VOLTAGE + 108
    RAW_EE_CE = LINEAR_DETECTOR_VOLTAGE + 110
    ACCURATE_MASS = LINEAR_DETECTOR_VOLTAGE + 111
    ACCURATE_MASS_FLAGS = LINEAR_DETECTOR_VOLTAGE + 112
    SCAN_ERROR_FLAG = LINEAR_DETECTOR_VOLTAGE + 113
    DRE_TRANSMISSION = LINEAR_DETECTOR_VOLTAGE + 114
    SCAN_PUSH_COUNT = LINEAR_DETECTOR_VOLTAGE + 115
    RAW_STAT_SWAVE_NORMALISATION_FACTOR = LINEAR_DETECTOR_VOLTAGE + 116
    MIN_DRIFT_TIME_CHANNEL = LINEAR_DETECTOR_VOLTAGE + 121
    MAX_DRIFT_TIME_CHANNEL = LINEAR_DETECTOR_VOLTAGE + 122
    TOTAL_ION_CURRENT = LINEAR_DETECTOR_VOLTAGE + 251
    BASE_PEAK_MASS = LINEAR_DETECTOR_VOLTAGE + 252
    BASE_PEAK_INTENSITY = LINEAR_DETECTOR_VOLTAGE + 253
    PEAKS_IN_SCAN = LINEAR_DETECTOR_VOLTAGE + 254
    UNINITIALISED = LINEAR_DETECTOR_VOLTAGE + 298

class MassLynxSampleListItem(IntEnum):
    FILE_NAME = 700
    FILE_TEXT = FILE_NAME + 1
    MS_FILE = FILE_NAME + 2
    MS_TUNE_FILE = FILE_NAME + 3
    INLET_FILE = FILE_NAME + 4
    INLET_PRERUN = FILE_NAME + 5
    INLET_POSTRUN = FILE_NAME + 6
    INLET_SWITCH = FILE_NAME + 7
    AUTO_FILE = FILE_NAME + 8
    PROCESS = FILE_NAME + 9
    PROCESS_PARAMS = FILE_NAME + 10
    PROCESS_OPTIONS = FILE_NAME + 11
    ACQU_PROCESS_FILE = FILE_NAME + 12
    ACQU_PROCESS_PARAMS = FILE_NAME + 13
    ACQU_PROCESS_OPTIONS = FILE_NAME + 14
    PROCESS_ACTION = FILE_NAME + 15
    SAMPLE_LOCATION = FILE_NAME + 16
    SAMPLE_GROUP = FILE_NAME + 17
    JOB = FILE_NAME + 18
    TASK = FILE_NAME + 19
    USER = FILE_NAME + 20
    SUBMITTER = FILE_NAME + 21
    CONDITIONS = FILE_NAME + 22
    TYPE = FILE_NAME + 23
    CONTROL = FILE_NAME + 24
    ID = FILE_NAME + 25
    CONC_A = FILE_NAME + 26
    CONC_B = FILE_NAME + 27
    CONC_C = FILE_NAME + 28
    CONC_D = FILE_NAME + 29
    CONC_E = FILE_NAME + 30
    CONC_F = FILE_NAME + 31
    CONC_G = FILE_NAME + 32
    CONC_H = FILE_NAME + 33
    CONC_I = FILE_NAME + 34
    CONC_J = FILE_NAME + 35
    CONC_K = FILE_NAME + 36
    CONC_L = FILE_NAME + 37
    CONC_M = FILE_NAME + 38
    CONC_N = FILE_NAME + 39
    CONC_O = FILE_NAME + 40
    CONC_P = FILE_NAME + 41
    CONC_Q = FILE_NAME + 42
    CONC_R = FILE_NAME + 43
    CONC_S = FILE_NAME + 44
    CONC_T = FILE_NAME + 45
    WAVELENGTH_A = FILE_NAME + 46
    WAVELENGTH_B = FILE_NAME + 47
    WAVELENGTH_C = FILE_NAME + 48
    WAVELENGTH_D = FILE_NAME + 49
    WAVELENGTH_E = FILE_NAME + 50
    WAVELENGTH_F = FILE_NAME + 51
    WAVELENGTH_G = FILE_NAME + 52
    WAVELENGTH_H = FILE_NAME + 53
    WAVELENGTH_I = FILE_NAME + 54
    WAVELENGTH_J = FILE_NAME + 55
    MASS_A = FILE_NAME + 56
    MASS_B = FILE_NAME + 57
    MASS_C = FILE_NAME + 58
    MASS_D = FILE_NAME + 59
    MASS_E = FILE_NAME + 60
    MASS_F = FILE_NAME + 61
    MASS_G = FILE_NAME + 62
    MASS_H = FILE_NAME + 63
    MASS_I = FILE_NAME + 64
    MASS_J = FILE_NAME + 65
    MASS_K = FILE_NAME + 66
    MASS_L = FILE_NAME + 67
    MASS_M = FILE_NAME + 68
    MASS_N = FILE_NAME + 59
    MASS_O = FILE_NAME + 70
    MASS_P = FILE_NAME + 71
    MASS_Q = FILE_NAME + 72
    MASS_R = FILE_NAME + 73
    MASS_S = FILE_NAME + 74
    MASS_T = FILE_NAME + 75
    MASS_U = FILE_NAME + 76
    MASS_V = FILE_NAME + 77
    MASS_W = FILE_NAME + 78
    MASS_X = FILE_NAME + 79
    MASS_Y = FILE_NAME + 80
    MASS_Z = FILE_NAME + 81
    MASS_AA = FILE_NAME + 82
    MASS_BB = FILE_NAME + 83
    MASS_CC = FILE_NAME + 84
    MASS_DD = FILE_NAME + 85
    FRACTION_FILE = FILE_NAME + 86
    FRACTION_1 = FILE_NAME + 87
    FRACTION_2 = FILE_NAME + 88
    FRACTION_3 = FILE_NAME + 89
    FRACTION_4 = FILE_NAME + 90
    FRACTION_5 = FILE_NAME + 91
    FRACTION_6 = FILE_NAME + 92
    FRACTION_7 = FILE_NAME + 93
    FRACTION_8 = FILE_NAME + 94
    FRACTION_9 = FILE_NAME + 95
    FRACTION_10 = FILE_NAME + 96
    FRACTION_BOOLEAN_LOGIC = FILE_NAME + 97
    FRACTION_START = FILE_NAME + 98
    INJ_VOL = FILE_NAME + 99
    STOCK_DIL = FILE_NAME + 100
    USER_DIVISOR_1 = FILE_NAME + 101
    USER_FACTOR_1 = FILE_NAME + 102
    USER_FACTOR_2 = FILE_NAME + 103
    USER_FACTOR_3 = FILE_NAME + 104
    SPARE_1 = FILE_NAME + 105
    SPARE_2 = FILE_NAME + 106
    SPARE_3 = FILE_NAME + 107
    SPARE_4 = FILE_NAME + 108
    SPARE_5 = FILE_NAME + 109
    HPLC_FILE = FILE_NAME + 110
    QUAN_REF = FILE_NAME + 111
    AUTO_ADDITION = FILE_NAME + 112
    MOLFILE = FILE_NAME + 113
    SUBJECTTEXT = FILE_NAME + 114
    SUBJECTTIME = FILE_NAME + 115
    METH_DB = FILE_NAME + 116
    CURVE_DB = FILE_NAME + 117


class MassLynxScanType(IntEnum):
    MS1 = 1
    MS2 = MS1 + 2
    UNINITIALISED = MS1 + 9

class MassLynxAcquisitionType(IntEnum):
    DDA = 0
    MSE = DDA + 1
    HDDDA = DDA + 2
    HDMSE = DDA + 3
    SONAR = DDA + 4
    UNINITIALISED = DDA + 99

class ThresholdParameters(IntEnum):
    VALUE = 0
    THRESHTYPE = 1



class ThresholdType2(IntEnum):
    ABSOLUTE_1 = 0
    RELATIVE_2 = 1



class SmoothParameter(IntEnum):
    NUMBER = 1
    WIDTH = NUMBER + 1
    SMOOTHTYPE = NUMBER + 2


class SmoothType(IntEnum):
    MEAN = 1
    MEDIAN = MEAN + 1
    SAVITZKY_GOLAY = MEAN + 2



class LockMassParameter(IntEnum):
    MASS = 1000
    TOLERANCE = MASS + 1
    FORCE = MASS + 2


class FunctionDefinition(IntEnum):
    CONTINUUM = 1100
    IONMODE = CONTINUUM + 1
    FUNCTIONTYPE = CONTINUUM + 2
    STARTMASS = CONTINUUM + 3
    ENDMASS = CONTINUUM + 4
    CDT_SCANS = CONTINUUM + 5,
    SAMPLINGFREQUENCY = CONTINUUM + 6
    LTEFF = CONTINUUM + 7
    VEFF = CONTINUUM + 8,


class AnalogParameter(IntEnum):
    DESCRIPTION = 1200 + 1
    UNITS = DESCRIPTION + 2
    TYPE = DESCRIPTION + 3


class AnalogTraceType(IntEnum):
    ANALOG = 1250
    ELSD = ANALOG + 1
    READBACK = ANALOG + 2


class AutoLynxStatus(IntEnum):
    QUEUED = 1300
    PROCESSED = QUEUED + 1
    FAILED = QUEUED + 2
    NOTFOUND = QUEUED + 3
    UNINITIALISED = QUEUED + 9

