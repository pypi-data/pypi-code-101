from typing import Tuple, Union

from .data_grid_type import DataGridType, data_grid_types_arg_parser, get_data_grid_type
from ...configure import get_config


def get_output_and_data_grid_type() -> Tuple[Union[None, str], "DataGridType"]:
    from .. import ContentType
    from ...delivery.data._data_provider_factory import get_api_config

    config = get_api_config(ContentType.DATA_GRID, get_config())
    data_grid_platform = config.setdefault(
        "underlying-platform", DataGridType.RDP.value
    )
    name_platform = data_grid_types_arg_parser.get_str(data_grid_platform)
    data_grid_type = get_data_grid_type.get(name_platform)
    output = config.setdefault("output", None)

    return output, data_grid_type
