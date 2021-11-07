#We use just-in-time importing here to improve load times
#Here are the imports:
#import plotly.express as px
#import matplotlib.pyplot as plt
from MLVisualizationTools.backend import GraphData, GraphDataTypes

class WrongDataFormatException(Exception):
    pass

def plotlyGrid(data: GraphData, x: str, y: str, output="Output", title="", key=True):
    """
    Calls px.scatter_3d with data. Returns a plotly figure.

    :param data: pandas dataframe with cols x, y, and output. Color is optional
    :param x: xcol in df
    :param y: ycol in df
    :param output: zcol in df
    :param title: Title for graph
    :param key: Show a key for the colors used
    """
    try:
        import plotly.express as px
    except:
        raise ImportError("Plotly is required to use this graph. Install with `pip install plotly`")

    if data.datatype != GraphDataTypes.Grid:
        raise WrongDataFormatException("Data was not formatted in grid.")

    df, colorkey, cdm, co, showlegend = data.compileColorizedData()

    fig = px.scatter_3d(df, x, y, output, color=colorkey, color_discrete_map=cdm,
                        category_orders=co, title=title)
    fig.update_layout(showlegend=showlegend and key)
    return fig

def plotlyAnimation(data: GraphData, x: str, y: str, anim:str, output="Output", title="", key=True):
    """
    Calls px.scatter_3d with data and animation frame. Returns a plotly figure.

    :param data: pandas dataframe with cols x, y, anim, and output. Color is optional
    :param x: xcol in df
    :param y: ycol in df
    :param anim: column for animation
    :param output: zcol in df
    :param title: Title for graph
    :param key: Show a key for the colors used
    """
    try:
        import plotly.express as px
    except:
        raise ImportError("Plotly is required to use this graph. Install with `pip install plotly`")

    if data.datatype != GraphDataTypes.Animation:
        raise WrongDataFormatException("Data was not formatted in animation.")

    df, colorkey, cdm, co, showlegend = data.compileColorizedData()

    fig = px.scatter_3d(df, x, y, output, animation_frame=anim, color=colorkey, color_discrete_map=cdm,
                        category_orders=co,
                        title=title, range_z=[data.dataframe[output].min(), data.dataframe[output].max()])

    fig.update_layout(showlegend=showlegend and key)
    return fig

def matplotlibGrid(data: GraphData, x: str, y: str, output="Output", title=""):
    """
    Calls ax.scatter with data. Returns a plt instance, a fig, and the ax.

    :param data: pandas dataframe with cols x, y, and output. Color is optional
    :param x: xcol in df
    :param y: ycol in df
    :param output: zcol in df
    :param title: Title for graph
    """
    try:
        import matplotlib.pyplot as plt
    except:
        raise ImportError("Matplotlib is required to use this graph. Install with `pip install matplotlib`")

    if data.datatype != GraphDataTypes.Grid:
        raise WrongDataFormatException("Data was not formatted in grid.")

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    df, color, cdm, co, showlegend = data.compileColorizedData()

    if color is not None:
        color = df[color]

    ax.scatter(df[x], df[y], df[output], c=color)
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    ax.set_zlabel(output)
    ax.set_title(title)

    return plt, fig, ax