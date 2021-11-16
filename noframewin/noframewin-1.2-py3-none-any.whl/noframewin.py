# -*- coding: utf-8 -*-
# @Time : 2021/11/16 9:05
# @Author: ZhangSheng
# @File : noframewin.py
# @Desc: PyCharm

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


class noframewin(QWidget):
    _startPos = None
    _endPos = None
    _isTracking = False

    def __init__(self, width, height):
        super().__init__()
        self._initUI(width, height)

    def _initUI(self, width, height):
        self.setFixedSize(QSize(width, height))
        self.setWindowFlags(Qt.FramelessWindowHint)  # 无边框
        self.show()

    def mouseMoveEvent(self, e: QMouseEvent):  # 重写移动事件
        self._endPos = e.pos() - self._startPos
        self.move(self.pos() + self._endPos)

    def mousePressEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._isTracking = True
            self._startPos = QPoint(e.x(), e.y())

    def mouseReleaseEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._isTracking = False
            self._startPos = None
            self._endPos = None


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = noframewin(400, 400)
    sys.exit(app.exec_())
