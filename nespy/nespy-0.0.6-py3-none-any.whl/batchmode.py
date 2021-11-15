from enum import Enum


class BatchMode(Enum):
    """
    This enum is for the batch function in the DataStream class.

    There are two:

    ON_CHANGE
    
    ON_TIME_OVER
    """
    ON_CHANGE = False
    ON_TIME_OVER = True
