from SchemaV.Schema import SpecError
from cube_plugin_async_w_kafka.Networkplane.A_Network_Plane import A_Network_Plane

class NetManager():

    def __init__(self, configManager):


        self.__config_manager=configManager
        self.__address = configManager.getAppAddress()

        self.__isProvider_Validated=False

        self.__validated_network_planes={}

    def init(self, params):
        #check if provider config is OK
        pass

    def validate_provider(self, provider_config, params):
        """

        :param provider_config:
        :param params: params["verify_reachable"]: True/False
        :return:
        :raises: SpecError
        """

        self.__validated_provider=self.__config_manager.validate_provider(provider_config,params)
        self.__isProvider_Validated=True

        return self.__validated_provider

    def validate_network_plane(self,networkplane_config, params):
        """

        :param networkplane_config:
        :param params:
        :return:
        :raises: SpecError, AssertionError
        """

        if self.__isProvider_Validated:

            validated_networkplane= self.__config_manager.validate_networkplane(networkplane_config, params)
            self.__validated_network_planes[validated_networkplane["DCWN"]]={"config":validated_networkplane,"networkplane_object":None}

        else:

            try: dcwn=networkplane_config["DCWN"]
            except: raise SpecError("SPEC ERROR - Network plane should have a DCWN address")

            raise AssertionError("VALIDATION ERROR - Need to validate the provider specification related to network-plane DCWN: "+str(dcwn)+ " first.")

    def get_NetwokPlane(self, networkplane_dcwn, podds_dcwn_specs):
        """

        :param networkplane_dcwn:
        :param podds_dcwn_specs:
        :return:
        :raises: AssertionError
        """

        if networkplane_dcwn in self.__validated_network_planes.keys():

            networkplane=self.__validated_network_planes[networkplane_dcwn]

            if networkplane["networkplane_object"] is None:

                networkplane["networkplane_object"] = A_Network_Plane(networkplane["config"], podds_dcwn_specs)
                return networkplane["networkplane_object"]
            else:
                return networkplane["networkplane_object"]

        else:
            raise AssertionError("NETWORK PLANE BUILDING ERROR - Need to validate the network-plane DCWN: "+str(networkplane_dcwn)+" specification first.")











