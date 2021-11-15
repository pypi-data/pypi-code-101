from analytics_command_center.modules.process_exec.process_exec_provider import ProcessExecProvider
from analytics_command_center.common.huemul_response_bloc import HuemulResponseBloc

class ProcessExecBloc:
    #
    # start processExecStartExecute
    # @param processExecStartModel processExecStartModel
    # @return HuemulResponseBloc[ProcessExecResponseModel]
    #
    def processExecStartExecute(self, processExecStartModel):
        continueInLoop = True
        attempt = 0
        result = HuemulResponseBloc()

        while (continueInLoop):
            result = ProcessExecProvider().processExecStartExecute(
                    processExecStartModel=processExecStartModel
            )
            attempt +=1
            continueInLoop = result.analyzeErrors(attempt)
        
        return result

    #
    # Stop processExecStopExecute
    # @param processExecStopModel processExecStopModel
    # @return HuemulResponseBloc[ProcessExecResponseModel]
    #
    def processExecStopExecute(self, processExecStopModel):
        continueInLoop = True
        attempt = 0
        result = HuemulResponseBloc()

        while (continueInLoop):
            result = ProcessExecProvider().processExecStopExecute(
                    processExecStopModel=processExecStopModel
            )
            attempt +=1
            continueInLoop = result.analyzeErrors(attempt)
        
        return result