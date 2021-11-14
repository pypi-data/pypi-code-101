"""Encoding definitions
"""

PATTERN_ID = "pattern_id"
CLUSTER = "cluster"
PATTERN_DEF = "pattern_def"
# P_COLUMNS        	   		= "P columns"
# RELATION_TYPE    	   		= "relation type"
# Q_COLUMNS        	   		= "Q columns"
# P_PART           	   		= "P"
# RELATION         	   		= "relation"
# Q_PART           	   		= "Q"
SUPPORT = "support"
EXCEPTIONS = "exceptions"
CONFIDENCE = "confidence"
RELATIVE_SUPPORT = "relative support"
RELATIVE_EXCEPTIONS = "relative exceptions"
ADDED_VALUE = "added value"
CASUAL_CONFIDENCE = "casual confidence"
CASUAL_SUPPORT = "casual support"
CERTAINTY_FACTOR = "certainty factor"
CONVICTION = "conviction"
COSINE = "cosine"
CONFIRMED_CONFIDENCE = "confirmed confidence"

PATTERN_STATUS = "pattern status"
ENCODINGS = "encodings"
PANDAS = "pandas"
ERROR = "Error message"
RESULT_TYPE = "result_type"
INDEX = "index"
P_VALUES = "P values"
Q_VALUES = "Q values"

ENCODE = "encode"

INITIAL_PATTERN_STATUS = "not defined"
TEXT_CONFIRMATION = "confirmation"
TEXT_EXCEPTION = "exception"

DEFAULT_SHEET_NAME_PATTERNS = "Patterns"
SHEET_NAME_POST_CO = "_co"
SHEET_NAME_POST_EX = "_ex"

DEFAULT_METRICS = [SUPPORT, EXCEPTIONS, CONFIDENCE]
ALL_METRICS = [
    SUPPORT,
    EXCEPTIONS,
    CONFIDENCE,
    RELATIVE_SUPPORT,
    RELATIVE_EXCEPTIONS,
    ADDED_VALUE,
    CASUAL_CONFIDENCE,
    CASUAL_SUPPORT,
    CERTAINTY_FACTOR,
    CONVICTION,
    COSINE,
    CONFIRMED_CONFIDENCE,
]

PATTERNS_COLUMNS = [
    PATTERN_ID,
    CLUSTER,
    PATTERN_DEF,
    SUPPORT,
    EXCEPTIONS,
    CONFIDENCE,
    PATTERN_STATUS,
    ENCODINGS,
    PANDAS,
    ERROR,
]

RESULTS_COLUMNS = [
    RESULT_TYPE,
    PATTERN_ID,
    CLUSTER,
    INDEX,
    SUPPORT,
    EXCEPTIONS,
    CONFIDENCE,
    PATTERN_DEF,
    P_VALUES,
    Q_VALUES,
]
