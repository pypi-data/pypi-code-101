from numpy import float64, int64
import pandas as pd
import re

# from pandas.core.arrays.integer import Int64Dtype


class ConductivityParser:
    def __init__(self, header=["source", "target", "conductivity"]):
        self.header = header

    def run(self, filename):
        df = pd.read_table(
            filename,
            delim_whitespace=True,
            header=None,
            names=self.header,
            dtype={"source": str, "target": str, "conductivity": float64},
        )
        return df


def get_number(col):
    return int(re.sub("^0+", "", col.split("_")[0]))


def get_residue(col):
    return col.split("_")[1]


class ConductivityFormatter:
    def __init__(self):
        pass

    def run(self, df):
        df = df.copy()
        for header in ["source", "target"]:
            df[f"{header}_number"] = df[header].map(get_number)
            df[f"{header}_residue"] = df[header].map(get_residue)
        return df


class BiovoronoiVolumeParser:
    def __init__(self) -> None:
        pass

    def run(self, filename):
        df = pd.read_csv(
            filename,
            dtype={
                "residue_number": int64,
                "residue_name": str,
                "atom_serial_number": int64,
                "volume": float64,
            },
        )
        return df


class BiovoronoiVolumeFormatter:
    def __init__(self):
        pass

    def run(self, df):
        df = df.drop(["atom_serial_number"], axis=1)
        return df


class VldpVolumeParser:
    def __init__(self) -> None:
        pass

    def run(self, filename):
        """parse vldp volume

        Args:
            filename (str): input file
        """
        df = pd.read_table(
            filename,
            delim_whitespace=True,
            comment="#",
            names=[
                "MOL",
                "NUMMOL",
                "ATM",
                "NUMATM",
                "X",
                "Y",
                "Z",
                "AREA",
                "VOLUME",
                "LOCUS",
            ],
            dtype={
                "MOL": str,
                "NUMMOL": int64,
                "ATM": str,
                "NUMATM": int64,
                "X": float64,
                "Y": float64,
                "Z": float64,
                "AREA": float64,
                "VOLUME": float64,
                "LOCUS": int64,
            },
        )
        return df


class VldpVolumeFormatter:
    def __init__(self) -> None:
        pass

    def run(self, df):
        df = df[["MOL", "NUMMOL", "VOLUME"]]
        df = df.rename(
            columns={
                "MOL": "residue_name",
                "NUMMOL": "residue_number",
                "VOLUME": "volume",
            }
        )
        return df
