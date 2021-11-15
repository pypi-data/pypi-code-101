from analytics_command_center.modules.process_exec_global_path.process_exec_global_path_provider import ProcessExecGlobalPathProvider
from analytics_command_center.common.huemul_response_bloc import HuemulResponseBloc

class ProcessExecGlobalPathBloc:
    #
    # start processExecGlobalPathCreate
    # @param ProcessExecGlobalPathModel ProcessExecGlobalPathModel
    # @return HuemulResponseBloc[ProcessExecGlobalPathModel]
    #
    def processExecGlobalPathCreate(self, ProcessExecGlobalPathModel):
        continueInLoop = True
        attempt = 0
        result = HuemulResponseBloc()

        while (continueInLoop):
            result = ProcessExecGlobalPathProvider().processExecGlobalPathCreate(
                    processExecGlobalPathModel=ProcessExecGlobalPathModel
            )
            attempt +=1
            continueInLoop = result.analyzeErrors(attempt)
        
        return result