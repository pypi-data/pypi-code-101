from src.Puffin.Dataset import DataFrameDataset
from src.Puffin.DatasetConfig import DatasetConfig
from src.Puffin.enums import DatasetType
from typing import List
from src.Puffin.enums import DatasetType


class DatasetLibrary:
    def add_dataset_config(self, config:DatasetConfig):
        if not hasattr(self, config.name):
            setattr(self, config.name, config)
        else:
            print(f'library already contains dataset with name {config.name}, skipping')

    def add_dataset_configs(self, configs:List[DatasetConfig]):
        for config in configs:
            self.add_dataset_config(config)

    def load(self, config_name):
        config = self.select_config(config_name)
        if config.type == DatasetType.file:
            df_ds = DataFrameDataset()
            df = df_ds.load_from_file(config)
            return df

    def save(self):
        pass

    def select_config(self, config_name):
        try:
            config = getattr(self, config_name)
        except AttributeError:
            print(f'config name {config_name} not found')
            config = None
        return config
