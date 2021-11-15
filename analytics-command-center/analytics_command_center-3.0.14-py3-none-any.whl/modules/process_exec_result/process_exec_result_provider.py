from analytics_command_center.common.huemul_response_bloc import HuemulResponseBloc
from analytics_command_center.common.huemul_response_error import HuemulResponseError
from analytics_command_center.common.huemul_connection import HuemulConnection
from analytics_command_center.common.huemul_functions import huemulFunctions
from analytics_command_center.modules.process_exec_result.process_exec_result_model import ProcessExecResultModel
import json

class ProcessExecResultProvider(HuemulResponseBloc):
    
    #
    # processExecResultCreate
    # @param processExecResultModel processExecResultModel
    # @return HuemulResponseBloc[ProcessExecResponseModel]
    #
    def processExecResultCreate(self, processExecResultModel):
        #self = HuemulResponseBloc()
        try:
            huemulFunctions.deleteArgs(processExecResultModel)
            dataIn = json.dumps(processExecResultModel, default=lambda obj: obj.__dict__)

            huemulResponse = HuemulConnection().postRequest(
                route = "processesExecResult/v1/",
                data = dataIn,
            )

            #get status from connection
            self.fromResponseProvider(huemulResponseProvider = huemulResponse)
            if (self.isSuccessful):
                self.data = [] if len(huemulResponse.dataRaw) == 0 else list(map(lambda x: ProcessExecResultModel(**x) ,huemulResponse.dataRaw))
        except Exception as e:
            self.errors.append(
                HuemulResponseError(errorId = "APP-101", errorTxt = str(e))
            )

        return self


        