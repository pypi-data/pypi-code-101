from enum import Enum

from ...tools import make_enum_arg_parser, ArgsParser, validate_bool_value


class DataGridType(Enum):
    UDF = "udf"
    RDP = "rdp"


get_data_grid_type = {
    DataGridType.UDF.value: DataGridType.UDF,
    DataGridType.RDP.value: DataGridType.RDP,
}

data_grid_types_arg_parser = make_enum_arg_parser(DataGridType)
use_field_names_in_headers_arg_parser = ArgsParser(validate_bool_value)
