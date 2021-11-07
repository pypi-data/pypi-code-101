import logging
import socket


class Provider_Checker():

    def __init__(self, address):
        self.__address = address

    def isString(self, x):
        return isinstance(x, str)

    def isInt(self, x):
        return isinstance(x, int)

    def isBoolean(self, x):
        return isinstance(x, bool)

    def isHostReachable(self, host):
        try:
            socket.gethostbyname(host)
            return True
        except socket.error:
            logging.getLogger(self.__address).error(
                "KAFKA BROKER UNREACHABLE - Host: " + str(host) + " is not reachable")
            return False

    def isValidPortNumber(self, port):
        if port >= 1 and port <= 65535:
            return True
        else:
            logging.getLogger(self.__address).error(
                "KAFKA BROKER PORT ADDRESS ERROR - Port: " + str(port) + " should be in range [1, 65535]")
            return False
