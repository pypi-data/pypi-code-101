from typing import Union

import dask.dataframe as dd
import pandas as pd
from dagster import InputDefinition, OutputDefinition
from qdk.base import BaseComponent
from qdk.dagster_types import DataFrameType, ModelType, SeriesType

from sklearn.base import BaseEstimator


class TrainingComponent(BaseComponent):
    compute_function = "train"
    tags = {"kind": "training"}
    input_defs = [
        InputDefinition("X", DataFrameType),
        InputDefinition("y", SeriesType),
        InputDefinition("model", ModelType),
    ]
    output_defs = [OutputDefinition(ModelType, "model")]

    @classmethod
    def train(
        cls,
        X: Union[pd.DataFrame, dd.DataFrame],
        y: Union[pd.Series, dd.Series],
        model: BaseEstimator,
    ) -> BaseEstimator:
        raise NotImplementedError(
            'Make sure you added a "train" function to the component'
        )
