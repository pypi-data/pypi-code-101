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
import datetime as dttm
import re as regx
from pathlib import Path as path_t
from typing import Sequence, Tuple, Union

import matplotlib.projections as prjs
import matplotlib.pyplot as pypl
import numpy as nmpy
import tifffile as tiff
from matplotlib import rc as SetMatplotlibConfig
from matplotlib.backend_bases import KeyEvent as key_event_t
from matplotlib.backend_bases import MouseEvent as mouse_event_t
from matplotlib.image import AxesImage as axes_image_t
from matplotlib.text import Annotation as annotation_t
from numpy import ndarray as array_t

from cell_tracking_BC.in_out.graphics.context import axes_2d_t as abstract_axes_2d_t
from cell_tracking_BC.in_out.graphics.dbe.matplotlib.any_d import axes_t as axes_anyd_t
from cell_tracking_BC.in_out.graphics.dbe.matplotlib.any_d import (
    figure_t as base_figure_t,
)
from cell_tracking_BC.in_out.graphics.dbe.matplotlib.style import (
    ANNOTATION_SIZE_CELL,
    BBOX_STYLE_DEFAULT_CELL_NNTT,
    BBOX_STYLE_HIGHLIGHT_CELL_NNTT,
    COLOR_DEFAULT_CELL_NNTT,
    COLOR_HIGHLIGHT_CELL_NNTT,
)
from cell_tracking_BC.in_out.graphics.generic.two_d_sequence import (
    s_viewer_2d_t as base_s_viewer_2d_t,
)
from cell_tracking_BC.in_out.graphics.generic.two_d_tracking import (
    t_viewer_2d_t as base_t_viewer_2d_t,
)


pypl_axes_t = pypl.Axes


@dtcl.dataclass(init=False, repr=False, eq=False)
class axes_t(axes_anyd_t, abstract_axes_2d_t):

    name = "ctBC_two_d_axes"
    _image: axes_image_t = None
    PlotPoints = pypl_axes_t.scatter
    PlotLines = pypl_axes_t.plot
    PlotText = pypl_axes_t.text
    PlotAnnotation = pypl_axes_t.annotate

    def SetTimeAxisProperties(self, latest: int, /) -> None:
        """"""
        self.set_xlim(0, latest)
        self.set_xticks(range(latest + 1))
        self.set_xticklabels(str(_idx) for _idx in range(latest + 1))

    def SetAxesPropertiesForTracking(self, tick_positions: Sequence[float], /) -> None:
        """"""
        self.set_xlabel("time points")
        self.set_ylabel("tracks")
        self.yaxis.set_label_position("right")
        self.yaxis.tick_right()
        self.yaxis.set_ticks(tick_positions)

    def PlotCellAnnotation(
        self, position: Tuple[float, float], text: str, /, **kwargs
    ) -> annotation_t:
        """"""
        return self.annotate(
            text,
            position,
            ha="center",
            fontsize=ANNOTATION_SIZE_CELL,
            fontweight="bold",
            **kwargs,
        )

    def PlotImage(
        self, image: array_t, /, *, interval: Tuple[float, float] = None
    ) -> None:
        """"""
        pypl_image = self.matshow(image, cmap="gray")
        if interval is not None:
            pypl_image.set_clim(*interval)

        self._image = pypl_image

    def UpdateImage(
        self,
        picture: array_t,
        /,
        *,
        interval: Tuple[float, float] = None,
        should_update_limits: bool = False,
    ) -> None:
        """"""
        self._image.set_array(picture)
        if should_update_limits:
            self._image.set_clim(*interval)


prjs.register_projection(axes_t)


@dtcl.dataclass(init=False, repr=False, eq=False)
class figure_t(base_figure_t):
    @classmethod
    def NewFigureAndAxes(
        cls, /, *, n_rows: int = 1, n_cols: int = 1, title: str = None
    ) -> Tuple[figure_t, Union[axes_t, Sequence[axes_t], Sequence[Sequence[axes_t]]],]:
        figure, axes = pypl.subplots(
            nrows=n_rows,
            ncols=n_cols,
            FigureClass=cls,
            subplot_kw={"projection": "ctBC_two_d_axes"},
        )

        if title is not None:
            first_axes = axes
            while isinstance(first_axes, Sequence):
                first_axes = first_axes[0]
            first_axes.set_title(title)

        return figure, axes


@dtcl.dataclass(repr=False, eq=False)
class s_viewer_2d_t(base_s_viewer_2d_t):
    def HighlightAnnotation(self, label: int, /, *, should_draw: bool = True) -> None:
        """"""
        if label == self.current_label:
            return

        for annotation in self.annotations:
            text = annotation[1]
            if label == annotation[0]:
                text.set_color(COLOR_HIGHLIGHT_CELL_NNTT)
                if "\n" in text.get_text():
                    text.set_bbox(BBOX_STYLE_HIGHLIGHT_CELL_NNTT)
            else:
                text.set_color(COLOR_DEFAULT_CELL_NNTT)
                if "\n" in text.get_text():
                    text.set_bbox(BBOX_STYLE_DEFAULT_CELL_NNTT)

        self.current_label = label

        if should_draw:
            self.figure.canvas.draw_idle()

    def AddColorbarForImage(self) -> None:
        """"""
        self.figure.colorbar(self.axes._image, ax=self.axes)

    def _ActivateEventProcessing(self, more_than_one: bool, /) -> None:
        """"""
        SetMatplotlibConfig("keymap", save=[])
        self.figure.canvas.mpl_connect("key_press_event", self._OnKeyPress)
        if more_than_one:
            self.figure.canvas.mpl_connect("button_press_event", self._OnButtonPress)
        if self.slider is not None:
            self.figure.canvas.mpl_connect("scroll_event", self._OnScrollEvent)

    def _OnKeyPress(
        self,
        event: key_event_t,
        /,
    ) -> None:
        """"""
        if event.key.lower() == "s":
            print("Sequence saving in progress...")
            volume = self.AsAnnotatedVolume()

            illegal = "[^-_a-zA-Z0-9]"
            version = regx.sub(illegal, "", self.current_version)
            now = regx.sub(illegal, "-", dttm.datetime.now().isoformat())
            path = path_t.home() / f"sequence-{version}-{now}.tif"
            if path.exists():
                print(f"{path}: Existing path; Cannot override")
                return

            tiff.imwrite(
                str(path),
                volume,
                photometric="rgb",
                compression="deflate",
                planarconfig="separate",
                metadata={"axes": "XYZCT"},
            )
            print(f"Annotated sequence saved at: {path}")

    def _OnButtonPress(
        self,
        event: mouse_event_t,
        /,
    ) -> None:
        """"""
        if event.inaxes is self.axes:
            self.ShowNextVersion()
        elif (self.slider is not None) and (event.inaxes is self.slider.ax):
            self.ShowFrame(time_point=self.slider.val, force_update=True)

    def _OnScrollEvent(self, event: mouse_event_t) -> None:
        """"""
        value = self.slider.val
        new_value = round(value + nmpy.sign(event.step))
        new_value = min(max(new_value, self.slider.valmin), self.slider.valmax)
        if new_value != value:
            self.ShowFrame(time_point=new_value)


@dtcl.dataclass(repr=False, eq=False)
class t_viewer_2d_t(base_t_viewer_2d_t):
    def _ShowAnnotation(
        self,
        event: mouse_event_t,
        /,
    ) -> None:
        """"""
        inside, details = self.scatter.contains(event)
        if inside:
            idx = details["ind"][0]
            time_point = self.time_points[idx]
            label = self.labels[idx]

            position = self.scatter.get_offsets()[idx]
            text = f"Time {time_point}\nCell {label}\nPJcd {self.affinities[idx]:.2f}"
            self.annotation.xy = position
            self.annotation.set_text(text)
            self.annotation.set_visible(True)

            self.viewer.ShowFrame(time_point=time_point, highlighted=label)
