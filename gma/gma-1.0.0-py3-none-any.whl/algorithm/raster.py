# -*- coding: utf-8 -*-
"""
Geographic information data processing function package!
=====

Update date: 2021.7.21

"""

import os, re
from osgeo import gdal, ogr, osr, gdal_array
import numpy as np
from gma.Relation import key
import psutil

gdal.UseExceptions()

def BandSynthesis(InFiles, OutFile, OutFormat = 'GTiff'):
    '''
    简介
    ----------
    波段合成。将单波段文件合成多波段文件。

    参数
    ----------
    InFiles: str 或 list。波段合成路径的结合。

    OutFile: str。输出栅格路径。

    **可选参数
    ----------
    OutFormat = str。输出文件格式，默认为 'GTiff'。其他格式详见 ToOtherFormat 函数。

    '''

    VRTXML = gdal.BuildVRT("", InFiles, separate = True, bandList = [1])

    RCOptions = key.GenRCOptions(OutFormat)

    Options = gdal.TranslateOptions(format = OutFormat,
                                    creationOptions = RCOptions,
                                    callback = gdal.TermProgress_nocb)

    gdal.Translate(OutFile, VRTXML, options = Options)

    GenerateOVR(OutFile)

def BandDecomposition(InFile, OutPath, Bands = None, OutFormat = 'GTiff'):
    '''
    简介
    ----------
    波段分解。将多波段文件拆分（或提取）为单波段文件。

    参数
    ----------
    InFile: str。输入栅格路径。

    OutPath: str。输出文件夹路径。

    **可选参数
    ----------
    Bands = None 或 list。需要导出文件的波段，编号从 1 开始。默认全部导出（None）。

    OutFormat = str。输出文件格式，默认为 'GTiff'。其他格式详见 ToOtherFormat 函数。

    '''

    BandInfo = gdal.Info(InFile, format = 'json')['bands']

    if BandInfo == []:
        raise TypeError('InFile 不存在或数据为空！')

    if Bands is None:
        Bands = np.arange(len(BandInfo)) + 1
    elif isinstance(Bands, int):
        Bands = [Bands]
    elif isinstance(Bands, list) is False:
        raise TypeError('Bands 类型必须为 int, list 或 None！')

    EXT = key.GetRasterEXTFromDriver(OutFormat)
    OutName = os.path.splitext(os.path.join(OutPath, os.path.basename(InFile)))[0]
    RCOptions = key.GenRCOptions(OutFormat)

    for b in Bands:

        OutFile = OutName + '_' + str(b) + EXT

        Options = gdal.TranslateOptions(format = OutFormat,
                                        creationOptions = RCOptions,
                                        bandList = [b],
                                        callback = gdal.TermProgress_nocb)

        gdal.Translate(OutFile, InFile, options = Options)

        GenerateOVR(OutFile)

def Clip(InFile, OutFile, CutLineFile, InNoData = None, OutNoData = None, MaskBoundary = True, OutFormat = 'GTiff'):
    '''
    简介
    ----------
    按矢量裁剪栅格。

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


    RCOptions = key.GenRCOptions(OutFormat)

    MemoryLimit = psutil.virtual_memory().free * 0.8

    Options = gdal.WarpOptions(format = OutFormat,
                               cutlineDSName = CutLineFile,
                               srcNodata = InNoData,
                               dstNodata = OutNoData,
                               cropToCutline = MaskBoundary,
                               warpMemoryLimit = MemoryLimit,
                               creationOptions = RCOptions,
                               callback = gdal.TermProgress_nocb)

    gdal.Warp(OutFile, InFile, options = Options)

    GenerateOVR(OutFile)

def ToOtherFormat(InFile, OutFile, OutFormat = 'GTiff'):
    '''
    简介
    ----------
    将一个栅格数据集转换为其他格式。

    参数
    ----------
    InFile: str。输入栅格路径。

    OutFile: str。输出栅格路径。

    **可选参数
    ----------
    OutFarmat = str。输出数据驱动。默认为'GTiff'。

        其他支持的格式: VRT, COG, NITF, HFA, ELAS, AAIGrid, DTED, PNG, JPEG, MEM, GIF,
            FITS, XPM, BMP, PCIDSK, PCRaster, ILWIS, SGI, SRTMHGT, Leveller, Terragen, GMT,
            netCDF, HDF4Image, ISIS3, ISIS2, PDS4, VICAR, ERS, JP2OpenJPEG, FIT, GRIB,
            RMF, WMS, RST, INGR, GSAG, GSBG, GS7BG, R, KMLSUPEROVERLAY, WEBP, PDF,
            Rasterlite, MBTiles, CALS, WMTS, MRF, PNM, PAux, MFF, MFF2, BT, LAN, IDA,
            LCP, GTX, NTv2, CTable2, KRO, ROI_PAC, RRASTER, BYN, ARG, USGSDEM, BAG, NWT_GRD,
            ADRG, BLX, PostGISRaster, SAGA, XYZ, HF2, ZMap, SIGDEM, EXR, DB2ODBC,
            GPKG, NGW, ENVI, EHdr, ISCE。

        注意：目前，除部分自带压缩的驱动，仅对 GTiff, HFA, netCDF 进行了完整的压缩支持。
        多维数据（netCDF, HDF4Image等）转出请使用 MultiSDSToTif。

    '''

    RCOptions = key.GenRCOptions(OutFormat)

    Options = gdal.TranslateOptions(format = OutFormat,
                                    creationOptions = RCOptions,
                                    callback = gdal.TermProgress_nocb)

    gdal.Translate(OutFile, InFile, options = Options)

    GenerateOVR(OutFile)

def Mosaic(InFiles, OutFile, InNoData = None, OutNoData = None, OutFormat = 'GTiff'):
    '''
    简介
    ----------
    影像【镶嵌】。

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

    if InNoData is None:
        WO = ['UNIFIED_SRC_NODATA=NO']
    else:
        WO = []

    RCOptions = key.GenRCOptions(OutFormat)
    MemoryLimit = psutil.virtual_memory().free * 0.8

    Options = gdal.WarpOptions(format = OutFormat,
                               srcNodata = InNoData,
                               dstNodata = OutNoData,
                               creationOptions = RCOptions,
                               warpOptions = WO,
                               warpMemoryLimit = MemoryLimit,
                               callback = gdal.TermProgress_nocb)

    gdal.Warp(OutFile, InFiles, options = Options)

    GenerateOVR(OutFile)

def Resample(InFile, OutFile, Resolution, Method = 2, InNoData = None, OutNoData = None, OutFormat = 'GTiff'):
    '''
    简介
    ----------
    栅格【重采样】。

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

    if InNoData is None:
        InNoData = Open(InFile).NoData

    if OutNoData is None:
        OutNoData = InNoData

    RCOptions = key.GenRCOptions(OutFormat)
    MemoryLimit = psutil.virtual_memory().free * 0.8

    Options = gdal.WarpOptions(format = OutFormat,
                               xRes = Resolution,
                               yRes = Resolution,
                               srcNodata = InNoData,
                               dstNodata = OutNoData,
                               resampleAlg = Method,
                               warpMemoryLimit = MemoryLimit,
                               creationOptions = RCOptions,
                               callback = gdal.TermProgress_nocb)

    gdal.Warp(OutFile, InFile, options = Options)

    GenerateOVR(OutFile)

def Reproject(InFile, OutFile, OutProjection, InNoData = None, OutNoData = None, OutFormat = 'GTiff'):
    '''
    简介
    ----------
    栅格【重投影】。

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
    if InNoData is None:
        InNoData = Open(InFile).NoData

    if OutNoData is None:
        OutNoData = InNoData

    RCOptions = key.GenRCOptions(OutFormat)
    MemoryLimit = psutil.virtual_memory().free * 0.8

    Options = gdal.WarpOptions(format = OutFormat,
                               dstSRS = OutProjection,
                               srcNodata = InNoData,
                               dstNodata = OutNoData,
                               creationOptions = RCOptions,
                               warpMemoryLimit = MemoryLimit,
                               callback = gdal.TermProgress_nocb)

    gdal.Warp(OutFile, InFile, options = Options)

    GenerateOVR(OutFile)

class Open:
    '''栅格操作。'''
    def __init__(self, RasterPath):
        self.RasterTran = gdal.Open(RasterPath)

    def GetGDALDataset(self):
        return self.RasterTran

    @property
    def Bands(self):
        '''输入栅格的波段数。类型: int。'''
        return self.RasterTran.RasterCount

    @property
    def Rows(self):
        '''输入栅格的行数（Y）。类型: int。'''
        return self.RasterTran.RasterYSize

    @property
    def Columns(self):
        '''输入栅格的列数（X）。类型: int。'''
        return self.RasterTran.RasterXSize

    @property
    def Projection(self):
        '''输入栅格的坐标系。 类型: str。'''
        return self.RasterTran.GetProjection()

    @property
    def GeoTransform(self):
        '''输入栅格的仿射变换. 类型: tuple。'''
        return self.RasterTran.GetGeoTransform()

    def ToArray(self):
        '''将栅格数据转换为 numpy 数组。'''
        return self.RasterTran.ReadAsArray()

    def GetBand(self, Band):
        '''获取波段数据。'''
        return self.RasterTran.GetRasterBand(Band)

    def GetBandToArray(self, Band):
        '''将某一波段数据转换为 numpy 数组。'''
        return self.RasterTran.GetRasterBand(Band).ReadAsArray()

    @property
    def DataType(self):
        '''获取栅格数据类型。类型: int。如果为多波段数据，则取所有波段数据类型的众数。'''
        DataTypeList = [self.GetBand(int(b + 1)).DataType for b in np.arange(self.Bands)]
        DataType = int(np.argmax(np.bincount(DataTypeList)))
        return DataType

    @property
    def NoData(self):
        '''获取输入栅格的无效值。类型: number。'''
        NoDataValue = self.GetBand(1).GetNoDataValue()
        return NoDataValue

def MultiSDSToTif(InFile, OutPath, Variable = None, Dimension = None, Projection = 'WGS84'):
    '''
    简介
    ----------
    将 科学数据集 数据【转换】为 GTiff 数据。

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

    Projection = osr.GetWellKnownGeogCSAsWKT(Projection)

    def _SubDataSetToTif(SubDataset):

        if Dimension is not None:

            Bands = [int(dim) for dim in Dimension if dim >= 0 and dim <= SubDataset.RasterCount - 1]

            if Bands is False:
                raise TypeError('维度参数设置错误！')
        else:
            Bands = np.arange(0, SubDataset.RasterCount)

        for b in Bands:

            TranDataset = SubDataset.GetRasterBand(int(b + 1))
            Metadata = TranDataset.GetMetadata()

            BaseName =  os.path.basename(InFile)
            FileNameWithoutE = BaseName[:len(BaseName.split('.')[-1])]
            VAL = [' '.join(V.split()[:3]) for V in Metadata.values()]
            OutName = FileNameWithoutE + '_' + '_'.join(VAL) + '.tif'
            OutName = re.sub(r"[\/\:\*\?\"\<\>\|\+]", "_", OutName).replace('/', 'per')
            OutFile = os.path.join(OutPath, OutName)


            RCOptions = key.GenRCOptions('GTiff')

            Options = gdal.TranslateOptions(format = 'GTiff',
                                            creationOptions = RCOptions,
                                            bandList = [b + 1],
                                            outputSRS = Projection,
                                            callback = gdal.TermProgress_nocb)

            gdal.Translate(OutFile, SubDataset, options = Options)

            GenerateOVR(OutFile)


    SDSDataset = gdal.Open(InFile)

    Subsets = SDSDataset.GetSubDatasets()

    if Subsets:

        for Subset in Subsets:
            Var = Subset[0].split(':')[-1]

            if Variable is not None:
                if Var in Variable:
                    SubDataset = gdal.Open(Subset[0])
                    _SubDataSetToTif(SubDataset)

            else:
                SubDataset = gdal.Open(Subset[0])
                _SubDataSetToTif(SubDataset)

    else:
          _SubDataSetToTif(SDSDataset)

def ToVector(InFile, OutVector, FieldName = 'Value', TranBand = 1, OutFormat = 'ESRI Shapefile'):
    '''
    简介
    ----------
    栅格转矢量。

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

    InDataSet = gdal.Open(InFile)
    TranData = InDataSet.GetRasterBand(TranBand)
    NoData = TranData.GetNoDataValue()

    # 创建掩膜。
    if NoData is None:
        Mask = None
    else:
        MaskArray = np.ones((InDataSet.RasterXSize, InDataSet.RasterXSize), int)
        MaskArray[np.where(TranData.ReadAsArray() == NoData)] = 0

        MaskDataSet = gdal_array.OpenArray(MaskArray, prototype_ds = InDataSet)
        Mask = MaskDataSet.GetRasterBand(1)

    Projection = InDataSet.GetProjection()
    Proj = osr.SpatialReference()
    Proj.ImportFromWkt(Projection)

    LCOptions = key.GenVCOptions(OutFormat)

    oDS = ogr.GetDriverByName(OutFormat).CreateDataSource(OutVector)
    oLayer = oDS.CreateLayer(os.path.splitext(OutVector)[0], srs = Proj,
                             geom_type = ogr.wkbUnknown, options = LCOptions)

    oFieldID = ogr.FieldDefn(FieldName, ogr.wkbUnknown)
    oLayer.CreateField(oFieldID)

    gdal.FPolygonize(TranData, Mask, oLayer, 0, callback = gdal.TermProgress_nocb)
    oDS.SyncToDisk()

def WriteRaster(OutFile, DataArray, Projection = None, Transform = None, Format = 'GTiff',
                DataType = 6, NoData = None):

    '''
    简介
    ----------
    将数组保存为栅格文件。

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

    xsize = DataArray.shape[-1]
    ysize = DataArray.shape[-2]
    if len(DataArray.shape) == 2:
        zsize = 1
    else:
        zsize = DataArray.shape[-3]

    DataFormat = gdal.GetDriverByName(Format)

    RCOptions = key.GenRCOptions(Format)
    Dataset = DataFormat.Create(OutFile, xsize, ysize, zsize, DataType, RCOptions)

    if Transform is not None:
        Dataset.SetGeoTransform(Transform)

    if Projection is not None:
        Dataset.SetProjection(Projection)

    for i in range(zsize):

        if NoData is not None:
            Dataset.GetRasterBand(i + 1).SetNoDataValue(NoData)

        if zsize == 1:
            Dataset.GetRasterBand(i + 1).WriteArray(DataArray)
        else:
            Dataset.GetRasterBand(i + 1).WriteArray(DataArray[i])

        Dataset.GetRasterBand(i + 1).ComputeStatistics(False)

    del Dataset

    GenerateOVR(OutFile)

def GenerateOVR(InFile, Method = 'NEAREST', BlockSize = 128, Force = False):
    '''
    简介
    ----------
    创建 .ovr 金字塔。

    参数
    ----------
    InFile: str。栅格文件路径。

    **可选参数
    ----------
    Method = str。创建 .ovr 金字塔重采样方法。默认为 'NEAREST'。其他方法包括：

        'AVERAGE'，'AVERAGE_MAGPHASE'，'RMS'，'BILINEAR'，'CUBIC'，'CUBICSPLINE'，
        'GAUSS'，'LANCZOS'，'MODE' 或 'NONE'。

    BlockSize = int。金字塔块大小。默认 128。BlockSize 值在 64 ~ 4096之间。

    Force = bool。是否为所有类型的文件添加 .ovr 金字塔。默认只为 GTiff 驱动的栅格添加金字塔。

    '''

    Dataset = gdal.Open(InFile)
    Driver = Dataset.GetDriver().ShortName

    if Driver == 'GTiff' or Force == True:

        gdal.SetConfigOption('COMPRESS_OVERVIEW', 'DEFLATE')
        gdal.SetConfigOption('TIFF_USE_OVR', 'True')

        Rows = Dataset.RasterYSize
        Columns = Dataset.RasterXSize

        MIN = min(Rows, Columns)
        MAX = max(Rows, Columns)

        Level = int(np.log2(MIN / BlockSize)  + (MAX // MIN) // 5)

        OverviewList = [int(2 ** i) for i in range(1, Level + 1)]

        Dataset.BuildOverviews(resampling = Method,
                               overviewlist = OverviewList,
                               callback = gdal.TermProgress_nocb)

class Fusion:
    '''
    类方法
    ----------
    【影像融合】。

    初始化
    ----------
    InPanchromatic: str。输入全色影像路径。

    Multispectral: str。输入多光谱影像数据。

    OutFile: str。输出栅格路径。

    '''

    def __init__(self, InPanchromatic, InMultispectral, OutFile):

        self.InPanchromatic = InPanchromatic
        self.InMultispectral = InMultispectral
        self.OutFile = OutFile

    def Pansharpen(self, ResampleMethod = None, SpatAdjust = None, Bands = None,
                   NumThreads = None, BitDepth = None, InNoData = None, OutFormat = 'GTiff'):
        '''
        简介
        ----------
        【Pansharp】融合。

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

        PanDataset = gdal.Open(self.InPanchromatic)
        if PanDataset is None:
            raise SyntaxError('全高分辨率色影像数据无法打开!')

        MultiDs = gdal.Open(self.InMultispectral)
        if MultiDs is None:
            raise SyntaxError('多光谱数据无法打开！')

        AllBandsNumbers = MultiDs.RasterCount
        if Bands is None:
            MultiDataset = [MultiDs.GetRasterBand(b + 1) for b in range(AllBandsNumbers)]
            Bands = [b + 1 for b in range(AllBandsNumbers)]
        else:
            MultiDataset = [MultiDs.GetRasterBand(b) for b in Bands]

        Weights = [1 / len(Bands) for b in Bands]

        VRTXml = """<VRTDataset subClass="VRTPansharpenedDataset">\n""" + """  <PansharpeningOptions>\n"""

        VRTXml += """      <AlgorithmOptions>\n"""
        VRTXml += """        <Weights>"""

        for i, weight in enumerate(Weights):
            if i > 0:
                VRTXml += ","
            VRTXml += "%.16g" % weight
        VRTXml += "</Weights>\n"
        VRTXml += """      </AlgorithmOptions>\n"""

        if ResampleMethod is not None:
            VRTXml += '      <Resampling>%s</Resampling>\n' % ResampleMethod

        if NumThreads is not None:
            VRTXml += '      <NumThreads>%s</NumThreads>\n' % NumThreads

        if BitDepth is not None:
            VRTXml += '      <BitDepth>%s</BitDepth>\n' % BitDepth

        if InNoData is not None:
            VRTXml += '      <NoData>%s</NoData>\n' % InNoData

        if SpatAdjust is not None:
            VRTXml += '      <SpatialExtentAdjustment>%s</SpatialExtentAdjustment>\n' % SpatAdjust

        PanRelative = '0'

        VRTXml += """    <PanchroBand>
          <SourceFilename relativeToVRT="%s">%s</SourceFilename>
          <SourceBand>1</SourceBand>
        </PanchroBand>\n""" % (PanRelative, self.InPanchromatic)

        for i, SBand in enumerate(MultiDataset):
            DstBand = ''
            for j, band in enumerate(Bands):
                if i + 1 == band:
                    DstBand = ' dstBand="%d"' % (j + 1)
                    break

            MsRelative = '0'
            MsName = MultiDs.GetDescription()

            VRTXml += """    <SpectralBand%s>
          <SourceFilename relativeToVRT="%s">%s</SourceFilename>
          <SourceBand>%d</SourceBand>
        </SpectralBand>\n""" % (DstBand, MsRelative, MsName, SBand.GetBand())

        VRTXml += """  </PansharpeningOptions>\n"""
        VRTXml += """</VRTDataset>\n"""

        VRTDataSet = gdal.Open(VRTXml)
        RCOptions = key.GenRCOptions(OutFormat)
        gdal.GetDriverByName(OutFormat).CreateCopy(self.OutFile, VRTDataSet, 0,
                                                   RCOptions,
                                                   callback = gdal.TermProgress_nocb)

        GenerateOVR(self.OutFile)

def OrthophotoCorrection(InFile, OutFile, DEM = None, Resample = 0, OutFormat = 'GTiff'):
    '''
    参数
    ----------
    正射校正。

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

    Info = gdal.Info(InFile)

    if 'RPC Metadata' not in Info:

        raise ValueError("未找到输入栅格的 RPC（有理多项式系数）元数据！输入栅格必须有内部 RPC 或同路径下描述 RPC 的外部 .rpb 或 _RPC.txt 文件。")

    if DEM is None:
        TFO = ''
    elif isinstance(DEM, str):
        TFO = [r'RPC_DEM=%s' % DEM]
    else:
        TFO = ['RPC_HEIGHT=%s' % float(DEM)]

    RCOptions = key.GenRCOptions(OutFormat)
    MemoryLimit = psutil.virtual_memory().free * 0.8

    Options = gdal.WarpOptions(format = OutFormat,
                               rpc = True,
                               transformerOptions = TFO,
                               resampleAlg = Resample,
                               creationOptions = RCOptions,
                               warpMemoryLimit = MemoryLimit,
                               callback = gdal.TermProgress_nocb)

    gdal.Warp(OutFile, InFile, options = Options)

    GenerateOVR(OutFile)

def Deformation(InFiles, OutFile, CutLineFile = None,
                ResampleMethod = 0, Resolution = None,
                OutProjection = None,
                InNoData = None, OutNoData = None,
                OutFormat = 'GTiff'):

    '''
    简介
    ----------
    栅格形变。完成镶嵌-裁剪-重采样-重投影-格式转换等其中一个或多个功能。

    参数
    ----------
    InFiles: str 或 list。输入栅格路径。如果为列表，则列表内所有的栅格将被【镶嵌】（Mosaic）。

    OutFile: str。输出栅格路径。

    **可选参数
    ----------
    CutLineFile = str。【裁剪】。如果有，将用此 矢量文件 裁剪输出栅格。

    Resolution = number。【重采样分辨率】。设置重采样分辨率。

    Resample = int 或 str。【重采样】方法。默认为 'Nearest Neighbour'法（0）。

        支持的重采样方法包括：0: Nearest Neighbour, 1: Bilinear, 2: Cubic, 3: CubicSpline, 4: Lanczos,
        5: Average, 6: RMS, Mode。

    OutProjection = str。【重投影】栅格坐标系名称。输出栅格坐标系（EPSG 、 wkb 或 坐标名称）。

    InNoData = number。【输入无效值】。输入栅格的无效值。

    OutNoData = number。【输出无效值】。输出栅格的无效值。

    OutFormat = str。【格式转换】。输出栅格格式，默认为 'GTiff'。其他格式详见 ToOtherFormat 函数。

    '''

    RCOptions = key.GenRCOptions(OutFormat)
    MemoryLimit = psutil.virtual_memory().free * 0.8

    Options = gdal.WarpOptions(format = OutFormat,
                               cutlineDSName = CutLineFile,
                               cropToCutline = True,
                               srcNodata = InNoData,
                               dstNodata = OutNoData,
                               dstSRS = OutProjection,
                               xRes = Resolution,
                               yRes = Resolution,
                               resampleAlg = ResampleMethod,
                               creationOptions = RCOptions,
                               warpMemoryLimit = MemoryLimit,
                               callback = gdal.TermProgress_nocb)

    gdal.Warp(OutFile, InFiles, options = Options)

    GenerateOVR(OutFile)

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
            '未知类型（字节型）': 0, '8位无符号整型': 1, '16位无符号整型': 2, '16位整型': 3, '32位无符号整型': 4,
            '32位整型': 5, '32位浮点': 6, '64位浮点': 7, '16位复整型': 8, '32位复整型': 9,
            '32位复浮点型': 10, '64位复浮点型': 11。

    **可选参数
    ----------
    NBITS = int。输出栅格位深。仅为 'GTiff' 文件提供位深支持。

    OutFormat = str。输出栅格格式，默认为 'GTiff'。其他格式详见 ToOtherFormat 函数。

    '''

    if OutFormat == 'GTiff' and BitDepth is not None:
        RCOptions = key.GetGTiffOptions(NBITS = BitDepth)
    else:
        RCOptions = key.GenRCOptions(OutFormat)

    MemoryLimit = psutil.virtual_memory().free * 0.8

    Options = gdal.WarpOptions(format = OutFormat,
                               creationOptions = RCOptions,
                               outputType = DataType,
                               warpMemoryLimit = MemoryLimit,
                               callback = gdal.TermProgress_nocb)

    gdal.Warp(OutFile, InFile, options = Options)

    GenerateOVR(OutFile)




