import logging


class NetworkPlane_Checker():

    def __init__(self, address):
        self.__address = address

    def isString(self, x):
        return isinstance(x, str)

    def isInt(self, x):
        return isinstance(x, int)

    def isBoolean(self, x):
        return isinstance(x, bool)

    def compression_Algo(self, algo):

        if algo == "snappy" or algo == "":
            return True

        else:
            logging.getLogger(self.__address).error("Compression Error - Compression algo: " + str(
                algo) + " is not supported, only supporting: snappy")
            return False

    def isTypeValid(self, type):
        if type.lower()=="async":
            return True
        else:
            return False