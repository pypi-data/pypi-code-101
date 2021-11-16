import os
import sys

from AnyQt.QtWidgets import QLineEdit, QFrame, QGridLayout, QPushButton, QMessageBox, QWidget, \
    QHBoxLayout, QVBoxLayout, QSizePolicy as Policy, QLabel

from AnyQt.QtCore import QRect, Qt

from Orange.widgets.widget import OWWidget
from Orange.widgets.utils.widgetpreview import WidgetPreview
from Orange.widgets.settings import Setting

from orangecontrib.blue_whale.i18n_config import *
from orangecontrib.blue_whale.widgets.utils import get_sample_datasets_dir

import requests

__all__ = ['MainWindow']


def __(key):
    return i18n.t("bluewhale.login." + key)


class MainWindow(OWWidget):
    name = __("name")
    want_basic_layout = False
    want_main_area = False
    want_control_area = False
    auto_commit = Setting(False)

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)

        self.__mainLayout = True
        self.__feedbackUrl = None
        self.__feedbackLabel = None

        self.session = args[0] if len(args) > 0 else {}
        self.setupUi()

    def setupUi(self):
        path = os.path.join(get_sample_datasets_dir(), '..', 'icons', 'login-bg.jpg')

        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().setSpacing(0)

        self.__mainLayout = QFrame()
        self.__mainLayout.setLayout(QVBoxLayout())
        self.__mainLayout.setObjectName("Login")
        self.__mainLayout.setSizePolicy(Policy.MinimumExpanding, Policy.MinimumExpanding)
        self.__mainLayout.setStyleSheet("#Login{border-image:url(%s);}" % path)
        self.layout().addWidget(self.__mainLayout)

        self.frame = QFrame(self.__mainLayout)
        self.frame.setStyleSheet("QFrame{background-color:rgb(255,255,255) !important}"
                                 "QFrame{height: 320px}"
                                 "QLineEdit{background-color:rgb(255,255,255) !important}"
                                 'QLineEdit{padding:6px 4px}'
                                 'QLineEdit{border-radius: 4px}'
                                 'QLineEdit{border: 1px solid #e9e9e9}'
                                 'QLineEdit{font-size: 14px}'
                                 'QLabel{font-size:14px}'
                                 'QLabel{color: #000 !important}'
                                 "QPushButton{color:black}"
                                 "QPushButton{height:30px}"
                                 "QPushButton{line-height:30px}"
                                 "QPushButton{border-radius:4px}"
                                 "QPushButton{font-size:14px}"
                                 "QPushButton{margin-top:18px}"
                                 "QPushButton{border:2px}"
                                 )
        self.frame.setGeometry(QRect(146, 96, 480, 320))
        self.frame.setFrameShadow(QFrame.Raised)

        self.frame.setContentsMargins(40, 40, 40, 40)

        user = QLabel(__("user"))
        pwd = QLabel(__("passwd"))
        pwd.setStyleSheet('QLabel{margin-top: 16px}')
        self.userLineEdit = QLineEdit()
        self.userLineEdit.setPlaceholderText(__("user"))
        self.pwdLineEdit = QLineEdit()
        self.pwdLineEdit.setPlaceholderText(__("passwd"))
        self.pwdLineEdit.setEchoMode(QLineEdit.Password)

        gridLayout = QGridLayout(self.frame)
        gridLayout.addWidget(user, 1, 0, 1, 2)
        gridLayout.addWidget(pwd, 3, 0, 1, 2)
        gridLayout.addWidget(self.userLineEdit, 2, 0, 1, 2)
        gridLayout.addWidget(self.pwdLineEdit, 4, 0, 1, 2)

        okBtn = QPushButton(__("sign_in"))
        okBtn.setStyleSheet(
            "QPushButton{background:#1890ff}"
            "QPushButton:hover{background:#00a9fd}"
            "QPushButton{color:#fff}"
        )
        cancelBtn = QPushButton(__("cancel"))
        cancelBtn.setStyleSheet(
            "QPushButton{background:#ccc}"
            "QPushButton:hover{background:#e9e9e9}"
        )

        gridLayout.layout().addWidget(okBtn, 5, 0, 1, 1)
        gridLayout.layout().addWidget(cancelBtn, 5, 1, 1, 1)

        okBtn.clicked.connect(self.accept)
        cancelBtn.clicked.connect(self.reject)

        user_tip = QLabel(textInteractionFlags=Qt.TextBrowserInteraction, openExternalLinks=True, visible=False)
        self.__mainLayout.layout().addWidget(user_tip, alignment=Qt.AlignRight | Qt.AlignBottom)
        self.setFeedbackUrl(url='https://badge.dashenglab.com/security', text=__("user_tip"), attribute=user_tip)

        bottom_bar = QWidget(objectName="bottom-bar")
        bottom_bar.setStyleSheet("background-color: #E8EFF1;")
        bottom_bar_layout = QHBoxLayout()
        bottom_bar_layout.setContentsMargins(20, 10, 20, 10)
        bottom_bar.setLayout(bottom_bar_layout)
        bottom_bar.setSizePolicy(Policy.MinimumExpanding,
                                 Policy.Maximum)

        self.blue_whale = QLabel(textInteractionFlags=Qt.TextBrowserInteraction, openExternalLinks=True, visible=False)
        bottom_bar_layout.addWidget(self.blue_whale, alignment=Qt.AlignLeft | Qt.AlignVCenter)

        self.resource_square = QLabel(textInteractionFlags=Qt.TextBrowserInteraction, openExternalLinks=True,
                                      visible=False)
        bottom_bar_layout.addWidget(self.resource_square, alignment=Qt.AlignCenter | Qt.AlignVCenter)

        self.login = QLabel(textInteractionFlags=Qt.TextBrowserInteraction, openExternalLinks=True,
                            visible=False)
        bottom_bar_layout.addWidget(self.login, alignment=Qt.AlignRight | Qt.AlignVCenter)

        self.layout().addWidget(bottom_bar, alignment=Qt.AlignBottom | Qt.AlignBottom)

        self.setFeedbackUrl(url='https://bw.dashenglab.com', text=__("blue_whale"), attribute=self.blue_whale)
        self.setFeedbackUrl(url='https://bo.dashenglab.com', text=__("resource_square"), attribute=self.resource_square)
        self.setFeedbackUrl(url='https://bo.dashenglab.com/login', text=__("login"), attribute=self.login)
        self.setSizeGripEnabled(False)
        self.setFixedSize(768, 550)

    def setFeedbackUrl(self, url, text, attribute):
        # type: (str) -> None
        """
        Set an 'feedback' url. When set a link is displayed in the bottom row.
        """
        self.__feedbackUrl = url
        if url:
            attribute.setText(
                '<a href="{url}">{text}</a>'.format(url=url, text=text)
            )
        else:
            attribute.setText("")
        attribute.setVisible(bool(url))

    def accept(self):
        url = "https://bo.dashenglab.com/api/oauth/user/login"
        headers = {
            "Grant-Type": "password",
        }
        data = {
            "username": self.userLineEdit.text().strip(),
            "password": self.pwdLineEdit.text().strip()
        }

        try:
            req = requests.post(url, headers=headers, data=data)
        except Exception as e:
            net_err = QMessageBox(
                self, windowTitle=self.tr(__("sign_in_tip")),
                icon=QMessageBox.Question,
                standardButtons=QMessageBox.Yes,
                text=self.tr(__("server_err")),
            )
            net_err.button(QMessageBox.Yes).setText(__("ok"))
            self.userLineEdit.setFocus()
            net_err.show()
        else:
            if req.status_code != 200:
                user_err = QMessageBox(
                    self, windowTitle=self.tr(__("sign_in_tip")),
                    icon=QMessageBox.Question,
                    standardButtons=QMessageBox.Yes,
                    text=self.tr(__("user_err")),
                )
                user_err.button(QMessageBox.Yes).setText(__("ok"))
                user_err.show()
                self.userLineEdit.setFocus()
            else:
                self.session.update({'SESSION': req.cookies.get('SESSION')})
                self.close()


if __name__ == "__main__":
    WidgetPreview(MainWindow).run()
