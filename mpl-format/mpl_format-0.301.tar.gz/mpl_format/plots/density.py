import matplotlib.pyplot as plt
from typing import Optional, List, Union

from matplotlib.axes import Axes
from numpy import concatenate
from pandas import DataFrame
from scipy.stats import poisson

from mpl_format.axes import AxesFormatter
from mpl_format.axes.axis_utils import new_axes
from mpl_format.compound_types import Color


def categorical_discrete_values_histogram(
        data: DataFrame,
        x: str, y: str,
        categories: Optional[List[str]] = None,
        colors: Union[Color, List[Color]] = 'k',
        ax: Optional[Axes] = None
):
    """
    Plot a histogram of several categories together.

    :param data: DataFrame with columns x and y
    :param x: Name of the category column. Categories will be found from the
              unique values of this column.
    :param y: Name of the value column. Each value is assumed to be a count,
              and the number of each count value will be counted.
    :param categories: Optional override for categories of x. Use to select a
                       subset of x, or to reorder x.
    :param colors: Single color or list of colors to override default color of
                   each histogram.
    :param ax: Optional matplotlib Axes instance to plot on.
    """
    ax: Axes = ax or new_axes()
    axf = AxesFormatter(ax)
    y_min = data[y].min()
    y_max = data[y].max()
    z = data.groupby([x, y]).size()
    z_max = z.max()
    if categories is None:
        categories = data[x].unique()
    num_cats = len(categories)
    if not isinstance(colors, list):
        colors = [colors] * num_cats
    for c, category, color in zip(
        range(num_cats),
        categories,
        colors
    ):
        cat_hist = z.loc[category, :]
        for (_, y_i), z_i in cat_hist.items():
            axf.add_rectangle(
                width=0.8, height=1,
                x_center=c + 1, y_center=y_i,
                alpha=z_i / z_max,
                color=color
            )
    axf.set_x_lim(0.5)
    axf.set_x_max(len(categories) + 0.5)
    axf.set_y_min(y_min - 1)
    axf.set_y_max(y_max + 1)
    axf.x_ticks.set_values(list(range(1, 1 + len(categories))))
    axf.x_ticks.set_labels(categories)
    axf.set_text(
        x_label=x, y_label=y
    )
    return ax


def do_test_plot():

    p = concatenate([
        poisson(3).rvs(1_000),
        poisson(7).rvs(1_000),
        poisson(10).rvs(1_000)
    ])
    d = DataFrame({
        'y': p,
        'x': ['a'] * 1000 + ['b'] * 1_000 + ['c'] * 1_000
    })
    ax = categorical_discrete_values_histogram(
        data=d, x='x', y='y'
    )
    plt.show()
    ax = categorical_discrete_values_histogram(
        data=d, x='x', y='y', categories=['c', 'a']
    )
    plt.show()
    ax = categorical_discrete_values_histogram(
        data=d, x='x', y='y', categories=['c', 'a'], colors=['r', 'g']
    )
    AxesFormatter(ax).set_axis_below().grid()
    plt.show()


if __name__ == '__main__':

    do_test_plot()
