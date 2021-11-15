#
# processId: String,
# processExecId: String,
# processExecStepId: String
#
class ProcessExecStepResponseModel:
    def __init__(self, processId, processExecId, processExecStepId, **args):
        self.processId = processId
        self.processExecId = processExecId
        self.processExecStepId = processExecStepId
        self.args = args