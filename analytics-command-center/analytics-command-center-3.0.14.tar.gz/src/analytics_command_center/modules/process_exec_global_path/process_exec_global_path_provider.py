from analytics_command_center.common.huemul_response_bloc import HuemulResponseBloc
from analytics_command_center.common.huemul_response_error import HuemulResponseError
from analytics_command_center.common.huemul_connection import HuemulConnection
from analytics_command_center.common.huemul_functions import huemulFunctions
from analytics_command_center.modules.process_exec_global_path.process_exec_global_path_model import ProcessExecGlobalPathModel
import json

class ProcessExecGlobalPathProvider(HuemulResponseBloc):
    
    #
    # processExecGlobalPathCreate
    # @param processExecGlobalPathModel processExecGlobalPathModel
    # @return HuemulResponseBloc[ProcessExecResponseModel]
    #
    def processExecGlobalPathCreate(self, processExecGlobalPathModel):
        #self = HuemulResponseBloc()
        try:
            huemulFunctions.deleteArgs(processExecGlobalPathModel)
            dataIn = json.dumps(processExecGlobalPathModel, default=lambda obj: obj.__dict__)

            huemulResponse = HuemulConnection().postRequest(
                route = "processesExecGlobalPath/v1/",
                data = dataIn,
            )

            #get status from connection
            self.fromResponseProvider(huemulResponseProvider = huemulResponse)
            if (self.isSuccessful):
                self.data = [] if len(huemulResponse.dataRaw) == 0 else list(map(lambda x: ProcessExecGlobalPathModel(**x) ,huemulResponse.dataRaw))
        except Exception as e:
            self.errors.append(
                HuemulResponseError(errorId = "APP-101", errorTxt = str(e))
            )

        return self


        