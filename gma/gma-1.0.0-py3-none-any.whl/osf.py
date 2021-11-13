# -*- coding: utf-8 -*-
"""
一些通用的处理包!
=====

Update date: 2021.5.5

"""

from datetime import datetime, timedelta
import os
import zipfile
import glob

def GetPath(Path, Search = 'FILE', EXT = None, String = None):

    '''
    简介
    ----------
    获取目标 【路径或路径集合】 下满足条件的所有 【文件夹和文件路径】。

    参数
    ----------
    Path: str 或 list。路径或路径集合。可以是：

        1.路径（str）。 例：'C:/SP'。

        2.路径集合（list）。 例： ['C:/SD', 'C:/SP']

    **可选参数
    ----------

    Search = 'FILE' 或其他类型。要查找路径的类型，默认为查找文件（'FILE'）。

        其他类型包括'DIR'(文件夹)，'ALL'(文件夹和文件)。如果设置的值不为以上所有类型，则认为是 'FILE' 。

    EXT = None 或 str、list。查找文件的扩展名或扩展名列表。只有在 SearchPath = 'FILE' 时, 此参数才生效。默认查找所有文件（None）。

    String = None 或 str、list。查找的文件路径中包含的 字符串 。

    返回
    ----------
    类型：list。满足条件的所有 【文件夹和文件路径】集合。重复的路径只会保留一个。

    '''

    # 格式化输入目录
    if isinstance(Path, str):
        Path = [Path]
    elif isinstance(Path, list) is False:
        return []

    # 格式化通配符
    if Search == 'DIR':
        Wildcard =  '/**/'
    elif Search == 'ALL':
        Wildcard =  '/**/*'
    else:
        if EXT is None:
            Wildcard =  '/**/*.*'
        elif isinstance(EXT, list):
            Wildcard = ['/**/*' + E for E in EXT]
        else:
            Wildcard = '/**/*' + EXT

    # 通配所有路径
    if isinstance(Wildcard, list):
        SPath = sum([glob.glob(P + W, recursive = True) for P in Path for W in Wildcard if os.path.exists(P)], [])
    else:
        SPath = sum([glob.glob(P + Wildcard, recursive = True) for P in Path if os.path.exists(P)], [])

    # 提取含设定字符串的路径
    if String is not None:
        if isinstance(String, str):
            String = [String]
        SPath = [P for P in SPath for S in String if S in os.path.basename(P)]

    return SPath

def Zip(Path, ZipFilePath, Mode = 'w'):
    '''
    简介
    ----------
    将【目标路径】下所有文件【压缩】为'.zip'格式。

    参数
    ----------
    Path: str。压缩目标路径。

    ZipFilePath: str。压缩结果文件路径。扩展名为'.zip'。

    **可选参数
    ----------
    Mode = 'w' 或 'a' 。压缩文件处理方法。

        'w': 如果目标'.zip'存在，则目标文件将会被替换。

        'a': 如果目标'.zip'存在，则目标文件内容会被更新。

    '''
    items = GetPath(Path, Search = 'ALL')
    new_zip = zipfile.ZipFile(ZipFilePath, Mode, zipfile.ZIP_DEFLATED)

    if os.path.isdir(Path):
        new_zip.write(Path, Path.replace(os.path.dirname(Path), ''))

    for item in items:
        new_zip.write(item, item.replace(os.path.dirname(Path), ''))

def UnZip(ZipFilePath, OutPath):
    '''
    简介
    ----------
    【解压缩】.zip文件。

    参数
    ----------
    ZipFilePath: str。需要解压缩的'.zip'文件路径。

    OutPath: str。解压后存储文件的路径。

    '''
    zip_fn = zipfile.ZipFile(ZipFilePath, "r")
    namelist = zip_fn.namelist()
    for item in namelist:
        zip_fn.extract(item, OutPath)

def DateSeries(StartDate, EndDate, DateDelta, Format = '%Y%m%d'):
    '''
    简介
    ----------
    创建一个【日期序列】列表。

    参数
    ----------
    StartDate: str。初始日期。例如'20200101'。

    EndDate: str。结束日期。例如'20201231'。

    DateDelta: int。间隔日期(天)。

    **可选参数
    ----------
    Format = '%Y%m%d'。日期序列格式。默认为 %Y%m%d'（年月日）。

    '''

    STDate = datetime.strptime(StartDate, Format)
    ENDate = datetime.strptime(EndDate, Format)

    DLTDay = (ENDate - STDate).days
    ResultList = []
    for i in range(0, DLTDay + 1, DateDelta):

        TMPDay = STDate + timedelta(days = i)
        TMPDayStr = TMPDay.strftime(Format)
        ResultList.append(TMPDayStr)

    return ResultList

class Rename:
    '''
    类简介
    ----------
    【重命名】文件或文件夹。

    初始化
    ----------
    FilePath: str。要重命名的文件或文件夹路径。

    '''
    def __init__(self, FilePath):

        self.FilePath = FilePath
        self.DIRPath = os.path.dirname(FilePath)
        self.FileName = os.path.basename(FilePath)

    def Modify(self, NewName):
        '''
        简介
        ----------
        将原文件或文件夹名【修改】为 NewName。

        参数
        ----------
        NewName: str。新文件或文件夹名。

        '''

        New = os.path.join(self.DIRPath, NewName)
        os.renames(self.FilePath, New)

    def Replace(self, OldString, NewString):
        '''
        简介
        ----------
        将原文件或文件夹名中的 OldString【替换】为 NewString 后作为新文件或文件夹名。

        参数
        ----------
        OldString: str。需要替换的字符串。

        NewString: str。替换后的新字符串。

        '''

        New = os.path.join(self.DIRPath, self.FileName.replace(OldString, NewString))
        os.renames(self.FilePath, New)

    def Intercept(self, Start, Length):
        '''
        简介
        ----------
        从原文件或文件夹名中第 Start 个字符开始【截取】 Length 个字符作为新文件或文件夹名。

            注：此方法自动忽略扩展名。即：不论 Start, Length设置为多少，扩展名都将被保留。

        参数
        ----------
        Start: int。截取字符串的位置。

        Length: int。截取字符串的长度。

        '''
        if os.path.isfile(self.FilePath):
            PureName = os.path.splitext(self.FileName)[0]
            EXT = os.path.splitext(self.FileName)[1]
            if EXT == '':
                return print('<%s>文件名为空！' % self.FilePath)
        else:
            PureName = self.FileName
            EXT = ''

        New = os.path.join(self.DIRPath, PureName[Start: Start + Length] + EXT)
        os.renames(self.FilePath, New)
