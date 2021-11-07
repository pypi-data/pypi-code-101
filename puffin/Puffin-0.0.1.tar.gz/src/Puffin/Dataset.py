import pandas as pd

class DataFrameDataset:
    def load_from_file(self, config):
        str_path = config.get_str_path()
        df = pd.read_csv(str_path)
        return df