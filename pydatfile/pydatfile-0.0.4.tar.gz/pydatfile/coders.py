import pydatfile.errors


def encode(_any: [int, str, float, list, dict], hold_readable=True):
    if hold_readable:
        _str = "#" + _any_type(_any) + "<" + _any_str(_any, unsecure=True) + ">"
    else:
        _str = _any_type(_any) + "<" + _any_str(_any) + ">"
    return _str


def decode(_str: str):
    _new_str, _type, mode, r = "", "", 0, -1
    for l in _str:
        r += 1
        if mode == 0:
            if l == ">":
                f = "Container-end in type-definition."
                raise pydatfile.errors.DecodeError.CorruptedFile(f"Unexpected '{l}' at position {r} (first is 0): {f}\n{_str}\n{(r)*' '}^")
            elif l == "<":
                mode = 1
                continue
            _type += l
        elif mode == 1:
            if l == "<":
                f = "Container-start in main-container."
                raise pydatfile.errors.DecodeError.CorruptedFile(f"Unexpected '{l}' at position {r} (first is 0): {f}\n{_str}\n{(r)*' '}^")
            if l == ">":
                mode = 2
                continue
            _new_str += l
        else:
            f = "Data outside main-container."
            raise pydatfile.errors.DecodeError.CorruptedFile(f"Unexpected '{l}' at position {r} (first is 0): {f}\n{_str}\n{(r)*' '}^")
    hold_readable = False
    if _type.startswith("#"):
        hold_readable = True
        _type = _type.replace("#", "")
    if _type == "":
        raise pydatfile.errors.DecodeError.EmptyFile("The given File is empty!")
    return _str_any(_new_str, _type, hold_readable), hold_readable


def _encode_dict(_dict: dict):
    if not isinstance(_dict, dict):
        raise pydatfile.errors.ParameterTypeError(
            f"Parameter 'dictionary' must have type '{type({})}', not {type(_dict)}")
    content = ""
    for key in _dict:
        content += "{" + _any_type(key) + "[" + _any_str(key) + "]" + _any_type(_dict[key]) + "[" + _any_str(
            _dict[key]) + "]}"
    return content


def _encode_list(_list: list):
    if not isinstance(_list, list):
        raise pydatfile.errors.ParameterTypeError(f"Parameter '_list' must have type '{type([])}', not {type(_list)}")
    content = ""
    for key in _list:
        content += "{" + _any_type(key) + "[" + _any_str(key) + "]}"
    return content


def _encode_tuple(_tuple: tuple):
    if not isinstance(_tuple, tuple):
        raise pydatfile.errors.ParameterTypeError(f"Parameter '_tuple' must have type '{type([])}', not {type(_tuple)}")
    content = ""
    for key in _tuple:
        content += "{" + _any_type(key) + "[" + _any_str(key) + "]}"
    return content


def _decode_dict(_str: str):
    if not isinstance(_str, str):
        raise pydatfile.errors.ParameterTypeError(f"Parameter 'string' must have type '{type('')}', not {type(_str)}")
    data = {}
    key = ""
    keytype = ""
    value = ""
    valuetype = ""
    mode = "ot"
    inner = 0
    r = -1
    for l in _str:
        r += 1
        if l == "{":
            if mode == "in" or mode == "ky" or mode == "vl":
                f = "No further information."
                if mode == "in":
                    f = "Record-start in type-definition."
                elif mode == "ky":
                    f = "Record-start in key."
                elif mode == "vl":
                    f = "Record-start in value."
                s = "{"
                raise pydatfile.errors.DecodeError.CorruptedFile(f"Unexpected '{s}' at position {r} (first is 0): {f}\n{_str}\n{(r)*' '}^")
            mode = "in"
            inner = 0
            continue
        if l == "[":
            inner += 1
            if inner == 1:
                mode = "ky"
                continue
            elif inner == 2:
                mode = "vl"
                continue
            f = "Object cannot be identified as key or value."
            if mode == "ot":
                f = "Object-start out of record."
            if mode == "in" and inner == 3:
                f = "Object-start in key."
            if mode == "vl" and inner == 3:
                f = "Object-start in value or values' type-definition."
            if keytype == "" and valuetype == "":
                f = "Object started without type-definition."
            s = "["
            raise pydatfile.errors.DecodeError.CorruptedFile(f"Unexpected '{s}' at position {r} (first is 0): {f}\n{_str}\n{(r)*' '}^")
        if l == "}":
            if mode == "ot":
                f = "Record-end outside of record."
                s = "}"
                raise pydatfile.errors.DecodeError.CorruptedFile(f"Unexpected '{s}' at position {r} (first is 0): {f}\n{_str}\n{(r)*' '}^")
            if inner <= 1:
                f = "Record not finished before end."
                s = "}"
                raise pydatfile.errors.DecodeError.CorruptedFile(f"Unexpected '{s}' at position {r} (first is 0): {f}\n{_str}\n{(r)*' '}^")
            mode = "ot"
            newkey = _str_any(key, keytype)
            newvalue = _str_any(value, valuetype)
            data.update({newkey: newvalue})
            key = ""
            value = ""
            keytype = ""
            valuetype = ""
            continue
        if l == "]":
            if mode == "ot":
                f = "Object-end out of record."
                s = "]"
                raise pydatfile.errors.DecodeError.CorruptedFile(f"Unexpected '{s}' at position {r} (first is 0): {f}\n{_str}\n{(r)*' '}^")
            if mode == "in":
                f = "Object-end in type definition."
                s = "]"
                raise pydatfile.errors.DecodeError.CorruptedFile(f"Unexpected '{s}' at position {r} (first is 0): {f}\n{_str}\n{(r)*' '}^")
            mode = "in"
            continue
        if mode == "ot" and l != "\\":
            f = "Data outside of record."
            s = l
            raise pydatfile.errors.DecodeError.CorruptedFile(f"Unexpected '{s}' at position {r} (first is 0): {f}\n{_str}\n{(r)*' '}^")
        if mode == "in" and inner >= 2:
            f = "Object cannot be identified as type of key or value."
            s = l
            raise pydatfile.errors.DecodeError.CorruptedFile(f"Unexpected '{s}' at position {r} (first is 0): {f}\n{_str}\n{(r)*' '}^")
        if mode == "ky":
            key += l
            continue
        if mode == "vl":
            value += l
            continue
        if mode == "in" and inner == 0:
            keytype += l
            continue
        if mode == "in" and inner == 1:
            valuetype += l
            continue
    if key != "" or keytype != "" or value != "" or valuetype != "":
        raise pydatfile.errors.DecodeError.CorruptedFile(
            f"Unexpected end of file at position {r} (first is 0): No further information")
    return data


def _decode_list(_str):
    if not isinstance(_str, str):
        raise pydatfile.errors.ParameterTypeError(f"Parameter '_str' must have type '{type('')}', not {type(_str)}")
    data = []
    value = ""
    valuetype = ""
    mode = "ot"
    inner = 0
    r = -1
    for l in _str:
        r += 1
        if l == "{":
            if mode == "in" or mode == "vl":
                f = "No further information."
                if mode == "in":
                    f = "Record-start in type-definition."
                elif mode == "vl":
                    f = "Record-start in value."
                s = "{"
                raise pydatfile.errors.DecodeError.CorruptedFile(f"Unexpected '{s}' at position {r} (first is 0): {f}\n{_str}\n{(r)*' '}^")
            mode = "in"
            inner = 0
            continue
        if l == "[":
            inner += 1
            if inner == 1:
                mode = "vl"
                continue
            f = "Object cannot be identified as key or value."
            if mode == "ot":
                f = "Object-start out of record."
            if mode == "vl" and inner == 2:
                f = "Object-start in value or values' type-definition."
            if valuetype == "":
                f = "Object started without type-definition."
            s = "["
            raise pydatfile.errors.DecodeError.CorruptedFile(f"Unexpected '{s}' at position {r} (first is 0): {f}\n{_str}\n{(r)*' '}^")
        if l == "}":
            if mode == "ot":
                f = "Record-end out of record."
                s = "}"
                raise pydatfile.errors.DecodeError.CorruptedFile(f"Unexpected '{s}' at position {r} (first is 0): {f}\n{_str}\n{(r)*' '}^")
            if inner <= 0:
                f = "Record not finished before end."
                s = "}"
                raise pydatfile.errors.DecodeError.CorruptedFile(f"Unexpected '{s}' at position {r} (first is 0): {f}\n{_str}\n{(r)*' '}^")
            mode = "ot"
            newvalue = _str_any(value, valuetype)
            data.append(newvalue)
            value = ""
            valuetype = ""
            continue
        if l == "]":
            if mode == "ot":
                f = "Object-end out of record."
                s = "]"
                raise pydatfile.errors.DecodeError.CorruptedFile(f"Unexpected '{s}' at position {r} (first is 0): {f}\n{_str}\n{(r)*' '}^")
            if mode == "in":
                f = "Object-end in type definition."
                s = "]"
                raise pydatfile.errors.DecodeError.CorruptedFile(f"Unexpected '{s}' at position {r} (first is 0): {f}\n{_str}\n{(r)*' '}^")
            mode = "in"
            continue
        if mode == "ot" and l != "\\":
            f = "Data outside of record."
            s = l
            raise pydatfile.errors.DecodeError.CorruptedFile(f"Unexpected '{s}' at position {r} (first is 0): {f}\n{_str}\n{(r)*' '}^")
        if mode == "in" and inner >= 2:
            f = "Object cannot be identified as type of key or value."
            s = l
            raise pydatfile.errors.DecodeError.CorruptedFile(f"Unexpected '{s}' at position {r} (first is 0): {f}\n{_str}\n{(r)*' '}^")
        if mode == "vl":
            value += l
            continue
        if mode == "in" and inner == 0:
            valuetype += l
            continue
    if value != "" or valuetype != "":
        raise pydatfile.errors.DecodeError.CorruptedFile(
            f"Unexpected end of file at position {r} (first is 0): No further information")
    return data


def _decode_tuple(_str):
    if not isinstance(_str, str):
        raise pydatfile.errors.ParameterTypeError(f"Parameter '_str' must have type '{type('')}', not {type(_str)}")
    data = []
    value = ""
    valuetype = ""
    mode = "ot"
    inner = 0
    r = -1
    for l in _str:
        r += 1
        if l == "{":
            if mode == "in" or mode == "vl":
                f = "No further information."
                if mode == "in":
                    f = "Record-start in type-definition."
                elif mode == "vl":
                    f = "Record-start in value."
                s = "{"
                raise pydatfile.errors.DecodeError.CorruptedFile(f"Unexpected '{s}' at position {r} (first is 0): {f}\n{_str}\n{(r)*' '}^")
            mode = "in"
            inner = 0
            continue
        if l == "[":
            inner += 1
            if inner == 1:
                mode = "vl"
                continue
            f = "Object cannot be identified as key or value."
            if mode == "ot":
                f = "Object-start out of record."
            if mode == "vl" and inner == 2:
                f = "Object-start in value or values' type-definition."
            if valuetype == "":
                f = "Object started without type-definition."
            s = "["
            raise pydatfile.errors.DecodeError.CorruptedFile(f"Unexpected '{s}' at position {r} (first is 0): {f}\n{_str}\n{(r)*' '}^")
        if l == "}":
            if mode == "ot":
                f = "Record-end out of record."
                s = "}"
                raise pydatfile.errors.DecodeError.CorruptedFile(f"Unexpected '{s}' at position {r} (first is 0): {f}\n{_str}\n{(r)*' '}^")
            if inner <= 0:
                f = "Record not finished before end."
                s = "}"
                raise pydatfile.errors.DecodeError.CorruptedFile(f"Unexpected '{s}' at position {r} (first is 0): {f}\n{_str}\n{(r)*' '}^")
            mode = "ot"
            newvalue = _str_any(value, valuetype)
            data.append(newvalue)
            value = ""
            valuetype = ""
            continue
        if l == "]":
            if mode == "ot":
                f = "Object-end out of record."
                s = "]"
                raise pydatfile.errors.DecodeError.CorruptedFile(f"Unexpected '{s}' at position {r} (first is 0): {f}\n{_str}\n{(r)*' '}^")
            if mode == "in":
                f = "Object-end in type definition."
                s = "]"
                raise pydatfile.errors.DecodeError.CorruptedFile(f"Unexpected '{s}' at position {r} (first is 0): {f}\n{_str}\n{(r)*' '}^")
            mode = "in"
            continue
        if mode == "ot" and l != "\\":
            f = "Data outside of record."
            s = l
            raise pydatfile.errors.DecodeError.CorruptedFile(f"Unexpected '{s}' at position {r} (first is 0): {f}\n{_str}\n{(r)*' '}^")
        if mode == "in" and inner >= 2:
            f = "Object cannot be identified as type of key or value."
            s = l
            raise pydatfile.errors.DecodeError.CorruptedFile(f"Unexpected '{s}' at position {r} (first is 0): {f}\n{_str}\n{(r)*' '}^")
        if mode == "vl":
            value += l
            continue
        if mode == "in" and inner == 0:
            valuetype += l
            continue
    if value != "" or valuetype != "":
        raise pydatfile.errors.DecodeError.CorruptedFile(
            f"Unexpected end of file at position {r} (first is 0): No further information")
    return data


def _any_type(_any: [str, int, float, list, tuple, dict, bool]):
    _type = ""
    if isinstance(_any, bool):
        _type = "bol"
    elif isinstance(_any, int):
        _type = "int"
    elif isinstance(_any, float):
        _type = "flt"
    elif isinstance(_any, str):
        _type = "str"
    elif isinstance(_any, list):
        _type = "lst"
    elif isinstance(_any, tuple):
        _type = "tup"
    elif isinstance(_any, dict):
        _type = "dct"
    else:
        raise pydatfile.errors.EncodeError(f"Objects of type {type(_any)} cannot be encoded (yet). [DETECTING]")
    return _type


def _any_str(_any: [str, int, float, list, tuple, dict, bool], unsecure=False):
    _str = ""
    _type = _any_type(_any)
    if _type == "str":
        _str = _secure(str(_any))
    elif _type == "int":
        _str = str(_any)
    elif _type == "bol":
        if _any is True:
            _str = "t"
        elif _any is False:
            _str = "f"
        elif _any is None:
            _str = "n"
        else:
            raise pydatfile.errors.DecodeError.IncorrectDataType(f"Object '{_str}' is not from type 'bool' as provided.")
    elif _type == "flt":
        _str = str(_any)
    elif _type == "lst":
        if unsecure:
            _str = _encode_list(_any)
        else:
            _str = _secure(_encode_list(_any))
    elif _type == "tup":
        if unsecure:
            _str = _encode_tuple(_any)
        else:
            _str = _secure(_encode_tuple(_any))
    elif _type == "dct":
        if unsecure:
            _str = _encode_dict(_any)
        else:
            _str = _secure(_encode_dict(_any))
    else:
        raise pydatfile.errors.EncodeError.UnknownDataType(
            f"Objects of internal type '{_any_type(_any)}' cannot be encoded (yet). [ENCODING]")
    return _str


def _str_any(_str: str, _type: str, secure=False):
    _any = pydatfile.errors.NotSet
    if _type == "int":
        try:
            _any = int(_str)
        except ValueError:
            raise pydatfile.errors.DecodeError.IncorrectDataType(f"Object '{_str}' is not from type 'int' as provided.")
    elif _type == "bol":
        if _str == "f":
            _any = False
        elif _str == "t":
            _any = True
        elif _str == "n":
            _any = None
        else:
            raise pydatfile.errors.DecodeError.IncorrectDataType(f"Object '{_str}' is not from type 'bool' as provided.")
    elif _type == "str":
        _any = _unsecure(str(_str))
    elif _type == "flt":
        _any = float(_str)
    elif _type == "lst":
        if secure:
            _any = _decode_list(_str)
        else:
            _any = _decode_list(_unsecure(_str))
    elif _type == "tup":
        if secure:
            _any = _decode_tuple(_str)
        else:
            _any = _decode_tuple(_unsecure(_str))
    elif _type == "dct":
        if secure:
            _any = _decode_dict(_str)
        else:
            _any = _decode_dict(_unsecure(_str))
    else:
        raise pydatfile.errors.DecodeError.UnknownDataType(
            f"Objects of internal type '{_type}' cannot be decoded (yet). [DECODING]")
    return _any


def _secure(_str: str):
    _str = _str.replace("$", "$0")
    _str = _str.replace("{", "$1")
    _str = _str.replace("}", "$2")
    _str = _str.replace("[", "$3")
    _str = _str.replace("]", "$4")
    _str = _str.replace("<", "$5")
    _str = _str.replace(">", "$6")
    return _str


def _unsecure(_str: str):
    _str = _str.replace("$6", ">")
    _str = _str.replace("$5", "<")
    _str = _str.replace("$4", "]")
    _str = _str.replace("$3", "[")
    _str = _str.replace("$2", "}")
    _str = _str.replace("$1", "{")
    _str = _str.replace("$0", "$")
    return _str
