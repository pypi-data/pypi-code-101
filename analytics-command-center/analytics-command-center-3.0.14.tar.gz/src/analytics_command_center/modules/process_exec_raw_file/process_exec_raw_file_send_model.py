#
# processId: String,
# processExecId: String,
# processExecStepId: String,
# orgId: String,
# rawFileId: String,
# rawFileParamYear: Int,
# rawFileParamMonth: Int,
# rawFileParamDay: Int,
# rawFileParamHour: Int,
# rawFileParamMin: Int,
# rawFileParamSec: Int,
# rawFileParamOthers: String,
# rawFileEnvironment: String,
#
class ProcessExecRawFileSendModel:
    def __init__(self, **args):
        self.processId = args["processId"] if "processId" in args else ""
        self.processExecId = args["processExecId"] if "processExecId" in args else ""
        self.processExecStepId = args["processExecStepId"] if "processExecStepId" in args else ""
        self.orgId = args["orgId"] if "orgId" in args else ""
        self.args = args
        self.rawFileId = args["rawFileId"] if "rawFileId" in args else ""
        self.rawFileParamYear = args["rawFileParamYear"] if "rawFileParamYear" in args else 0
        self.rawFileParamMonth = args["rawFileParamMonth"] if "rawFileParamMonth" in args else 0
        self.rawFileParamDay = args["rawFileParamDay"] if "rawFileParamDay" in args else 0
        self.rawFileParamHour = args["rawFileParamHour"] if "rawFileParamHour" in args else 0
        self.rawFileParamMin = args["rawFileParamMin"] if "rawFileParamMin" in args else 0
        self.rawFileParamSec = args["rawFileParamSec"] if "rawFileParamSec" in args else 0
        self.rawFileParamOthers = args["rawFileParamOthers"] if "rawFileParamOthers" in args else ""
        self.rawFileEnvironment = args["rawFileEnvironment"] if "rawFileEnvironment" in args else ""