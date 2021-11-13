import numpy as np
import pandas as pd
from collections import OrderedDict, Counter
import itertools
from typing import *

Group = tuple[str, list[int]]
Groups = list[Group]


def df_groups(groups: Groups) -> pd.DataFrame:
    return pd.DataFrame(dict_groups.values(), index=dict_groups.keys())
