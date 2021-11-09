import sys

import pydatfile.errors
import pydatfile.coders

class File:
    def __init__(self, file, ignore_errors=False, ensure_with=pydatfile.errors.NotSet):
        self.path = file
        self.made_for_humans = False
        f = False
        try:
            if not ignore_errors:
                self.read()
        except pydatfile.errors.DecodeError.IncorrectDataType as e:
            f = e
        except pydatfile.errors.DecodeError.CorruptedFile as e:
            f = e
        except pydatfile.errors.DecodeError.UnknownDataType as e:
            f = e
        except pydatfile.errors.DecodeError.EmptyFile as e:
            f = e
        except FileNotFoundError as e:
            f = e
        except pydatfile.errors.DecodeError as e:
            f = e
        if f:
            if not isinstance(ensure_with, pydatfile.errors.NotSet):
                if isinstance(f, FileNotFoundError):
                    self.write(ensure_with)
                elif isinstance(f, pydatfile.errors.DecodeError.EmptyFile):
                    self.write(ensure_with)
                else:
                    try:
                        raise pydatfile.errors.ReadError(f"Error while opening File. (May the File has been damaged):\n>>> {f.STR}: {f}")
                    except AttributeError:
                        raise pydatfile.errors.ReadError(f"Error while opening File. (May the File has been damaged):", f)
            else:
                try:
                    raise pydatfile.errors.ReadError(f"Error while opening File. (May the File has been damaged):\n>>> {f.STR}: {f}")
                except AttributeError:
                    raise pydatfile.errors.ReadError(f"Error while opening File. (May the File has been damaged):", f)

    def write(self, data, force_human_readable=None):
        if force_human_readable is not None:
            self.made_for_humans = force_human_readable
        try:
            self._r.close()
        except AttributeError:
            pass
        self._w = open(self.path, "w")
        self._w.write(pydatfile.coders.encode(data, self.made_for_humans))
        self._w.close()
        self._r = open(self.path, "r")

    def read(self):
        try:
            self._w.close()
        except AttributeError:
            pass
        self._r = open(self.path, "r")
        data = pydatfile.coders.decode(self._r.read())
        self.made_for_humans = data[1]
        self._r.close()
        return data[0]

    def set(self, key, value):
        data = self.read()
        data.update({key: value})
        self.write(data)

    def get(self, key):
        data = self.read()
        try:
            return data[key]
        except KeyError:
            return pydatfile.errors.NotSet(f"Key '{key}' is not set.")

    def __getitem__(self, item):
        return self.get(item)

    def __setitem__(self, key, value):
        return self.set(key, value)
