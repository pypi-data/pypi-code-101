"""
This module contains the Database class.

It is used to create new databases, and add or drop tables.
"""

import json
import os
from .table import Table
from .utils import log_transaction
from .constants import initialize_constants, \
    get_db_path, \
    get_db_dir


class Database():
    """Class to create db, and create or drop tables."""

    db = {}

    def __init__(self, db_directory):
        """
        Initialize a new db.

        :param db_directory: directory to store db data and logs.
        """
        initialize_constants(db_directory)
        if not os.path.exists(get_db_dir()):
            os.makedirs(get_db_dir())
        if not os.path.exists('{}/db'.format(get_db_dir())):
            os.makedirs('{}/db'.format(get_db_dir()))
        if not os.path.exists('{}/log'.format(get_db_dir())):
            os.makedirs('{}/log'.format(get_db_dir()))
        self.data_filepath = '{}/{}'.format(
            get_db_dir(), get_db_path())
        self.log_filepath = '{}/{}'.format(
            get_db_dir(), get_db_path())
        self._load_db()

    def _load_db(self):
        if os.path.exists(self.data_filepath):
            data = json.load(open(self.data_filepath))
            for key in data.keys():
                self.db[key] = Table(key, data[key])

    def _save_to_disk(self):
        with open(self.data_filepath, 'w') as outfile:
            res = {k: v.records for (k, v) in self.db.items()}
            json.dump(res, outfile)
        if os.path.exists(self.log_filepath):
            os.remove(self.log_filepath)

    @log_transaction
    def add_table(self, table_name):
        """
        Add a new table. If table name exists, returns existing table.

        :param table_name: name of table
        :return: new :class:`Table`, or existing :class:`Table` matching table_name
        """
        if table_name in self.db:
            print('{} already exists'.format(table_name))
            return self.db[table_name]
        else:
            table = Table(table_name, {})
            self.db[table_name] = table
            return table

    @log_transaction
    def drop_table(self, table_name):
        """
        Drop a table from db.

        :param table_name: name of table to drop
        :return: True if drop successful, False otherwise.

        """
        if table_name in self.db:
            del self.db[table_name]
            return True
        else:
            print('{} does not exist'.format(table_name))
            return False

    def show_tables(self):
        """
        Return list of tables.

        :return: List of tables in db.

        """
        return list(self.db.keys())


if __name__ == '__main__':
    print("hello, world.")
