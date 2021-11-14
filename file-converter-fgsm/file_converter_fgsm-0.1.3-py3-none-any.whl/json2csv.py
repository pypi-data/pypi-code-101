"""Converts CSV file(s) to a JSON format"""
from typing import Any, Dict, List

from file_converter.utils import process_input_path


def json2csv(
    input_path: str,
    output_path: str = ".",
    separator: str = ",",
    prefix: str = "",
) -> List[List[str]]:
    """Converts file(s) from CSV format to JSON
    In case of a directory, all files must have the CSV extension and the same
    separator.

    Parameters
    ----------
    input_path
        A string with the path of the file or directory.
        Examples:
        - "./sample_file.json"
        - "/home/username/json_dir/"
        - "."

    output_path
        Output path to save the converted files

    separator
        Character used to separate the data in the converted CSV file.
        Possibilities are {",", ":", ";", "\t"}

    prefix
        String to prepend the converted files

    Returns
    -------
    A list of lists, each one with the rows of the converted CSV file.
    Moreover, new files are created in the desired directory.
    """

    file_names = process_input_path(input_path, "json")
    csv_lists = [
        _convert_file(file_name, separator=separator)
        for file_name in file_names
    ]

    for file_name, csv_list in zip(file_names, csv_lists):
        csv_file_name = f"{output_path}/{prefix}{file_name.stem}.csv"
        with open(csv_file_name, "w", encoding="utf-8") as f:
            f.writelines(csv_list)

    return csv_lists


def _convert_file(file_name: str, separator: str = ",") -> List[str]:
    """Converts file from CSV format to JSON"""

    json_list = _read_json(file_name)
    csv_list = []

    # Header
    # We assume all json elements have the same keys, so we can use any of them
    keys = list(json_list[0].keys())  # convert to list to ensure ordering
    header_line = separator.join(key for key in keys)
    header_line += "\n"
    csv_list.append(header_line)

    # Data lines
    def write_data_line(json_dict: Dict[str, Any]) -> str:
        # We explicitly use `json_dict[key]` instead of iterating in the values
        # to ensure the same order
        data_line = separator.join(json_dict[key] for key in keys)
        data_line += "\n"
        return data_line

    data_lines = [write_data_line(json_dict) for json_dict in json_list]
    csv_list.extend(data_lines)

    return csv_list


def _read_json(file_name: str):
    """Emulate the `json.load` function

    Notes
    -----
    We assume a JSON with the format
    `
    [
        {
            "key1": value1,
            "key2": value2,
        },
        ...
    ]
    `

    The algorithm thus groups all lines ignoring the brackets and splits each
    dictionary with "},". For each individual dictionary, we can iterate over
    each line split by ":" and get the key and values. Notice, while the key is
    always a string, the value should be properly parsed as it can be a string,
    an integer, a float or null. In the latter case, it is parsed as an empty
    string in the final CSV.
    """
    with open(file_name, "r", encoding="utf-8") as f:
        all_lines = "".join(line.strip() for line in f.readlines())

    useful_lines = all_lines[1:-2]  # remove the closing brackets and last "}"

    def _read_dictionary(dict_str: str) -> Dict[str, str]:
        dict_data_raw = dict_str.replace("{", "").split(",")
        dict_data = {}
        for item in dict_data_raw:
            key, value = item.split(":")
            dict_data[_parse_value(key)] = _parse_value(value)

        return dict_data

    return [
        _read_dictionary(dict_str) for dict_str in useful_lines.split("},")
    ]


def _parse_value(value_raw: Any) -> str:
    """Parse a value to string

    Notes
    -----
    Here are the conditions:
    1. If the value is constrained by double quotes, it is a string;
    2. If it is a `null`, return an empty string;
    3. Otherwise it is a number. Return it as given.
    """

    value = value_raw.strip()
    # import ipdb; ipdb.set_trace()
    if value[0] == '"' and value[-1] == '"':
        return value[1:-1]

    if value == "null":
        return ""

    return value
