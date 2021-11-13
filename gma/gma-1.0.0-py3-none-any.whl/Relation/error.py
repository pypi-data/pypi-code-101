# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 15:56:45 2021

@author: admin
"""
import os
from gma.Relation import key
from osgeo import osr, gdal

gdal.UseExceptions()

class InTypeError(Exception):
    '''已经定义的输入参数类型错误：

    1、【'字符串', '无符号整型', '整型', '正整数', '实数', '正数', '布尔型'】类型错误；

    2、【'路径'】错误。

    3、【'格式'】错误。

    4、【'方法'】错误。

    5、【'坐标系'】错误。

    6、【'分块'】错误。

    7、【'线程数量'】错误。

    8、【'路径'】错误。

    '''

    def __init__(self, Values, Type = '其他'):
        self.Values = Values
        self.Type = Type

    def __str__(self):

        if self.Type in ['字符串', '无符号整型', '整型', '正整数', '实数', '正数', '布尔型']:
            return '参数 %s 错误，类型必须为 %s ！' % (self.Values, self.Type)
        elif self.Type == '路径':
            return '路径 %s 不存在！' % self.Values
        elif self.Type == '格式':
            return '驱动 %s 错误，不支持的驱动格式！' % self.Values
        elif self.Type == '方法':
            return '重采样方法 %s 错误，不支持的方法！' % self.Values
        elif self.Type == '坐标系':
            return '坐标系 %s 错误，不支持的坐标系！' % self.Values
        elif self.Type == '分块':
            return '分块 %s 错误，不支持的分块！块大小在 64 ~ 4096之间 且为整数！' % self.Values
        elif self.Type == '线程数量':
            return '线程数量 %s 错误！不支持的线程数量设置！线程数量必须为正整数 或 "ALL_CPUS"！' % self.Values
        elif self.Type == '位深':
            return '位深 %s 设置错误！位深设置 ：8位无符号整型：1~7；16位无符号整型：9~15；32位无符号整型：16~31；32位浮点型：16。"！' % self.Values
        elif self.Type == '数据类型':
            return '数据类型 %s 设置错误！数据类型必须为：%s！' % (self.Values, key.DataType)
        else:
            return '未知错误: %s !' % self.Values

class Check:

    def FilePath(Path):
        '''路经检查'''
        if isinstance(Path, str) is False:
            raise InTypeError(Path, '路径')
        elif os.path.exists(Path) is False:
            raise InTypeError(Path, '路径')

    def ValueType(Value, Type):
        '''数据类型检查'''
        if Type == '字符串':
            if isinstance(Value, str) is False:
                raise InTypeError(Value, Type)
        elif Type in ['无符号整型', '正整数', '整数']:
            if isinstance(Value, int) is False:
                raise InTypeError(Value, Type)
            elif Type == '无符号整型':
                if Value < 0:
                    raise InTypeError(Value, Type)
            elif Type == '正整数':
                if Value <= 0:
                    raise InTypeError(Value, Type)
        elif Type == '实数':
            if isinstance(Value, (int, float)) is False:
                raise InTypeError(Value, Type)
        elif Type == '布尔型':
            if isinstance(Value, bool) is False:
                raise InTypeError(Value, Type)
        elif Type == '正数':
            if isinstance(Value, (int, float)) is False:
                raise InTypeError(Value, Type)
            elif Value <= 0:
                raise InTypeError(Value, Type)

def CheckRASPPAR(InFiles = None, OutFile = None, RasterFormat = None, Bands = None,
                 CutLineFile = None, InNoData = None, OutNoData = None, MaskBoundary = None,
                 Resolution = None, ResampleMethod = None, Projection = None, Variable = None,
                 Dimension = None, VectorFormat = None, BlockSize = None, Force = None,
                 NumThreads = None, BitDepth = None, DataType = None):

    # 输入路经检查
    if InFiles is None:
        pass
    elif isinstance(InFiles, list):
        for F in InFiles:
            Check.FilePath(F)
    elif isinstance(InFiles, str):
        Check.FilePath(InFiles)
    else:
        raise InTypeError(InFiles, '路径')

    # 输出路径检查
    if OutFile is None:
        pass
    elif isinstance(OutFile, str):
        if os.path.exists(os.path.dirname(OutFile)) is False:
            raise InTypeError(os.path.dirname(OutFile) + '（输出文件所在的文件夹）', '路径')
    else:
        raise InTypeError(OutFile, '路径')

    # 栅格文件格式
    if RasterFormat is None:
        pass
    elif RasterFormat not in key.RasterFormat:
        raise InTypeError(RasterFormat, '格式')

    # 波段设置
    if Bands is None:
        pass
    elif isinstance(Bands, list):
        for B in Bands:
            Check.ValueType(B, '正整数')
    else:
        Check.ValueType(Bands, '正整数')

    # 矢量文件路径检查
    if CutLineFile is None:
        pass
    else:
        Check.FilePath(CutLineFile)

    # NoData 设置检查
    if InNoData is None:
        pass
    else:
        Check.ValueType(InNoData, '实数')

    if OutNoData is None:
        pass
    else:
        Check.ValueType(OutNoData, '实数')

    # 掩膜参数
    if MaskBoundary is None:
        pass
    else:
        Check.ValueType(MaskBoundary, '布尔型')

    # 重采样分辨率
    if Resolution is None:
        pass
    else:
        Check.ValueType(Resolution, '正数')

    # 重采样方法
    if ResampleMethod is None:
        pass
    elif ResampleMethod not in sum(key.ResampleMethod.items(), ()):
         raise InTypeError(ResampleMethod, '方法')

    # 坐标系
    if Projection is None:
        pass
    elif isinstance(Projection, str):
        if osr.GetWellKnownGeogCSAsWKT(Projection) == 6:
            raise InTypeError(Projection, '坐标系')
    else:
        raise InTypeError(Projection, '坐标系')

    # 变量
    if Variable is None:
        pass
    else:
        Check.ValueType(Variable, '字符串')

    # 维度
    if Dimension is None:
        pass
    else:
        Check.ValueType(Dimension, '正整数')

    # 矢量文件格式
    if VectorFormat is None:
        pass
    elif VectorFormat not in key.VectorFormat:
        raise InTypeError(VectorFormat, '格式')

    # 分块
    if BlockSize is None:
        pass
    else:
        Check.ValueType(BlockSize, '正整数')
        if BlockSize < 64 or BlockSize > 4096:
            raise InTypeError(BlockSize, '分块')

    # 强制
    if Force is None:
        pass
    else:
        Check.ValueType(Force, '布尔型')

    # 多线程
    if NumThreads is None:
        pass
    elif isinstance(NumThreads, int):
        if NumThreads <= 0:
            raise InTypeError(NumThreads, '线程数量')
    elif NumThreads != 'ALL_CPUS':
        raise InTypeError(NumThreads, '线程数量')

    # 位深
    if BitDepth is None:
        pass
    else:
        Check.ValueType(BitDepth, '无符号整型')

    # 数据类型
    if DataType is None:
        pass
    elif isinstance(DataType, int):
        if DataType not in key.DataType.values():
            raise InTypeError(DataType, '数据类型')
    else:
        raise InTypeError(DataType, '数据类型')



def CheckVESPPAR(InFiles = None, OutFile = None, OutNameField = None, Separator = None,
                 VectorFormat = None, Attribute = None, OutNoData = None, RasterFormat = None,
                 Projection = None, Resolution = None):

    # 输入路经检查
    if InFiles is None:
        pass
    elif isinstance(InFiles, list):
        for F in InFiles:
            Check.FilePath(F)
    elif isinstance(InFiles, str):
        Check.FilePath(InFiles)
    else:
        raise InTypeError(InFiles, '路径')

    # 输出路径检查
    if OutFile is None:
        pass
    elif isinstance(OutFile, str):
        if os.path.exists(os.path.dirname(OutFile)) is False:
            raise InTypeError(os.path.dirname(OutFile) + '（输出文件所在的文件夹）', '路径')
    else:
        raise InTypeError(OutFile, '路径')

    # 字段名称检查
    if OutNameField == None:
        pass
    elif isinstance(OutNameField, list):
        for s in OutNameField:
            Check.ValueType(s, '字符串')
    elif isinstance(OutNameField, str) is False:
        raise InTypeError(OutNameField, '字符串')

    # 字段分隔符设置检查
    if Separator == None:
        pass
    elif isinstance(Separator, str) is False:
        raise InTypeError(Separator, '字符串')

    # 矢量文件格式
    if VectorFormat is None:
        pass
    elif VectorFormat not in key.VectorFormat:
        raise InTypeError(VectorFormat, '格式')

    # 输出字段属性检查
    if Attribute == None:
        pass
    elif isinstance(Attribute, str) is False:
        raise InTypeError(Attribute, '字符串')

    # 栅格文件格式
    if RasterFormat is None:
        pass
    elif RasterFormat not in key.RasterFormat:
        raise InTypeError(RasterFormat, '格式')

    # 输出栅格无效值检查
    if OutNoData is None:
        pass
    else:
        Check.ValueType(OutNoData, '实数')

    # 坐标系
    if Projection is None:
        pass
    elif isinstance(Projection, str):
        try:
            if osr.GetWellKnownGeogCSAsWKT(Projection) == 6:
                raise InTypeError(Projection, '坐标系')
        except:
            raise InTypeError(Projection, '坐标系')
    else:
        raise InTypeError(Projection, '坐标系')

    # 重采样分辨率
    if Resolution is None:
        pass
    else:
        Check.ValueType(Resolution, '正数')

