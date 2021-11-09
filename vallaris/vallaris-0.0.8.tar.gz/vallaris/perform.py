################# Vallaris map ##################
############## By : sattawat arab ###############
###### GIS Analyst End Backend Engineer #########
########### i-bitz company limited ##############
##################### 2020 ######################

import time
import tempfile
import os
import json
import requests
from geopandas import GeoSeries
from shapely.geometry import Polygon
import geopandas as gpd
import pandas as pd
from shapely.geometry import Polygon
from vallarismaps.utils import *


def setEnviron(storage, parameter):
    print("Set Environ")
    # os.environ["APIKey"] = str(APIKey)
    # os.environ["vallarisApikey"] = str(APIKey)

# def getAPIKey():
#     return  os.environ["vallarisApikey"]


def getInputValue(storage, parameter):
    try:
        msgOption = parameter
        input = msgOption['process']['inputs']['input'][0]['input']
        return input
    except Exception as e:
        print(e)
        input = False
        return input


def getParamValue(storage, parameter):
    try:
        msgOption = parameter
        param = msgOption['process']['inputs']['parameter'][0]['input']
        return param
    except Exception as e:
        print(e)
        param = False
        return param


def getCollectionValue(storage, parameter):
    try:
        msgOption = parameter
        collection = msgOption['process']['inputs']['input'][0]['input']
        dataset_id = collection[0]['value']
        VallarisServer = os.environ["VallarisServer"]
        Api_Key = os.environ["APIKey"]

        dataCollection = getData(storage, dataset_id, VallarisServer, Api_Key)

        if dataCollection != "something wrong":
            input = dataCollection
            return input

        else:
            input = False
            return input
    except Exception as e:
        print(e)
        input = False
        return input


def getExportValue(storage, parameter):
    try:
        msgOption = parameter
        collection = msgOption['id']
        dataset_id = collection
        VallarisServer = os.environ["VallarisServer"]
        Api_Key = os.environ["APIKey"]

        dataExport = getExport(storage, dataset_id, VallarisServer, Api_Key)

        if dataExport != "something wrong":
            return dataExport

        else:
            dataExport = False
            return dataExport

    except Exception as e:
        print(e)
        dataExport = False
        return dataExport


def getImportValue(storage, parameter):
    try:
        msgOption = parameter
        collection = msgOption['id']
        dataset_id = collection
        VallarisServer = os.environ["VallarisServer"]
        Api_Key = os.environ["APIKey"]
        pathFile = os.environ["pathFile"]
        dataImport = getImport(storage, dataset_id,
                               pathFile, VallarisServer, Api_Key)

        if dataImport != "something wrong":
            return dataImport

        else:
            dataImport = False
            return dataImport

    except Exception as e:
        print(e)
        dataImport = False
        return dataImport


def getUpdateFeatures(storage, parameter):
    try:
        msgOption = parameter
        dataset_id = msgOption['collectionId']
        features_id = msgOption['featuresId']
        data = msgOption['geojson']
        VallarisServer = os.environ["VallarisServer"]
        Api_Key = os.environ["APIKey"]
        dataEdit = editFeatures(storage, dataset_id,
                                features_id, data,  VallarisServer, Api_Key)

        if dataEdit != "something wrong":
            return dataEdit

        else:
            dataEdit = False
            return dataEdit

    except Exception as e:
        print(e)
        dataEdit = False
        return dataEdit


def getDeleteFeatures(storage, parameter):
    try:
        msgOption = parameter
        dataset_id = msgOption['collectionId']
        features_id = msgOption['featuresId']
        VallarisServer = os.environ["VallarisServer"]
        Api_Key = os.environ["APIKey"]
        dataDelete = deleteFeatures(
            storage, dataset_id, features_id,  VallarisServer, Api_Key)

        if dataDelete != "something wrong":
            return dataDelete

        else:
            dataDelete = False
            return dataDelete

    except Exception as e:
        print(e)
        dataDelete = False
        return dataDelete


def getNewCollection(storage, parameter):
    try:
        msgOption = parameter
        title = msgOption['title']
        description = msgOption['title']
        itemType = msgOption['itemType']
        VallarisServer = os.environ["VallarisServer"]
        Api_Key = os.environ["APIKey"]

        dataNew = newCollection(
            storage, title, description, itemType, VallarisServer, Api_Key)

        if dataNew != "something wrong":
            return dataNew

        else:
            dataNew = False
            return dataNew

    except Exception as e:
        print(e)
        dataNew = False
        return dataNew


def getUpdateCollection(storage, parameter):
    try:
        msgOption = parameter
        dataset_id = msgOption['id']
        title = msgOption['title']
        description = msgOption['title']
        itemType = msgOption['itemType']
        VallarisServer = os.environ["VallarisServer"]
        Api_Key = os.environ["APIKey"]

        editImport = editCollection(
            storage, dataset_id, title, description, itemType, VallarisServer, Api_Key)

        if editImport != "something wrong":
            return editImport

        else:
            editImport = False
            return editImport

    except Exception as e:
        print(e)
        dataImport = False
        return dataImport


def getdeleteCollection(storage, parameter):
    try:
        msgOption = parameter
        dataset_id = msgOption['id']
        VallarisServer = os.environ["VallarisServer"]
        Api_Key = os.environ["APIKey"]

        deleteData = deleteCollection(
            storage, dataset_id, VallarisServer, Api_Key)

        if deleteData != "something wrong":
            return deleteData

        else:
            deleteData = False
            return deleteData

    except Exception as e:
        print(e)
        deleteData = False
        return deleteData
