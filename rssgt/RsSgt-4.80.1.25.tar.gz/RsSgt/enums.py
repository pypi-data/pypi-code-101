from enum import Enum


# noinspection SpellCheckingInspection
class AnalogDigitalMode(Enum):
	"""2 Members, ANALog ... DIGital"""
	ANALog = 0
	DIGital = 1


# noinspection SpellCheckingInspection
class ArbClockMode(Enum):
	"""2 Members, MSAMple ... SAMPle"""
	MSAMple = 0
	SAMPle = 1


# noinspection SpellCheckingInspection
class ArbClockSyncMode(Enum):
	"""4 Members, DIIN ... SLAVe"""
	DIIN = 0
	MASTer = 1
	NONE = 2
	SLAVe = 3


# noinspection SpellCheckingInspection
class ArbLevMode(Enum):
	"""2 Members, HIGHest ... UNCHanged"""
	HIGHest = 0
	UNCHanged = 1


# noinspection SpellCheckingInspection
class ArbMultCarrCresMode(Enum):
	"""3 Members, MAX ... OFF"""
	MAX = 0
	MIN = 1
	OFF = 2


# noinspection SpellCheckingInspection
class ArbMultCarrLevRef(Enum):
	"""2 Members, PEAK ... RMS"""
	PEAK = 0
	RMS = 1


# noinspection SpellCheckingInspection
class ArbMultCarrSigDurMod(Enum):
	"""4 Members, LCM ... USER"""
	LCM = 0
	LONG = 1
	SHORt = 2
	USER = 3


# noinspection SpellCheckingInspection
class ArbMultCarrSpacMode(Enum):
	"""2 Members, ARBitrary ... EQUidistant"""
	ARBitrary = 0
	EQUidistant = 1


# noinspection SpellCheckingInspection
class ArbSegmNextSourIntNext(Enum):
	"""2 Members, INTernal ... NEXT"""
	INTernal = 0
	NEXT = 1


# noinspection SpellCheckingInspection
class ArbSignType(Enum):
	"""4 Members, AWGN ... SINE"""
	AWGN = 0
	CIQ = 1
	RECT = 2
	SINE = 3


# noinspection SpellCheckingInspection
class ArbTrigSegmModeNoEhop(Enum):
	"""4 Members, NEXT ... SEQuencer"""
	NEXT = 0
	NSEam = 1
	SAME = 2
	SEQuencer = 3


# noinspection SpellCheckingInspection
class ArbWaveSegmClocMode(Enum):
	"""3 Members, HIGHest ... USER"""
	HIGHest = 0
	UNCHanged = 1
	USER = 2


# noinspection SpellCheckingInspection
class ArbWaveSegmMarkMode(Enum):
	"""2 Members, IGNore ... TAKE"""
	IGNore = 0
	TAKE = 1


# noinspection SpellCheckingInspection
class ArbWaveSegmPowMode(Enum):
	"""2 Members, ERMS ... UNCHanged"""
	ERMS = 0
	UNCHanged = 1


# noinspection SpellCheckingInspection
class ArbWaveSegmRest(Enum):
	"""5 Members, MRK1 ... OFF"""
	MRK1 = 0
	MRK2 = 1
	MRK3 = 2
	MRK4 = 3
	OFF = 4


# noinspection SpellCheckingInspection
class AttMode(Enum):
	"""3 Members, APASsive ... FIXed"""
	APASsive = 0
	AUTO = 1
	FIXed = 2


# noinspection SpellCheckingInspection
class BbImpOptMode(Enum):
	"""4 Members, FAST ... UCORrection"""
	FAST = 0
	QHIGh = 1
	QHTable = 2
	UCORrection = 3


# noinspection SpellCheckingInspection
class BbinSampRateMode(Enum):
	"""2 Members, DIN ... USER"""
	DIN = 0
	USER = 1


# noinspection SpellCheckingInspection
class BbSystemConfiguration(Enum):
	"""2 Members, AFETracking ... STANdard"""
	AFETracking = 0
	STANdard = 1


# noinspection SpellCheckingInspection
class ByteOrder(Enum):
	"""2 Members, NORMal ... SWAPped"""
	NORMal = 0
	SWAPped = 1


# noinspection SpellCheckingInspection
class CalDataMode(Enum):
	"""2 Members, CUSTomer ... FACTory"""
	CUSTomer = 0
	FACTory = 1


# noinspection SpellCheckingInspection
class CalPowDetAtt(Enum):
	"""4 Members, HIGH ... OFF"""
	HIGH = 0
	LOW = 1
	MED = 2
	OFF = 3


# noinspection SpellCheckingInspection
class CfrAlgo(Enum):
	"""1 Members, CLFiltering ... CLFiltering"""
	CLFiltering = 0


# noinspection SpellCheckingInspection
class CfrFiltMode(Enum):
	"""2 Members, ENHanced ... SIMPle"""
	ENHanced = 0
	SIMPle = 1


# noinspection SpellCheckingInspection
class ClockSourceB(Enum):
	"""3 Members, AINTernal ... INTernal"""
	AINTernal = 0
	EXTernal = 1
	INTernal = 2


# noinspection SpellCheckingInspection
class ClocOutpMode(Enum):
	"""2 Members, BIT ... SYMBol"""
	BIT = 0
	SYMBol = 1


# noinspection SpellCheckingInspection
class ClocSourBb(Enum):
	"""4 Members, AINTernal ... INTernal"""
	AINTernal = 0
	COUPled = 1
	EXTernal = 2
	INTernal = 3


# noinspection SpellCheckingInspection
class Colour(Enum):
	"""4 Members, GREen ... YELLow"""
	GREen = 0
	NONE = 1
	RED = 2
	YELLow = 3


# noinspection SpellCheckingInspection
class DataSour(Enum):
	"""11 Members, DLISt ... ZERO"""
	DLISt = 0
	ONE = 1
	PATTern = 2
	PN11 = 3
	PN15 = 4
	PN16 = 5
	PN20 = 6
	PN21 = 7
	PN23 = 8
	PN9 = 9
	ZERO = 10


# noinspection SpellCheckingInspection
class DevExpFormat(Enum):
	"""4 Members, CGPRedefined ... XML"""
	CGPRedefined = 0
	CGUSer = 1
	SCPI = 2
	XML = 3


# noinspection SpellCheckingInspection
class DexchExtension(Enum):
	"""2 Members, CSV ... TXT"""
	CSV = 0
	TXT = 1


# noinspection SpellCheckingInspection
class DexchMode(Enum):
	"""2 Members, EXPort ... IMPort"""
	EXPort = 0
	IMPort = 1


# noinspection SpellCheckingInspection
class DexchSepCol(Enum):
	"""4 Members, COMMa ... TABulator"""
	COMMa = 0
	SEMicolon = 1
	SPACe = 2
	TABulator = 3


# noinspection SpellCheckingInspection
class DexchSepDec(Enum):
	"""2 Members, COMMa ... DOT"""
	COMMa = 0
	DOT = 1


# noinspection SpellCheckingInspection
class DmFilterA(Enum):
	"""18 Members, APCO25 ... SPHase"""
	APCO25 = 0
	C2K3x = 1
	COEQualizer = 2
	COF705 = 3
	COFequalizer = 4
	CONE = 5
	COSine = 6
	DIRac = 7
	ENPShape = 8
	EWPShape = 9
	GAUSs = 10
	LGAuss = 11
	LPASs = 12
	LPASSEVM = 13
	PGAuss = 14
	RCOSine = 15
	RECTangle = 16
	SPHase = 17


# noinspection SpellCheckingInspection
class DmTrigMode(Enum):
	"""5 Members, AAUTo ... SINGle"""
	AAUTo = 0
	ARETrigger = 1
	AUTO = 2
	RETRigger = 3
	SINGle = 4


# noinspection SpellCheckingInspection
class DpdPowRef(Enum):
	"""3 Members, ADPD ... SDPD"""
	ADPD = 0
	BDPD = 1
	SDPD = 2


# noinspection SpellCheckingInspection
class DpdShapeMode(Enum):
	"""3 Members, NORMalized ... TABLe"""
	NORMalized = 0
	POLYnomial = 1
	TABLe = 2


# noinspection SpellCheckingInspection
class FormData(Enum):
	"""2 Members, ASCii ... PACKed"""
	ASCii = 0
	PACKed = 1


# noinspection SpellCheckingInspection
class FormStatReg(Enum):
	"""4 Members, ASCii ... OCTal"""
	ASCii = 0
	BINary = 1
	HEXadecimal = 2
	OCTal = 3


# noinspection SpellCheckingInspection
class FreqStepMode(Enum):
	"""2 Members, DECimal ... USER"""
	DECimal = 0
	USER = 1


# noinspection SpellCheckingInspection
class IecDevId(Enum):
	"""2 Members, AUTO ... USER"""
	AUTO = 0
	USER = 1


# noinspection SpellCheckingInspection
class IecTermMode(Enum):
	"""2 Members, EOI ... STANdard"""
	EOI = 0
	STANdard = 1


# noinspection SpellCheckingInspection
class ImpG50G10K(Enum):
	"""2 Members, G10K ... G50"""
	G10K = 0
	G50 = 1


# noinspection SpellCheckingInspection
class InclExcl(Enum):
	"""2 Members, EXCLude ... INCLude"""
	EXCLude = 0
	INCLude = 1


# noinspection SpellCheckingInspection
class InputImpRf(Enum):
	"""3 Members, G10K ... G50"""
	G10K = 0
	G1K = 1
	G50 = 2


# noinspection SpellCheckingInspection
class Interpolation(Enum):
	"""3 Members, LINear ... POWer"""
	LINear = 0
	OFF = 1
	POWer = 2


# noinspection SpellCheckingInspection
class IqMode(Enum):
	"""2 Members, ANALog ... BASeband"""
	ANALog = 0
	BASeband = 1


# noinspection SpellCheckingInspection
class IqOutDispViaType(Enum):
	"""2 Members, LEVel ... PEP"""
	LEVel = 0
	PEP = 1


# noinspection SpellCheckingInspection
class IqOutEnvAdaption(Enum):
	"""3 Members, AUTO ... POWer"""
	AUTO = 0
	MANual = 1
	POWer = 2


# noinspection SpellCheckingInspection
class IqOutEnvDetrFunc(Enum):
	"""3 Members, F1 ... F3"""
	F1 = 0
	F2 = 1
	F3 = 2


# noinspection SpellCheckingInspection
class IqOutEnvEtRak(Enum):
	"""4 Members, ET1V2 ... USER"""
	ET1V2 = 0
	ET1V5 = 1
	ET2V0 = 2
	USER = 3


# noinspection SpellCheckingInspection
class IqOutEnvScale(Enum):
	"""2 Members, POWer ... VOLTage"""
	POWer = 0
	VOLTage = 1


# noinspection SpellCheckingInspection
class IqOutEnvShapeMode(Enum):
	"""6 Members, DETRoughing ... TABLe"""
	DETRoughing = 0
	LINear = 1
	OFF = 2
	POLYnomial = 3
	POWer = 4
	TABLe = 5


# noinspection SpellCheckingInspection
class IqOutEnvTerm(Enum):
	"""2 Members, GROund ... WIRE"""
	GROund = 0
	WIRE = 1


# noinspection SpellCheckingInspection
class IqOutEnvVrEf(Enum):
	"""2 Members, VCC ... VOUT"""
	VCC = 0
	VOUT = 1


# noinspection SpellCheckingInspection
class IqOutMode(Enum):
	"""3 Members, FIXed ... VATTenuated"""
	FIXed = 0
	VARiable = 1
	VATTenuated = 2


# noinspection SpellCheckingInspection
class IqOutType(Enum):
	"""2 Members, DIFFerential ... SINGle"""
	DIFFerential = 0
	SINGle = 1


# noinspection SpellCheckingInspection
class NetMode(Enum):
	"""2 Members, AUTO ... STATic"""
	AUTO = 0
	STATic = 1


# noinspection SpellCheckingInspection
class NoisAwgnDispModeRfBb(Enum):
	"""2 Members, BB ... RF"""
	BB = 0
	RF = 1


# noinspection SpellCheckingInspection
class NoisAwgnMode(Enum):
	"""3 Members, ADD ... ONLY"""
	ADD = 0
	CW = 1
	ONLY = 2


# noinspection SpellCheckingInspection
class NoisAwgnPowMode(Enum):
	"""3 Members, CN ... SN"""
	CN = 0
	EN = 1
	SN = 2


# noinspection SpellCheckingInspection
class NoisAwgnPowRefMode(Enum):
	"""2 Members, CARRier ... NOISe"""
	CARRier = 0
	NOISe = 1


# noinspection SpellCheckingInspection
class NormalInverted(Enum):
	"""2 Members, INVerted ... NORMal"""
	INVerted = 0
	NORMal = 1


# noinspection SpellCheckingInspection
class NumbersA(Enum):
	"""2 Members, _1 ... _2"""
	_1 = 0
	_2 = 1


# noinspection SpellCheckingInspection
class OpMode(Enum):
	"""2 Members, BBBYpass ... NORMal"""
	BBBYpass = 0
	NORMal = 1


# noinspection SpellCheckingInspection
class Parity(Enum):
	"""3 Members, EVEN ... ODD"""
	EVEN = 0
	NONE = 1
	ODD = 2


# noinspection SpellCheckingInspection
class PowAlcState(Enum):
	"""4 Members, _1 ... ON"""
	_1 = 0
	AUTO = 1
	OFF = 2
	ON = 3


# noinspection SpellCheckingInspection
class PowLevBehaviour(Enum):
	"""6 Members, AUTO ... USER"""
	AUTO = 0
	CVSWr = 1
	CWSWr = 2
	MONotone = 3
	UNINterrupted = 4
	USER = 5


# noinspection SpellCheckingInspection
class PowLevMode(Enum):
	"""4 Members, LOWDistortion ... USER"""
	LOWDistortion = 0
	LOWNoise = 1
	NORMal = 2
	USER = 3


# noinspection SpellCheckingInspection
class PowOutpPonMode(Enum):
	"""2 Members, OFF ... UNCHanged"""
	OFF = 0
	UNCHanged = 1


# noinspection SpellCheckingInspection
class PowRfOffMode(Enum):
	"""2 Members, FIXed ... MAX"""
	FIXed = 0
	MAX = 1


# noinspection SpellCheckingInspection
class PowSensWithUndef(Enum):
	"""9 Members, SENS1 ... UNDefined"""
	SENS1 = 0
	SENS2 = 1
	SENS3 = 2
	SENS4 = 3
	SENSor1 = 4
	SENSor2 = 5
	SENSor3 = 6
	SENSor4 = 7
	UNDefined = 8


# noinspection SpellCheckingInspection
class PulsMode(Enum):
	"""4 Members, DOUBle ... SINGle"""
	DOUBle = 0
	PHOPptrain = 1
	PTRain = 2
	SINGle = 3


# noinspection SpellCheckingInspection
class PulsTrigMode(Enum):
	"""3 Members, AUTO ... EXTernal"""
	AUTO = 0
	EGATe = 1
	EXTernal = 2


# noinspection SpellCheckingInspection
class RecScpiCmdMode(Enum):
	"""4 Members, AUTO ... OFF"""
	AUTO = 0
	DAUTo = 1
	MANual = 2
	OFF = 3


# noinspection SpellCheckingInspection
class RefLoOutput(Enum):
	"""3 Members, LO ... REF"""
	LO = 0
	OFF = 1
	REF = 2


# noinspection SpellCheckingInspection
class RoscBandWidtExt(Enum):
	"""2 Members, NARRow ... WIDE"""
	NARRow = 0
	WIDE = 1


# noinspection SpellCheckingInspection
class RoscFreqExt(Enum):
	"""4 Members, _1000MHZ ... _13MHZ"""
	_1000MHZ = 0
	_100MHZ = 1
	_10MHZ = 2
	_13MHZ = 3


# noinspection SpellCheckingInspection
class Rs232BdRate(Enum):
	"""7 Members, _115200 ... _9600"""
	_115200 = 0
	_19200 = 1
	_2400 = 2
	_38400 = 3
	_4800 = 4
	_57600 = 5
	_9600 = 6


# noinspection SpellCheckingInspection
class SatNavClockMode(Enum):
	"""2 Members, MSYMbol ... SYMBol"""
	MSYMbol = 0
	SYMBol = 1


# noinspection SpellCheckingInspection
class SlopeType(Enum):
	"""2 Members, NEGative ... POSitive"""
	NEGative = 0
	POSitive = 1


# noinspection SpellCheckingInspection
class SourceInt(Enum):
	"""2 Members, EXTernal ... INTernal"""
	EXTernal = 0
	INTernal = 1


# noinspection SpellCheckingInspection
class Test(Enum):
	"""4 Members, _0 ... STOPped"""
	_0 = 0
	_1 = 1
	RUNning = 2
	STOPped = 3


# noinspection SpellCheckingInspection
class TestExtIqMode(Enum):
	"""2 Members, IQIN ... IQOut"""
	IQIN = 0
	IQOut = 1


# noinspection SpellCheckingInspection
class TrigDelUnit(Enum):
	"""2 Members, SAMPle ... TIME"""
	SAMPle = 0
	TIME = 1


# noinspection SpellCheckingInspection
class TriggerSourceB(Enum):
	"""4 Members, BEXTernal ... OBASeband"""
	BEXTernal = 0
	EXTernal = 1
	INTernal = 2
	OBASeband = 3


# noinspection SpellCheckingInspection
class TrigMarkMode(Enum):
	"""6 Members, PATTern ... UNCHanged"""
	PATTern = 0
	PULSe = 1
	RATio = 2
	RESTart = 3
	TRIGger = 4
	UNCHanged = 5


# noinspection SpellCheckingInspection
class TrigRunMode(Enum):
	"""2 Members, RUN ... STOP"""
	RUN = 0
	STOP = 1


# noinspection SpellCheckingInspection
class UnitAngle(Enum):
	"""3 Members, DEGree ... RADian"""
	DEGree = 0
	DEGRee = 1
	RADian = 2


# noinspection SpellCheckingInspection
class UnitPower(Enum):
	"""3 Members, DBM ... V"""
	DBM = 0
	DBUV = 1
	V = 2


# noinspection SpellCheckingInspection
class UnitSlB(Enum):
	"""2 Members, SAMPle ... SEQuence"""
	SAMPle = 0
	SEQuence = 1


# noinspection SpellCheckingInspection
class UnitSlXmRadio(Enum):
	"""3 Members, MCM ... TPL"""
	MCM = 0
	SAMPle = 1
	TPL = 2


# noinspection SpellCheckingInspection
class Unknown(Enum):
	"""2 Members, DBM ... V"""
	DBM = 0
	V = 1


# noinspection SpellCheckingInspection
class UserPlug(Enum):
	"""18 Members, CIN ... TRIGger"""
	CIN = 0
	COUT = 1
	HIGH = 2
	LOW = 3
	MARRived = 4
	MKR1 = 5
	MKR2 = 6
	MLATency = 7
	NEXT = 8
	PEMSource = 9
	PETRigger = 10
	PVOut = 11
	SIN = 12
	SNValid = 13
	SOUT = 14
	SVALid = 15
	TOUT = 16
	TRIGger = 17


# noinspection SpellCheckingInspection
class XmRadioMarkMode(Enum):
	"""7 Members, MCM ... USER"""
	MCM = 0
	PATTern = 1
	PULSe = 2
	RATio = 3
	TPL = 4
	TRIGger = 5
	USER = 6


# noinspection SpellCheckingInspection
class XmRadioPhysLayer(Enum):
	"""6 Members, SAT1A ... TERRB"""
	SAT1A = 0
	SAT1B = 1
	SAT2A = 2
	SAT2B = 3
	TERRA = 4
	TERRB = 5
