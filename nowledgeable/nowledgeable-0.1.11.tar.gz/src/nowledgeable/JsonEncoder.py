import json


class CustomEncoder(json.JSONEncoder):

    @classmethod
    def format(cls, obj, quote=True):

        if isinstance(obj, bool):
            return obj

        if isinstance(obj, dict):
            r = {}
            for k, v in obj.items():

                r[k] = cls.format(v)

            return r

        if isinstance(obj, list):
            return [cls.format(v, False) for v in obj]

        if isinstance(obj, tuple):

            return "(" + ", ".join(tuple(str(cls.format(v)) for v in obj)) + ")"

        if isinstance(obj, (map,)):
            return cls.format(list(map), False)

        import numpy as np
        np.set_printoptions(threshold=200)

        numpy_types = (np.int_, np.intc, np.intp, np.int8,np.int16, np.int32, np.int64, np.uint8,np.uint16, np.uint32, np.uint64,np.bool, np.bool_, np.float_, np.float16, np.float32,np.float64)
        if isinstance(obj, numpy_types):
            return str(obj)

        if hasattr(obj, 'to_frame'):#pandas series
            return obj.to_frame().to_html(max_rows=10)

        if hasattr(obj, 'to_html'):  #pandas dataframe
            return obj.to_html(max_rows=10)

        from scipy.sparse import csr_matrix, csc_matrix
        if isinstance(obj, (np.ndarray, csr_matrix, csc_matrix)):
            return str(obj)

        if hasattr(obj, 'get_config'): #for keras, no need to import
            return str(obj.get_config())

        if callable(obj) or hasattr(obj, "__call__"):
            import inspect
            return inspect.getsource(obj)

        if isinstance(obj, str):
            if quote:
                return "'" + obj + "'"

        if cls.is_serializable(obj):
            return obj

        return str(obj)

    @classmethod
    def is_serializable(cls, obj):


        import json
        try:
            json.dumps(obj)
            return True
        except (TypeError, OverflowError):
            return False


    @classmethod
    def to_json(cls, data):
        return json.dumps(cls.format(data))
