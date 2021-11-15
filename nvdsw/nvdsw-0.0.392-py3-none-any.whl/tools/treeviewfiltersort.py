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
        """make column visible"""
        return self.treeview.get_column(column_num).set_visible(flag)

    def append_datarow(self, datarow):
        """append data only"""
        if len(datarow) != self.ncols:
            raise ValueError("datarow has an incorrect dimension")

        self.liststore.append(datarow)

    def remove_all_rows(self):
        """empty out all the data"""
        liter = self.liststore.get_iter_first()
        while liter:
            self.liststore.remove(iter)
            liter = self.liststore.get_iter_first()
