# Libraries
import ctypes
import os
import sys
import traceback
from logging import exception
from math import exp
import typing

import cv2
import numpy as np
import qdarkstyle
import tifffile as tf
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from pyueye import ueye

from .thread_worker import *
from .ueye_camera import IDS_Camera
from .thorlabs import *
from .thorlabs_panel import Thorlabs_Panel
from .ueye_panel import IDS_Panel


class CameraListWidget(QWidget):

    addCamera = pyqtSignal(dict)
    removeCamera = pyqtSignal(dict)

    def __init__(self, parent: typing.Optional['QWidget'] = None):
        super().__init__(parent=parent)

        self.cam_list = None
        self.item_model = QStandardItemModel()

        #  Layout
        self.InitLayout()

    def InitLayout(self):

        # main layout
        self.mainLayout = QVBoxLayout()

        self.cam_table = QTableView()
        self.cam_table.setModel(self.item_model)
        self.cam_table.clearSelection()
        self.cam_table.horizontalHeader().setStretchLastSection(True)
        self.cam_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.ResizeToContents)
        self.cam_table.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows)
        self.cam_table.setSelectionMode(
            QAbstractItemView.SelectionMode.SingleSelection)

        self.HL_buttons = QHBoxLayout()

        self.add_cam = QPushButton(
            "Add Camera", clicked=lambda: self.add_camera())

        self.remove_cam = QPushButton(
            "Remove Camera", clicked=lambda: self.remove_camera())

        self.refresh = QPushButton(
            "Refresh List", clicked=lambda: self.refresh_list())

        self.HL_buttons.addWidget(self.add_cam)
        self.HL_buttons.addWidget(self.remove_cam)
        self.HL_buttons.addWidget(self.refresh)

        self.mainLayout.addWidget(self.cam_table)
        self.mainLayout.addLayout(self.HL_buttons)

        self.setLayout(self.mainLayout)

        self.refresh_list()

    def add_camera(self):
        if len(self.cam_table.selectedIndexes()) > 0:
            cam = self.cam_list[self.cam_table.currentIndex().row()]
            self.addCamera.emit(cam)
            self.refresh_list()
        else:
            QMessageBox.warning(
                self,
                "Warning",
                "Please select a device.",
                QMessageBox.StandardButton.Ok)

    def remove_camera(self):
        if len(self.cam_table.selectedIndexes()) > 0:
            cam = self.cam_list[self.cam_table.currentIndex().row()]
            self.removeCamera.emit(cam)
            self.refresh_list()
        else:
            QMessageBox.warning(
                self,
                "Warning",
                "Please select a device.",
                QMessageBox.StandardButton.Ok)

    def refresh_list(self):
        self.cam_list = IDS_Camera.get_camera_list() + \
            thorlabs_camera.get_camera_list()

        if self.cam_list is None:
            self.cam_list = []
            print('No cameras connected.')

        self.item_model = QStandardItemModel(len(self.cam_list), 8)

        self.item_model.setHorizontalHeaderLabels(
            ["In Use", "Camera ID", "Device ID",
             "Model", "Serial", "Status", "Sensor ID", 'Driver'])

        for i in range(len(self.cam_list)):
            self.item_model.setItem(
                i, 0,
                QStandardItem(str(self.cam_list[i]["InUse"])))
            self.item_model.setItem(
                i, 1,
                QStandardItem(str(self.cam_list[i]["camID"])))
            self.item_model.setItem(
                i, 2,
                QStandardItem(str(self.cam_list[i]["devID"])))
            self.item_model.setItem(
                i, 3,
                QStandardItem(self.cam_list[i]["Model"]))
            self.item_model.setItem(
                i, 4,
                QStandardItem(self.cam_list[i]["Serial"]))
            self.item_model.setItem(
                i, 5,
                QStandardItem(str(self.cam_list[i]["Status"])))
            self.item_model.setItem(
                i, 6,
                QStandardItem(str(self.cam_list[i]["senID"])))
            self.item_model.setItem(
                i, 7,
                QStandardItem(str(self.cam_list[i]["Driver"])))

        self.cam_table.setModel(self.item_model)
