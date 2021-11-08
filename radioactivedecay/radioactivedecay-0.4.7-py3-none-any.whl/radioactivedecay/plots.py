"""
The plots module defines functions used for creating decay chain diagrams via the Nuclide
class ``plot()`` method, and activity decay graphs via the Inventory class ``plot()`` method.

"""

from typing import List, Set, Optional, Tuple
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


# pylint: disable=too-many-arguments, too-many-locals


def _parse_nuclide_label(nuclide: str) -> str:
    """
    Format a nuclide string to mass number, meta-stable state character in
    superscript, then element symbol. Output is used on node labels in decay
    chain plots.

    Parameters
    ----------
    nuclide : str
        Nuclide string in element-mass format.

    Returns
    -------
    str
        Parsed string for node label in ^{mass}element format.

    """

    if nuclide == "SF":
        return "various"

    nuclide_conversion = {
        "0": "\N{SUPERSCRIPT ZERO}",
        "1": "\N{SUPERSCRIPT ONE}",
        "2": "\N{SUPERSCRIPT TWO}",
        "3": "\N{SUPERSCRIPT THREE}",
        "4": "\N{SUPERSCRIPT FOUR}",
        "5": "\N{SUPERSCRIPT FIVE}",
        "6": "\N{SUPERSCRIPT SIX}",
        "7": "\N{SUPERSCRIPT SEVEN}",
        "8": "\N{SUPERSCRIPT EIGHT}",
        "9": "\N{SUPERSCRIPT NINE}",
        "m": "\N{MODIFIER LETTER SMALL M}",
        "n": "\N{SUPERSCRIPT LATIN SMALL LETTER N}",
        "o": "\N{MODIFIER LETTER SMALL O}",
    }

    element, isotope = nuclide.split("-")
    return "".join(map(lambda char: nuclide_conversion[char], list(isotope))) + element


def _parse_decay_mode_label(mode: str) -> str:
    """
    Format a decay mode string for edge label on decay chain plot.

    Parameters
    ----------
    mode : str
        Decay mode string.

    Returns
    -------
    str
        Formatted decay mode string for use in an edge label.

    """

    mode_conversion = {
        "α": "\N{GREEK SMALL LETTER ALPHA}",
        "β": "\N{GREEK SMALL LETTER BETA}",
        "+": "\N{SUPERSCRIPT PLUS SIGN}",
        "-": "\N{SUPERSCRIPT MINUS}",
    }

    for unformatted, formatted in mode_conversion.items():
        mode = mode.replace(unformatted, formatted)
    return mode


def _check_fig_axes(
    fig_in: Optional[matplotlib.figure.Figure],
    axes_in: Optional[matplotlib.axes.Axes],
    **kwargs,
) -> Tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    """
    Checks to see if user supplies Matplotlib Figure and/or Axes objects. Creates them where
    necessary.

    Parameters
    ----------
    fig_in : None or matplotlib.figure.Figure
        matplotlib figure object to use, or None creates one.
    axes_in : matplotlib.axes.Axes or None, optional
        matplotlib axes object to use, or None creates one.
    **kwargs
        All additional keyword arguments to supply to plt.subplots().

    Returns
    -------
    fig : matplotlib.figure.Figure
        matplotlib figure object used to plot decay chain.
    axes : matplotlib.axes.Axes
        matplotlib axes object used to plot decay chain.

    """

    if fig_in is None and axes_in is None:
        fig, axes = plt.subplots(**kwargs)
    elif fig_in is None:
        axes = axes_in
        fig = axes.get_figure()
    elif axes_in is None:
        fig = fig_in
        axes = fig.gca()
    else:
        fig = fig_in
        axes = axes_in

    return fig, axes


def _decay_graph(
    time_points: np.ndarray,
    ydata: np.ndarray,
    nuclides: List[str],
    xunits: str,
    ylabel: str,
    xscale: str,
    yscale: str,
    ylimits: List[float],
    display: Set[str],
    fig_in: Optional[matplotlib.figure.Figure],
    axes_in: Optional[matplotlib.axes.Axes],
    **kwargs,
) -> Tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    """
    Plots a decay graph showing the change in activity of an inventory over time. Creates
    matplotlib fig, axes objects if they are not supplied. Returns fig, axes tuple.

    Parameters
    ----------
    time_points : numpy.ndarray
        Time points for x-axis.
    ydata : numpy.ndarray
        y-axis data.
    nuclides : list
        List of the nuclides (string format is 'H-3', etc.).
    xunits : str
        Units for decay time axis.
    ylabel : str
        Units for the y-axis
    xscale : str
        The time axis scale type to apply ('linear' or 'log').
    yscale : str
        The y-axis scale type to apply ('linear' or 'log').
    ylimits : list
        Limits for the y-axis (list or numpy.ndarray with two elements).
    display : set of str
        Nuclides to display on the graph.
    fig_in : None or matplotlib.figure.Figure
        matplotlib figure object to use, or None creates one.
    axes_in : matplotlib.axes.Axes or None, optional
        matplotlib axes object to use, or None creates one.
    **kwargs
        All additional keyword arguments to supply to matplotlib plot().

    Returns
    -------
    fig : matplotlib.figure.Figure
        matplotlib figure object used to plot decay chain.
    axes : matplotlib.axes.Axes
        matplotlib axes object used to plot decay chain.

    """

    fig, axes = _check_fig_axes(fig_in, axes_in)

    for idx, label in enumerate(nuclides):
        if label in display:
            axes.plot(time_points, ydata[idx], label=label, **kwargs)
    axes.legend(loc="upper right")
    xlabel = "Time (" + xunits + ")"
    axes.set(
        xlabel=xlabel,
        ylabel=ylabel,
        xscale=xscale,
        yscale=yscale,
    )
    axes.set_ylim(ylimits)

    return fig, axes
