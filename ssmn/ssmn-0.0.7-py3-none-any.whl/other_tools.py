import win32com.client
import os
import random

def makeoddnumber(len): #홀수 만들기
    all = "" #str
    first = random.randint(1, 9) #int
    first2 = str(first) #str
    all += first2 #가장 첫번째 숫자


    len2 = len - 2 #int 길이
    last1 = random.randint(1, 5) #int
    last2 = last1 * 2 - 1#int
    last3 = str(last2) #str 가장 마지막 숫자.


    t = 0 #int
    while len2 != t:
        a = random.randint(0, 9) #int
        a2 = str(a) #str
        all += a2 #str
        t = t - 1 #int

    all += last3 #str

    return all


def reverse(strdata1): #문자열 뒤집기
    reverse_1 = strdata1[::-1]

    return reverse_1

def AddStartUpProgram(TheNameOfTheLink, PathToTheProgram):
    # 프로그램을 시작프로그램에 등록하는 코드다.

    def plus():
        # pythoncom.CoInitialize() # remove the '#' at the beginning of the line if running in a thread.
        desktop = r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp'  # path to where you want to put the .lnk
        path = os.path.join(desktop, '{0}.lnk'.format(TheNameOfTheLink))
        target = r'{0}'.format(PathToTheProgram)

        shell = win32com.client.Dispatch("WScript.Shell")
        shortcut = shell.CreateShortCut(path)
        shortcut.Targetpath = target
        shortcut.WindowStyle = 7  # 7 - Minimized, 3 - Maximized, 1 - Normal
        shortcut.save()

    plus()

def MakeProgramShortcut(PathToLink, TheNameOfTheLink, PathToTheProgram):
    # 프로그램 바로가기를 만드는 코드다.
    def plus():
        # pythoncom.CoInitialize() # remove the '#' at the beginning of the line if running in a thread.
        desktop = r'{0}'.format(PathToLink)  #링크파일을 위치할 경로
        path = os.path.join(desktop, '{0}.lnk'.format(TheNameOfTheLink))
        target = r'{0}'.format(PathToTheProgram)

        shell = win32com.client.Dispatch("WScript.Shell")
        shortcut = shell.CreateShortCut(path)
        shortcut.Targetpath = target
        shortcut.WindowStyle = 7  # 7 - Minimized, 3 - Maximized, 1 - Normal
        shortcut.save()

    plus()

def AddApp(ProgramName, ProgramPath):
    # 윈도우 앱에 자신의 프로그램을 추가하는 코드다.
    def plus():
        # pythoncom.CoInitialize() # remove the '#' at the beginning of the line if running in a thread.
        desktop = r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs'  #링크파일을 위치할 경로
        path = os.path.join(desktop, '{0}.lnk'.format(ProgramName)) #링크파일의 이름
        target = r'{0}'.format(ProgramPath) #프로그램 경로

        shell = win32com.client.Dispatch("WScript.Shell")
        shortcut = shell.CreateShortCut(path)
        shortcut.Targetpath = target
        shortcut.WindowStyle = 7  # 7 - Minimized, 3 - Maximized, 1 - Normal
        shortcut.save()

    plus()

