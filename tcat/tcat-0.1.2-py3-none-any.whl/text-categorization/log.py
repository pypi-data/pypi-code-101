import os
import sys

def appendLog(messagge, name):
    createLogsFolderIfNotExist()
    logFile = open(f"{sys.path[0]}/logs/{name}", "a")
    logFile.write(str(messagge))
    logFile.close

def printAndLog(message, name):
    print(message)
    appendLog(message, name)

def createLogsFolderIfNotExist():
    if checkLogsFolder() == False:
        os.mkdir(f"{sys.path[0]}/logs")

def checkLogsFolder():
    return os.path.isdir(f"{sys.path[0]}/logs")