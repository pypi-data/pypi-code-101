from enum import Enum, auto


class APIType(Enum):
    CFS = auto()
    FINANCIAL_CONTRACTS = auto()
    CURVES_AND_SURFACES = auto()
    HISTORICAL_PRICING = auto()
    ESG = auto()
    PRICING = auto()
    OWNERSHIP = auto()
    CHAINS = auto()
    DATA_GRID = auto()
