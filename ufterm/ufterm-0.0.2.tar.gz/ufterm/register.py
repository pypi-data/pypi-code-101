import threading
import json
import sys
import yaml
import os
import itertools
import atexit

from yaml import representer
from typing import Dict, Union, List
from datetime import datetime

RegisterValueType = Union[int, str, None, List['RegisterValueType'], Dict[str, 'RegisterValueType']]


class _RegisterDict(dict):

    def __getattr__(self, key: str):
        """
        Overriding this allow developers to access values with the dot notation on the children nodes.
        Example:
            value = Register.sub_node.key
        """
        return self.__getitem__(key)

    def __setattr__(self, key, value):
        super(_RegisterDict, self).__setitem__(key, value)
        _RegisterMeta._sub_collection_commit(self)

    def __setitem__(self, key, value):
        super(_RegisterDict, self).__setitem__(key, value)
        _RegisterMeta._sub_collection_commit(self)

    def get(self, key: str, default: any) -> any:
        result = super(_RegisterDict, self).get(key, default)
        self.__setitem__(key, result)
        return result


class _RegisterList(list):

    def append(self, *args, **kwargs):
        super().append(*args, **kwargs)
        _RegisterMeta._sub_collection_commit(self)

    def clear(self, *args, **kwargs):
        super().clear(*args, **kwargs)
        _RegisterMeta._sub_collection_commit(self)

    def insert(self, *args, **kwargs):
        super().insert(*args, **kwargs)
        _RegisterMeta._sub_collection_commit(self)

    def pop(self, *args, **kwargs):
        res = super().pop(*args, **kwargs)
        _RegisterMeta._sub_collection_commit(self)
        return res

    def remove(self, *args, **kwargs):
        super().remove(*args, **kwargs)
        _RegisterMeta._sub_collection_commit(self)

    def reverse(self, *args, **kwargs):
        super().reverse(*args, **kwargs)
        _RegisterMeta._sub_collection_commit(self)

    def sort(self, *args, **kwargs):
        super().sort(*args, **kwargs)
        _RegisterMeta._sub_collection_commit(self)

    def __setitem__(self, key: int, value: RegisterValueType):
        super().__setitem__(key, _RegisterMeta._observe(value))
        _RegisterMeta._sub_collection_commit(self)


class _RegisterMeta(type):

    ###########################################################################
    # Attribute section
    ###########################################################################
    # As the register object is a singleton, we can save its attributes into it class.

    _instance = None
    _sub_collection = set()
    _file_path = None
    _auto_commit = True
    _file_threads = []
    _file_mutex = threading.Lock()

    ###########################################################################
    # Override section
    ###########################################################################
    # In this section we override python behaviour just to make the developer job more easy :-)

    def __getattr__(self, key: str) -> RegisterValueType:
        """
        Overriding this allow developers to access values with the dot notation on the class itself.
        Example:
            value = Register.key
        """
        return self().__getitem__(key)

    def __getitem__(self, key: str):
        """
        Overriding this allow developers to use square brackets on the class itself to access values.
        Example:
            value = Register[key]
        """
        return self().__getitem__(key)

    def __setattr__(self, key: str, value: RegisterValueType):
        """
        Overriding this allow developers to use the dot notation on the class itself to save values.
        Example:
            Register.key = value
        """
        self().__setitem__(key, value)

    def __setitem__(self, key: str, value: RegisterValueType):
        """
        Overriding this allow developers to use square brackets on the class itself to save values.
        Example:
            Register[key] = value
        """
        self().__setitem__(key, value)

    ###########################################################################
    # File section
    ###########################################################################
    # We use yaml file to record the value. This format allow us to have a nice visibility.
    # Like that Humans could open it and update values

    yaml.add_representer(_RegisterDict, yaml.representer.SafeRepresenter.represent_dict)
    yaml.add_representer(_RegisterList, yaml.representer.SafeRepresenter.represent_list)

    @staticmethod
    def _load_from_file(replace_value=True):
        if _RegisterMeta._file_path is not None and os.path.isfile(_RegisterMeta._file_path):
            _RegisterMeta._file_mutex.acquire()

            Register()  # make sure that we created the instance. This could create 'None Access' errors later
            with open(_RegisterMeta._file_path, 'r') as fd:
                loading_file = yaml.load(fd, Loader=yaml.FullLoader)
                if loading_file is not None:
                    for k, v in loading_file.items():
                        if replace_value:
                            _RegisterMeta._instance.__dict__[k] = _RegisterMeta._observe(v)
                        else:
                            _RegisterMeta._instance.__dict__[k] = _RegisterMeta._instance.get(k, _RegisterMeta._observe(v))
            _RegisterMeta._file_mutex.release()

    @staticmethod
    def _save_on_file():
        if _RegisterMeta._file_path is not None:
            _RegisterMeta._file_mutex.acquire()
            # Make sure the folder holding the file is present
            directory = os.path.dirname(_RegisterMeta._file_path)
            if not os.path.isdir(directory) and directory != "":
                os.makedirs(directory)

            now = datetime.now()
            comment = "# File wrote by the user-friendly-terminal library at %s on the %s\n" % \
                      (now.strftime("%H:%M:%S"), now.strftime("%Y-%m-%d"))
            # Here we only sort the first node. Indeed the recorded file could be open by a human.
            # It'll be easier to look for the right value to update.
            # But we don't update the sub node because the order could be important.
            with open(_RegisterMeta._file_path, 'w+') as fd:
                fd.write(comment)
                sorted_dict = dict(sorted(_RegisterMeta._instance.__dict__.items()))
                yaml.dump(sorted_dict, fd, sort_keys=False)
            _RegisterMeta._file_mutex.release()

    @staticmethod
    def _observe(value):
        """
        This function will create List and Dict observed by the Register

        :param value:  The value to be observed
        :return:  The same value as before but observed be the register
        """
        if value.__class__ == list:
            observed = _RegisterList()
            for element in value:
                observed.append(_RegisterMeta._observe(element))
        elif value.__class__ == dict:
            observed = _RegisterDict()
            for key in value:
                observed[key] = _RegisterMeta._observe(value[key])
        else:
            return value

        _RegisterMeta._sub_collection.add(id(observed))

        return observed

    @staticmethod
    def _sub_collection_commit(collection):
        if id(collection) in _RegisterMeta._sub_collection:
            Register.commit()


class Register(metaclass=_RegisterMeta):

    def __new__(cls, *args) -> Union['Register', RegisterValueType, List[RegisterValueType]]:
        if _RegisterMeta._instance is None:
            _RegisterMeta._instance = object.__new__(cls)
        if len(args) == 0:
            return _RegisterMeta._instance
        elif len(args) == 1:
            return _RegisterMeta._instance.__getattr__(args[0])
        else:
            result = []
            for arg in args:
                result.append(cls.__instance.__getattr__(arg))
            return result

    def __getattr__(self, key: str) -> RegisterValueType:
        """
        Overriding this allow the developer to access the value with a dot notation.
        Example:
            value = register.key
        """
        return self.__getitem__(key)

    def __getitem__(self, key: str) -> RegisterValueType:
        """
        Overriding this allow the developer to use square brackets to access to values.
        Example:
            value = register[key]
        """
        return self.__dict__[key]

    def __setattr__(self, key: str, value: RegisterValueType):
        """
        Overriding this allow the developer to use dot notation to save values.
        Example:
            register.key = value
        """
        self.__setitem__(key, value)

    def __setitem__(self, key: str, value: RegisterValueType):
        """
        Overriding this allow the developer to use square brackets to save values.
        Example:
            register[key] = value
        """
        try:
            _RegisterMeta._sub_collection.remove(id(self.__dict__[key]))
        except KeyError:
            pass
        self.__dict__[key] = _RegisterMeta._observe(value)

        Register.commit()

    def __str__(self):
        return json.dumps(self.__dict__, sort_keys=True, indent=2)

    @staticmethod
    def get(key: str, default: RegisterValueType = None):
        tmp = Register().__dict__.get(key, default)
        tmp = _RegisterMeta._observe(tmp)
        Register().__dict__[key] = tmp
        Register.commit()
        return tmp

    @staticmethod
    def reset():
        keys = tuple(vars(Register()).keys())
        for key in keys:
            del Register().__dict__[key]
        _RegisterMeta._load_from_file(False)

    @staticmethod
    def clear():
        _RegisterMeta._instance = None
        _RegisterMeta._sub_collection = set()
        _RegisterMeta._file_path = None
        _RegisterMeta._auto_commit = True
        _RegisterMeta._file_threads = []
        _RegisterMeta._file_mutex = threading.Lock()

        keys = tuple(vars(Register()).keys())
        for key in keys:
            del Register().__dict__[key]

    @staticmethod
    def delete_recorded_file():
        os.remove(_RegisterMeta._file_path)
        _RegisterMeta._file_path = None

    @staticmethod
    def is_all_commit_finished():
        _RegisterMeta.file_thread[:] = itertools.filterfalse(lambda s: not s.is_alive(), _RegisterMeta.file_thread)
        return len(_RegisterMeta._file_threads) == 0

    @staticmethod
    def wait_commit_to_finish():
        [t.join() for t in _RegisterMeta._file_threads]
        _RegisterMeta._file_threads = []

    @staticmethod
    def set_auto_commit(value: bool):
        _RegisterMeta._auto_commit = value

    @staticmethod
    def commit():
        if _RegisterMeta._auto_commit:
            thread = threading.Thread(target=_RegisterMeta._save_on_file)
            _RegisterMeta._file_threads.append(thread)
            thread.start()

    @staticmethod
    def record_in_file(file_path: str):
        file_path = file_path.replace('/', os.path.sep)
        file_path = file_path.replace('\\', os.path.sep)
        # If the path start with a tilde '~' and the platform is Windows we replace it by the user home path.
        if file_path.startswith(f"~{os.path.sep}"):
            file_path = os.path.expanduser(file_path)
        # If the file didn't finish with the right extension we add it
        if not file_path.endswith(".yml") and not file_path.endswith(".yaml"):
            file_path += ".yml"
        _RegisterMeta._file_path = file_path
        if os.path.isfile(_RegisterMeta._file_path):
            _RegisterMeta._load_from_file(False)
        atexit.register(Register.wait_commit_to_finish)
        Register.commit()
