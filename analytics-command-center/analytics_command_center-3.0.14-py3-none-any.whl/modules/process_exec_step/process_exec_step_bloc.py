from analytics_command_center.modules.process_exec_step.process_exec_step_provider import ProcessExecStepProvider
from analytics_command_center.common.huemul_response_bloc import HuemulResponseBloc

class ProcessExecStepBloc:
    #
    # start processExecStepCreate
    # @param ProcessExecStepModel ProcessExecStepModel
    # @return HuemulResponseBloc[ProcessExecStepResponseModel]
    #
    def processExecStepCreate(self, ProcessExecStepModel):
        continueInLoop = True
        attempt = 0
        result = HuemulResponseBloc()

        while (continueInLoop):
            result = ProcessExecStepProvider().processExecStepCreate(
                    processExecStepModel=ProcessExecStepModel
            )
            attempt +=1
            continueInLoop = result.analyzeErrors(attempt)
        
        return result