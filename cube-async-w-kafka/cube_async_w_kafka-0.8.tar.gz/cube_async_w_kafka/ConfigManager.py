from SchemaV.Checker import Checker
from SchemaV.Schema import Validator

from cube_async_w_kafka.Checkers import NetworkPlane_Checker
from cube_async_w_kafka.Checkers import Provider_Checker
import json


class ConfigManager():

    def __init__(self, address):

        self.__address = address
        self.__properties_file= "properties.json"
        self.__provider_checker = Provider_Checker(address)
        self.__networkplane_checker = NetworkPlane_Checker(address)

    def load_properties(self):

        try:

            with open(self.__properties_file) as propf:
                properties = json.load(propf)
            propf.close()

        except Exception as e:
            propf.close()
            raise ImportError("KAFKA OUTBOUND PROPERTIES FILE IMPORT ERROR - file :"+str(self.__properties_file)+" is not json consistent or does not exist, details: "+str(e))

        try:

            self.__version=properties["version"]

            self.__provider_name=properties["provider"]["name"]
            self.__check_reachable=properties["provider"]["check_reachable"]

            self.__io_policy=properties["networkplane"]["io_policy"]
            self.__type = properties["networkplane"]["type"]

            self.__default_compression_codec=properties["networkplane"]["compression_codec"]
            self.__default_enable_stats=properties["networkplane"]["enable_stats"]
            self.__default_connection_timeout=properties["networkplane"]["connection_timeout"]
            self.__default_allow_data_loss=properties["networkplane"]["allow_data_loss"]
            self.__default_allow_data_duplication=properties["networkplane"]["allow_data_duplication"]

            self.__default_buffer_max_records=properties["networkplane"]["buffer_max_records"]
            self.__default_buffer_max_size=properties["networkplane"]["buffer_max_size"]
            self.__default_burst_buffer_max_records=properties["networkplane"]["burst_buffer_max_records"]

            self.__default_batch_build_delay=properties["networkplane"]["batch_build_delay"]
            self.__default_batch_max_records=properties["networkplane"]["batch_max_records"]
            self.__default_batch_max_size=properties["networkplane"]["batch_max_size"]
            self.__default_per_request_max_batches=properties["networkplane"]["per_request_max_batches"]

        except Exception as e:
            raise ImportError("KAFKA OUTBOUND PROPERTIES FILE IMPORT ERROR - In file :"+str(self.__properties_file)+", details: "+str(e))

    def get_version(self):
        return self.__version

    def get_provider_schema(self, params):
        """

        :param params: params["verify_reachable"]: True/False
        :return:
        """

        try:
            connectivity_check = params["check_reachable"]
        except:
            connectivity_check = self.__check_reachable

        if connectivity_check:
            host_checker = Checker(True, self.__provider_checker.isHostReachable, None)
        else:
            host_checker = Checker(True, None, None)

        schema = {'checkIn': None,
                  'checkNext': {
                      'name': {'checkIn': Checker(False, self.__provider_checker.isString, "NA"), 'checkNext': None},
                      'DCWN': {'checkIn': Checker(True, self.__provider_checker.isString, None), 'checkNext': None},
                      'region': {'checkIn': Checker(True, self.__provider_checker.isString, None), 'checkNext': None},
                      'record-address': {'checkIn': Checker(True, None, None),
                                         'checkNext': [{'checkIn': Checker(True, None, None), 'checkNext': {
                                             'host': {
                                                 'checkIn': host_checker,
                                                 'checkNext': None},
                                             'port': {
                                                 'checkIn': Checker(True, self.__provider_checker.isValidPortNumber,
                                                                    None),
                                                 'checkNext': None}}}
                                                       ]
                                         }
                  }

                  }

        return schema

    def get_networkplane_schema(self, params):

        return {'checkIn': None, 'checkNext': {

            'name': {'checkIn': Checker(False, self.__networkplane_checker.isString, "NA"), 'checkNext': None},
            'DCWN': {'checkIn': Checker(True, self.__networkplane_checker.isString, None), 'checkNext': None},
            'data-service': {'checkIn': Checker(True, self.__networkplane_checker.isString, None), 'checkNext': None},
            'compression-codec': {'checkIn': Checker(False, self.__networkplane_checker.compression_Algo, self.__default_compression_codec),
                                  'checkNext': None},
            'enable-stats': {'checkIn': Checker(False, self.__networkplane_checker.isBoolean, self.__default_enable_stats), 'checkNext': None},
            'connection-timeout': {'checkIn': Checker(False, self.__networkplane_checker.isInt, self.__default_connection_timeout),
                                   'checkNext': None},

            'on-failure': {'checkIn': Checker(False, None, {'allow-data-loss': self.__default_allow_data_loss}), 'checkNext': {
                'allow-data-loss': {'checkIn': Checker(False, self.__networkplane_checker.isInt, self.__default_allow_data_loss), 'checkNext': None}}
                           },

            'on-recover': {'checkIn': Checker(False, None, {'allow-data-duplication': self.__default_allow_data_duplication}), 'checkNext': {
                'allow-data-duplication': {'checkIn': Checker(False, self.__networkplane_checker.isBoolean, self.__default_allow_data_duplication),
                                           'checkNext': None}}
                           },

            'buffering': {'checkIn': Checker(True, None, {'buffer-max-records': self.__default_buffer_max_records, 'buffer-max-size': self.__default_buffer_max_size,
                                                          "burst-buffer-max-records": self.__default_burst_buffer_max_records}), 'checkNext': {
                'buffer-max-records': {'checkIn': Checker(False, self.__networkplane_checker.isInt, self.__default_buffer_max_records),'checkNext': None},
                'buffer-max-size': {'checkIn': Checker(False, self.__networkplane_checker.isInt, self.__default_buffer_max_size),'checkNext': None},
                'burst-buffer-max-records': {'checkIn': Checker(False, self.__networkplane_checker.isInt, self.__default_burst_buffer_max_records),'checkNext': None}}
                          },

            'batching': {'checkIn': Checker(False, None, {'batch-build-delay': self.__default_batch_build_delay, 'batch-max-records': self.__default_batch_max_records,
                                                          "batch-max-size": self.__default_batch_max_size, 'per-request-max-batches': self.__default_per_request_max_batches}),
                         'checkNext': {
                             'batch-build-delay': {'checkIn': Checker(False, self.__networkplane_checker.isInt, self.__default_batch_build_delay),'checkNext': None},
                             'batch-max-records': {'checkIn': Checker(False, self.__networkplane_checker.isInt, self.__default_batch_max_records),'checkNext': None},
                             'batch-max-size': {'checkIn': Checker(False, self.__networkplane_checker.isInt, self.__default_batch_max_size),'checkNext': None},
                             'per-request-max-batches': {'checkIn': Checker(False, self.__networkplane_checker.isInt, self.__default_per_request_max_batches),'checkNext': None}}}
        }
                }

    def validate_provider(self,provider_config,params):
        """

        :param provider_config:
        :param params: params["verify_reachable"]: True/False
        :return:
        """

        provider_validator=Validator(self.get_provider_schema(params))
        return provider_validator.validate(provider_config)

    def validate_networkplane(self,networkplane_config, params):

        networkplane_validator = Validator(self.get_networkplane_schema(params))
        return networkplane_validator.validate(networkplane_config)
