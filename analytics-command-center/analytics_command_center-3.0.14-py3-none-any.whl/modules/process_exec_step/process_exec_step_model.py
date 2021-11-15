#
# processId: String,
# processExecId: String,
# processExecStepId: String
#
class ProcessExecStepModel:
    def __init__(self, processId, processExecId, processExecStepId, processExecStepName, processExecStepIdPrevious, processExecErrorId):
        self.processId = processId
        self.processExecId = processExecId
        self.processExecStepId = processExecStepId
        self.processExecStepName = processExecStepName
        self.processExecStepIdPrevious = processExecStepIdPrevious
        self.processExecErrorId = processExecErrorId