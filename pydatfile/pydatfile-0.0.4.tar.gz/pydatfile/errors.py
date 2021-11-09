class DecodeError(BaseException):
    STR = "pydatfile.errors.DecodeError"

    class UnknownDataType(BaseException):
        STR = "pydatfile.errors.DecodeError.UnknownDataType"

    class IncorrectDataType(BaseException):
        STR = "pydatfile.errors.DecodeError.IncorrectDataType"

    class CorruptedFile(BaseException):
        STR = "pydatfile.errors.DecodeError.CorruptedFile"

    class EmptyFile(BaseException):
        STR = "pydatfile.errors.DecodeError.EmptyFile"


class EncodeError(BaseException):
    STR = "pydatfile.errors.EncodeError"

    class UnknownDataType(BaseException):
        STR = "pydatfile.errors.EncodeError.UnknownDataType"

    class IncorrectDataType(BaseException):
        STR = "pydatfile.errors.EncodeError.IncorrectDataType"


class ParameterTypeError(TypeError):
    STR = "pydatfile.errors.ParameterTypeError"


class NotSet(KeyError):
    STR = "pydatfile.errors.NotSet"


class ReadError(BaseException):
    STR = "pydatfile.errors.ReadError"

    class CorruptedFile(BaseException):
        STR = "pydatfile.errors.ReadError.CorruptedFile"
