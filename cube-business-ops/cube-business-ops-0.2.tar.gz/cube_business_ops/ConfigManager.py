import json
import os.path

from SchemaV.Checker import Checker
from SchemaV.Schema import Validator

from cube_business_ops.Checkers.Bizops_Checker import Bizops_Checker


class ConfigManager():

    def __init__(self, address):

        self.__address = address
        self.__properties_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "properties.json")
        self.__app_checker = Bizops_Checker(address)

    def __prepare_default_log_dir(self, default_log_dir):
        # can raise permission denied
        try:
            os.makedirs(default_log_dir, exist_ok=True)
            return default_log_dir
        except:
            raise

    def load_properties(self):

        try:

            with open(self.__properties_file) as propf:
                properties = json.load(propf)
            propf.close()

        except Exception as e:
            raise ImportError("BIZOPS PROPERTIES FILE IMPORT ERROR - file :" + str(
                self.__properties_file) + " is not json consistent or does not exist, details: " + str(e))

        try:

            self.__bizops_version = properties["bizops_version"]

            # ------------- application Data--------------
            self.__default_data_DCWN = properties["data"]["DCWN"]
            self.__default_data_podd_buffer_size = properties["data"]["podd_buffer_size"]

            # ------------- application Monitor --------------
            self.__default_monitor_DCWN = properties["monitor"]["DCWN"]

            # ------------- application Monitor Notifications --------------
            self.__default_notify_DCWN = properties["monitor"]["notify"]["DCWN"]
            self.__default_notify_podd_DCWN = properties["monitor"]["notify"]["podd_DCWN"]
            self.__default_notify_podd_buffer_size = properties["monitor"]["notify"]["podd_buffer_size"]

            # ------------- application Monitor Metrics --------------
            self.__default_metrics_DCWN = properties["monitor"]["metrics"]["DCWN"]
            self.__default_metrics_podd_DCWN = properties["monitor"]["metrics"]["podd_DCWN"]
            self.__default_metrics_heartbeat = properties["monitor"]["metrics"]["heartbeat"]
            self.__default_metrics_watch = properties["monitor"]["metrics"]["watch"]
            self.__default_metric_podd_buffer_size = properties["monitor"]["metrics"]["podd_buffer_size"]

            # ------------- application Log --------------
            self.__default_log_DCWN = properties["log"]["DCWN"]

            # ------------- application Log Local On Disk --------------
            self.__default_local_log_DCWN = properties["log"]["toDisk"]["DCWN"]
            self.__default_local_log_level = properties["log"]["toDisk"]["logging-level"]
            self.__default_max_log_files = properties["log"]["toDisk"]["max-log-count"]
            self.__default_max_log_size = properties["log"]["toDisk"]["max-log-size"]
            self.__default_log_dir = properties["log"]["toDisk"]["logging-dir"]
            self.__default_local_log_format=properties["log"]["toDisk"]["logging-format"]

            # ------------- application Log Stream--------------
            self.__default_stream_log_DCWN = properties["log"]["stream"]["DCWN"]
            self.__default_stream_log_podd_DCWN = properties["log"]["stream"]["podd_DCWN"]
            self.__default_stream_log_level = properties["log"]["stream"]["logging-level"]
            self.__default_stream_log_podd_buffer_size = properties["log"]["stream"]["podd_buffer_size"]
            self.__default_stream_log_format = properties["log"]["stream"]["logging-format"]


        except Exception as e:
            raise ImportError(
                "BIZOPS PROPERTIES FILE IMPORT ERROR - In file :" + str(self.__properties_file) + ", details: " + str(
                    e))

    def get_app_schema(self, params):
        """

        :param params: params["verify_reachable"]: True/False
        :return:
        """

        try:
            self.__group_name = params["group-name"]
        except:
            raise AssertionError("BUSINESS PROFILE IMPORT ERROR - Cannot import schema without a defined Business Group Name")

        # default Topics & Keys

        self.__default_notification_topic = self.__group_name.upper() + "_NOTIFICATIONS"
        self.__default_metrics_topic = self.__group_name.upper() + "_METRICS"
        self.__default_streamlog_topic = self.__group_name.upper() + "_LOG"

        self.__default_data_podd_key = "None"
        self.__default_notification_podd_key = self.__address
        self.__default_metrics_podd_key = self.__address
        self.__default_streamlog_podd_key = self.__address

        schema = {'checkIn': None, 'checkNext': {
            'version': {'checkIn': Checker(False, self.__app_checker.isString, "NA"), 'checkNext': None},
            'desc': {'checkIn': Checker(False, self.__app_checker.isString, "NA"), 'checkNext': None},

            'name': {'checkIn': Checker(False, self.__app_checker.isString, "NA"), 'checkNext': None},
            'DCWN': {'checkIn': Checker(True, self.__app_checker.isString, None), 'checkNext': None},

            # region: used to force the app deployment in a specified region, NA for any where
            'region': {'checkIn': Checker(None, self.__app_checker.isString, "NA"), 'checkNext': None},

            'data': {'checkIn': None, 'checkNext': {

                'DCWN': {'checkIn': Checker(False, self.__app_checker.isString, self.__default_data_DCWN),
                         'checkNext': None},

                'podd': {'checkIn': None, 'checkNext': [{'checkIn': None, 'checkNext': {

                    'name': {'checkIn': Checker(True, self.__app_checker.isString, None), 'checkNext': None},
                    'DCWN': {'checkIn': Checker(True, self.__app_checker.isString, None), 'checkNext': None},
                    'network-plane': {'checkIn': Checker(True, self.__app_checker.isString, None), 'checkNext': None},
                    'topic': {'checkIn': Checker(True, self.__app_checker.isString, None), 'checkNext': None},
                    'key': {'checkIn': Checker(False, self.__app_checker.isString, self.__default_data_podd_key),
                            'checkNext': None},
                    'buffer': {
                        'checkIn': Checker(False, self.__app_checker.isInt, self.__default_data_podd_buffer_size),
                        'checkNext': None}}}]}}},

            'monitor': {'checkIn': Checker(True, None, None), 'checkNext': {

                'DCWN': {'checkIn': Checker(False, self.__app_checker.isString, self.__default_monitor_DCWN),
                         'checkNext': None},
                'notify': {'checkIn': Checker(True, None, None), 'checkNext': {

                    'DCWN': {'checkIn': Checker(False, self.__app_checker.isString, self.__default_notify_DCWN),
                             'checkNext': None},

                    'podd': {'checkIn': Checker(True, None, None), 'checkNext': {

                        'name': {'checkIn': Checker(False, self.__app_checker.isString, "NA"), 'checkNext': None},
                        'DCWN': {
                            'checkIn': Checker(False, self.__app_checker.isString, self.__default_notify_podd_DCWN),
                            'checkNext': None},
                        'network-plane': {'checkIn': Checker(True, self.__app_checker.isString, None),
                                          'checkNext': None},
                        'topic': {
                            'checkIn': Checker(False, self.__app_checker.isString, self.__default_notification_topic),
                            'checkNext': None},
                        'key': {'checkIn': Checker(False, self.__app_checker.isString,
                                                   self.__default_notification_podd_key), 'checkNext': None},
                        'buffer': {
                            'checkIn': Checker(False, self.__app_checker.isInt, self.__default_notify_podd_buffer_size),
                            'checkNext': None}}}}},

                'metrics': {'checkIn': Checker(True, None, None), 'checkNext': {

                    'DCWN': {'checkIn': Checker(False, self.__app_checker.isString, self.__default_metrics_DCWN),
                             'checkNext': None},
                    'heartbeat': {'checkIn': Checker(False, self.__app_checker.isInt, self.__default_metrics_heartbeat),
                                  'checkNext': None},
                    'watch': {'checkIn': Checker(False, self.__app_checker.check_watch, self.__default_metrics_watch),
                              'checkNext': None},

                    'podd': {'checkIn': Checker(True, None, None), 'checkNext': {

                        'name': {'checkIn': Checker(False, self.__app_checker.isString, "NA"), 'checkNext': None},
                        'DCWN': {
                            'checkIn': Checker(False, self.__app_checker.isString, self.__default_metrics_podd_DCWN),
                            'checkNext': None},
                        'network-plane': {'checkIn': Checker(True, self.__app_checker.isString, None),
                                          'checkNext': None},
                        'topic': {'checkIn': Checker(False, self.__app_checker.isString, self.__default_metrics_topic),
                                  'checkNext': None},
                        'key': {'checkIn': Checker(False, self.__app_checker.isString, self.__default_metrics_podd_key),
                                'checkNext': None},
                        'buffer': {
                            'checkIn': Checker(False, self.__app_checker.isInt, self.__default_metric_podd_buffer_size),
                            'checkNext': None}}}}}}},

            'log': {'checkIn': Checker(True, None, None), 'checkNext': {

                'DCWN': {'checkIn': Checker(False, self.__app_checker.isString, self.__default_log_DCWN),
                         'checkNext': None},

                'toDisk': {'checkIn': Checker(False, None, []), 'checkNext': [{
                     "checkIn":Checker(False, None, {}),
                     "checkNext":{

                    'logging-level': {'checkIn': Checker(False, self.__app_checker.check_local_log_level,
                                                   self.__default_local_log_level), 'checkNext': None},

                    'logging-format':  {'checkIn': Checker(False, self.__app_checker.check_log_format,
                                                   self.__default_local_log_format), 'checkNext': None},

                    'DCWN': {'checkIn': Checker(False, self.__app_checker.isString, self.__default_local_log_DCWN),
                             'checkNext': None},
                    'logging-dir': {'checkIn': Checker(False, self.__app_checker.isDirectory,
                                                     self.__prepare_default_log_dir(self.__default_log_dir)),
                                  'checkNext': None},
                    'max-log-count': {'checkIn': Checker(False, self.__app_checker.isInt, self.__default_max_log_files),
                                      'checkNext': None},
                    'max-log-size': {'checkIn': Checker(False, self.__app_checker.isInt, self.__default_max_log_size),
                                     'checkNext': None}
                }}]
                           },

                'stream': {'checkIn': Checker(True, None, None), 'checkNext': [{
                    "checkIn": Checker(True, None, None),
                    "checkNext": {

                    'logging-level': {'checkIn': Checker(False, self.__app_checker.check_stream_log_level,
                                                   self.__default_stream_log_level), 'checkNext': None},

                    'logging-format': {'checkIn': Checker(False, self.__app_checker.check_log_format,
                                                      self.__default_stream_log_format), 'checkNext': None},

                    'DCWN': {'checkIn': Checker(False, self.__app_checker.isString, self.__default_stream_log_DCWN),
                             'checkNext': None},

                    'podd': {'checkIn': Checker(True, None, None), 'checkNext': {

                        'name': {'checkIn': Checker(False, self.__app_checker.isString, "NA"), 'checkNext': None},
                        'DCWN': {
                            'checkIn': Checker(False, self.__app_checker.isString, self.__default_stream_log_podd_DCWN),
                            'checkNext': None},
                        'network-plane': {'checkIn': Checker(True, self.__app_checker.isString, None),
                                          'checkNext': None},
                        'topic': {
                            'checkIn': Checker(False, self.__app_checker.isString, self.__default_streamlog_topic),
                            'checkNext': None},
                        'key': {
                            'checkIn': Checker(False, self.__app_checker.isString, self.__default_streamlog_podd_key),
                            'checkNext': None},
                        'buffer': {'checkIn': Checker(False, self.__app_checker.isInt,
                                                      self.__default_stream_log_podd_buffer_size), 'checkNext': None}}}
                }}]
                           }
            }
                    }}}

        return schema

    def validate_profile(self, application_config, params):

        app_validator = Validator(self.get_app_schema(params))
        return app_validator.validate(application_config)
