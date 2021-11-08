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

import dataclasses as dtcl
from multiprocessing import Process as process_t
from typing import Any, Dict, Optional, Sequence, Tuple, Union

import vedo.colors as clrs
from vedo import Plotter as vedo_figure_t

from cell_tracking_BC.in_out.graphics.context import axes_t as abstract_axes_t
from cell_tracking_BC.in_out.graphics.context import colormap_h
from cell_tracking_BC.in_out.graphics.context import figure_t as base_figure_t
from cell_tracking_BC.in_out.graphics.context import rgb_color_h, rgba_color_h
from cell_tracking_BC.in_out.graphics.dbe.vedo.style import (
    COLOR_DEFAULT_CELL_NNTT,
    COLOR_HIGHLIGHT_CELL_NNTT,
)


STYLE_DEFAULT_CELL = {"color": COLOR_DEFAULT_CELL_NNTT}

_BBOX_AXES_MARGIN = 0.1


@dtcl.dataclass(init=False, repr=False, eq=False)
class figure_t(vedo_figure_t, base_figure_t, abstract_axes_t):

    bbox: Sequence[Sequence[float]] = None

    def UpdateBBoxFromOne(self, new_point: Sequence[float], /) -> None:
        """"""
        if self.bbox is None:
            self.bbox = (new_point, new_point)
        else:
            minima = [min(_new, _old) for _new, _old in zip(new_point, self.bbox[0])]
            maxima = [max(_new, _old) for _new, _old in zip(new_point, self.bbox[1])]
            self.bbox = (minima, maxima)

    def UpdateBBoxFromMany(
        self, exc_s: Sequence[float], why_s: Sequence[float], zee_s: Sequence[float], /
    ) -> None:
        """"""
        minima = [min(exc_s), min(why_s), min(zee_s)]
        maxima = [max(exc_s), max(why_s), max(zee_s)]
        if self.bbox is not None:
            minima = [min(_new, _old) for _new, _old in zip(minima, self.bbox[0])]
            maxima = [max(_new, _old) for _new, _old in zip(maxima, self.bbox[1])]
        self.bbox = (minima, maxima)

    @property
    def bbox_extent(self) -> Sequence[float]:
        """"""
        return tuple(_max - _min for _min, _max in zip(*self.bbox))

    @property
    def bbox_origin_and_corner(self) -> Tuple[Sequence[float], Sequence[float]]:
        """"""
        extent = self.bbox_extent
        output = tuple(
            (_min - _BBOX_AXES_MARGIN * _xtt, _max + _BBOX_AXES_MARGIN * _xtt)
            for _min, _max, _xtt in zip(self.bbox[0], self.bbox[1], extent)
        )

        return tuple(zip(*output))

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

        def Colormap(
            value: Union[float, Sequence[float]], /
        ) -> Union[rgba_color_h, Sequence[rgba_color_h]]:
            """"""
            if isinstance(value, Sequence):
                return tuple(Colormap(_vle) for _vle in value)

            n_milestones = milestones.__len__()
            m_idx = 0
            while (m_idx < n_milestones) and (value > milestones[m_idx][0]):
                m_idx += 1
            if m_idx >= n_milestones:
                color = milestones[-1][1]
            elif value < milestones[m_idx][0]:
                if m_idx > 0:
                    previous = m_idx - 1
                else:
                    previous = 0
                interval = (milestones[previous][1], milestones[m_idx][1])
                interval = (clrs.getColor(_clr) for _clr in interval)
                ratio = (value - milestones[previous][0]) / (
                    milestones[m_idx][0] - milestones[previous][0]
                )
                color = tuple(
                    ratio * _end + (1.0 - ratio) * _stt for _stt, _end in zip(*interval)
                )
            else:
                color = milestones[m_idx][1]

            if isinstance(color, str):
                color = clrs.getColor(color)
            color = (*color, 1.0)

            return color

        return Colormap

    def Show(
        self,
        /,
        *,
        interactively: bool = True,
        in_main_thread: bool = True,
    ) -> None:
        """"""
        if in_main_thread:
            self.show().close()
        else:
            thread = process_t(target=lambda: self.show().close())
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
