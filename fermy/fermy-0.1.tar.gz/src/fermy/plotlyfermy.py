"""
Created the 2021/10/13
v0.0 First version
v0.1 Add link with pandasfermy
v0.2 Add control chart graph
v0.3 Add powerfoce option to control chart and bug fix if no vialtion of rules

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

__version__ = 0.3


import pandas as pd
from typing import List, Dict, Iterable, Tuple, Union
import plotly.express as px
import plotly.graph_objects as go  # only for multi y plot
import os
import argparse
import numpy as np

#layout
layoutdic = dict(modebar_add=["v1hovermode", "toggleSpikeLines"],
                    title='Fermentation data',
                    xaxis_title="Time (in hours)",
                    yaxis_title="Growth proxy",
                    font=dict(
                        family='Linux Libertine, Times New Roman',
                        size = 20,
                        color='#000'
                    ),
                    legend=dict(
                        title=dict(text="Bioreactors",side="top"),
                        x=0,
                        y=-0.2,
                        orientation="h",
                        font=dict(
                            family='Linux Libertine, Times New Roman',
                            size = 10,
                            color='#000'
                        ),
                        traceorder="normal"  # "normal" or "grouped"
                    ),
                        updatemenus=[
                            dict(
                                buttons=list([
                                    dict(label="Linear",  
                                        method="relayout", 
                                        args=[{"yaxis.type": "linear", "yaxis.title" : f"Growth proxy"}]),
                                    dict(label="Log", 
                                        method="relayout", 
                                        args=[{"yaxis.type": "log", "yaxis.title" : f"ln(Growth proxy)"}])
                                  ]),
                                x=0.5,
                                y=1.5,
                                  ),
                                  {'type': 'buttons',
                    "showactive":True,
                    "x" : 0.6,
                    "y" : 1.5,
                    'buttons': [{'label': 'Legend',
                                'method': 'relayout',
                                'args': ['showlegend', True],
                                'args2': ['showlegend', False]}],
                    }
                                  
                                  
                                  ]
                )



class ParseKwargs(argparse.Action):
    """Class to add deal with dict as arg in argparse
    """
    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, dict())
        for value in values:
            key, value = value.split('=')
            getattr(namespace, self.dest)[key] = value



def basicplot(data: pd.DataFrame, path:str=""):
    """Plot all columns of a Dataframe as Y and index for x
    """
    fig = px.line(data, x=data.index, y=data.columns, markers=True)
    fig.update_layout(layoutdic, template="simple_white")
    if path != "":
        fig.write_html(os.path.splitext(path)[0]+"_sfgraph.html")
    fig.show()


dicoyrule = {'119080 main' : "y", 'LaPaDa DEX 36' : "y2"}

def multiyplot(data: pd.DataFrame, path:str="", groupbyferm:bool = True):
    """Plot all columns of a Dataframe with multiY  axis and index for x
    if groupbyferm = True legend is group by file (fermentation) else
    it is group by parameters
    """
    fig = go.Figure()  # creat an empty fig
    
    #dicorule e.g. {pH : "y", temperaure : "y2"...}
    dicoyrule = {}
    for index, param in enumerate(list(set(dicogroupaxes.values()))):
        if index == 0:
            dicoyrule[param] = "y"
        else:
            dicoyrule[param] = f"y{index+1}"
    #dicogroupaxes e.g. {"pH-bio1" : "pH"}
    #dicoy e.g. {"pH-bio1" : y}
    dicogroupaxes ={}
    dicoy = {}
    for header in data.columns.tolist():
        dicogroupaxes[header] = header.split("-")[0]
        dicoy[header] = dicoyrule[header.split("-")[0]]
    #dicogroupferm e.g. {"pH-bio1" : "bio1"}
    dicogroupferm = {}
    for header in data.columns.tolist():
        if len(header.split("-")) > 1:
            dicogroupferm[header] = header.split("-")[1]
    
    
    for column in data.columns:
        if groupbyferm:
            fig.add_trace(go.Scatter(x=data.index, y=data[column], name=column, line=dict(dash = 'dash', width = 1), visible='legendonly', legendgroup=dicogroupferm[column], yaxis=dicoy[column]))
        else:
            fig.add_trace(go.Scatter(x=data.index, y=data[column], name=column, line=dict(dash = 'dash', width = 1), visible='legendonly', legendgroup=dicogroupaxes[column], yaxis=dicoy[column]))
    
    fig.update_layout(layoutdic, template="simple_white")
    
    fig.update_layout(
    xaxis=dict(),
    yaxis=dict(
        title="yaxis title",
        titlefont=dict(
            color="#1f77b4"
        ),
        tickfont=dict(
            color="#1f77b4"
        )
    ),
    yaxis2=dict(
        title="yaxis2 title",
        titlefont=dict(
            color="#ff7f0e"
        ),
        tickfont=dict(
            color="#ff7f0e"
        ),
        anchor="free",
        overlaying="y",
        side="left",
        position=0.15
    ))
    
    
    fig.show()
    
    
    if path != "":
        fig.write_html(os.path.splitext(path)[0]+"_sfgraph.html")
    fig.show()
    
    
    

def ccplot(data: pd.DataFrame, variableofinterest: str, path:str="", dicorename:Dict={}, forcepower:bool=False) -> pd.DataFrame:
    """
    Function to comput and plot a simple and pretty Control Chart with plotly express
    Data will be columns values of column named variableofinterest and index of the data as index
    if path is provided the graph will be saved in this path
    dicorename allow users to custom names of axis with {"old name" : "desired name"}
    forcepwoer allow users to force scientific notation 10^n for y axis
    return the DataFrame with a new column named CClimitctrl that reccord Control Chart violations
    """
    #basic data to compute LCL, center and UCL
    center = data[variableofinterest].mean()
    std = data[variableofinterest].std()
    nbsigma = [1,2,3]
    
    #color values add column in dataframe if value not ok regarding CC rules
    conditions = [  (data[variableofinterest]>=center+std*3),  # Out-of-control rule 1 > +3 sigma
                    (data[variableofinterest]<=center-std*3), # Out-of-control rule 1 < -3 sigma
                    ((data[variableofinterest] < center) & # Out-of-control rule 2 Nine points in a row -3 sigma
                    (data[variableofinterest].shift(1) < center) &
                    (data[variableofinterest].shift(2) < center) &
                    (data[variableofinterest].shift(3) < center) &
                    (data[variableofinterest].shift(4) < center) &
                    (data[variableofinterest].shift(5) < center) &
                    (data[variableofinterest].shift(6) < center) &
                    (data[variableofinterest].shift(7) < center) &
                    (data[variableofinterest].shift(8) < center)),
                    ((data[variableofinterest] > center) & # Out-of-control rule 2 Nine points in a row +3 sigma
                    (data[variableofinterest].shift(1) > center) &
                    (data[variableofinterest].shift(2) > center) &
                    (data[variableofinterest].shift(3) > center) &
                    (data[variableofinterest].shift(4) > center) &
                    (data[variableofinterest].shift(5) > center) &
                    (data[variableofinterest].shift(6) > center) &
                    (data[variableofinterest].shift(7) > center) &
                    (data[variableofinterest].shift(8) > center)),
                    ((data[variableofinterest].shift(2) >=center+std*2) & # Out-of-control rule 5 Two out of three points in a row +2 sigma
                    (data[variableofinterest].shift(1) >=center+std*2) &
                    (data[variableofinterest] >=center)),
                    ((data[variableofinterest].shift(2) >=center+std*2) & # Out-of-control rule 5 Two out of three points in a row +2 sigma
                    (data[variableofinterest] >=center+std*2) &
                    (data[variableofinterest].shift(1) >=center)),
                    ((data[variableofinterest].shift(2) <=center-std*2) & # Out-of-control rule 5 Two out of three points in a row -2 sigma
                    (data[variableofinterest].shift(1) <=center-std*2) &
                    (data[variableofinterest] <=center)),
                    ((data[variableofinterest].shift(2) <=center-std*2) & # Out-of-control rule 5 Two out of three points in a row -2 sigma
                    (data[variableofinterest] <=center-std*2) &
                    (data[variableofinterest].shift(1) <=center)),
                    ] # create a list of our conditions
    print("\nOut-of-control rule 1: > +3 sigma or < -3 sigma\nOut-of-control rule 2: Nine points in a row -3 sigma or +3 simga\nOut-of-control rule 5: Two out of three points in a row +2 sigma or -2 sigma\n")
    values = ['Out-of-control rule 1', 'Out-of-control rule 1', 'Out-of-control rule 2', 'Out-of-control rule 2', 'Out-of-control rule 5', 'Out-of-control rule 5', 'Out-of-control rule 5', 'Out-of-control rule 5'] # create a list of the values we want to assign for each condition
    #creat a new column with control status
    data['CClimitctrl'] = np.select(conditions, values, default = "Under control")
    # difine color map to unlight out-of-control
    color_discrete_map = {'Out-of-control rule 1': 'rgb(255,0,0)', 'Under control': 'rgb(31,119,180)', 'Out-of-control rule 2': 'rgb(217,75,83)' , 'Out-of-control rule 5' : 'rgb(238,25,154)'}
    #plot Control chart
    fig = px.scatter(data, x=data.index, y=variableofinterest,
                        #size  = variableofinterest, # size as function of a column
                        color = data.CClimitctrl, # color as function of a column
                        color_discrete_map=color_discrete_map, # set color according to user define map
                        #symbol = variableofinterest, # symbol as function of a column
                        title=f"Control Chart",
                        range_y = [center-6*std,center+6*std], # set default limit for Y
                        labels = dicorename,
                        template="simple_white"  # set easy template
                    )
    #Add LCL UCL pretty print
    fig.add_hline(y=center, line_dash="longdashdot", line_color="blue", line_width=1, opacity=1)  #set center
    for sigma in nbsigma:
        if sigma<3:
            fig.add_hline(y=center+sigma*std, line_dash="dash", line_color="red", line_width=1, opacity = sigma/3)  # UCL
            fig.add_hline(y=center-sigma*std, line_dash="dash", line_color="red", line_width=1, opacity = sigma/3)  # LCL
        else:
            fig.add_hline(y=center+sigma*std, line_dash="longdash", line_color="red", line_width=1, opacity = sigma/3)  # UCL
            fig.add_hline(y=center-sigma*std, line_dash="longdash", line_color="red", line_width=1, opacity = sigma/3)  # LCL

    if len(data['CClimitctrl'].unique())<=1:
        fig.update(layout_showlegend=False) #hide legend if all point under control
        batchwithissues = pd.DataFrame()
    else:
        batchwithissues = data.loc[data['CClimitctrl']!="Under control",:]
        fig.update_layout(legend =dict(title=dict(text="Control Chart Violations")))
        
    if forcepower:
        fig.update_yaxes(exponentformat="power")  # force 10^n notation
                # add anotation ULC / AVG / LCL
        #ULC
        fig.add_annotation(
                x=1,
                y=center+3*std,
                xref="paper",
                yref="y",
                text=f"UCL={round(center+3*std,1):0.2E}",
                showarrow = False,
                yshift=10
                )
        #LCL
        fig.add_annotation(
                x=1,
                y=center-3*std,
                xref="paper",
                yref="y",
                text=f"LCL={round(center-3*std,1):0.2E}",
                showarrow = False,
                yshift=10
                )
        #center
        fig.add_annotation(
                x=1,
                y=center,
                xref="paper",
                yref="y",
                text=f"Avg={round(center,1):0.2E}",
                showarrow = False,
                yshift=10
                )
    else:
        # add anotation ULC / AVG / LCL
        #ULC
        fig.add_annotation(
                x=1,
                y=center+3*std,
                xref="paper",
                yref="y",
                text=f"UCL={round(center+3*std,1)}",
                showarrow = False,
                yshift=10
                )
        #LCL
        fig.add_annotation(
                x=1,
                y=center-3*std,
                xref="paper",
                yref="y",
                text=f"LCL={round(center-3*std,1)}",
                showarrow = False,
                yshift=10
                )
        #center
        fig.add_annotation(
                x=1,
                y=center,
                xref="paper",
                yref="y",
                text=f"Avg={round(center,1)}",
                showarrow = False,
                yshift=10
                )
                
    if path != "":
        fig.write_html(os.path.splitext(path)[0]+"_CCgraph.html")
        
    fig.show()
    return batchwithissues

pd.core.base.PandasObject.sfplot = basicplot
pd.core.base.PandasObject.ccplot = ccplot


if __name__ == '__main__':
    """here argparser code"""
    parser = argparse.ArgumentParser(description = "Plotlyfermy add to Fermy method to plot fermentation data", 
    epilog="For Help or more information please contact Nicolas Hardy")
    
    parser.add_argument("filepath", metavar = "Root of data (Excel file)", type = str, help = "File with fermentation data first column have to be time (in datetime or float of hours)")
    parser.add_argument("-s","--save", action='store_true', dest="saved", help = "Option to save graph in the data folder")
    parser.add_argument("-cc", dest="variableofinterest", type = str, default = None, help = "Varaible of interest to use for the control chart creation")
    parser.add_argument('-d', '--dico', dest="dicorename", default= {}, nargs='*', action=ParseKwargs, help = "oldname1=newname1 oldname2=newname2 : is the renaming option format")
    
    
    args = parser.parse_args()
    filepath = args.filepath # filepath = "C:\\Users\\yp6247\\Desktop\\sampledata.xlsx"
    saved = args.saved # saved = True
    variableofinterest = args.variableofinterest
    dicorename = args.dicorename  # load dicorename
    """"code here"""
    data = pd.read_excel(filepath, index_col=0)  #load data with Pandas index have to be datetime.datetime
    if variableofinterest:
        if saved:
            data.ccplot(variableofinterest, path=filepath, dicorename=dicorename)
        else:
            data.ccplot(variableofinterest, dicorename=dicorename)
    else:
        if saved:
            data.sfplot(filepath)
        else:
            data.sfplot()
