from analytics_command_center.common.huemul_common import huemulCommon
from analytics_command_center.common.huemul_logging import huemulLogging

 # errorTrace, 
 # errorClassName, 
 # errorFileName, 
 # errorLineNumber, 
 # errorMethodName, 
 # errorMessage, 
 # errorIsError, 
 # errorCode
class HuemulError:
    def __init__(self, **args):
        self.errorId = ""
        self.orgId = huemulCommon.getOrgId()
        self.errorDetail = ""
        self.errorWhoIs = ""
        self.errorWhoCode = ""

        if (len(args) == 0):
            #val Invoker: Array[StackTraceElement] = new Exception().getStackTrace
            self.errorIsError = False
            self.errorCode = ""
            self.errorTrace = ""
            self.errorClassName = ""
            self.errorFileName = "" # Invoker(3).getFileName //todo: obtener dinamicamente a partir de los nombres de las clases (descartando)
            self.errorLineNumber = "" #Invoker(3).getLineNumber
            self.errorMethodName = ""
            self.errorMessage = ""
        elif (len(args) == 4):
            #val Invoker: Array[StackTraceElement] = new Exception().getStackTrace
            self.errorIsError = True
            self.errorCode = args["code"]
            self.errorTrace = ""
            self.errorClassName = args["getClassName"]
            self.errorFileName = "" # Invoker(3).getFileName //todo: obtener dinamicamente a partir de los nombres de las clases (descartando)
            self.errorLineNumber = "" #Invoker(3).getLineNumber
            self.errorMethodName = args["getMethodName"]
            self.errorMessage = args["message"]

            self.printError(self.errorMessage)
        elif len(args) > 4:
            self.errorTrace = args["errorTrace"]
            self.errorClassName = args["errorClassName"]
            self.errorFileName = args["errorFileName"]
            self.errorLineNumber = args["errorLineNumber"]
            self.errorMethodName = args["errorMethodName"]
            self.errorMessage = args["errorMessage"]
            self.errorIsError = args["errorIsError"]
            self.errorCode = args["errorCode"]


    # return boolean
    def isOK(self):
        return not (self.errorIsError)

    
    def printError(self, error):
        huemulLogging.logMessageError("***************************************************************")
        huemulLogging.logMessageError("HuemulLauncher: Error Detail")
        huemulLogging.logMessageError("***************************************************************")
        huemulLogging.logMessageError("error_ClassName: " + self.errorClassName)
        huemulLogging.logMessageError("error_FileName: " + self.errorFileName)
        huemulLogging.logMessageError("error_ErrorCode: " + self.errorCode)
        huemulLogging.logMessageError("error_LineNumber: " + self.errorLineNumber)
        huemulLogging.logMessageError("error_MethodName: " + self.errorMethodName)
        huemulLogging.logMessageError("error_Message: " + self.errorMessage)
        huemulLogging.logMessageError("error_Trace: " + self.errorTrace)

        huemulLogging.logMessageError("Detail")
        huemulLogging.logMessageError(error)

