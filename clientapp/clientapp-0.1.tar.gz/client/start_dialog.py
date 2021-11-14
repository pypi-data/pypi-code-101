from PyQt5.QtWidgets import QDialog, QPushButton, QLineEdit, QApplication, \
    QLabel, qApp
from PyQt5.QtCore import QEvent


class UserNameDialog(QDialog):
    '''
    Класс запрашивабщий логин и пароль пользователя.
    '''
    def __init__(self):
        super().__init__()

        self.ok_pressed = False

        self.setWindowTitle('Привет!')
        self.setFixedSize(210, 143)

        self.label = QLabel('Введите имя пользователя:', self)
        self.label.move(10, 10)
        self.label.setFixedSize(180, 10)

        self.client_name = QLineEdit(self)
        self.client_name.setFixedSize(185, 20)
        self.client_name.move(10, 30)

        self.lbl_passwd = QLabel('Введите пароль:', self)
        self.lbl_passwd.move(10, 55)
        self.lbl_passwd.setFixedSize(180, 15)

        self.client_pass = QLineEdit(self)
        self.client_pass.setFixedSize(185, 20)
        self.client_pass.move(10, 75)
        self.client_pass.setEchoMode(QLineEdit.Password)

        self.btn_ok = QPushButton('Начать', self)
        self.btn_ok.move(110, 105)
        self.btn_ok.clicked.connect(self.click)

        self.btn_cancel = QPushButton('Выход', self)
        self.btn_cancel.move(10, 105)
        self.btn_cancel.clicked.connect(qApp.exit)

        self.show()

    def click(self):
        '''Метод обрабтчик кнопки ОК.'''
        if self.client_name.text() and self.client_pass.text():
            self.ok_pressed = True
            qApp.exit()


if __name__ == '__main__':
    app = QApplication([])
    dial = UserNameDialog()
    app.exec_()
