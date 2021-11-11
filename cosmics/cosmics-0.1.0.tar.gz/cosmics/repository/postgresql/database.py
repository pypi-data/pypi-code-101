import logging
from typing import Any
from typing import Optional
from typing import Union

import psycopg2.extensions
import psycopg2.extras
from psycopg2 import sql

from . import _query_builder as query_builder
from cosmics.repository import database

logger = logging.getLogger(__name__)


class Client(database.AbstractClient):
    """Client to connect to a Postgresql database and read from/write to it."""

    def __init__(self, user: str, password: str, host: str, port: int, database: str):
        """Initialize SQL Client.

        Parameters
        ----------
        user : str
            Database user name.
        password : str
            Password for given user.
        host : str
            IP address or hostname of database host.
        port : int
            Port at which the database accepts connections.
        database : str
            Name of the database.

        """
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database
        self._connection = None

    def __enter__(self):
        """Return instance when entering context manager."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Close database connection on exit."""
        self.__del__()

    def __del__(self):
        """Close database connection on deletion."""
        if self._connection is not None:
            self._connection.commit()
            self._connection.close()
            self._connection = None

    @property
    def credentials(self) -> dict[str, Union[str, int]]:
        """Return username, password, host, port, and dbname as dict.

        Returns
        -------
        dict[str, str | int]

        """
        return {
            "user": self.user,
            "password": self.password,
            "host": self.host,
            "port": self.port,
            "database": self.database,
        }

    @property
    def connection(self) -> psycopg2.extensions.connection:
        """Create SQL database connection.

        Returns
        -------
        psycopg2.extensions.connection

        """
        if self._connection is None:
            self._connection = psycopg2.connect(**self.credentials)
            logger.debug(
                "Connected to database %s as user %s", self.database, self.user
            )
        return self._connection

    def _insert(self, target: str, data: database.Info) -> None:
        """Insert row into table.

        Parameters
        ----------
        target : str
            Table name.
        data : dict[str, Any]
            Data to insert.

        """
        with self.connection.cursor() as cursor:
            query = query_builder.create_insert_query(table=target, data=data)
            self._execute_query(cursor, query=query)

    def insert_and_return_row_id(self, target: str, data: database.Info) -> int:
        """Insert row into table and return the inserted row's ID.

        Parameters
        ----------
        target : str
            Table name.
        data : dict[str, Any]
            Data to insert.

        Returns
        -------
        int
            ID of inserted row.

        """
        with self.connection.cursor() as cursor:
            query = query_builder.create_insert_query(table=target, data=data)
            self._execute_query(cursor, query=query)
            return cursor.lastrowid

    def _select(
        self,
        target: str,
        where: Optional[database.Info] = None,
    ) -> list[dict[str, Any]]:
        """Select columns from table.

        Parameters
        ----------
        target : str
            View or table name.
        where : dict[str, Any]
            Criteria which row(s) to update.

        Returns
        -------
        list[dict[str, Any]]
            All matching rows.

        """
        with self.connection.cursor(
            cursor_factory=psycopg2.extras.RealDictCursor
        ) as cursor:
            query = query_builder.create_select_query(table=target)
            if where is not None:
                query += query_builder.create_where_clause(where)
            query += sql.SQL(";")
            self._execute_query(cursor, query=query)
            return [dict(row) for row in cursor.fetchall()]

    def _update(
        self,
        target: str,
        data: database.Info,
        where: database.Info,
    ) -> None:
        """Update entry.

        Parameters
        ----------
        target : str
            Table name.
        data : dict[str, Any]
            Columns to update.
        where : dict
            Current details.
            Used to find matching row(s) in a table.

        """
        with self.connection.cursor() as cursor:
            query = query_builder.create_update_query(table=target, data=data)
            query += query_builder.create_where_clause(where)
            query += sql.SQL(";")
            self._execute_query(cursor, query=query)

    def _delete(self, target: str, where: database.Info, force: bool = False) -> None:
        """Delete entry.

        Parameters
        ----------
        target : str
            Table from which to delete the row.
        where : dict[str, Any]
            Criteria for matching rows to delete.
        force : bool, default False
            Whether to force the deletion.
            If `True`, all rows in other tables referencing this row will be deleted as well.

        """
        with self.connection.cursor() as cursor:
            query = query_builder.create_delete_query(table=target)
            query += query_builder.create_where_clause(where)
            query += sql.SQL(";")
            self._execute_query(cursor, query=query)

    def _execute_query(
        self, cursor: psycopg2.extras._cursor, query: sql.Composed
    ) -> None:
        logger.debug("Executing query %s", query.as_string(self.connection))
        cursor.execute(query)
