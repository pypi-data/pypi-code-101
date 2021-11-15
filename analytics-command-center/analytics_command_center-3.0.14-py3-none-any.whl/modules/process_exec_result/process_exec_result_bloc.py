from analytics_command_center.modules.process_exec_result.process_exec_result_provider import ProcessExecResultProvider
from analytics_command_center.common.huemul_response_bloc import HuemulResponseBloc

class ProcessExecResultBloc:
    #
    # start processExecResultCreate
    # @param ProcessExecResultModel ProcessExecResultModel
    # @return HuemulResponseBloc[ProcessExecResultModel]
    #
    def processExecResultCreate(self, ProcessExecResultModel):
        continueInLoop = True
        attempt = 0
        result = HuemulResponseBloc()

        while (continueInLoop):
            result = ProcessExecResultProvider().processExecResultCreate(
                    processExecResultModel=ProcessExecResultModel
            )
            attempt +=1
            continueInLoop = result.analyzeErrors(attempt)
        
        return result