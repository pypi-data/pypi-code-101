# -*- coding:utf-8 -*-
import pandas as pd
import plotly.graph_objects as go

def genScatters(fn, tags, xDataArr, yDataArr, modes, isShow):
    fig = go.Figure()
    
    for i in range(len(tags)):
        fig.add_trace(go.Scatter(x=xDataArr[i], y=yDataArr[i],
                            mode=modes[i],
                            name=tags[i]))

    if fn and isinstance(fn, str):
        fig.write_html(fn)
    
    if isShow:
        fig.show()

def genDataFrameScattersWithColumn(df, colName, addTags, xCols, yCols, fn, mode, isShow):
    lstTags = df[colName].unique()
    
    tags = []
    xs = []
    ys = []
    modes = []
    for i in range(len(lstTags)):
        for j in range(len(addTags)):
            tags.append('{} {}'.format(lstTags[i], addTags[j]))
            xs.append(df[df[colName] == lstTags[i]][xCols[j]].values)
            ys.append(df[df[colName] == lstTags[i]][yCols[j]].values)
            modes.append(mode)
            
    genScatters(fn, tags, xs, ys, modes, isShow)
