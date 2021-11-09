# Copyright CNRS/Inria/UCA
# Contributor(s): Eric Debreuve (since 2021)
#
# eric.debreuve@cnrs.fr
#
# This software is governed by the CeCILL  license under French law and
# abiding by the rules of distribution of free software.  You can  use,
# modify and/ or redistribute the software under the terms of the CeCILL
# license as circulated by CEA, CNRS and INRIA at the following URL
# "http://www.cecill.info".
#
# As a counterpart to the access to the source code and  rights to copy,
# modify and redistribute granted by the license, users are provided only
# with a limited warranty  and the software's author,  the holder of the
# economic rights,  and the successive licensors  have only  limited
# liability.
#
# In this respect, the user's attention is drawn to the risks associated
# with loading,  using,  modifying and/or developing or reproducing the
# software by the user in light of its specific status of free software,
# that may mean  that it is complicated to manipulate,  and  that  also
# therefore means  that it is reserved for developers  and  experienced
# professionals having in-depth computer knowledge. Users are therefore
# encouraged to load and test the software's suitability as regards their
# requirements in conditions enabling the security of their systems and/or
# data to be ensured and,  more generally, to use and operate it in the
# same conditions as regards security.
#
# The fact that you are presently reading this means that you have had
# knowledge of the CeCILL license and that you accept its terms.

from __future__ import annotations

# For using Matplotlib and Mayavi together. /!\ Unfortunately, it does not work so that the Mayavi dbe is currently
# unusable.
import matplotlib  # isort:skip
matplotlib.use('Qt5Agg')  # isort:skip
matplotlib.interactive(True)  # isort:skip

import dataclasses as dtcl
from multiprocessing import Process as process_t
from typing import Any, Dict, Optional, Sequence, Tuple, Union

import vedo.colors as clrs
from mayavi import mlab
from mayavi.core.api import Scene as mayavi_figure_t

import cell_tracking_BC.in_out.graphics.generic.any_d as gnrc
from cell_tracking_BC.in_out.graphics.context import axes_t as abstract_axes_t
from cell_tracking_BC.in_out.graphics.context import colormap_h
from cell_tracking_BC.in_out.graphics.context import figure_t as base_figure_t
from cell_tracking_BC.in_out.graphics.context import rgb_color_h, rgba_color_h
from cell_tracking_BC.in_out.graphics.dbe.mayavi.style import (
    COLOR_DEFAULT_CELL_NNTT,
    COLOR_HIGHLIGHT_CELL_NNTT,
)


STYLE_DEFAULT_CELL = {"color": COLOR_DEFAULT_CELL_NNTT}


@dtcl.dataclass(init=False, repr=False, eq=False)
class figure_t(mayavi_figure_t, base_figure_t, abstract_axes_t):
    @staticmethod
    def ColorAndAlpha(
        color: Union[str, rgb_color_h, rgba_color_h], /, *, convert_to_rgb: bool = False
    ) -> Tuple[Union[str, rgb_color_h], Optional[float]]:
        """"""
        if (is_str := isinstance(color, str)) or (color.__len__() == 3):
            alpha = None
            if is_str and convert_to_rgb:
                color = clrs.getColor(color)
        else:
            alpha = color[-1]
            color = color[:-1]

        return color, alpha

    @staticmethod
    def ColormapFromMilestones(
        milestones: Sequence[Tuple[float, str]], /
    ) -> colormap_h:
        """"""
        return lambda _vle: gnrc.ZeroOneValueToRGBAWithMilestones(
            _vle, milestones, clrs.getColor
        )

    def Show(
        self,
        /,
        *,
        interactively: bool = True,
        in_main_thread: bool = True,
    ) -> None:
        """"""
        if in_main_thread:
            mlab.show()
        else:
            thread = process_t(target=lambda: mlab.show())
            thread.start()

    def Figure(self) -> figure_t:
        """"""
        return self


axes_t = figure_t


def CellAnnotationStyle(highlighted: bool, multi_track: bool, /) -> Dict[str, Any]:
    """"""
    output = STYLE_DEFAULT_CELL.copy()

    if highlighted:
        output["color"] = COLOR_HIGHLIGHT_CELL_NNTT
    else:
        output["color"] = COLOR_DEFAULT_CELL_NNTT

    return output
