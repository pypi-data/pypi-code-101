from pathlib import Path
from typing import Dict, List, Optional, Tuple


def ids_file_abs() -> str:
    ids_file_name = 'type_id_names.csv'
    ids_file_src = Path(__file__).parent / ids_file_name
    if not ids_file_src.exists():
        raise RuntimeError("cannot find ids file: ", ids_file_src)
    return ids_file_src


class ClassIdManagerError(BaseException):
    pass


class ClassIdManager(object):
    """
    loads and manages type_name_ids mapping dictionary from csv file
    Discussions:
        csv file has the following format:
            type id, main type name, alias type name 1, alias type name 2, ...
        for example:
            27, airplane, aeroplane \n
            30, tv, tvmonitor \n
            31, dog \n
        for type id 27, we call airplane as the main type name, while aeroplane as alias. \n
        in our returned dict, this line will have 2 records:
            record 1: key: airplane, value: (27, None)
            record 2: key: aeroplane, value: (27, airplane)
        for each alias or main type name, you can get type idx and main type name from the value pair
    """
    __slots__ = ("_csv_path", "_type_name_id_dict", "_type_id_name_dict", "_max_id", "_dirty_id_names_dict")

    # life cycle
    def __init__(self) -> None:
        super().__init__()
        self._csv_path = None
        self._type_name_id_dict = {}  # type: Dict[str, Tuple[int, Optional[str]]]
        self._type_id_name_dict = {}  # type: Dict[int, str]
        self._dirty_id_names_dict = {}  # type: Dict[int, str]
        self._max_id = 0
        self.__load(ids_file_abs())

    # private: load and unload
    def __load(self, csv_path: str) -> bool:
        if not csv_path:
            raise ClassIdManagerError("empty path received")
        if self._csv_path:
            raise ClassIdManagerError("already loaded from: {}".format(self._csv_path))

        with open(csv_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                components = line.split(",")
                if len(components) <= 1:
                    continue  # empty lines also ignored here

                type_id = int(components[0])
                if type_id > self._max_id:
                    self._max_id = type_id

                main_type_name = None

                for type_name_idx, type_name in enumerate(components[1:]):
                    type_name = type_name.strip().lower()

                    # handle error situations
                    if type_name in self._type_name_id_dict:
                        previous_pair = self._type_name_id_dict[type_name]
                        raise ClassIdManagerError("dumplicate type name: {}, previous: {}, now: {}".format(
                            type_name, previous_pair[0], type_id))
                    if not type_name:
                        raise ClassIdManagerError("empty type name for type id: {}".format(type_id))

                    if type_name_idx == 0:
                        main_type_name = type_name
                        self._type_name_id_dict[type_name] = (type_id, None)
                        self._type_id_name_dict[type_id] = type_name
                    else:
                        self._type_name_id_dict[type_name] = (type_id, main_type_name)

        self._csv_path = csv_path
        return True

    # public: general
    def save_dirty_dict(self) -> bool:
        if not self._csv_path:
            raise ClassIdManagerError("not loadef")
        if len(self._dirty_id_names_dict) == 0:
            return True  # no need to save

        with open(self._csv_path + ".new", "a") as f:
            for type_id, type_name in self._dirty_id_names_dict.items():
                f.write(f"{type_id}, {type_name}\n")
        return True

    def id_and_main_name_for_name(self, name: str, add_if_no_exists: bool = True) -> Tuple[int, Optional[str]]:
        name = name.strip()
        if not self._csv_path:
            raise ClassIdManagerError("not loadef")
        if not name:
            raise ClassIdManagerError("empty name")

        if name not in self._type_name_id_dict:
            if add_if_no_exists:
                self._max_id += 1
                self._type_name_id_dict[name] = (self._max_id, None)
                self._type_id_name_dict[self._max_id] = name
                self._dirty_id_names_dict[self._max_id] = name
            else:
                raise ClassIdManagerError("not exists: {}".format(name))

        return self._type_name_id_dict[name]

    def main_name_for_id(self, type_id: int) -> Optional[str]:
        return self._type_id_name_dict.get(type_id, None)

    def id_for_names(self, names: List[str]) -> List[int]:
        type_ids = []
        for name in names:
            type_ids.append(self.id_and_main_name_for_name(name=name, add_if_no_exists=False)[0])
        return type_ids

    def all_main_names(self) -> List[str]:
        return list(self._type_id_name_dict.values())

    def size(self) -> int:
        return len(self._type_id_name_dict)
