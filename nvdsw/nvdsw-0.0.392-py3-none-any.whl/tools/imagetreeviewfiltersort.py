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
dispays images
"""

import gi

# from treeviewfiltersort import TreeViewFilterSort

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GObject, GdkPixbuf
import timeago
import datetime
import os
import pathlib

PKG_DIR = str(pathlib.Path(__file__).parent.absolute())


class CRIconClickable(Gtk.CellRendererPixbuf):
    @GObject.Signal(
        flags=GObject.SignalFlags.RUN_LAST,
        return_type=bool,
        arg_types=(
            object,
            Gtk.Widget,
            str,
        ),
        accumulator=GObject.signal_accumulator_true_handled,
    )
    def clickt(self, event, widget, path):
        return True

    def do_activate(self, event, widget, path, background_area, cell_area, flags):
        self.emit("clickt", object(), widget, path)
        return True


# class ImageTreeViewFilterSort(TreeViewFilterSort):
class ImageTreeViewFilterSort:
    """Structure for resources, local and remote"""

    # the last two data columns are button names for the Actions column
    data_column_types = (str, str, str, str, str, GdkPixbuf.Pixbuf, GdkPixbuf.Pixbuf)

    column_names = (
        "Name",
        "Tag",
        "Status",
        "Created",
        "Size",
        "Actions",
    )

    column_resizable_flags = (
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
        False,
    )
    init_column_visibilities = (
        True,
        True,
        True,
        True,
        True,
        True,
    )

    # initially, sort by the created column
    init_sort_column_id = 3

    def __init__(self, conf):
        #
        self.config = conf
        self.liststore = Gtk.ListStore(*self.data_column_types)
        self.treeview = Gtk.TreeView.new_with_model(
            model=Gtk.TreeModelSort(model=self.liststore)
        )

        self._build_view()

    #        super().__init__(
    #            (
    #                self.column_names,
    #                self.column_types,
    #                self.column_resizable_flags,
    #                self.column_sortable_flags,
    #                self.init_column_visibilities,
    #                self.init_sort_column_id,
    #            )
    #        )

    def clear(self):
        return self.liststore.clear()

    def get_treeview(self):
        return self.treeview

    def append_row(self, local_image, tag):
        """construct a row out of a pair of resource and menu item objects"""

        s_created = "None"
        if tag.get("created") is not None:
            s_created = timeago.format(float(tag["created"]), datetime.datetime.now())

        s_size = "None"
        if tag.get("size") is not None:
            # size in GB
            s_size = "{:.1f}".format(tag["size"] / 1024 / 1024 / 1024)

        download_button, action_button = self._make_buttons(local_image, tag)
        datarow = (
            local_image["name"],
            tag["tag"],
            tag["status"],
            s_created,
            s_size,
            download_button,
            action_button,
        )

        self.liststore.append(datarow)
        return

    def _make_buttons(self, local_image, tag):
        """based on the image status, return the list of appropriate buttons"""
        download_icon = None
        action_icon = None
        if tag["status"] == "pulled":
            # action_icon = "edit-delete"
            fname = os.path.abspath(
                PKG_DIR + "/../" + self.config["icons"]["RESOURCE_DELETE"]
            )
            action_icon = GdkPixbuf.Pixbuf.new_from_file_at_scale(
                filename=fname, width=16, height=16, preserve_aspect_ratio=True
            )
        #        b = Gtk.Image.new_from_icon_name("edit-delete", Gtk.IconSize.MENU)
        #        b.connect(
        #            "clicked", self.on_image_delete_clicked, self.local_rt, local_image, tag
        #        )
        #        b.set_tooltip_text("delete image")

        elif tag["status"] == "pulling" or tag["status"] == "queued":
            # action_icon = "media-playback-pause"
            fname = os.path.abspath(PKG_DIR + "/../" + self.config["icons"]["PAUSE"])
            action_icon = GdkPixbuf.Pixbuf.new_from_file_at_scale(
                filename=fname, width=16, height=16, preserve_aspect_ratio=True
            )
        #            b = Gtk.Image.new_from_icon_name("media-playback-pause", Gtk.IconSize.MENU)

        #            b.connect(
        #                "clicked", self.on_image_pause_clicked, self.local_rt, local_image, tag
        #            )
        #            b.set_tooltip_text("pause pull")

        elif tag["status"] == "paused":
            # action_icon = "media-playback-start"
            fname = os.path.abspath(PKG_DIR + "/../" + self.config["icons"]["START"])
            action_icon = GdkPixbuf.Pixbuf.new_from_file_at_scale(
                filename=fname, width=16, height=16, preserve_aspect_ratio=True
            )
        #        b = Gtk.Image.new_from_icon_name("media-playback-start", Gtk.IconSize.MENU)

        #        b.connect(
        #            "clicked",
        #            self.on_image_unpause_clicked,
        #            self.local_rt,
        #            local_image,
        #            tag,
        #        )
        #        b.set_tooltip_text("resume pull")

        elif tag["status"] == "not pulled":
            #     action_icon = "emblem-downloads"
            #            b = Gtk.Button()
            #            b.set_relief(Gtk.ReliefStyle.NONE)
            fname = os.path.abspath(PKG_DIR + "/../" + self.config["icons"]["DOWNLOAD"])
            action_icon = GdkPixbuf.Pixbuf.new_from_file_at_scale(
                filename=fname, width=16, height=16, preserve_aspect_ratio=True
            )
        #            b.set_image(Gtk.Image.new_from_pixbuf(pixbuf))
        #            b.set_tooltip_text("pull image")

        # b.set_image(Gtk.Image.new_from_icon_name('emblem-downloads', Gtk.IconSize.MENU))
        #        b.connect(
        #                "clicked",
        #                self.on_image_download_clicked,
        #                self.local_rt,
        #                local_image,
        #                tag,
        #            )

        if tag["status"] == "pulling":
            ## download_icon = "video-display"
            fname = os.path.abspath(PKG_DIR + "/../" + self.config["icons"]["LOG"])
            action_icon = GdkPixbuf.Pixbuf.new_from_file_at_scale(
                filename=fname, width=16, height=16, preserve_aspect_ratio=True
            )
        #            b = Gtk.Image.new_from_icon_name("video-display", Gtk.IconSize.MENU)
        #            b.set_tooltip_text("build output")
        #            b.connect("clicked", self.on_image_build_log_clicked, local_image, tag)

        return download_icon, action_icon

    def _build_view(self):
        """builds and returns the TreeView object"""

        # The first five columns are just text
        for i in range(0, 5):
            col = Gtk.TreeViewColumn(
                self.column_names[i], Gtk.CellRendererText(), text=i
            )
            col.set_resizable(self.column_resizable_flags[i])
            col.set_visible(self.init_column_visibilities[i])
            if self.column_sortable_flags[i]:
                col.set_sort_column_id(i)
            self.treeview.append_column(col)

        # the 6th column is one or two action buttons
        col = Gtk.TreeViewColumn(self.column_names[5])

        db = CRIconClickable()
        ab = CRIconClickable()
        db.set_property("mode", Gtk.CellRendererMode.ACTIVATABLE)
        ab.set_property("mode", Gtk.CellRendererMode.ACTIVATABLE)
        # db = Gtk.CellRendererPixbuf()
        # ab = Gtk.CellRendererPixbuf()

        col.pack_start(db, True)
        col.pack_start(ab, True)

        # col.add_attribute(db, "icon_name", 5)
        # col.add_attribute(ab, "icon_name", 6)

        col.add_attribute(db, "pixbuf", 5)
        col.add_attribute(ab, "pixbuf", 6)

        self.treeview.append_column(col)

        ### self.treeview.set_sort_column_id(self.init_sort_column_id)
