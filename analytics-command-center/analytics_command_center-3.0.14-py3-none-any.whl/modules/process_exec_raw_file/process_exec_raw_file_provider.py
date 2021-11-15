from analytics_command_center.common.huemul_response_bloc import HuemulResponseBloc
from analytics_command_center.common.huemul_response_error import HuemulResponseError
from analytics_command_center.common.huemul_connection import HuemulConnection
from analytics_command_center.common.huemul_functions import huemulFunctions
from analytics_command_center.modules.process_exec_raw_file.process_exec_raw_file_model import ProcessExecRawFileModel
import json

class ProcessExecRawFileProvider(HuemulResponseBloc):
    
    #
    # processExecRawFileGetInfo
    # @param ProcessExecRawFileSendModel ProcessExecRawFileSendModel
    # @return HuemulResponseBloc[ProcessExecResponseModel]
    #
    def processExecRawFileGetInfo(self, ProcessExecRawFileSendModel):
        #self = HuemulResponseBloc()
        try:
            huemulFunctions.deleteArgs(ProcessExecRawFileSendModel)
            dataIn = json.dumps(ProcessExecRawFileSendModel, default=lambda obj: obj.__dict__)

            huemulResponse = HuemulConnection().putRequest(
                route = "processesExecRawFile/v1/getRawFileInfo/",
                data = dataIn,
            )

            #get status from connection
            self.fromResponseProvider(huemulResponseProvider = huemulResponse)
            if (self.isSuccessful):
                self.data = [] if len(huemulResponse.dataRaw) == 0 else list(map(lambda x: ProcessExecRawFileModel(**x) ,huemulResponse.dataRaw))
        except Exception as e:
            self.errors.append(
                HuemulResponseError(errorId = "APP-101", errorTxt = str(e))
            )

        return self


        