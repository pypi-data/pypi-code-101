from typing import List, Dict
import pandas as pd
from os import path

#Backend functions and classes used by the other scripts

def colinfo(data: pd.DataFrame, exclude:List[str] = None) -> List[Dict]:
    """
    Helper function for generating column info dict for a datframe

    :param data: A pandas Dataframe
    :param exclude: A list of data items to exclude
    """
    if exclude is None:
        exclude = []

    coldata = []
    for item in data.columns:
        if item not in exclude:
            coldata.append({'name': item, 'mean': data[item].mean(),
                            'min': data[item].min(), 'max': data[item].max()})
    return coldata

def fileloader(target: str):
    """Specify a path relative to MLVisualizationTools"""
    return path.dirname(__file__) + '/' + target

class GraphDataTypes:
    Grid = 'Grid'
    Animation = 'Animation'

class ColorizerModes:
    NotColorized = "NotColorized"
    Simple = "Simple"
    Binary = "Binary"

class GraphData:
    def __init__(self, dataframe: pd.DataFrame, datatype: GraphDataTypes):
        """Class for holding information about grid or animation data to be graphed."""
        self.dataframe = dataframe
        self.datatype = datatype

        self.colorized = ColorizerModes.NotColorized
        self.truecolor = None
        self.falsecolor = None

        self.truemsg = "Avg. Value is True"
        self.falsemsg = "Avg. Value is False"

    def compileColorizedData(self):
        """
        Process a dataframe for use in a plotly graph.
        Returns a dataframe, a color key, a color_discrete_map, a category order, and a show legend bool
        """
        if self.colorized == ColorizerModes.NotColorized:
            return self.dataframe, None, None, None, False

        elif self.colorized == ColorizerModes.Simple:
            return self.dataframe, 'Color', None, None, False

        elif self.colorized == ColorizerModes.Binary:
            self.dataframe.loc[self.dataframe['Color'] == self.truecolor, 'Color'] = self.truemsg
            self.dataframe.loc[self.dataframe['Color'] == self.falsecolor, 'Color'] = self.falsemsg
            cdm = {self.truemsg: self.truecolor, self.falsemsg: self.falsecolor}
            co = {'Color': [self.truemsg, self.falsemsg]}
            return self.dataframe, 'Color', cdm, co, True
