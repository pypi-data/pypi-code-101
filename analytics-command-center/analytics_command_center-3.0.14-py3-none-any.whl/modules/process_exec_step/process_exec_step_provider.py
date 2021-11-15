from analytics_command_center.common.huemul_response_bloc import HuemulResponseBloc
from analytics_command_center.common.huemul_response_error import HuemulResponseError
from analytics_command_center.common.huemul_connection import HuemulConnection
from analytics_command_center.common.huemul_functions import huemulFunctions
from analytics_command_center.modules.process_exec_step.process_exec_step_response_model import ProcessExecStepResponseModel
import json

class ProcessExecStepProvider(HuemulResponseBloc):
    
    #
    # processExecStepCreate
    # @param processExecStepModel processExecStepModel
    # @return HuemulResponseBloc[ProcessExecResponseModel]
    #
    def processExecStepCreate(self, processExecStepModel):
        #self = HuemulResponseBloc()
        try:
            huemulFunctions.deleteArgs(processExecStepModel)
            dataIn = json.dumps(processExecStepModel, default=lambda obj: obj.__dict__)

            huemulResponse = HuemulConnection().postRequest(
                route = "processesExecStep/v1/newStep/",
                data = dataIn,
            )

            #get status from connection
            self.fromResponseProvider(huemulResponseProvider = huemulResponse)
            if (self.isSuccessful):
                self.data = [] if len(huemulResponse.dataRaw) == 0 else list(map(lambda x: ProcessExecStepResponseModel(**x) ,huemulResponse.dataRaw))
        except Exception as e:
            self.errors.append(
                HuemulResponseError(errorId = "APP-101", errorTxt = str(e))
            )

        return self


        