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
Deals with sortable, filterable, resizable columns
"""


import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class TreeViewFilterSort:
    """
    Contains sortable, filterable, resizable columns, both model and view
    """

    def __init__(
        self,
        column_names,
        column_types,
        column_resizable_flags,
        column_sortable_flags,
        init_column_visibility,
        init_sort_column_id,
    ):
        """
        cols:
        column_names
        column_types
        column_sortable flags
        init_column_visibility
        init_sort_column_id
        """

        self.ncols = len(column_names)
        if not (
            self.ncols == len(column_types)
            and self.ncols == len(column_sortable_flags)
            and self.ncols == len(init_column_visibility)
            and self.ncols == len(column_resizable_flags)
        ):
            raise ValueError("params should have the same dimension")

        if init_sort_column_id >= self.ncols:
            raise ValueError("init_sort_column_id is not a valid column")

        self.liststore = Gtk.ListStore(column_types)
        self.treeview = Gtk.TreeView.new_with_model(
            model=Gtk.TreeModelSort(model=self.liststore)
        )
        for i, column_title in enumerate(column_names):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(column_title, renderer, text=i)
            column.set_resizable(column_resizable_flags[i])
            column.set_visible(init_column_visibility[i])
            if column_sortable_flags[i]:
                column.set_sort_column_id(i)

            self.treeview.append_column(column)

        self.treeview.set_sort_column_id(init_sort_column_id)

    def set_visible_column(self, column_num, flag):
        return self.treeview.get_column(column_num).set_visible(flag)

    def append_datarow(self, datarow):
        """append data only"""
        if len(datarow) != self.ncols:
            raise ValueError("datarow has an incorrect dimension")

        self.liststore.append(datarow)

    def remove_all_rows(self):
        """empty out all the data"""
        iter = self.liststore.get_iter_first()
        while iter:
            self.liststore.remove(iter)
            iter = self.liststore.get_iter_first()


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

    def append_resource_row(self, res, menu_item):
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

    def _gpus2text(gpus):
        """convert the list of gpus to something we can display"""
        if gpus is None:
            return ""

        return "\n".join(gpus)

    def _ports2text(ports):
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

    def _volumes2text(volumes):
        """convert the volumes information to something we can display"""
        return ""

    def _make_buttons(status):
        """based on the resource status, create the appropriate action buttons"""
        return ""
