from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import TYPE_CHECKING, Any, Dict, Iterable, Mapping, Optional

from .._path_utils import PathLike, to_absolute_path
from ..client_side_encryption import ClientSideEncryption
from . import DataSource

if TYPE_CHECKING:
    from .._java_api import JavaApi
    from ..table import Table
    from ..type import DataType


def create_csv_params(
    *,
    path: PathLike,
    separator: Optional[str],
    encoding: str,
    process_quotes: Optional[bool],
    array_separator: Optional[str],
    pattern: Optional[str],
    date_patterns: Mapping[str, str],
    client_side_encryption: Optional[ClientSideEncryption],
) -> Dict[str, Any]:
    """Create the CSV specific parameters."""
    return {
        "absolutePath": to_absolute_path(path),
        "separator": separator,
        "encoding": encoding,
        "processQuotes": process_quotes,
        "arraySeparator": array_separator,
        "globPattern": pattern,
        "datePatterns": date_patterns,
        "clientSideEncryption": asdict(client_side_encryption)
        if client_side_encryption is not None
        else None,
    }


@dataclass(frozen=True)
class CsvFileFormat:
    process_quotes: bool
    separator: str
    types: Mapping[str, DataType]
    date_patterns: Mapping[str, str]


class CsvDataSource(DataSource):
    """CSV data source."""

    def __init__(self, java_api: JavaApi):
        """Init."""
        super().__init__(java_api, "CSV")

    def discover_file_format(
        self,
        path: PathLike,
        *,
        keys: Iterable[str],
        separator: Optional[str],
        encoding: str,
        process_quotes: Optional[bool],
        array_separator: Optional[str],
        pattern: Optional[str],
        date_patterns: Mapping[str, str],
        client_side_encryption: Optional[ClientSideEncryption],
    ) -> CsvFileFormat:
        """Infer Table types from a CSV file or directory."""
        source_params = create_csv_params(
            path=path,
            separator=separator,
            encoding=encoding,
            process_quotes=process_quotes,
            array_separator=array_separator,
            pattern=pattern,
            date_patterns=date_patterns,
            client_side_encryption=client_side_encryption,
        )
        return self._java_api.discover_csv_file_format(
            keys=keys,
            source_params=source_params,
        )

    def load_csv_into_table(
        self,
        path: PathLike,
        table: Table,
        *,
        scenario_name: str,
        separator: Optional[str],
        encoding: str,
        process_quotes: bool,
        array_separator: Optional[str],
        pattern: Optional[str],
        date_patterns: Mapping[str, str],
        client_side_encryption: Optional[ClientSideEncryption],
    ):
        """Load a csv into an existing table."""
        source_params = create_csv_params(
            path=path,
            separator=separator,
            encoding=encoding,
            process_quotes=process_quotes,
            array_separator=array_separator,
            pattern=pattern,
            date_patterns=date_patterns,
            client_side_encryption=client_side_encryption,
        )
        self.load_data_into_table(
            table.name,
            scenario_name=scenario_name,
            source_params=source_params,
        )
