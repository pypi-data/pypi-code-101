"""
Aggregators for file mining results
"""
from collections import Counter
from typing import Dict, \
    Union

from cocluremig.analyzer.commit.util import AverageElement


def additive_dict_merge(dict_1: Dict[str, Union[int, float, AverageElement]],
                        dict_2: Dict[str, Union[int, float, AverageElement]]) \
        -> Dict[str, Union[int, float, AverageElement]]:
    """
    Dictionary per key value addition
    @param dict_1: a dictionary
    @param dict_2: another dictionary
    @return: A dictionary containing added values
    """
    dict_1 = Counter(dict_1)
    dict_1.update(dict_2)
    return dict_1
