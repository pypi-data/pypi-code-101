import logging
from multiprocessing import Queue
from logging.handlers import QueueHandler, QueueListener,RotatingFileHandler

class Cubelog():

    def __init__(self, __app_address, __log_formatter):

        self.__app_address=__app_address

        self.__log_formatter = logging.Formatter(__log_formatter)

        self.__cube_logger = logging.getLogger(self.__app_address)
        self.__cube_logger.setLevel(logging.DEBUG)

        self.log_queue = Queue(-1)  # local queue
        queue_handler = QueueHandler(self.log_queue)

        self.__cube_logger.addHandler(queue_handler)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(self.__log_formatter)
        console_handler.setLevel(logging.DEBUG)

        console_handler_DCWN= "CONSOLE"
        self.__handlers = {console_handler_DCWN:console_handler}

        self.__cube_logger.propagate = True




    def start(self):

        logging.getLogger(self.__app_address).info("CUBE LOGGING - Starting logging OPS")
        self.listener = QueueListener(self.log_queue, *self.__handlers.values(), respect_handler_level=True)
        self.listener.start()
        logging.getLogger(self.__app_address).info("CUBE LOGGING - Logging OPS is started for logging handlers: "+str(list(self.__handlers.keys())))

    def stop(self):

        logging.getLogger(self.__app_address).info("CUBE LOGGING - Stopping logging OPS for all handlers: "+str(list(self.__handlers.keys()))+" - End of logging.")
        self.listener.stop()

        for handler_dcwn, handler in self.__handlers.items():
            handler.flush()
            handler.close()




    def add_log_handlers(self, handlers):

        #check if new handlers
        new_handlers=True
        existing_dcwn=""
        for new_handler_dcwn in handlers.keys():
            if new_handler_dcwn in self.__handlers.keys():
                existing_dcwn=new_handler_dcwn
                new_handlers=False
                break

        if new_handlers:

            #stopping current listener and flush logs
            self.listener.stop()

            for handler_dcwn, handler in self.__handlers.items():
                handler.flush()

            #add new handlers
            for new_handler_dcwn, handler in handlers.items():
                self.__handlers[new_handler_dcwn]=handler
                logging.getLogger(self.__app_address).info("CUBE LOGGING - Added logging handler: " + str(new_handler_dcwn))

            #start listener
            self.listener = QueueListener(self.log_queue, *self.__handlers.values(), respect_handler_level=True)
            self.listener.start()
            logging.getLogger(self.__app_address).info(
                "CUBE LOGGING - Logging OPS is started for logging handlers: " + str(list(self.__handlers.keys())))

        else:
            logging.getLogger(self.__app_address).error("CUBE LOGGING - Failed to add logging handler: " + str(existing_dcwn)+", handler with the same DCWN already exist")
            raise ValueError("CUBE LOGGING - Failed to add logging handler: " + str(existing_dcwn)+", handler with the same DCWN already exist")


    #review
    def remove_log_handler(self, dcwn):

        try:
            handler=self.__handlers[dcwn]
        except KeyError:
            logging.getLogger(self.__app_address).error("CUBE LOGGING - Failed to remove logging handler: " + str(dcwn)+", handler does not exist")
            raise ValueError("CUBE LOGGING - Failed to remove logging handler: " + str(dcwn)+", handler does not exist")

        except Exception as e:
            logging.getLogger(self.__app_address).error("CUBE LOGGING - Unknown error when removing handler: " + str(dcwn)+", details: "+str(e))
            raise ValueError("CUBE LOGGING - Unknown error when removing handler: " + str(dcwn)+", details: "+str(e))

        handler.close()
        self.listener.stop()
        del self.__handlers[dcwn]
        # start listener
        self.listener = QueueListener(self.log_queue, *self.__handlers.values(), respect_handler_level=True)
        self.listener.start()
        logging.getLogger(self.__app_address).info("CUBE LOGGING - Deleted logging handler: " + str(dcwn))
        logging.getLogger(self.__app_address).info(
            "CUBE LOGGING - Logging OPS is started for logging handlers: " + str(list(self.__handlers.keys())))









