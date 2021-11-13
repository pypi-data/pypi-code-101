# -*- coding: utf-8 -*-
"""
一些必要的参数。
"""
RasterFormat = {'AAIGrid', 'BT', 'CALS', 'COG', 'DTED', 'EHdr', 'ENVI', 'ERS',
                'EXR', 'FIT', 'GIF', 'GPKG', 'GRIB', 'GS7BG', 'GSAG', 'GSBG',
                'GTiff', 'HDF4Image','HF2', 'HFA', 'ISCE', 'ISIS2', 'ISIS3',
                'JP2OpenJPEG', 'JPEG', 'LAN', 'MBTiles', 'XPM', 'XYZ', 'netCDF',
                'MFF2', 'MRF', 'NITF', 'PAux', 'PCIDSK', 'PCRaster', 'PNG',
                'RST', 'Rasterlite', 'SIGDEM', 'USGSDEM', 'VICAR', 'VRT'}

VectorFormat = {'ESRI Shapefile', 'PCIDSK', 'PDS4', 'PDF', 'MBTiles',
                'MapInfo File', 'Memory', 'CSV', 'GML', 'LIBKML', 'KML',
                'GeoJSON', 'OGR_GMT', 'GPKG', 'SQLite', 'WAsP',
                'FlatGeobuf', 'Geoconcept', 'GeoRSS', 'ODS', 'XLSX',
                'JML', 'VDV', 'MVT', 'MapML'}

DataType = {'未知类型': 0, '8位无符号整型': 1, '16位无符号整型': 2, '16位整型': 3,
            '32位无符号整型': 4, '32位整型': 5, '32位浮点': 6, '64位浮点': 7,
            '16位复整型': 8, '32位复整型': 9, '32位复浮点型': 10, '64位复浮点型': 11}

ResampleMethod = {0: 'Nearest Neighbour', 1: 'Bilinear', 2: 'Cubic', 3: 'CubicSpline',
                  4: 'Lanczos', 5: 'Average', 6: 'RMS', 7: 'Mode'}

FeatureType = {'未知':0,'点':1, '线':2, '面':3, '多点':4, '多线':5, '多面':6}

def GetGTiffOptions(TFW = False, RPB = False, NBITS = None, COMPRESS = 'LZW', BIGTIFF = 'IF_SAFER'):
    '''
    简介
    ----------
    获取创建 GTiff 栅格文件的 【选项】列表!

    参数
    ----------
    TFW = bool。是否生成 ESRI 世界文件（.tfw ）。默认不生成（False）。

    RPB = bool。是否生成（.RPB）文件来描述 RPC（有理多项式系数）。默认不生成（False）。

    NBITS = None 或 int。创建一个传递值。通常与 DISCARD_LSB 一同设置，组成影像位深。默认不设置（None）。

    COMPRESS = 'LZW' 或 其他支持的压缩方式。默认为'LZW'压缩。

        支持的压缩方式包括：'JPEG'，'LZW'，'PACKBITS'，'DEFLATE'，'CCITTRLE'，'CCITTFAX3'，'CCITTFAX4'，
        'LZMA'，'ZSTD'，'LERC'，'LERC_DEFLATE'，'LERC_ZSTD'，'WEBP'等，也可为 'NONE'(不压缩)。

    BIGTIFF = 'IF_SAFER' 或 其他方式。是否生成 BIGTIFF 文件。默认通过估算生成文件大小来确定是否生成 BIGTIFF 文件（'IF_SAFER'）。

        其他方式包括'YES'（是），'NO'（否），'IF_NEEDED'（如果需要。在 压缩 条件下此选项不准确）。

    '''

    RCOptions = []
    if TFW is True:
        RCOptions.append('TFW=YES')

    if RPB is True:
        RCOptions.append('RPB=YES')

    if NBITS is not None:
        RCOptions.append('NBITS=%s' % int(NBITS))
        RCOptions.append('DISCARD_LSB=%s' % int(NBITS))

    RCOptions.append('COMPRESS=%s' % COMPRESS)
    RCOptions.append('BIGTIFF=%s' % BIGTIFF)

    return RCOptions

def GenRCOptions(Format):
    '''根据栅格格式生成创建选项。'''
    if Format == 'GTiff':
        return GetGTiffOptions()
    elif Format == 'HFA':
        return ['COMPRESSED=YES']
    elif Format == 'netCDF':
        return ['COMPRESS=DEFLATE', 'FORMAT=NC4C']
    elif Format == 'NITF':
        return ['IC=C8']
    else:
        return []

def GetRasterEXTFromDriver(Driver):

    '''根据栅格驱动名称输出扩展名。'''

    if Driver == 'GTiff' or Driver == 'COG':
        EXT = '.tif'
    elif Driver == 'HFA':
        EXT = '.img'
    elif Driver == 'JPEG':
        EXT = '.jpg'
    elif Driver == 'netCDF':
        EXT = '.nc'
    elif Driver == 'HDF4Image':
        EXT = '.hdf'
    elif Driver == 'JP2OpenJPEG':
        EXT = '.jp2'
    elif Driver == 'ENVI':
        EXT = '.dat'
    elif Driver == 'AAIGrid':
        EXT = '.asc'
    elif Driver == 'EHdr':
        EXT = '.bil'
    elif Driver == 'CALS':
        EXT = '.cal'
    elif Driver == 'ISIS3':
        EXT = '.cub'
    elif Driver == 'USGSDEM':
        EXT = '.dem'
    elif Driver == 'Rasterlite':
        EXT = '.db'
    else:
        EXT = '.%s' % Driver.lower()

    return EXT

def GetVectorEXTFromDriver(Driver):

    '''根据矢量驱动名称输出扩展名。'''

    if Driver == 'ESRI Shapefile':
        EXT = '.shp'
    elif Driver == 'FlatGeobuf':
        EXT = '.fgb'
    elif Driver == 'Geoconcept':
        EXT = '.gxt'
    elif Driver == 'LIBKML':
        EXT = '.kml'
    elif Driver == 'PGDUMP':
        EXT = '.sql'
    elif Driver == 'MapInfo File':
        EXT = '.tab'
    elif Driver == 'Geoconcept':
        EXT = '.txt'
    elif Driver == 'PDS4':
        EXT = '.xml'
    else:
        EXT = '.%s' % Driver.lower()

    return EXT


def GetSHPOptions(ENCODING = 'UTF-8',
                  RESIZE = True,
                  LIMIT_2GB = False,
                  SPATIAL_INDEX = False
                  ):
    '''
    简介
    ----------
    获取创建 ESRI Shapefile 矢量文件的 【选项】列表!

    参数
    ----------
    ENCODING = 'UTF-8' 或 其他格式。创建矢量文件的字段编码。默认为'utf-8'。

        其他格式 可参考 'https://baike.baidu.com/item/%E5%AD%97%E7%AC%A6%E7%BC%96%E7%A0%81/8446880?fr=aladdin'。

    RESIZE = bool。是否调整字段大小为最佳。默认自动调整（True）。

    LIMIT_2GB = bool。是否强制解除 '.SHP'、'.DBF' 文件2GB大小的限制。默认不解除（False）。

    SPATIAL_INDEX = bool。是否生成空间索引文件（.qix）。默认不生成（False）。

    返回
    ----------
    创建矢量文件选项，类型为列表（list）。

    '''
    LCOptions = []

    LCOptions.append('ENCODING=%s' % ENCODING)

    if RESIZE is True:
        LCOptions.append('RESIZE=YES')

    if LIMIT_2GB is True:
        LCOptions.append('2GB_LIMIT=YES')

    if SPATIAL_INDEX is True:
        LCOptions.append('SPATIAL_INDEX=YES')

    return LCOptions

def GenVCOptions(Format):
    '''根据矢量格式生成创建选项。'''
    if Format == 'ESRI Shapefile':
        return GetSHPOptions()
    else:
        return []




