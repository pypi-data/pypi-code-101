from __future__ import annotations

from dataclasses import asdict
from typing import TYPE_CHECKING, Any, Dict, Iterable, Mapping, Optional

from .._path_utils import PathLike, to_absolute_path
from ..client_side_encryption import ClientSideEncryption
from . import DataSource

if TYPE_CHECKING:
    from .._java_api import JavaApi
    from ..table import Table


def create_parquet_params(
    *,
    path: PathLike,
    pattern: Optional[str],
    parquet_column_name_to_table_column_name: Optional[Mapping[str, str]],
    client_side_encryption: Optional[ClientSideEncryption],
    is_temporary_file: bool,
) -> Dict[str, Any]:
    """Create the Parquet specific parameters."""
    return {
        "absolutePath": to_absolute_path(path),
        "globPattern": pattern,
        "parquetColumnNamesToStoreFieldNamesMapping": parquet_column_name_to_table_column_name,
        "clientSideEncryption": asdict(client_side_encryption)
        if client_side_encryption is not None
        else None,
        "isTemporaryFile": is_temporary_file,
    }


class ParquetDataSource(DataSource):
    """Parquet data source."""

    def __init__(self, java_api: JavaApi):
        """Init."""
        super().__init__(java_api, "PARQUET")

    def infer_parquet_types(
        self,
        *,
        path: PathLike,
        keys: Iterable[str],
        pattern: Optional[str],
        _parquet_column_name_to_table_column_name: Mapping[str, str],
        client_side_encryption: Optional[ClientSideEncryption],
    ):
        """Infer Table types from a Parquet file."""
        return self._java_api.infer_table_types_from_source(
            source_key=self.source_key,
            keys=keys,
            source_params=create_parquet_params(
                path=path,
                pattern=pattern,
                parquet_column_name_to_table_column_name=_parquet_column_name_to_table_column_name,
                client_side_encryption=client_side_encryption,
                is_temporary_file=False,
            ),
        )

    def load_parquet_into_table(
        self,
        *,
        path: PathLike,
        table: Table,
        scenario_name: str,
        pattern: Optional[str] = None,
        client_side_encryption: Optional[ClientSideEncryption] = None,
        _parquet_column_name_to_table_column_name: Mapping[str, str],
        _is_temporary_file: bool,
    ):
        """Load a Parquet into an existing table."""
        self.load_data_into_table(
            table.name,
            scenario_name=scenario_name,
            source_params=create_parquet_params(
                path=path,
                pattern=pattern,
                parquet_column_name_to_table_column_name=_parquet_column_name_to_table_column_name,
                client_side_encryption=client_side_encryption,
                is_temporary_file=_is_temporary_file,
            ),
        )
