# -*- coding: utf-8 -*-
"""
Geographic information data processing function package!
=====

Update date: 2021.7.21

"""

import os
# import shutil

from osgeo import gdal, ogr
import numpy as np
from gma.Relation import key

gdal.UseExceptions()

def Split(InFile, OutPath, OutNameField = None, Separator = None, OutFormat = 'ESRI Shapefile'):
    '''
    简介
    ----------
    将矢量文件中的每个要素【拆分】为单个矢量文件。

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
    EXT = key.GetVectorEXTFromDriver(OutFormat)
    

    DataSet = ogr.Open(InFile)
    Layer = DataSet.GetLayer()

    Spat = Layer.GetSpatialRef()

    VectorType = Layer.GetGeomType()

    LayerDefn = Layer.GetLayerDefn()
    FieldCount = LayerDefn.GetFieldCount()

    Feature = Layer.GetNextFeature()
    while Feature:

        if OutNameField is None:
            Fid = Feature.GetFID()
            OutName, OutLayerName = str(Fid), str(Fid)
        else:
            if isinstance(OutNameField, list):
                OutLayerName = Feature.GetFieldAsString(OutNameField[0])
                OutName = ''
                for Name in OutNameField:
                    if OutName != '' and Separator is not None:
                        OutName = OutName + Separator
                    OutName = OutName + Feature.GetFieldAsString(Name)
            else:
                OutLayerName = Feature.GetFieldAsString(OutNameField)
                OutName = OutLayerName

        OutFilePath = os.path.join(OutPath, OutName + EXT)
        while os.path.exists(OutFilePath):
            OutFilePath = OutFilePath.replace(EXT, "_1" + EXT)

        OutData = ogr.GetDriverByName(OutFormat).CreateDataSource(OutFilePath)
        LCOptions = key.GenVCOptions(OutFormat)
        OutLayer = OutData.CreateLayer(OutLayerName, srs = Spat, geom_type = VectorType,
                                       options = LCOptions)

        for FieldIndex in range(FieldCount):

            FieldDefn = LayerDefn.GetFieldDefn(FieldIndex)
            OutLayer.CreateField(FieldDefn)

        # OutLayer = OutData.GetLayer()
        OutLayer.CreateFeature(Feature)
        Feature = Layer.GetNextFeature()

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
    VDataset = ogr.Open(InFile)
    Invalid = {}
    InvalidFeatureCount = 0

    LayerCount = VDataset.GetLayerCount()
    for LNumber in range(LayerCount):

        Layer = VDataset.GetLayerByIndex(LNumber)
        InvalidFID = []

        Feature = Layer.GetNextFeature()
        while Feature is not None:
            FGeometry = Feature.GetGeometryRef()
            if not ogr.Geometry.IsValid(FGeometry):
                InvalidFID.append(Feature.GetFID())

            Feature = Layer.GetNextFeature()

        Invalid.update({Layer.GetName(): InvalidFID})
        InvalidFeatureCount = InvalidFeatureCount + len(InvalidFID)

    if not InvalidFID:
        return 'Pass'
    else:
        Result = {'Invalid number': InvalidFeatureCount, 'Invalid layer&FID': Invalid}
        return Result

def ToRaster(InFile, OutFile, Resolution, Attribute = None, OutNoData = None, OutFormat = 'GTiff'):
    '''
    简介
    ----------
    矢量【转栅格】。

    参数
    ----------
    InFile: str。输入矢量文件路径。

    OutFile: str。输出栅格文件路径。

    **可选参数
    ----------
    Attribute = None。进行转换的矢量数据的字段。如果未设置（None），则生成由 0 和 1 组成的栅格。0 是 nodata 值。

    OutNoData = None。输出栅格的值无效。默认不设置（None）无效值。如果 Attribute 不为 None 且 OutNoData 未设置，则 OutNoData 修改为无穷大（inf）。

    OutFormat = str。输出文件格式，默认为 'ESRI Shapefile'。其他格式详见 ToOtherFormat 函数。

    '''

    if Attribute == None:
        outputType = 1
        burnValues = 1
        OutNoData = 0
        RCOptions = key.GetGTiffOptions(NBITS = 1)

    else:
        outputType = 0
        burnValues = None
        if OutNoData == None:
            OutNoData = np.inf

    RCOptions = key.GenRCOptions(OutFormat)

    Options = gdal.RasterizeOptions(format = OutFormat, outputType = outputType, xRes = Resolution,
                                    yRes = Resolution, creationOptions = RCOptions, attribute = Attribute,
                                    noData = OutNoData, burnValues = burnValues)

    gdal.Rasterize(OutFile, InFile, options = Options)

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

    '''

    LCOptions = key.GenVCOptions(OutFormat)

    Options = gdal.VectorTranslateOptions(format = OutFormat,
                                          dstSRS = Projection,
                                          layerCreationOptions = LCOptions)

    gdal.VectorTranslate(OutFile, InFile, options = Options)

class VectorGEOProcessing:
    
    def __init__(self, InFile, MethodFile, OutFile, OutFormat):
        self.InFile = InFile
        self.MethodFile = MethodFile
        self.OutFile = OutFile
        self.OutFormat = OutFormat
        
        gdal.PopErrorHandler()
        
    def GetLayers(self):
        self.InDataSet = ogr.Open(self.InFile)
        self.InLayer = self.InDataSet.GetLayer()
        InLayerName = self.InLayer.GetName()

        Proj = self.InLayer.GetSpatialRef()
        GeoType = self.InLayer.GetGeomType()

        self.MethodDataSet = ogr.Open(self.MethodFile)
        self.MethodLayer = self.MethodDataSet.GetLayer()
        # MethodProj = self.MethodLayer.GetSpatialRef()

        self.oDS = ogr.GetDriverByName(self.OutFormat).CreateDataSource(self.OutFile)
        LCOptions = key.GenVCOptions(self.OutFormat)

        self.oLayer = self.oDS.CreateLayer(InLayerName, srs = Proj,
                                           geom_type = GeoType, options = LCOptions)

    def Clip(self):
        VectorGEOProcessing.GetLayers(self)
        ogr.Layer.Clip(self.InLayer, self.MethodLayer, self.oLayer,
                       options = ['SKIP_FAILURES=YES', 'PROMOTE_TO_MULTI=YES'],
                       callback = gdal.TermProgress_nocb)

    def Erase(self):
        VectorGEOProcessing.GetLayers(self)
        ogr.Layer.Erase(self.InLayer, self.MethodLayer, self.oLayer,
                        options = ['SKIP_FAILURES=YES', 'PROMOTE_TO_MULTI=YES'],
                        callback = gdal.TermProgress_nocb)

    def Intersection(self):
        VectorGEOProcessing.GetLayers(self)
        ogr.Layer.Intersection(self.InLayer, self.MethodLayer, self.oLayer,
                               options = ['SKIP_FAILURES=YES','PROMOTE_TO_MULTI=YES',
                                          'INPUT_PREFIX=L1_','METHOD_PREFIX=L2_'],
                               callback = gdal.TermProgress_nocb)

    def Union(self):
        VectorGEOProcessing.GetLayers(self)
        ogr.Layer.Union(self.InLayer, self.MethodLayer, self.oLayer,
                        options = ['SKIP_FAILURES=YES','PROMOTE_TO_MULTI=YES',
                                   'INPUT_PREFIX=L1_','METHOD_PREFIX=L2_'],
                        callback = gdal.TermProgress_nocb)

    def Update(self):
        VectorGEOProcessing.GetLayers(self)
        ogr.Layer.Update(self.InLayer, self.MethodLayer, self.oLayer,
                         options = ['SKIP_FAILURES=YES','PROMOTE_TO_MULTI=YES'],
                         callback = gdal.TermProgress_nocb)

def ToOtherFormat(InFile, OutFile, OutFormat = 'ESRI Shapefile'):
    '''
    简介
    ----------
    矢量【格式转换】。

    参数
    ----------
    InFile: str。输入矢量文件路径。

    OutFile: str。输出矢量文件路径。

    **可选参数
    ----------
    OutFormat = str。输出文件格式，默认为 'ESRI Shapefile'。

        其他支持的格式: 'ESRI Shapefile', "FITS", "PCIDSK", "netCDF", "PDS4", "VICAR",
            "PDF", "MBTiles", "BAG", "DB2ODBC", "MapInfo File", "S57",
            "DGN", "Memory", "CSV", "GML", "GPX", "LIBKML", "KML", "GeoJSON",
            "GeoJSONSeq", "OGR_GMT", "GPKG", "SQLite", "ODBC", "WAsP", "MSSQLSpatial",
            "PostgreSQL", "DXF", "FlatGeobuf", "Geoconcept", "GeoRSS", "GPSTrackMaker",
            "PGDUMP", "GPSBabel", "CouchDB", "Cloudant", "ODS", "XLSX",
            "Elasticsearch", "Carto", "AmigoCloud", "Selafin", "JML", "VDV",
            "MVT", "NGW", "MapML", "TIGER"。

    '''

    LCOptions = key.GenVCOptions(OutFormat)

    Options = gdal.VectorTranslateOptions(format = OutFormat,
                                          layerCreationOptions = LCOptions)

    gdal.VectorTranslate(OutFile, InFile, options = Options)
