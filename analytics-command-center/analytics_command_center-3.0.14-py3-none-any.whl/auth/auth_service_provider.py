from analytics_command_center.common.huemul_response_bloc import HuemulResponseBloc
from analytics_command_center.common.huemul_response_error import HuemulResponseError
from analytics_command_center.common.huemul_connection import HuemulConnection
from analytics_command_center.auth.auth_service_model import AuthServiceModel
import base64

class AuthServiceProvider(HuemulResponseBloc):
    
    #
    # create new element
    # @param consumerId consumerId: String
    # @param consumerSecret consumerSecret: String
    # @param orgId orgId: String
    # @param applicationName applicationName: String
    # @return HuemulResponseBloc[AuthServiceModel]
    #
    def authSignInService(self, consumerId, consumerSecret, orgId, applicationName):
        #self = HuemulResponseBloc()
        try:
            dataIn = consumerId + ":" + orgId + ":" + applicationName + ":" + consumerSecret
            bytes = dataIn.encode('ascii') #.getBytes(StandardCharsets.UTF_8)
            base64Str = base64.b64encode(bytes).decode('ascii')

            huemulResponse = HuemulConnection().authRequest(
                route = "authService/v1/sign-in-service/",
                data = base64Str,
                orgId = orgId
            )

            #get status from connection
            self.fromResponseProvider(huemulResponseProvider = huemulResponse)
            if (self.isSuccessful):
                self.data = [] if len(huemulResponse.dataRaw) == 0 else list(map(lambda x: AuthServiceModel(**x) ,huemulResponse.dataRaw))
        except Exception as e:
            self.errors.append(
                HuemulResponseError(errorId = "APP-101", errorTxt = str(e))
            )

        return self


        