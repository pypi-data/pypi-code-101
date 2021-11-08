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

from typing import Optional, Sequence, Tuple, Union

import numpy as nmpy
import skimage.measure as msre

from cell_tracking_BC.in_out.graphics.context import (
    _sg,
    annotation_h,
    axes_2d_t,
    axes_3d_t,
)
from cell_tracking_BC.type.frame import frame_t
from cell_tracking_BC.type.segmentation import compartment_t
from cell_tracking_BC.type.sequence import sequence_h, sequence_t
from cell_tracking_BC.type.tracks import tracks_t


array_t = nmpy.ndarray


def AnnotateCells(
    frame: Union[array_t, frame_t],
    cell_contours: Optional[Sequence[array_t]],
    with_cell_labels: bool,
    cell_frame: Optional[frame_t],
    tracks: Optional[tracks_t],
    axes: Union[axes_2d_t, axes_3d_t],
    AnnotationStyle: _sg.cell_annotation_style_h,
    /,
    *,
    highlighted: int = -1,
    elevation: float = None,
) -> Sequence[Tuple[int, annotation_h]]:
    """"""
    output = []

    if with_cell_labels or (tracks is not None):
        if elevation is None:
            axes.RemoveLinesAndAnnotations()

        if cell_frame is None:
            labeled = msre.label(frame, connectivity=1)
            cells = msre.regionprops(labeled)
        else:
            cells = cell_frame.cells
        assert hasattr(cells[0], "centroid") and hasattr(
            cells[0], "label"
        ), "Please contact developer about API change"

        for cell in cells:
            if elevation is None:
                position = nmpy.flipud(cell.centroid)
            else:
                position = (*cell.centroid, elevation)
            text = []
            if with_cell_labels:
                text.append(str(cell.label))
            else:
                text.append("")
            if tracks is None:
                text.append("")
            else:
                labels = tracks.TrackLabelsContainingCell(cell)
                if labels is None:
                    text.append("?")
                else:
                    if labels.__len__() > 1:
                        labels = "\n".join(str(_lbl) for _lbl in labels)
                    else:
                        labels = str(labels[0])
                    text.append(labels)
            text = ",".join(text)

            additionals = AnnotationStyle(cell.label == highlighted, "\n" in text)
            annotation = axes.PlotCellAnnotation(position, text, **additionals)

            output.append((cell.label, annotation))

    # Leave this block after cell annotation since, if placed before, the (new) contours are considered as previous
    # artists and removed.
    if cell_contours is not None:
        if elevation is None:
            for contour in cell_contours:
                axes.PlotLines(
                    contour[:, 1],
                    contour[:, 0],
                    linestyle=":",
                    color=(0.0, 1.0, 1.0, 0.3),
                )
        else:
            for contour in cell_contours:
                heights = contour.shape[0] * [elevation]
                axes.PlotLines(
                    contour[:, 1],
                    contour[:, 0],
                    heights,
                    linestyle=":",
                    color=(0.0, 1.0, 1.0, 0.3),
                )

    return output


def CellContours(
    sequence: sequence_h, with_segmentation: bool, /
) -> Optional[Sequence[Sequence[array_t]]]:
    """"""
    if (
        with_segmentation
        and isinstance(sequence, sequence_t)
        and (sequence.segmentations is not None)
    ):
        output = []
        for segmentation in sequence.segmentations.CompartmentsWithVersion(
            compartment_t.CELL
        ):
            output.append(msre.find_contours(segmentation))
    else:
        output = None

    return output


def CellTracks(sequence: sequence_h, with_track_labels: bool, /) -> Optional[tracks_t]:
    """"""
    with_track_labels = (
        with_track_labels
        and isinstance(sequence, sequence_t)
        and (sequence.tracks is not None)
    )
    if with_track_labels:
        output = sequence.tracks
    else:
        output = None

    return output
