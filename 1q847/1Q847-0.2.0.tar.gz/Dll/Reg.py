import ctypes, os
from comtypes.client import CreateObject
path = os.path.split(os.path.realpath(__file__))[0]

class RegDm:

    @classmethod
    def reg(cls):
        path = os.path.split(os.path.realpath(__file__))[0]
        reg_dm = ctypes.windll.LoadLibrary(path + '\DmReg.dll')
        reg_dm.SetDllPathW(path + '\dm.dll', 0)
        return CreateObject('dm.dmsoft')


    @classmethod
    def CreateDm(cls):
        dm = CreateObject('dm.dmsoft')
        return dm




# 这里只能用 comtypes 不能用win32com来调用.不然会报错,研究了贼久才搞明白!并且必须是32位的python
def regLW():
    '''
    注册乐玩插件,需要把文件lw.dll放在根目录
    :return: 返回乐玩对象
    '''
    try:
        lw = CreateObject("lw.lwsoft3")
    except:
        os.system('regsvr32 '+ path +'\lw.dll')
        lw = CreateObject("lw.lwsoft3")
    return lw


def unRegLW():
    '''
    从系统中卸载乐玩插件,有些时候注册不成功,可以先卸载一下
    :return:
    '''
    os.system('regsvr32 lw.dll /u')





if __name__ == '__main__':
    # dm = RegDm.reg()
    # print(dm.ver())
    lw=unRegLW()
    print(lw.ver())
