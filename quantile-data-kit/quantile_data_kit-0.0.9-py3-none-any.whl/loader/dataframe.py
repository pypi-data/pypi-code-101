from typing import Any, Dict, Union

import dask.dataframe as dd
import pandas as pd
from dagster import Field, OutputDefinition, Permissive
from qdk.base import BaseComponent
from qdk.dagster_types import DataFrameType


class DataFrameLoader(BaseComponent):
    compute_function = "load"
    tags = {
        "kind": "loader",
    }
    input_defs = []
    output_defs = [
        OutputDefinition(DataFrameType, "df"),
    ]
    config_schema = {
        "uri": Field(
            str,
            description="The uri to load the dataframe from.",
        ),
        "use_dask": Field(
            bool,
            default_value=False,
            description="Whether to load the dataframe using Dask.",
        ),
        "repartitions": Field(
            int,
            is_required=False,
            description="How many partitions to create.",
        ),
        "drop_na": Field(
            bool,
            default_value=False,
            description="Whether to drop rows with missing values.",
        ),
        "load_params": Field(
            Permissive({}),
            description="Extra parameters that get passed to the loading function.",
        ),
    }

    @classmethod
    def load(
        cls,
        uri: str,
        use_dask: bool = False,
        repartitions: int = None,
        drop_na: bool = False,
        load_params: Dict[str, Any] = {},
    ) -> Union[pd.DataFrame, dd.DataFrame]:
        # Choose which framework to use for loading the data
        framework = dd if use_dask else pd

        if uri.endswith(".csv"):
            df = framework.read_csv(uri, **load_params)

        elif (
            uri.endswith(".json")
            or uri.endswith(".jsonl")
            or uri.endswith(".jsonlines")
        ):
            df = framework.read_json(uri, orient="records", lines=True, **load_params)

        elif uri.endswith(".pkl"):
            df = pd.read_pickle(uri, **load_params)

            if use_dask:
                df = dd.from_pandas(df, npartitions=repartitions)

        # If using dask and repartitions are supplied
        if use_dask and repartitions is not None:
            df = df.repartition(npartitions=repartitions)

        # Drop rows with missing values
        if drop_na:
            df = df.dropna()
            df = df.reset_index(drop=True)

        return df
