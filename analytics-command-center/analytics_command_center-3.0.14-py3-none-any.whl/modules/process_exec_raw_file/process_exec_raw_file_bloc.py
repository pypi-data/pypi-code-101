from analytics_command_center.modules.process_exec_raw_file.process_exec_raw_file_provider import ProcessExecRawFileProvider
from analytics_command_center.common.huemul_response_bloc import HuemulResponseBloc

class ProcessExecRawFileBloc:
    #
    # start processExecRawFileGetInfo
    # @param ProcessExecRawFileSendModel ProcessExecRawFileSendModel
    # @return HuemulResponseBloc[ProcessExecRawFileSendModel]
    #
    def processExecRawFileGetInfo(self, ProcessExecRawFileSendModel):
        continueInLoop = True
        attempt = 0
        result = HuemulResponseBloc()

        while (continueInLoop):
            result = ProcessExecRawFileProvider().processExecRawFileGetInfo(
                    ProcessExecRawFileSendModel=ProcessExecRawFileSendModel
            )
            attempt +=1
            continueInLoop = result.analyzeErrors(attempt)
        
        return result