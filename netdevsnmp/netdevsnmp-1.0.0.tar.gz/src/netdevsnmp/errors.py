class NetdevsnmpError(Exception):
    pass


class ArgumentError(NetdevsnmpError):
    pass


class SnmpError(NetdevsnmpError):
    pass
