"""Converts CSV file(s) to a JSON format"""
from typing import Any, Dict, List

from file_converter.utils import process_input_path


def csv2json(
    input_path: str,
    output_path: str = ".",
    separator: str = ",",
    prefix: str = "",
) -> List[List[Dict[str, Any]]]:
    """Converts file(s) from CSV format to JSON
    The converted files will be saved with the same file name, with a possible
    prefix if desired.
    In case of a directory, all files must have the CSV extension and the same
    separator.

    Parameters
    ----------
    input_path
        A string with the path of the file or directory.
        Examples:
        - "./sample_file.csv"
        - "/home/username/csv_dir/"
        - "."

    output_path
        Output path to save the converted files

    separator
        Character used to separate the data in the CSV file. Possibilities are
        {",", ":", ";", "\t"}

    prefix
        String to prepend the converted files

    Returns
    -------
    A list of dictionaries. The list size is the same as the number of files to
    be converted.
    Moreover, new files are created in the desired directory.
    """

    file_names = process_input_path(input_path, "csv")

    json_lists = [
        _convert_file(file_name, separator=separator)
        for file_name in file_names
    ]

    for file_name, json_list in zip(file_names, json_lists):
        json_file_name = f"{output_path}/{prefix}{file_name.stem}.json"
        _write_json(json_file_name, json_list)

    return json_lists


def _convert_file(
    file_name: str, separator: str = ","
) -> List[Dict[str, Any]]:
    """Converts file from CSV format to JSON"""

    def _process_line(line: str) -> Dict[str, Any]:
        line_values = line.strip().split(separator)
        return dict(zip(keys, line_values))

    with open(file_name, "r", encoding="utf-8") as f:
        header = next(f)
        keys = header.strip().split(separator)
        json_list = [_process_line(line) for line in f]

    return json_list


def _write_json(file_name: str, json_list: List[Dict[str, Any]]):
    """
    Emulate the `json.dump` function writing a JSON file from a list of dicts
    """
    json_list_len = len(json_list)

    lines = ""
    lines += "[\n"
    lines += "\n".join(
        _write_dictionary(d_json, add_final_comma=i == json_list_len)
        for i, d_json in enumerate(json_list, start=1)
    )
    lines += "]"

    with open(file_name, "w", encoding="utf-8") as f:
        f.writelines(lines)


def _write_dictionary(d_json: Dict[str, str], add_final_comma: bool = True):
    """Write a dictionary as a formatted JSON.
    The values are parsed depending on their format.
    """
    lines = "\t{\n"
    lines += ",\n".join(
        f'\t\t"{key}": {_parse_value(value)}' for key, value in d_json.items()
    )
    lines += "\n"
    lines += "\t}," if not add_final_comma else "\t}\n"
    return lines


def _parse_value(value: str) -> Any:
    """Parse an incoming value into a number, string or None
    Here are the possibilities:
        - An empty string: set to null;
        - All digits: convert into an integer;
        - Digits and a decimal point: convert into a float;
        - Otherwise, return the original string.
    """
    if not value:
        return "null"

    if value.isdigit():
        return str(int(value))

    # Finally, we are left with a floating point or a regular string
    try:
        return str(float(value))
    except ValueError:
        return f'"{value}"'
