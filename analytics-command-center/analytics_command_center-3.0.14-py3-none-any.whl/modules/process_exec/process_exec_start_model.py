# param processExecId: String,
# param processExecIdParent: String,
# param schedulerId: String,
# param operatorId: String,
# param processId: String,
# param processName: String,
# param applicationId: String,
# param processExecParamYear: Int,
# param processExecParamMonth: Int,
# param processExecParamDay: Int,
# param processExecParamHour: Int,
# param processExecParamMin: Int,
# param processExecParamSec: Int,
# param processExecHuemulVersion: String,
# param processExecDebugMode: Boolean,
# param processExecAnnotations: String,
# param processExecParamOthers: Array[ProcessExecParamModel]
class ProcessExecStartModel:
    def __init__(self, processExecId, processExecIdParent, schedulerId, operatorId, processId, processName, applicationId, processExecParamYear, processExecParamMonth, processExecParamDay, processExecParamHour, processExecParamMin, processExecParamSec, processExecHuemulVersion, processExecDebugMode, processExecAnnotations, processExecParamOthers):
        self.processExecId = processExecId
        self.processExecIdParent = processExecIdParent
        self.schedulerId = schedulerId
        self.operatorId = operatorId
        self.processId = processId
        self.processName = processName
        self.applicationId = applicationId
        self.processExecParamYear = processExecParamYear
        self.processExecParamMonth = processExecParamMonth
        self.processExecParamDay = processExecParamDay
        self.processExecParamHour = processExecParamHour
        self.processExecParamMin = processExecParamMin
        self.processExecParamSec = processExecParamSec
        self.processExecHuemulVersion = processExecHuemulVersion
        self.processExecDebugMode = processExecDebugMode
        self.processExecAnnotations = processExecAnnotations
        self.processExecParamOthers = processExecParamOthers
        
        