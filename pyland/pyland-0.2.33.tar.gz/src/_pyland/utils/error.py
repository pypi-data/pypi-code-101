# coding=utf8


class Sqlerror(IOError):
    pass


class MissingError(KeyError):
    pass

# try:
#     raise Sqlerror("Bad hostname")
# except Sqlerror as e:
#     print(e)
