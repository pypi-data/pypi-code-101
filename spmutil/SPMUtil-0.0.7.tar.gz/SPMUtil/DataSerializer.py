import pickle, os
import numpy as np
import base64
import json


class DataSerializer:

    def __init__(self, path, custom_ext=".pkl"):
        self.path = path
        self._ext = custom_ext
        self.header = None
        self.data_dict = {}

    @property
    def header_key(self):
        return "data_main_header"

    def set_header(self, header):
        self.data_dict[self.header_key] = header

    def save(self):
        if self.header_key not in self.data_dict:
            raise ValueError("Save file need a header, use set_header(type(dict)) function")
        filename, file_extension = os.path.splitext(self.path)
        with open(filename + self._ext, "wb") as f:
            pickle.dump(self.data_dict, f, pickle.HIGHEST_PROTOCOL)
            print("save to", filename + self._ext)

    def load(self):
        filename, file_extension = os.path.splitext(self.path)
        if file_extension != self._ext:
            filename = self.path
        with open(filename + self._ext, "rb") as f:
            self.data_dict = pickle.load(f)
            self.header = self.data_dict[self.header_key]

    def add_data(self, key, data, overwrite=False, save=False):
        if key in self.data_dict:
            if overwrite:
                self.data_dict.pop(key)
                self.data_dict[key] = data
        else:
            self.data_dict[key] = data

        if save:
            self.save()

    def remove_data(self, key, save=False):
        if key in self.data_dict:
            self.data_dict.pop(key)
        if save:
            self.save()

    @staticmethod
    def to_matrix_buffer(ndarray):
        return ndarray.tobytes()

    @staticmethod
    def from_matrix_buffer(buffer):
        return np.frombuffer(buffer)




# class NdarrayEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, np.integer):
#             return int(obj)
#         elif isinstance(obj, np.floating):
#             return float(obj)
#         elif isinstance(obj, np.ndarray):
#             return obj.tolist()
#         else:
#             return super(NdarrayEncoder, self).default(obj)

class NdarrayEncoder(json.JSONEncoder):
    """
    - Serializes python/Numpy objects via customizing json encoder.
    - **Usage**
        - `json.dumps(python_dict, cls=EncodeFromNumpy)` to get json string.
        - `json.dump(*args, cls=EncodeFromNumpy)` to create a file.json.
    """

    def default(self, obj):
        import numpy
        if isinstance(obj, numpy.ndarray):
            return {
                "_kind_": "ndarray",
                "_value_": obj.tolist()
            }
        if isinstance(obj, numpy.integer):
            return int(obj)
        elif isinstance(obj, numpy.floating):
            return float(obj)
        elif isinstance(obj, range):
            value = list(obj)
            return {
                "_kind_": "range",
                "_value_": [value[0], value[-1] + 1]
            }
        return super(NdarrayEncoder, self).default(obj)



class NdarrayDecoder(json.JSONDecoder):
    """
    - Deserilizes JSON object to Python/Numpy's objects.
    - **Usage**
        - `json.loads(json_string,cls=DecodeToNumpy)` from string, use `json.load()` for file.
    """
    def __init__(self, *args, **kwargs):
        json.JSONDecoder.__init__(self, object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, obj):
        import numpy
        if '_kind_' not in obj:
            return obj
        kind = obj['_kind_']
        if kind == 'ndarray':
            return numpy.array(obj['_value_'])
        elif kind == 'range':
            value = obj['_value_']
            return range(value[0],value[-1])
        return obj

