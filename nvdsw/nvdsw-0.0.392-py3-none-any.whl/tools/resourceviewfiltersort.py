#!/usr/bin/env python3
#
# coding: utf-8

# Copyright (c) 2019-2020, NVIDIA CORPORATION.  All Rights Reserved.
#
# NVIDIA CORPORATION and its licensors retain all intellectual property
# and proprietary rights in and to this software, related documentation
# and any modifications thereto.  Any use, reproduction, disclosure or
# distribution of this software and related documentation without an express
# license agreement from NVIDIA CORPORATION is strictly prohibited.
#

"""
displays resources, local and remote
"""

import gi
from treeviewfiltersort import TreeViewFilterSort

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class ResourceTreeViewFilterSort(TreeViewFilterSort):
    """Structure for resources, local and remote"""

    column_names = (
        "Name",
        "Status",
        "Type",
        "Image name",
        "Tag",
        "GPUs",
        "Ports",
        "Volumes",
        "Created",
        "Actions",
    )
    column_types = (str, str, str, str, str, str, str, str, str, str)

    column_resizable_flags = (
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        False,
    )
    column_sortable_flags = (
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        False,
    )
    init_column_visibilities = (
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
    )

    # initially, sort by the created column
    init_sort_column_id = 8

    def __init__(self):
        super().__init__(
            (
                self.column_names,
                self.column_types,
                self.column_resizable_flags,
                self.column_sortable_flags,
                self.init_column_visibilities,
                self.init_sort_column_id,
            )
        )

    def append_row(self, res, menu_item):
        """construct a row out of a pair of resource and menu item objects"""
        datarow = (
            res["name"],
            res["status"],
            res["rtype"],
            menu_item["name"],
            res["tag"],
            self._gpus2text(res["gpus"]),  # need to convert this to string
            self._ports2text(res["ports"]),  # need to convert this to string
            self._volumes2text(res["volumes"]),  # need to convert this to string
            self._make_buttons(res["status"]),  # need to make buttons here
        )
        return self.append_datarow(datarow)

    def _gpus2text(self, gpus):
        """convert the list of gpus to something we can display"""
        if gpus is None:
            return ""

        return "\n".join(gpus)

    def _ports2text(self, ports):
        """convert the port information to something we can display along with clickable links"""

        # if len(local_resource["ports"]) == 0 or len(local_resource["ports"]) == 1:
        #             if len(local_resource["ports"]) == 1:
        #                 port = list(local_resource["ports"].items())[0]
        #                 ports_label = (
        #                     "<a href='http://localhost:"
        #                     + port[1]
        #                     + "/lab'>"
        #                    + self.ports2str(port)
        #                    + "</a>"
        #                )
        #                 l = Gtk.Label()
        #                 l.set_markup(ports_label)
        #             else:
        #                 l = Gtk.Label(label="")

        #        c = port_tuple[0]
        #        h = port_tuple[1]
        #        pstr = c.split("/")[0] + ":" + h
        #        return pstr
        return ""

    def _volumes2text(self, volumes):
        """convert the volumes information to something we can display"""
        return ""

    def _make_buttons(self, status):
        """based on the resource status, create the appropriate action buttons"""
        return ""
