class ProcessExecResponseModel:
    def __init__(self, **args):
        self.processId = args["processId"] if "processId" in args else ""
        self.processExecId = args["processExecId"] if "processExecId" in args else ""
        self.processExecStepId = args["processExecStepId"] if "processExecStepId" in args else ""
        self.status = args["status"] if "status" in args else ""
        self.message = args["message"] if "message" in args else ""
        self.args = args