#
# processId: String,
# processExecId: String,
# processExecStepId: String
# processExecResultId: string
# orgId: String
# processExecResultName: String,
# processExecResultType: String,
# processExecResultValueText: String,
# processExecResultValueNumber: BigDecimal,
# processExecResultValueDate: String
#
class ProcessExecResultModel:
    def __init__(self, **args):
        self.processId = args["processId"] if "processId" in args else ""
        self.processExecId = args["processExecId"] if "processExecId" in args else ""
        self.processExecStepId = args["processExecStepId"] if "processExecStepId" in args else ""
        self.processExecResultId = args["processExecResultId"] if "processExecResultId" in args else ""
        self.orgId = args["orgId"] if "orgId" in args else ""
        self.processExecResultName = args["processExecResultName"] if "processExecResultName" in args else ""
        self.processExecResultType = args["processExecResultType"] if "processExecResultType" in args else ""
        self.processExecResultValueText = args["processExecResultValueText"] if "processExecResultValueText" in args else ""
        self.processExecResultValueNumber = args["processExecResultValueNumber"] if "processExecResultValueNumber" in args else 0
        self.processExecResultValueDate = args["processExecResultValueDate"] if "processExecResultValueDate" in args else ""
        self.args = args