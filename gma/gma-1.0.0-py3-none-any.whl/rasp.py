# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 20:42:47 2021

@author: Suppe
"""
from gma.algorithm import raster
from gma.Relation import key, error

os = raster.os
Open = raster.Open
CheckPAT = error.CheckRASPPAR

def BandSynthesis(InFiles, OutFile, OutFormat = 'GTiff'):
    '''
    简介
    ----------
    【波段合成】。将单波段文件合成多波段文件。

    参数
    ----------
    InFiles: str 或 list。波段合成路径的结合。

    OutFile: str。输出栅格路径。

    **可选参数
    ----------
    OutFormat = str。输出文件格式，默认为 'GTiff'。其他格式详见 ToOtherFormat 函数。

    '''

    CheckPAT(InFiles = InFiles, OutFile = OutFile, RasterFormat = OutFormat)

    raster.BandSynthesis(InFiles, OutFile, OutFormat)

def BandDecomposition(InFile, OutPath, Bands = None, OutFormat = 'GTiff'):
    '''
    简介
    ----------
    【波段分解】。将多波段文件拆分（或提取）为单波段文件。

    参数
    ----------
    InFile: str。输入栅格路径。

    OutPath: str。输出文件夹路径。

    **可选参数
    ----------
    Bands = None 或 list。需要导出文件的波段，编号从 1 开始。默认全部导出（None）。

    OutFormat = str。输出文件格式，默认为 'GTiff'。其他格式详见 ToOtherFormat 函数。

    '''
    CheckPAT(InFiles = InFile, OutFile = OutPath, Bands = Bands, RasterFormat = OutFormat)

    raster.BandDecomposition(InFile, OutPath, Bands = Bands, OutFormat = OutFormat)

def Clip(InFile, OutFile, CutLineFile, InNoData = None, OutNoData = None, MaskBoundary = True, OutFormat = 'GTiff'):
    '''
    简介
    ----------
    【裁剪】。按矢量边界裁剪栅格 。

    参数
    ----------
    InFile: str。输入栅格路径。

    OutFile: str。输出栅格路径。

    CutLineFile: str。裁剪矢量文件路径。

    **可选参数
    ----------
    InNoData = number。输入栅格的无效值。默认不指定（None）无效值。

    OutNoData = number。输出栅格的无效值。默认不指定（None）无效值。

    MaskBoundary = bool。是否掩膜边界外数据。默认掩膜（True）。

    OutFormat = str。输出文件格式，默认为 'GTiff'。其他格式详见 ToOtherFormat 函数。

    '''

    CheckPAT(InFiles = InFile, OutFile = OutFile, CutLineFile = CutLineFile,
             InNoData = InNoData, OutNoData = OutNoData,
             MaskBoundary = MaskBoundary, RasterFormat = OutFormat)

    raster.Clip(InFile, OutFile, CutLineFile, InNoData = InNoData,
                OutNoData = OutNoData, MaskBoundary = MaskBoundary,
                OutFormat = OutFormat)

def ToOtherFormat(InFile, OutFile, OutFormat = 'GTiff'):
    '''
    简介
    ----------
    【格式转换】。一种栅格格式转换为另一种栅格格式。

    参数
    ----------
    InFile: str。输入栅格路径。

    OutFile: str。输出栅格路径。

    **可选参数
    ----------
    OutFarmat = str。输出数据驱动。默认为'GTiff'。

        其他支持的格式:'AAIGrid', 'BT', 'CALS', 'COG', 'DTED', 'EHdr', 'ENVI', 'ERS',
                        'EXR', 'FIT', 'GIF', 'GPKG', 'GRIB', 'GS7BG', 'GSAG', 'GSBG',
                        'GTiff', 'HDF4Image','HF2', 'HFA', 'ISCE', 'ISIS2', 'ISIS3',
                        'JP2OpenJPEG', 'JPEG', 'LAN', 'MBTiles', 'XPM', 'XYZ', 'netCDF',
                        'MFF2', 'MRF', 'NITF', 'PAux', 'PCIDSK', 'PCRaster', 'PNG',
                        'RST', 'Rasterlite', 'SIGDEM', 'USGSDEM', 'VICAR', 'VRT'。

        注意：目前，除部分自带压缩的驱动，仅对 GTiff, HFA, netCDF 进行了完整的压缩支持。
        多维数据（netCDF, HDF4Image等）转出请使用 MultiSDSToTif。

    '''

    CheckPAT(InFiles = InFile, OutFile = OutFile, RasterFormat = OutFormat)

    raster.ToOtherFormat(InFile, OutFile, OutFormat = OutFormat)

def Mosaic(InFiles, OutFile, InNoData = None, OutNoData = None, OutFormat = 'GTiff'):
    '''
    简介
    ----------
    栅格【镶嵌】。将多个栅格数据集合并到一个新的栅格数据集中。

    参数
    ----------
    InFiles: list。镶嵌影像路径集合。

    OutFile: str。输出文件路径。

    **可选参数
    ----------
    InNoData = number 或 list。输入栅格的无效值。默认自动搜索每个输入栅格的无效值（None）。

    OutNoData = number。输出栅格的无效值。默认根据输入栅格自动设置（None）。

    OutFarmat = str。输出数据格式。默认为'GTiff'。其他格式详见 ToOtherFormat 函数。

    '''

    CheckPAT(InFiles = InFiles, OutFile = OutFile, InNoData = InNoData,
             OutNoData = OutNoData, RasterFormat = OutFormat)

    raster.Mosaic(InFiles, OutFile, InNoData = InNoData, OutNoData = OutNoData, OutFormat = OutFormat)

def Resample(InFile, OutFile, Resolution, Method = 2, InNoData = None, OutNoData = None, OutFormat = 'GTiff'):
    '''
    简介
    ----------
    栅格【重采样】。更改栅格数据的空间分辨率。

    参数
    ----------
    InFile: str。输入栅格路径。

    OutFile: str。输出栅格路径。

    Resolution: number。重采样分辨率。

    **可选参数
    ----------
    Method = int 或 str。重采样方法。默认为 'Cubic'法（2）。

        支持的重采样方法包括：0: Nearest Neighbour, 1: Bilinear, 2: Cubic, 3: CubicSpline, 4: Lanczos,
        5: Average, 6: RMS, 7: Mode。

    InNoData = number。输入栅格的无效值。默认自动搜索输入栅格的无效值（None）。

    OutNoData = number。输出栅格的无效值。默认与 InNoData 的无效值相同（None）。

    OutFarmat = str。输出数据格式。默认为'GTiff'。其他格式详见 ToOtherFormat 函数。

    '''

    CheckPAT(InFiles = InFile, OutFile = OutFile, Resolution =  Resolution,
             ResampleMethod = Method, InNoData = InNoData, OutNoData = OutNoData, RasterFormat = OutFormat)

    raster.Resample(InFile, OutFile, Resolution, Method = Method,
                    InNoData = InNoData, OutNoData = InNoData, OutFormat = OutFormat)

def Reproject(InFile, OutFile, OutProjection, InNoData = None, OutNoData = None, OutFormat = 'GTiff'):
    '''
    简介
    ----------
    栅格【重投影】。将空间数据从一种坐标系投影到另一种坐标系。

    参数
    ----------
    InFile: str。输入栅格路径。

    OutFile: str。输出栅格路径。

    OutProjection: str。输出栅格坐标系（EPSG 或 wkb 格式）。

    **可选参数
    ----------
    InNoData = number。输入栅格的无效值。默认自动搜索输入栅格的无效值（None）。

    OutNoData = number。输出栅格的无效值。默认与 InNoData 的无效值相同（None）。

    OutFormat = str。输出文件格式，默认为 'GTiff'。其他格式详见 ToOtherFormat 函数。

    '''
    CheckPAT(InFiles = InFile, OutFile = OutFile, Projection = OutProjection,
             InNoData = InNoData, OutNoData = OutNoData, RasterFormat = OutFormat)

    raster.Reproject(InFile, OutFile, OutProjection, InNoData = InNoData,
                     OutNoData = InNoData, OutFormat = OutFormat)

def ChangeDataType(InFile, OutFile, DataType, BitDepth = None, OutFormat = 'GTiff'):
    '''
    简介
    ----------
    【数据类型转换】。转换栅格数据的数据类型。

    参数
    ----------
    InFiles: str 输入栅格路径。

    OutFile: str。输出栅格路径。

    DataType: int。输出栅格数据类型的代码。

        数据类型包括：
            '未知类型': 0, '8位无符号整型': 1, '16位无符号整型': 2, '16位整型': 3, '32位无符号整型': 4,
            '32位整型': 5, '32位浮点': 6, '64位浮点': 7, '16位复整型': 8, '32位复整型': 9,
            '32位复浮点型': 10, '64位复浮点型': 11。

    **可选参数
    ----------
    BitDepth = int。输出栅格位深。仅为 'GTiff' 文件提供位深支持。

    OutFormat = str。输出栅格格式，默认为 'GTiff'。其他格式详见 ToOtherFormat 函数。

    '''
    CheckPAT(InFiles = InFile, OutFile = OutFile, BitDepth = BitDepth, DataType = DataType,
             RasterFormat = OutFormat)

    if BitDepth is None:
        pass
    else:
        if DataType == 1:
            if BitDepth > 8:
                raise error.InTypeError(BitDepth, '位深')
        elif DataType == 2:
            if BitDepth < 8 or BitDepth > 15:
                raise error.InTypeError(BitDepth, '位深')
        elif DataType == 4:
            if BitDepth < 16 or BitDepth > 31:
                raise error.InTypeError(BitDepth, '位深')
        elif DataType == 6:
            if BitDepth != 16:
                raise error.InTypeError(BitDepth, '位深')
        else:
            raise error.InTypeError(BitDepth, '位深')

    raster.ChangeDataType(InFile, OutFile, DataType, BitDepth = BitDepth,
                          OutFormat = OutFormat)

def MultiSDSToTif(InFile, OutPath, Variable = None, Dimension = None, Projection = 'WGS84'):
    '''
    简介
    ----------
    【多维数据转GTiff】。将含有子数据集的多维数据提取为GTiff。

    参数
    ----------
    InFile: str。输入栅格路径。

    OutPath: str。输出文件夹路径。

    **可选参数
    ----------
    Variable = list。要转换变量的 字符串 列表。默认转换所有变量（None）。

    Dimension = list。要转换维度的 整型数 列表。默认转换所有维度（None）。

    Projection = str。输入数据的 X,Y 坐标系。默认为 'WGS84'。

    '''

    CheckPAT(InFiles = InFile, OutFile = OutPath, Variable = Variable,
             Dimension = Dimension, Projection = Projection)

    raster.MultiSDSToTif(InFile, OutPath, Variable = Variable,
                         Dimension = Dimension, Projection = Projection)

def ToVector(InFile, OutVector, FieldName = 'Value', TranBand = 1, OutFormat = 'ESRI Shapefile'):
    '''
    简介
    ----------
    【栅格转矢量】。将栅格数据转换为矢量数据。

    参数
    ----------
    InFile: str。输入栅格路径。

    OutVector: str。输出矢量路径

    **可选参数
    ----------
    FieldName = str。输出矢量字段的名称。默认为 'Value'。

    TranBand = int。要转换的波段。默认转换第一个波段（1）。

    OutFormat = str。输出文件格式，默认为 'ESRI Shapefile'。其他格式详见 ToOtherFormat 函数。

    描述
    ----------
    不需要设置类型（点、线、面等），默认根据栅格数据自动确定类型。

    '''

    CheckPAT(InFiles = InFile, OutFile = OutVector, Variable = FieldName, Bands = TranBand,
             VectorFormat = OutFormat)

    raster.ToVector(InFile, OutVector, FieldName = FieldName, TranBand = TranBand,
                          OutFormat = OutFormat)

def WriteRaster(OutFile, DataArray, Projection = None, Transform = None, Format = 'GTiff',
                DataType = 6, NoData = None):
    '''
    简介
    ----------
    【写出栅格】。将数组保存为栅格文件。

    参数
    ----------
    OutFile: str。输出栅格路径。

    DataArray: array。输入数组。

    **可选参数
    ----------
    Projection = str。输出栅格坐标系。默认不指定坐标系（None）。

    Transform = tuple。输出栅格的仿射变换。默认不指定仿射变换（None）。

    Format = str。输出文件格式。默认为 'GTiff'。其他格式详见 ToOtherFormat 函数。

    DataType = int。输出栅格数据类型。默认为 float32（6）。

        其他的数据类型还包括：
            '未知类型': 0, '8位无符号整型': 1, '16位无符号整型': 2, '16位整型': 3, '32位无符号整型': 4,
            '32位整型': 5, '32位浮点': 6, '64位浮点': 7, '16位复整型': 8, '32位复整型': 9,
            '32位复浮点型': 10, '64位复浮点型': 11。

    NoData = int。输出栅格的无效值。默认不设置无效值（None）。

    '''
    CheckPAT(OutFile = OutFile, Projection = Projection, RasterFormat = Format, OutNoData = NoData)

    if isinstance(DataArray, raster.np.ndarray) is False:
        raise TypeError(' 写出数据 必须为 数组! ')
    if isinstance(Transform, tuple) is False:
        raise TypeError(' 仿射变换 必须为 6数据元组! ')
    elif len(Transform) != 6:
        raise TypeError(' 仿射变换 必须为 6数据元组! ')
    if DataType not in key.DataType.values():
        raise TypeError(' 输出数据 类型错误! ')

    raster.WriteRaster(OutFile, DataArray, Projection = Projection, Transform = Transform,
                       Format = Format, DataType = DataType, NoData = NoData)

def GenerateOVR(InFile, Force = False):
    '''
    简介
    ----------
    【构建栅格金字塔】。为GTiff文件构造.ovr栅格金字塔，或为其他类型的栅格数据强制构造.ovr金字塔 。

    参数
    ----------
    InFile: str。栅格文件路径。

    **可选参数
    ----------
    Force = bool。是否为所有类型的文件添加 .ovr 金字塔。默认（False）只为 GTiff 驱动的栅格添加金字塔。

    '''
    CheckPAT(InFiles = InFile, Force = Force)

    raster.GenerateOVR(InFile, Method = 'NEAREST', BlockSize = 128, Force = Force)

def OrthophotoCorrection(InFile, OutFile, DEM = None, Resample = 0, OutFormat = 'GTiff'):
    '''
    参数
    ----------
    【正射校正】。根据有理多项式系数（RPC）对影像进行正射校正。

    参数
    ----------
    InFile: str。栅格文件路径。

        输入栅格必须有内部 RPC（有理多项式系数）元数据或同路径下描述 RPC 的外部 .rpb 或 _RPC.txt 文件。

    OutFile: str。输出栅格路径。

    **可选参数
    ----------
    DEM = number 或 str。用于 RPC 计算的固定高度 或 DEM 文件的名称。默认不设置此参数（None）。

    Resample = int 或 str。重采样方法。默认为 'Nearest Neighbour'法（0）。

        支持的重采样方法包括：0: Nearest Neighbour, 1: Bilinear, 2: Cubic, 3: CubicSpline, 4: Lanczos,
        5: Average, 6: RMS, Mode。

    OutFormat = str。输出文件格式，默认为 'GTiff'。其他格式详见 ToOtherFormat 函数。

    '''

    CheckPAT(InFiles = InFile, OutFile = OutFile, ResampleMethod = Resample, RasterFormat = OutFormat)
    if DEM is None:
        pass
    elif isinstance(DEM, (int, float, str)) is False:
        raise TypeError('DEM 必须为 None, 数字或一个栅格文件的路径。')
    elif isinstance(DEM, str):
        if os.path.isfile(str(DEM)) is False:
            raise TypeError('DEM 必须为 None, 数字或一个栅格文件的路径。')

    raster.OrthophotoCorrection(InFile, OutFile, DEM = None, Resample = Resample, OutFormat = OutFormat)

def Deformation(InFiles, OutFile, CutLineFile = None,
                ResampleMethod = 0, Resolution = None,
                OutProjection = 'WGS84',
                InNoData = None, OutNoData = None,
                OutFormat = 'GTiff'):

    '''
    简介
    ----------
    【流程化处理】。完成镶嵌-裁剪-重采样-重投影-格式转换等其中一个或多个功能。

    参数
    ----------
    InFiles: str 或 list。输入栅格路径。如果为列表，则列表内所有的栅格将被【镶嵌】（Mosaic）。

    OutFile: str。输出栅格路径。

    **可选参数
    ----------
    CutLineFile = str。【裁剪】。如果有，将用此 矢量文件 裁剪输出栅格。

    Resolution = number。【重采样分辨率】。设置重采样分辨率。

    ResampleMethod = int 或 str。【重采样】方法。默认为 'Nearest Neighbour'法（0）。

        支持的重采样方法包括：0: Nearest Neighbour, 1: Bilinear, 2: Cubic, 3: CubicSpline, 4: Lanczos,
        5: Average, 6: RMS, Mode。

    OutProjection = str。【重投影】栅格坐标系名称。输出栅格坐标系（EPSG 、 wkb 或 坐标名称）。

    InNoData = number。【输入无效值】。输入栅格的无效值。

    OutNoData = number。【输出无效值】。输出栅格的无效值。

    OutFormat = str。【格式转换】。输出栅格格式，默认为 'GTiff'。其他格式详见 ToOtherFormat 函数。

    '''

    CheckPAT(InFiles = InFiles, OutFile = OutFile, CutLineFile = CutLineFile,
             Resolution = Resolution, ResampleMethod = ResampleMethod,
             Projection = OutProjection, InNoData = InNoData, OutNoData = OutNoData,
             RasterFormat = OutFormat)

    raster.Deformation(InFiles, OutFile, CutLineFile = CutLineFile,
                       ResampleMethod = ResampleMethod, Resolution = Resolution,
                       OutProjection = OutProjection,
                       InNoData = InNoData, OutNoData = OutNoData,
                       OutFormat = OutFormat)

class Fusion:
    '''
    类简介
    ----------
    【影像融合】。

    初始化
    ----------
    InPanchromatic: str。输入全色影像路径。

    Multispectral: str。输入多光谱影像数据。

    OutFile: str。输出栅格路径。

    '''

    def __init__(self, InPanchromatic, InMultispectral, OutFile):

        CheckPAT(InFiles = [InPanchromatic, InMultispectral], OutFile = OutFile)

        self.FusionFileSet = raster.Fusion(InPanchromatic, InMultispectral, OutFile)

    def Pansharpen(self, ResampleMethod = None, SpatAdjust = None, Bands = None,
                   NumThreads = None, BitDepth = None, InNoData = None, OutFormat = 'GTiff'):
        '''
        简介
        ----------
        【Pansharp】融合。对全色影像和多光谱影像基于Pansharpen方法进行融合。

        **可选参数
        ----------
        ResampleMethod: str。重采样方法。默认为 'Cubic'（None）。

            重采样方法包括：'Nearest', 'Bilinear', 'Cubic', 'CubicSpline', 'Lanczos', 'Average'。

        SpatAdjust: str。空间坐标系调整。默认为'Union'（None）。

            调整方法包括：'Union', 'Intersection', 'None', 'NoneWithoutWarning'。

        Bands = list。融合多光谱波段列表。例如[1,2...]，波段计数从 1 开始。默认融合输入多光谱数据的所有波段（None）。

            ***每个波段的权重值（'Weights'）相同，根据 Bands 数量确定，为 1 / len(Bands)。

        NumThreads = int 或 'ALL_CPUS'。融合使用计算机 CPU 的线程数。默认不使用多线程（None）。

        BitDepth = int。生成数据的位深。默认不设置位深（None）, 但如果全色波段存在 NBITS 值，则使用该值作为位深。

        InNoData = number。全色和多光谱影像的无效值（所有输入数据的无效值应当相同，否则该设置无效），输出文件的无效值也为该值。默认不设置无效值（None）。

        OutFormat = str。输出文件格式，默认为 'GTiff'。其他格式详见 ToOtherFormat 函数。

        '''
        CheckPAT(ResampleMethod = ResampleMethod, Projection = SpatAdjust, Bands = Bands,
                 NumThreads = NumThreads, BitDepth = BitDepth, InNoData = InNoData,
                 RasterFormat = OutFormat)


        self.FusionFileSet.Pansharpen(ResampleMethod = ResampleMethod, SpatAdjust = SpatAdjust,
                                      Bands = Bands, NumThreads = NumThreads, BitDepth = BitDepth,
                                      InNodata = InNoData, OutFormat = OutFormat)
