from analytics_command_center.common.huemul_response_bloc import HuemulResponseBloc
from analytics_command_center.common.huemul_response_error import HuemulResponseError
from analytics_command_center.common.huemul_connection import HuemulConnection
from analytics_command_center.common.huemul_functions import huemulFunctions
from analytics_command_center.modules.process_exec.process_exec_response_model import ProcessExecResponseModel
import json

class ProcessExecProvider(HuemulResponseBloc):
    
    #
    # processExecStartExecution
    # @param processExecModel ProcessExecModel
    # @return HuemulResponseBloc[ProcessExecResponseModel]
    #
    def processExecStartExecute(self, processExecStartModel):
        #self = HuemulResponseBloc()
        try:
            huemulFunctions.deleteArgs(processExecStartModel)
            dataIn = json.dumps(processExecStartModel, default=lambda obj: obj.__dict__)

            huemulResponse = HuemulConnection().postRequest(
                route = "processesExec/v1/startExecution/",
                data = dataIn,
            )

            #get status from connection
            self.fromResponseProvider(huemulResponseProvider = huemulResponse)
            if (self.isSuccessful):
                self.data = [] if len(huemulResponse.dataRaw) == 0 else list(map(lambda x: ProcessExecResponseModel(**x) ,huemulResponse.dataRaw))
        except Exception as e:
            self.errors.append(
                HuemulResponseError(errorId = "APP-101", errorTxt = str(e))
            )

        return self

    #
    # processExecStopExecution
    # @param processExecStopModel processExecStopModel
    # @return HuemulResponseBloc[ProcessExecResponseModel]
    #
    def processExecStopExecute(self, processExecStopModel):
        #self = HuemulResponseBloc()
        try:
            huemulFunctions.deleteArgs(processExecStopModel)
            dataIn = json.dumps(processExecStopModel, default=lambda obj: obj.__dict__)

            huemulResponse = HuemulConnection().postRequest(
                route = "processesExec/v1/closeExecution/",
                data = dataIn,
            )

            #get status from connection
            self.fromResponseProvider(huemulResponseProvider = huemulResponse)
            if (self.isSuccessful):
                self.data = [] if len(huemulResponse.dataRaw) == 0 else list(map(lambda x: ProcessExecResponseModel(**x) ,huemulResponse.dataRaw))
        except Exception as e:
            self.errors.append(
                HuemulResponseError(errorId = "APP-101", errorTxt = str(e))
            )

        return self


        