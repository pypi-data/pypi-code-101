from SchemaV.Schema import SpecError
from cube_business_ops.LogHandlers.LogToDisk import LogToDisk
from cube_business_ops.LogHandlers.LogToPoDD import LogToPoDD

class OPSManager():

    def __init__(self, configManager,app_address):


        self.__config_manager=configManager
        self.__app_address = app_address

    def validate_profile(self,application_config, params):

        self.__validated_bizops_conf= self.__config_manager.validate_profile(application_config, params)
        return self.__validated_bizops_conf


    def get_LogToDisk_handlers(self):

        handlers={}

        try: self.__validated_bizops_conf
        except : raise AssertionError("CUBE ERROR - Should validate BIZOPS profile before building log components")

        try: local_log_conf=self.__validated_bizops_conf["log"]["toDisk"]
        except: SpecError("SPEC ERROR - ToDisk logging section not found in profile")



        for log_conf in local_log_conf:

            if not log_conf["DCWN"] in handlers.keys():


                handlers[log_conf["DCWN"]]=LogToDisk(self.__app_address,log_conf)

            else:
                raise SpecError("SPEC ERROR - ToDisk DCWN: "+str(log_conf["DCWN"])+" should be unique")


        return handlers

    def get_stream_handlers(self):
        pass








    def get_monitor(self, metrics_podd, notification_pod):
        pass

