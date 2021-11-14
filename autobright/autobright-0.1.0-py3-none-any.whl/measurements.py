import datetime
import pathlib

import pandas as pd
from appdirs import AppDirs


class Measurements:
    def __init__(self):
        self.path = (
            pathlib.Path(AppDirs("autobright", "Martin Ueding").user_data_dir)
            / "measurements.js"
        )
        if not self.path.parent.exists():
            self.path.parent.mkdir()
        if self.path.exists():
            self.df = pd.read_json(self.path)
        else:
            self.df = pd.DataFrame(columns=["datetime", "reading", "brightness"])

    def add_measurement(self, reading: int, brightness: int) -> None:
        self.df = pd.concat(
            [
                self.df,
                pd.DataFrame(
                    [
                        dict(
                            datetime=datetime.datetime.now(),
                            reading=reading,
                            brightness=brightness,
                        )
                    ]
                ),
            ],
            ignore_index=True,
        )
        self.df.to_json(self.path)

    def get_measurements(self) -> pd.DataFrame:
        return self.df
