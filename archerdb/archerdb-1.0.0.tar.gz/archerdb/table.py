"""Table class supporting read and write operations."""

import uuid
from .utils import log_transaction


class Table():
    """Stores a group of similar records and supports read and write operations."""

    def __init__(self, name, records):
        """
        Initialize a new table.

        :param name: table name
        :param records: initial set of records
        """
        self.name = name
        self.records = records
        self.index = {}

    def get(self, id):
        """
        Get a record from table by id.

        :param id: record id
        :return: record
        """
        try:
            return self.records[id]
        except KeyError:
            print("Key not found: {} in table {}".format(id, self.name))
            return None

    # @log_transaction
    def add(self, data):
        """
        Add new record to table.

        :param data: record data
        :return: record id
        """
        try:
            newId = str(uuid.uuid4())
            self.records[newId] = data
            return newId
        except Exception as e:
            print("Error adding record to db: " + str(e))
            return None

    @log_transaction
    def delete(self, id):
        """
        Delete a record from table by id.

        :param id: record id
        :return: deleted record id
        """
        try:
            del self.records[id]
            return id
        except KeyError:
            print("Key not found: {}".format(id))

    def search(self, params, return_doc=False):
        """
        Search for records in table matching params.

        :param params: map of keys and values to search table for
        :param return_doc: True return matching records, otherwise return matching ids.
        :return: list of matching ids or records
        """
        matches = []
        search_records = {}

        index_params = {k: params[k] for k in params.keys() if k in self.index}
        if len(index_params) != 0:
            search_records = self._search_by_indexes(index_params)
        else:
            search_records = self.records
        for id in search_records.keys():
            match = True
            for key in [k for k in params.keys() if k not in self.index]:
                if key not in search_records[id]:
                    match = False
                    break
                if search_records[id][key] != params[key]:
                    match = False
                    break
            if match:
                matches.append(search_records[id]) if return_doc \
                    else matches.append(id)
        return matches

    def _search_by_indexes(self, params):
        sets = [self.index[i].get(params[i]) for i in params.keys()]
        intersection = set.intersection(*sets)
        return {id: self.get(id) for id in intersection}

    def add_index(self, index_name):
        if index_name in self.index:
            print('index on {} already exists'.format(index_name))
            return True

        index_data = {}
        index = Index(index_name, index_data)
        for id in self.records:
            if index_name in self.records[id]:
                index.add(id, self.records[id][index_name])
        self.index[index_name] = index
        return True

    def remove_index(self, index_name):
        if index_name not in self.index:
            print('index on {} does not exist'.format(index_name))
            return False

        del self.index[index_name]
        return True


class Index():

    def __init__(self, name, data):
        self.name = name
        self.data = data

    def add(self, key, value):
        if value in self.data:
            self.data[value].append(key)
        else:
            self.data[value] = [key]

    def get(self, value):
        if value in self.data:
            return set(self.data[value])
        return set()
