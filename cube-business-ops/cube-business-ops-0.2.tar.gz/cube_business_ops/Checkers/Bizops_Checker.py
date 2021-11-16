import logging
import os



class Bizops_Checker():

    def __init__(self, address):
        self.__address = address
        self.__supported_watch_list = ["CPU", "RAM", "NETWORK", "PODD"]
        self.__supported_log_level=["DEBUG","INFO","WARNING","ERROR","CRITICAL"]

    def isString(self, x):
        return isinstance(x, str)

    def isInt(self, x):
        return isinstance(x, int)

    def check_log_format(self,x):
        try:
            formatter = logging.Formatter(x)
            return True
        except:
            logging.getLogger(self.__address).error("LOG FORMAT ERROR - " + "Log Formatter: "+str(x) + " is not correct")
            return False

    def isBoolean(self, x):
        return isinstance(x, bool)

    def isDirectory(self, dir):
        if os.path.isdir(dir):
            return True
        else:
            logging.getLogger(self.__address).error(
                "LOCAL LOG ERROR - " + str(dir) + ": is not a valid directory")
            return False


    def check_watch(self, params):

        to_watch = params.replace(' ', '').split(",")
        for param in to_watch:
            if not param in self.__supported_watch_list:
                logging.getLogger(self.__address).error("METRIC ERROR - "+str(param)+" metric is not supported")
                print(param)
                return False

        return True

    def check_local_log_level(self, verbose):

        if verbose in self.__supported_log_level:
            return True
        else:
            logging.getLogger(self.__address).error("LOCAL LOG ERROR - " + str(verbose) + ": verbosity level is not supported")
            return False


    def check_stream_log_level(self, verbose):

        if verbose in self.__supported_log_level:
            return True
        else:
            logging.getLogger(self.__address).error("STREAM LOG ERROR - " + str(verbose) + ": verbosity level is not supported")
            return False



