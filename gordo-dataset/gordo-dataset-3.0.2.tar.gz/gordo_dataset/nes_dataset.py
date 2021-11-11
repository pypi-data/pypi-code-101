import re

from typing import List, Union, Optional, cast

from .datasets import TimeSeriesDataset, GordoBaseDataProvider, TagList
from .sensor_tag import (
    SensorTag,
    normalize_sensor_tag,
    unique_tag_names,
    SensorTagNormalizationError,
)

from .data_provider.nes_provider import NesDataProvider
from .assets_config import AssetsConfig

nes_asset_re = re.compile(r"^([^-]+)-")


def extract_nes_asset(sensor: str) -> Optional[str]:
    m = nes_asset_re.match(sensor)
    if m:
        return m[1]
    return None


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
        tag_list = cast(List[Union[str, SensorTag]], [])
        for sensor in sensors:
            sensor_tag = normalize_sensor_tag(assets_config, sensor, asset)
            if isinstance(sensor_tag, str):
                nes_asset = extract_nes_asset(cast(str, sensor))
                if nes_asset is None:
                    raise SensorTagNormalizationError(
                        f"Unable to extract NES asset from the tag name '{sensor}'. "
                        "Asset name should be specified as a prefix. "
                        "Example: ASSET-TAG1"
                    )
                sensor_tag = SensorTag(sensor, nes_asset)
            tag_list.append(sensor_tag)
        unique_tag_names(tag_list)
        return tag_list
