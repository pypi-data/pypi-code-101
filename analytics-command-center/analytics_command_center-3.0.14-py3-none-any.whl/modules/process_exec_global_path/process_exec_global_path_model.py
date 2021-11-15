#
# processId: String,
# processExecId: String,
# processExecStepId: String
# processExecGlobalPathId: string
# orgId: String
# globalPathId: globalPathId
# globalPathCode: globalPathCode
# globalPathRoute: globalPathRoute
# globalPathName: globalPathName
#
class ProcessExecGlobalPathModel:
    def __init__(self, processId, processExecId, processExecStepId, processExecGlobalPathId, orgId, globalPathId, globalPathCode, globalPathRoute, globalPathName, **args):
        self.processId = processId
        self.processExecId = processExecId
        self.processExecStepId = processExecStepId
        self.processExecGlobalPathId = processExecGlobalPathId
        self.orgId = orgId
        self.globalPathId = globalPathId
        self.globalPathCode = globalPathCode
        self.globalPathRoute = globalPathRoute
        self.globalPathName = globalPathName
        self.args = args