import logging

class LogToPoDD(logging.Handler):

    def __init__(self,app_address, config, podd):

        logging.Handler.__init__(self)

        self.__address = app_address
        self.__podd=podd



        verbose = config["level"]
        if verbose == "DEBUG":
            level = logging.DEBUG
        elif verbose == "CRITICAL":
            level = logging.CRITICAL
        elif verbose == "ERROR":
            level = logging.ERROR
        elif verbose == "WARNING":
            level = logging.WARNING
        elif verbose == "INFO":
            level = logging.INFO
        else:
            level = logging.DEBUG

        self.setLevel(level)
        formatter = config["format"]
        self.setFormatter(formatter)



    def emit(self, record):  # override Handler's `emit` method

        try:

            self.__podd.send(str(self.format(record)))

        except: #drop that record
            pass




