from analytics_command_center.common.huemul_functions import HuemulFunctions
from analytics_command_center.modules.process_exec_result.process_exec_result_bloc import ProcessExecResultBloc
from analytics_command_center.modules.process_exec_result.process_exec_result_model import ProcessExecResultModel
from analytics_command_center.modules.process_exec_global_path.process_exec_global_path_bloc import ProcessExecGlobalPathBloc
from analytics_command_center.modules.process_exec_global_path.process_exec_global_path_model import ProcessExecGlobalPathModel
from analytics_command_center.modules.process_exec_step.process_exec_step_bloc import ProcessExecStepBloc
from analytics_command_center.modules.process_exec_step.process_exec_step_model import ProcessExecStepModel
from analytics_command_center.modules.process_exec_raw_file.process_exec_raw_file_send_model import ProcessExecRawFileSendModel
from analytics_command_center.modules.process_exec_raw_file.process_exec_raw_file_bloc import ProcessExecRawFileBloc
from analytics_command_center.modules.process_exec.process_exec_bloc import ProcessExecBloc
from analytics_command_center.common.huemul_error import HuemulError
from analytics_command_center.common.huemul_logging import huemulLogging
from analytics_command_center.common.huemul_common import huemulCommon
from analytics_command_center.auth.auth_service_bloc import AuthServiceBloc
from analytics_command_center.auth.auth_model import AuthModel
from analytics_command_center.modules.process_exec.process_exec_start_model import ProcessExecStartModel
from analytics_command_center.modules.process_exec.process_exec_stop_model import ProcessExecStopModel
from analytics_command_center.modules.process_exec_param.process_exec_param_model import ProcessExecParamModel
from datetime import datetime

# processId: String,
# processName: String,
# processTechDescription: String,
# runFrequency: HuemulTypeFrequency = manual,
# parent: HuemulLauncher = null,
# yearParam: Int = 0,
# monthParam: Int = 0,
# dayParam: Int = 0,
# hourParam: Int = 0,
# minuteParam: Int = 0,
# secondParam: Int = 0,
# othersParams: Array[HuemulParam] = Array[HuemulParam](),
# authData: AuthModel
class Launcher:
    def __init__(self, processId, processName, processTechDescription, authData, yearParam, monthParam, dayParam, hourParam=0,minuteParam=0, secondParam=0, othersParams="", runFrequency = "", parent = None):
        self.processId = processId
        self.processName = processName
        self.processTechDescription = processTechDescription
        self.runFrequency = runFrequency
        self.parent = parent
        self.yearParam = yearParam
        self.monthParam = monthParam
        self.dayParam = dayParam
        self.hourParam = hourParam
        self.minuteParam = minuteParam
        self.secondParam = secondParam
        self.authData = authData

        self._canExecute = False
        self._isOpen = True
        self._processExecId = ""
        self._processExecStepId = ""
        self._errorMessage = ""
        self.othersParams = []

        self.processExecIdParent = None if (parent == None) else parent.processExecId
        self.controlClassName = "" #: String = Invoker(1).getClassName.replace("$", "")
        self.controlMethodName = "" #: String = Invoker(1).getMethodName.replace("$", "")
        #val controlFileName: String = Invoker(1).getFileName.replace("$", "")
        self.controlError = HuemulError()
        #self._processExecModel = ""

        #### START

        huemulLogging.logMessageInfo(message = "WELCOME to the Huemul Analytics Command Center...")
        huemulLogging.logMessageInfo(message = processId)
        #login
        huemulLogging.logMessageInfo(message = "calling Ground Control for launch authorization...")
        authInfoResponse = AuthServiceBloc().authSignInService(authData)

        if (not authInfoResponse.isSuccessful):
            self._canExecute = False
            self._errorMessage = authInfoResponse.message if (authInfoResponse.errors.len == 0) else authInfoResponse.errors[0].errorTxt
            huemulLogging.logMessageError(message = "error: " + self._errorMessage)
            return

        huemulLogging.logMessageInfo(message = "authorized...")

        #store credentials and token
        huemulCommon.setOrgId(authData.orgId)
        huemulCommon.setConsumerId(authData.consumerId)
        huemulCommon.setConsumerSecret(authData.consumerSecret)
        huemulCommon.setApplicationName(authData.applicationName)
        huemulCommon.setTokenId(authInfoResponse.data[0].tokenId)

        #create processExec
        huemulLogging.logMessageInfo(message = "starting process launch in 3..2..1..")
        self._processExecModel = ProcessExecStartModel(
            processExecId = "",
            processExecIdParent = self.processExecIdParent,
            schedulerId = "",
            operatorId = "",
            processId = processId,
            processName = processName,
            applicationId = "",
            processExecParamYear = yearParam,
            processExecParamMonth = monthParam,
            processExecParamDay = dayParam,
            processExecParamHour = hourParam,
            processExecParamMin = minuteParam,
            processExecParamSec = secondParam,
            processExecHuemulVersion = "",
            processExecDebugMode = False,
            processExecAnnotations = processTechDescription,
            processExecParamOthers = list(map(lambda x: ProcessExecParamModel(
                processExecParamName = x.name,
                processExecParamValue = str(x.value)
                ), othersParams))
        )

        #create
        processExecResult = ProcessExecBloc().processExecStartExecute(self._processExecModel)
        if (not processExecResult.isSuccessful):
            self._canExecute = False
            self._errorMessage = processExecResult.message if (len(processExecResult.errors) == 0) else processExecResult.errors[0].errorTxt
            huemulLogging.logMessageError(message = "error: " + self._errorMessage)

            return
        elif (processExecResult.data[0].status == "reprocessCheckError"):
            self._canExecute = False
            self._errorMessage = processExecResult.data[0].message
            huemulLogging.logMessageError(message = "error process was executed: " + self._errorMessage)

            return
        elif (processExecResult.data[0].status != "OK"):
            self._canExecute = False
            self._errorMessage = processExecResult.data[0].message
            huemulLogging.logMessageError(message = "error returned by Ground Control, cannot continue: " + self._errorMessage)

            return
        
        self._canExecute = True
        self._processExecId = processExecResult.data[0].processExecId
        self._processExecStepId = processExecResult.data[0].processExecStepId
        huemulLogging.logMessageInfo(message = "process " + processId + " STARTED!!!")

        ### END START
        
    def isOpen(self):
        return self._isOpen

    #
    # return processExecId
    # @return
    #
    def processExecId(self):
        return self._processExecId

    #
    # return processExecStepId
    # @return
    #
    def getProcessExecStepId(self):
        return self._processExecStepId

    #/************************************************************************************/
    #/******************  R E S U L T S    ***********************************************/
    #/************************************************************************************

    #
    # add new Text result
    # @param resultName result name
    # @param resultValue result value (text)
    #
    def addResult(self, resultName, resultValue="", year = 0, month = 0, day = 0, hour = 0, minute = 0, second = 0):
        if (not self.canExecute()):
            return

        _result = None
        if (year > 1900):
            paramDate = datetime(year, month, day, hour, minute, second)
            _result = ProcessExecResultModel(
                processExecResultId = "",
                processExecResultName = resultName,
                processExecResultType = "DATE",
                processExecResultValueText = "",
                processExecResultValueNumber = 0,
                processExecResultValueDate = HuemulFunctions().getDateForLog(paramDate),
                processExecStepId = self.getProcessExecStepId(),
                processId = self.processId,
                processExecId = self.processExecId(),
                orgId = huemulCommon.getOrgId(),
            )
        elif (type(resultValue) is int or type(resultValue) is float):
            _result = ProcessExecResultModel(
                processExecResultId = "",
                processExecResultName = resultName,
                processExecResultType = "NUMBER",
                processExecResultValueText = "",
                processExecResultValueNumber = resultValue,
                processExecResultValueDate = "",
                processExecStepId = self.getProcessExecStepId(),
                processId = self.processId,
                processExecId = self.processExecId(),
                orgId = huemulCommon.getOrgId(),
            )
        else:
            _result = ProcessExecResultModel(
                processExecResultId = "",
                processExecResultName = resultName,
                processExecResultType = "STRING",
                processExecResultValueText = str(resultValue),
                processExecResultValueNumber = 0,
                processExecResultValueDate = "",
                processExecStepId = self.getProcessExecStepId(),
                processId = self.processId,
                processExecId = self.processExecId(),
                orgId = huemulCommon.getOrgId(),
            )


        ProcessExecResultBloc().processExecResultCreate(_result)
    

    #/************************************************************************************/
    #/******************  S T E P S    ***************************************************/
    #/************************************************************************************

    #
    # register new step
    # @param stepName step name
    # @param raiseErrorIfFail default false. true if raise exception on fail
    # @return Boolean
    #
    def newStep(self, stepName, raiseErrorIfFail = False):
        if (not self.canExecute()):
            return

        huemulLogging.logMessageInfo(message = "step: " + stepName)
        _processExecStepModel = ProcessExecStepModel(
            processExecId = self.processExecId(),
            processId= self.processId,
            processExecStepId = "",
            processExecStepName = stepName,
            processExecStepIdPrevious = self.getProcessExecStepId(),
            processExecErrorId = ""
        )

        processExecStepResult = ProcessExecStepBloc().processExecStepCreate(_processExecStepModel)
        #if error
        if (not processExecStepResult.isSuccessful):
            self._canExecute = False
            self._errorMessage = processExecStepResult.message if (len(processExecStepResult.errors) == 0) else processExecStepResult.errors[0].errorTxt
            huemulLogging.logMessageError(message = "error in step: " + self._errorMessage)

            if (raiseErrorIfFail):
                raise NameError(self._errorMessage)
            else:
                print(self._errorMessage)
                return False

        #if all ok, continue
        self._processExecStepId = processExecStepResult.data[0].processExecStepId

        return True
    


    #/************************************************************************************/
    #/******************  R A W   F I L E S    *******************************************/
    #/************************************************************************************

    #get Raw File Info and Columns
    # rawFileCode: String, 
    # year: Int, 
    # month: Int, 
    # day: Int, 
    # hour: Int, 
    # minute: Int, 
    # second: Int, 
    # raiseErrorIfEmpty: Boolean = true
    # return ProcessExecRawFileModel

    def getRawFileInfo(self, rawFileCode, year, month, day, hour, minute, second, raiseErrorIfEmpty = True):
        if (not self.canExecute()):
            return None
        
        huemulLogging.logMessageInfo(message = "get Raw File Info " + rawFileCode)
        _processExecRawFileSendModel = ProcessExecRawFileSendModel(
            processExecStepId = self.getProcessExecStepId(),
            processId = self.processId,
            processExecId = self.processExecId(),
            orgId = huemulCommon.getOrgId(),
            rawFileId = rawFileCode,
            rawFileParamYear = year,
            rawFileParamMonth = month,
            rawFileParamDay = day,
            rawFileParamHour = hour,
            rawFileParamMin = minute,
            rawFileParamSec = second,
            rawFileParamOthers = "",
            rawFileEnvironment = ""
        )

        processExecRawFileResult = ProcessExecRawFileBloc().processExecRawFileGetInfo(_processExecRawFileSendModel)
        #if error
        if (not processExecRawFileResult.isSuccessful):
            self._errorMessage = processExecRawFileResult.message if (processExecRawFileResult.errors.isEmpty) else processExecRawFileResult.errors[0].errorTxt
            huemulLogging.logMessageError(message = "error getting raw file info [" + rawFileCode + "]: " + self._errorMessage)

            if (raiseErrorIfEmpty):
                self.finishError(errorCode="RAWFILE-NOT-FOUND", errorMessage=self._errorMessage)
                raise NameError(self._errorMessage)

            return None

        return processExecRawFileResult.data[0]
    

    #/************************************************************************************/
    #/******************  G L O B A L   P A T H S    *************************************/
    #/************************************************************************************

    # return global path from code
    # globalPathCode code
    # raiseErrorIfEmpty True for raise error if fail
    def getGlobalPath(self, globalPathCode, raiseErrorIfEmpty = True):
        if (not self.canExecute()):
            return ""

        huemulLogging.logMessageInfo(message = "get Global Path " + globalPathCode)
        _processExecGlobalPathModel = ProcessExecGlobalPathModel(
            processExecGlobalPathId = "",
            processExecStepId = self.getProcessExecStepId(),
            globalPathCode = globalPathCode,
            processId = self.processId,
            processExecId = self.processExecId(),
            orgId = huemulCommon.getOrgId(),
            globalPathId = "",
            globalPathName = "",
            globalPathRoute = ""
        )

        processExecGlobalPathResult = ProcessExecGlobalPathBloc().processExecGlobalPathCreate(_processExecGlobalPathModel)
        #if error
        if (not processExecGlobalPathResult.isSuccessful):
            self._errorMessage = processExecGlobalPathResult.message if (len(processExecGlobalPathResult.errors) == 0) else processExecGlobalPathResult.errors[0].errorTxt
            huemulLogging.logMessageError(message = "error getting global path [" + globalPathCode + "]: " + self._errorMessage)

            if (raiseErrorIfEmpty):
                self.finishError(errorCode="GLOBALPATH-NOT-FOUND", errorMessage=self._errorMessage)
                raise NameError(self._errorMessage)

            return ""


        pathToReturn = processExecGlobalPathResult.data[0].globalPathRoute
        if (len(pathToReturn) == 0):
            self._errorMessage = "error: global path [" + globalPathCode + "] not valid, detail: " + self.errorMessage
            huemulLogging.logMessageError(message = self._errorMessage)
            if (raiseErrorIfEmpty):
                self.finishError(errorCode="GLOBALPATH-EMPTY", errorMessage=self._errorMessage)
                raise NameError(self._errorMessage)
            

            return ""

        return pathToReturn

    #/************************************************************************************/
    #/******************  F I N I S H    *************************************************/
    #/************************************************************************************/

    #
    # finish execution successfully
    # @return True if finish 
    #
    def finishOk(self):
        if (not self._isOpen):
            huemulLogging.logMessageError(message = "execution was closed, can't close again")
            return False
        
        self._isOpen = True

        huemulLogging.logMessageInfo(message = "start landing...")
        _processExecStopModel = ProcessExecStopModel(
            processExecId = self.processExecId(),
            processExecStepId = self.getProcessExecStepId(),
            error = HuemulError()
        )

        processExecResult = ProcessExecBloc().processExecStopExecute(processExecStopModel = _processExecStopModel)
        if (not processExecResult.isSuccessful):
            self._canExecute = False
            self._errorMessage = processExecResult.message if (len(processExecResult.errors) == 0) else processExecResult.errors[0].errorTxt
            huemulLogging.logMessageError(message = "error landing: " + self.errorMessage)

            return False
        
        huemulLogging.logMessageInfo(message = "CONGRATULATIONS!. Mission successfully completed ;-)")

        return True


    #
    # finish execution with error
    # @return
    #
    def finishError(self, errorCode, errorMessage):
        if (not self._isOpen):
            huemulLogging.logMessageError(message = "execution was closed, can't close again")
            return False
    
        self._isOpen = False

        huemulLogging.logMessageError(message = "registering failed process...")
        _processExecStopModel = ProcessExecStopModel(
            processExecId = self.processExecId(),
            processExecStepId = self.getProcessExecStepId(),
            error = HuemulError(
                message= errorMessage, 
                getClassName="", #controlClassName, 
                getMethodName="", #controlMethodName, 
                code= str(errorCode))
        )

        processExecResult = ProcessExecBloc().processExecStopExecute(processExecStopModel = _processExecStopModel)
        if (not processExecResult.isSuccessful):
            self._canExecute = False
            self._errorMessage = processExecResult.message if (len(processExecResult.errors) == 0) else processExecResult.errors[0].errorTxt
            huemulLogging.logMessageError(message = "error landing: " + self._errorMessage)

            return False
        
        huemulLogging.logMessageError(message = "WHAT A SAD... Mission FAILED :-(")

        True

    #/************************************************************************************/
    #/******************  U T I L   F U N C T I O N S    *********************************/
    #/************************************************************************************/

    #
    # true for execute, false can't execute
    # @return
    #
    def canExecute(self):
        return self._canExecute

    #
    # return error message
    # @return
    #
    def getErrorMessage(self):
        return self._errorMessage
    
    