"""[summary]
"""
import pprint
from typing import Any
from typing import List
from typing import Union

from energinetml.core.logger import MetricsLogger


class AzureMlLogger(MetricsLogger):
    """[summary]"""

    def __init__(self, run):
        """
        :param azureml.core.Run run:
        """
        self.run = run

    def echo(self, s: str) -> None:
        """Echo wrapper.

        Args:
            s (str): String we want to log.
        """
        print(s)

    def log(self, name, value):
        self.run.log(name, value)
        self.echo(f"LOG: {name} = {value}")

    def tag(self, key, value):
        self.run.tag(key, value)
        self.echo(f"TAG: {key} = {value}")

    def table(
        self, name: Union[str, Any], dict_of_lists: List[dict], echo=True
    ) -> None:
        """[summary]

        Args:
            name (Union[str, Any]): [description]
            dict_of_lists (List[dict]): [description]
            echo (bool, optional): [description]. Defaults to True.
        """
        list_of_dicts = [
            dict(zip(dict_of_lists, t)) for t in zip(*dict_of_lists.values())
        ]

        for _dict in list_of_dicts:
            self.run.log_table(name, _dict)

        if echo:
            # TODO print actual table
            self.echo(f"{name}:")
            self.echo(pprint.PrettyPrinter(indent=4).pformat(dict_of_lists))

    def dataframe(self, name, df):
        df = df.reset_index()
        self.table(name, df.to_dict(orient="list"), echo=False)
        self.echo(df.to_string())
