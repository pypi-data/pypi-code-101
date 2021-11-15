from analytics_command_center.common.huemul_response_bloc import HuemulResponseBloc
from analytics_command_center.common.huemul_logging import huemulLogging
from analytics_command_center.common.huemul_common import huemulCommon
from analytics_command_center.auth.auth_service_provider import AuthServiceProvider

class AuthServiceBloc(HuemulResponseBloc):
    #
    # start authSignInService
    # @param authModel authModel
    # @return HuemulResponseBloc[AuthServiceModel]
    #
    def authSignInService(self, authModel):
        continueInLoop = True
        attempt = 0
        #result = HuemulResponseBloc()

        huemulLogging.logMessageInfo("Ground Control station: " + authModel.urlService)
        huemulCommon.setServiceUrl(value = authModel.urlService)

        while (continueInLoop):
            result = AuthServiceProvider().authSignInService(
                consumerId = authModel.consumerId,
                consumerSecret = authModel.consumerSecret,
                orgId = authModel.orgId,
                applicationName = authModel.applicationName
            )

            attempt +=1
            continueInLoop = result.analyzeErrors(attempt)
        

        return result