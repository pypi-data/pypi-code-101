"""
Created the 2021/10/08
v0.0 First version
v0.1 Update graph by line instead of scatter
v0.2 add multirenaming option
@author: Nicolas Hardy

This file is part of Fermy.

    Fermy is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Fermy is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Fermy.  If not, see <https://www.gnu.org/licenses/>.
"""

__version__ = 0.1


import pandas as pd
import numpy as np
from typing import List, Dict, Iterable, Tuple, Union
import os
import datetime
import argparse

from . import plotlyfermy

def linearareaselection(data: pd.Series, percent: float=0.95) -> pd.Series:
    """"Function to return series that map best lineare area
    return the table wiht na or slope. slopes area where it is linear
    """
    maxslope = data.max() * percent
    return data.where(data>maxslope).dropna()

def EGRAdataselection(data: pd.Series, originaldataset: pd.DataFrame) -> pd.Series:
    """Function to return series that map with EGRA
    return orginialdataset filter by non na data values
    """
    EGRA = originaldataset[data.name].loc[data.dropna().index]  #select data from smooth data matching with EGRA
    return EGRA

def normalizedata(data: pd.Series, regardingmax:bool=True, percentofmax:float=0.05, numberofpointformin:int=5) -> pd.Series:
    """Function to normilized by the average value of first five points not null
    or if regardingmax = True: normilized by percentofmax of maximum value
    if data is low than normalized value put it at 1
    """
    if regardingmax:
        normalvalue = data.max() * percentofmax
        normalizeddata = data/normalvalue
    else:
        normalvalue = data.replace(to_replace=0, value=np.nan).dropna().iloc[:numberofpointformin].mean()
        normalizeddata = data/normalvalue
    normalizeddata = [1 if valeur < 1 else valeur for valeur in normalizeddata]  # if value <1 replace it by 1
    return normalizeddata

def reglin(valuesx: np.ndarray, valuesy: np.ndarray, slopeonly=False) -> Union[float, List[float]]:
    """Minimal linear regression with numpy. You can set slopeonly at True
    to return only slope else return both
    """
    slope, intercept = np.polyfit(valuesx, valuesy, 1)  # deg 1: ax+b
    if slopeonly:
        return slope
    else:
        return [float(slope), float(intercept)]

def calcslope(data: pd.Series, slopeonly=True) -> Union[float, List[float]]:
    """Function to compute slope from a Serie
    return slope or list with slope and intercept
    """
    data.dropna(inplace=True)
    slope = reglin(data.index.values, data.values, slopeonly=slopeonly)
    return slope

def localmax(data: pd.DataFrame) -> pd.Series:
    """Function to found local max of slopes
    """
    peak_df = data[(data.shift(1) < data) & (data.shift(-1) < data)]
    return peak_df


def multireg(data: pd.Series, windows: float=5)-> List[float]:
    """Function to list mu (slope) and lagtime (-intercepts/slope)
    return list of mu, list of lagtime and list of time to mu
    need series and index of slopes
    """
    indexlocalmax = (
            data
            .rolling(5, center=True).apply(calcslope)  # compute rolling slope
            .rolling(windows, center=True).mean()  # smooth to reduce local maximum number
            .to_frame()  # trick because local comput only on DF
            .apply(localmax)
            .dropna().index # Local max index
            )
    listmu = []
    lagtime = None
    firstlagtimeflag = True  #to know if it is the first lagtime
    for slopeindex in indexlocalmax:
        indexlist = []
        slopeindexnum = data.index.get_loc(slopeindex)
        for switchtnum in range(-2,3):
            indexlist.append(slopeindexnum+switchtnum)
        x, y = data.iloc[indexlist].index, data.iloc[indexlist].values
        listmu.append(round(reglin(x,y)[0],2))
        if firstlagtimeflag:
            lagtime = round(-reglin(x,y)[1]/reglin(x,y)[0],2)
            if lagtime:
                firstlagtimeflag = False  # Check if lagtime exist
    return [listmu, lagtime, [round(time, 2) for time in indexlocalmax.to_list()]]


def fanodygrowth(data: pd.DataFrame, percentofmax:float=0.05, usemax:bool=True) -> pd.DataFrame:
    """Function to compute growth rate and lagtime
    It is based on a mix of two algorithms describes in the following publication:
        M. Toussaint, G. Levasseur, J. Gervais-Bird, R. J. Wellinger, S. A. Elela, and A. Conconi.
    A high-throughput method to measure the sensitivity of yeast cells to genotoxic agents in liquid cultures.
    Mutation Research/Genetic Toxicology and Environmental Mutagenesis, 606(1-2):92–105, jul 2006.
        B. G. Hall, H. Acar, A. Nandipati, and M. Barlow. Growth rates made easy. Molecular Biology and Evolution, 31(1):232–238, 2014.
    
    A DataFrame with only data considered as proxy of biomass can be used with time in decimal form as index
    return a DataFrame with lagtime and growth rate
    """
    datatemp = data.copy()
    if isinstance(datatemp.index, pd.DatetimeIndex):
        # set index as derltatime in hours
        datatemp.index = datatemp.index-datatemp.index[0]  # cal detlatime
        datatemp.index = datatemp.index.total_seconds()/3600 #index in hour in decimal format
    elif datatemp.index.dtype == float:
        print("We assumed a DataFrame with float in hours as index")
    else:
        print("Please provide a Dataframe with Datetime as index\n")
    #FanODy algo from table data with decimal deltatime in index and gowth proxy in columns help to Pandas pipe
    #clean data set
    datasmooth = (
        datatemp
        .apply(normalizedata, args=(usemax, percentofmax))  # normalized data by first five point average
        .apply(np.log)  # ln(data/datamin)
        .rolling(window=9, center=True).mean()  # smooth ln(data) window of 9
    )
    
    #found index of slope max
    indexmax = (
    datasmooth
    .rolling(5, center=True).apply(calcslope)  # compute rolling slope
    .idxmax()
    )
    
    #Compute growthrate and lagtime
    fanody = (
        datasmooth
        .rolling(5, center=True).apply(calcslope)  # compute rolling slope
        .apply(linearareaselection, percent=0.95) # selection of relevent slope area as % variation of max slope EGRA
        .apply(EGRAdataselection, args=(datasmooth,))  # selection of relevent data from smotth table to compute µ
        .apply(calcslope, args=(False,)).T  # compute Slope and Intercept and transposed
        .rename(columns = {0:"maximal_growth_rate_per_h", 1 : "lagtime_h"})  # renaming
        .assign(lagtime_h = lambda df: -df["lagtime_h"]/df["maximal_growth_rate_per_h"])  #compute lagtime (basted on intercept already named lagtime
        .assign(maximal_growth_rate_time_h = indexmax)  #add time of mumax
        .round(2)  #round at two decimals
            )
    
    return fanody


def fanodymultiauxic(data:pd.DataFrame, windows:float=5, percentofmax: float=0.05, usemax:bool=True) -> pd.DataFrame:
    """Function to compute growths rates and lagtimes for multiauxies
    from a DataFrame with only data can be used as a proxy of biomass
    It uses algorithms like in fanodygrowth function whereas growth rates are found with local max computation.
    with time in decimal form as index
    return a DataFrame with lagtimes and growth rates
    """
    datatemp = data.copy()
    if isinstance(datatemp.index, pd.DatetimeIndex):
        # set index as derltatime in hours
        datatemp.index = datatemp.index-datatemp.index[0]  # cal detlatime
        datatemp.index = datatemp.index.total_seconds()/3600 #index in hour in decimal format
    elif datatemp.index.dtype == float:
        print("We assumed a DataFrame with float in hours as index")
    else:
        print("Please provide a Dataframe with Datetime as index\n")
    #FanODy algo from table data with decimal deltatime in index and gowth proxy in columns help to Pandas pipe
    #clean data set
    datasmooth = (
        datatemp
        .apply(normalizedata, args=(usemax, percentofmax))  # normalized data by first five point average
        .apply(np.log)  # ln(data/datamin)
        .rolling(window=9, center=True).mean()  # smooth ln(data) window of 9
    )
    
    #compute growthrate and lagtimes for multiauxic growth
    fanodymulti =(
                datasmooth.apply(multireg, args=(windows,)).T # compute Slopes and Intercepts and transposed
                .rename(columns = {0:"maximal_growth_rate_per_h", 1 : "lagtime_h", 2 : "maximal_growth_rate_time_h"})  # renaming
                )
                
                
    return fanodymulti


def builddicorename(DFdata : pd.DataFrame, dicorenamingrullsuserdef: Dict) -> Dict:
    """Function to build a specific rename dicotionary for DataFrame columns names
    input: DFdata a Pandas DataFrame
            dicorull with key as new column name and values differents values possibly present in
            the dataframe
    output: the dictionary to achieve dataframe.rename(columns=builddicorename(dataframe, dicorenamingrullsuserdef), inplace=True)
    """
    columnlist = DFdata.columns.tolist()
    listvalues = list(dicorenamingrullsuserdef.values())
    listkeys = list(dicorenamingrullsuserdef.keys())
    dicorename = {}
    for columname in columnlist:
        for index, values in enumerate(listvalues):
            if columname in values:
                dicorename[columname] = listkeys[index]
    return dicorename

def customedrenamefunction(DFdata:pd.DataFrame, dicorenamingrullsuserdef:Dict, inplace:bool=False) -> pd.DataFrame:
    """Function to rename from a dicotionary in forme {"newname" : (possibleoldname1, possibleoldname2)}
    and rename columns in a DFdata like possiblename1 ==> newname
    """
    outDF = DFdata.rename(columns=builddicorename(DFdata, dicorenamingrullsuserdef), inplace=inplace)
    return outDF


pd.core.base.PandasObject.fermgrowth = fanodygrowth # monkey-patch the DataFrame class to add growth rate calculation
pd.core.base.PandasObject.multirename = customedrenamefunction # monkey-patch the DataFrame class to add multiranaming function
pd.core.base.PandasObject.fermmultiaux = fanodymultiauxic # monkey-patch the DataFrame class to add multiphasic growth rates calculation


if __name__ == '__main__':
    """here argparser code"""
    parser = argparse.ArgumentParser(description = "Pandasfermy add to Pandas method to compute analysis on fermentation data", 
    epilog="For Help or more information please contact Nicolas Hardy")
    
    parser.add_argument("filepath", metavar = "Root of data", type = str, help = "File with fermentation data first column have to be time")
    parser.add_argument("-p","--percent", dest="percentofmax", type = float, default = 0.05, help = "Percentage of the maximal value considered as relevant by default it is egal to 0.05 (for 5 percent)")
    parser.add_argument("-m","--min", action='store_false', dest="usemax", help = "Option to use mininaml value for nomalization (like in FanODy) instead of maximal value percentage")
    
    
    args = parser.parse_args()
    
    percentofmax = args.percentofmax
    filepath = args.filepath
    usemax = args.usemax
    """"code here"""
    #load data
    data = pd.read_excel(filepath, index_col=0)  #load data with Pandas index have to be datetime.datetime
    #plot
    #plotlyfermy.basicplot(data, filepath)
    data.sfplot(filepath)
    #use the pandasfermy
    print(usemax)
    print(f"percent of max value for nomalization will be {percentofmax*100}%")
    fanody = data.fermgrowth(percentofmax=percentofmax ,usemax=usemax)
    multiaux = data.fermmultiaux(windows=5,percentofmax=percentofmax, usemax=usemax)
    print(fanody, multiaux)
    #Save data
    fanody.to_excel(os.path.splitext(filepath)[0]+f"{percentofmax}_out.xlsx")
    multiaux.to_excel(os.path.splitext(filepath)[0]+f"{percentofmax}_multiaux_out.xlsx")
