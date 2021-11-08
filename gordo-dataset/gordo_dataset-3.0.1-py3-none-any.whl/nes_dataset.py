from typing import List, Union, Dict

from .datasets import TimeSeriesDataset, GordoBaseDataProvider, TagList
from .sensor_tag import SensorTag, SensorTagNormalizationError

from .data_provider.nes_provider import NesDataProvider
from .assets_config import AssetsConfig


class NesTimeSeriesDataset(TimeSeriesDataset):
    @staticmethod
    def create_default_data_provider() -> GordoBaseDataProvider:
        return NesDataProvider()

    @staticmethod
    def tag_normalizer(
        assets_config: AssetsConfig,
        sensors: TagList,
        asset: str = None,
    ) -> List[Union[str, SensorTag]]:
        if asset is None:
            raise SensorTagNormalizationError("asset is empty")
        return TimeSeriesDataset.tag_normalizer(assets_config, sensors, asset=asset)
