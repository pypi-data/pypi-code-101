# -*- coding: utf-8 -*-
"""
## 矢量数据处理
"""

from gma.algorithm import vector
from gma.Relation import error

CheckPAT = error.CheckVESPPAR

def Split(InFile, OutPath, OutNameField = None, Separator = None, OutFormat = 'ESRI Shapefile'):
    '''
    简介
    ----------
    【矢量文件分解】。将矢量文件中的每个要素【拆分】为单个矢量文件。

    参数
    ----------
    InFile: str。输入矢量文件路径。

    OutPath: str。输出文件夹路径

    **可选参数
    ----------
    OutNameField = str 或 list。标记输出文件名的字段名称或多个字段名称组成的列表。
        默认(None)按照 <0.shp, 1.shp, ...>的方式输出。

    Separator = str。多字段连接方式。如果 OutNameField 定义了一个多字段名称的列表，
        则 Separator 为输出文件名中不同字段的连接方式，默认（None）不以任何进行字段连接。例如：

            outnamefield = ['City', 'Country'], Separator = '_'

            > > > City_County.shp

    OutFormat = str。输出文件格式，默认为 'ESRI Shapefile'。其他格式详见 ToOtherFormat 函数。

    '''
    CheckPAT(InFiles = InFile, OutFile = OutPath, OutNameField = OutNameField, Separator = Separator,
             VectorFormat = OutFormat)
    vector.Split(InFile, OutPath, OutNameField = OutNameField, Separator = Separator,
                 OutFormat = OutFormat)

def Check(InFile):
    '''
    简介
    ----------
    【检查】文件每个要素的有效性。

    参数
    ----------
    InFile: str。输入矢量文件路径。

    返回
    ----------
    如果输入矢量通过检查，则返回 'Pass'。否则返回无效信息(tuple)。

    无效信息组成：

        Invalid number: 无效要素的数量。

        Invalid layer&FID: 无效图层和图层内无效要素的FID。

    '''
    CheckPAT(InFiles = InFile)
    return vector.Check(InFile)

def ToRaster(InFile, OutFile, Resolution, Attribute = None, OutNoData = None, OutFormat = 'GTiff'):
    '''
    简介
    ----------
    【矢量转栅格】。将矢量图层转换为栅格文件。

    参数
    ----------
    InFile: str。输入矢量文件路径。

    OutFile: str。输出栅格文件路径。

    Resolution: int。输出栅格的分辨率。

    **可选参数
    ----------
    Attribute = None。进行转换的矢量数据的字段。如果未设置（None），则生成由 0 和 1 组成的栅格，0 是 nodata 值。

    OutNoData = None。输出栅格的值无效。默认不设置（None）无效值。如果 Attribute 不为 None 且 OutNoData 未设置，则 OutNoData 修改为无穷大（inf）。

    OutFormat = str。输出文件格式，默认为 'ESRI Shapefile'。其他格式详见 ToOtherFormat 函数。

    '''
    CheckPAT(InFiles = InFile, OutFile = OutFile, Resolution = Resolution,
             Attribute = Attribute, OutNoData = OutNoData, RasterFormat = OutFormat)

    vector.ToRaster(InFile, OutFile, Resolution, Attribute = Attribute,
                    OutNoData = OutNoData, OutFormat = OutFormat)

def Reproject(InFile, OutFile, Projection, OutFormat = 'ESRI Shapefile'):
    '''
    简介
    ----------
    矢量【重投影】。

    参数
    ----------
    InFile: str。输入矢量文件路径。

    OutFile: str。输出矢量文件路径。

    Projection: str。输出矢量文件的坐标系，EPSG 或 wkb格式。

    **可选参数
    ----------
    OutFormat = str。输出文件格式，默认为 'ESRI Shapefile'。其他格式详见 ToOtherFormat 函数。

    '''
    CheckPAT(InFiles = InFile, OutFile = OutFile, Projection = Projection,
             VectorFormat = OutFormat)

    vector.Reproject(InFile, OutFile, Projection, OutFormat = OutFormat)

def Clip(InFile, MethodFile, OutFile, OutFormat = 'ESRI Shapefile'):

    '''
    简介
    ----------
    矢量【裁剪】。矢量裁剪矢量。

    参数
    ----------
    InFile: str。输入矢量文件路径。

    MethodFile: str。裁剪矢量范围文件路径。

    OutFile: str。输出矢量文件路径。

    **可选参数
    ----------
    OutFormat = str。输出文件格式，默认为 'ESRI Shapefile'。其他格式详见 ToOtherFormat 函数。

    '''
    CheckPAT(InFiles = [InFile, MethodFile] , OutFile = OutFile, VectorFormat = OutFormat)

    vector.VectorGEOProcessing(InFile, MethodFile, OutFile, OutFormat = OutFormat).Clip()

def Erase(InFile, MethodFile, OutFile, OutFormat = 'ESRI Shapefile'):

    '''
    简介
    ----------
    【擦除】。从第一个矢量中去除与第二个矢量交叉的部分。

    参数
    ----------
    InFile: str。输入矢量文件路径。

    MethodFile: str。擦除矢量范围文件路径。

    OutFile: str。输出矢量文件路径。

    **可选参数
    ----------
    OutFormat = str。输出文件格式，默认为 'ESRI Shapefile'。其他格式详见 ToOtherFormat 函数。

    '''
    CheckPAT(InFiles = [InFile, MethodFile] , OutFile = OutFile, VectorFormat = OutFormat)

    vector.VectorGEOProcessing(InFile, MethodFile, OutFile, OutFormat = OutFormat).Erase()

def Intersection(InFile, MethodFile, OutFile, OutFormat = 'ESRI Shapefile'):
    '''
    简介
    ----------
    矢量取【交集】。取两个矢量的交集。

    参数
    ----------
    InFile: str。第一个矢量文件路径。

    MethodFile: str。第二个矢量文件路径。

    OutFile: str。输出矢量文件路径。

    **可选参数
    ----------
    OutFormat = str。输出文件格式，默认为 'ESRI Shapefile'。其他格式详见 ToOtherFormat 函数。

    '''
    CheckPAT(InFiles = [InFile, MethodFile] , OutFile = OutFile, VectorFormat = OutFormat)

    vector.VectorGEOProcessing(InFile, MethodFile, OutFile, OutFormat = OutFormat).Intersection()

def Union(InFile, MethodFile, OutFile, OutFormat = 'ESRI Shapefile'):
    '''
    简介
    ----------
    矢量【合并】。取两个矢量的并集。

    参数
    ----------
    InFile: str。输入矢量文件路径。

    MethodFile: str。合并矢量文件路径。

    OutFile: str。输出矢量文件路径。

    **可选参数
    ----------
    OutFormat = str。输出文件格式，默认为 'ESRI Shapefile'。其他格式详见 ToOtherFormat 函数。

    '''
    CheckPAT(InFiles = [InFile, MethodFile] , OutFile = OutFile, VectorFormat = OutFormat)

    vector.VectorGEOProcessing(InFile, MethodFile, OutFile, OutFormat = OutFormat).Union()

def Update(InFile, MethodFile, OutFile, OutFormat = 'ESRI Shapefile'):
    '''
    简介
    ----------
    矢量【更新】。用一个矢量更新另一个矢量。

    参数
    ----------
    InFile: str。输入矢量文件路径。

    MethodFile: str。更新矢量文件路径。

    OutFile: str。输出矢量文件路径。

    **可选参数
    ----------
    OutFormat = str。输出文件格式，默认为 'ESRI Shapefile'。其他格式详见 ToOtherFormat 函数。

    '''
    CheckPAT(InFiles = [InFile, MethodFile] , OutFile = OutFile, VectorFormat = OutFormat)

    vector.VectorGEOProcessing(InFile, MethodFile, OutFile, OutFormat = OutFormat).Update()

def ToOtherFormat(InFile, OutFile, OutFormat = 'ESRI Shapefile'):
    '''
    简介
    ----------
    矢量【格式转换】。一种矢量格式转换为另一种矢量格式。

    参数
    ----------
    InFile: str。输入矢量文件路径。

    OutFile: str。输出矢量文件路径。

    **可选参数
    ----------
    OutFormat = str。输出文件格式，默认为 'ESRI Shapefile'。

        其他支持的格式: 'ESRI Shapefile', 'PCIDSK', 'PDS4', 'PDF', 'MBTiles',
                        'MapInfo File', 'Memory', 'CSV', 'GML', 'LIBKML', 'KML',
                        'GeoJSON', 'OGR_GMT', 'GPKG', 'SQLite', 'WAsP',
                        'FlatGeobuf', 'Geoconcept', 'GeoRSS', 'ODS', 'XLSX',
                        'JML', 'VDV', 'MVT', 'MapML'。

    '''
    CheckPAT(InFiles = InFile, OutFile = OutFile, VectorFormat = OutFormat)

    vector.ToOtherFormat(InFile, OutFile, OutFormat = OutFormat)