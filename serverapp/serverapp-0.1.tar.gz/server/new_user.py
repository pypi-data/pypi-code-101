import binascii
import hashlib
import logging

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QPushButton, QLineEdit, QApplication, \
    QLabel, QMessageBox

LOGGER = logging.getLogger('server')


class RegisterUser(QDialog):
    '''Класс диалог регистрации пользователя на сервере.'''

    def __init__(self, database, server):
        super().__init__()

        self.database = database
        self.server = server

        self.setWindowTitle('Регистрация')
        self.setFixedSize(250, 183)
        self.setModal(True)
        self.setAttribute(Qt.WA_DeleteOnClose)

        self.lbl_username = QLabel('Введите имя пользователя:', self)
        self.lbl_username.move(10, 10)
        self.lbl_username.setFixedSize(170, 15)

        self.edit_username = QLineEdit(self)
        self.edit_username.setFixedSize(220, 20)
        self.edit_username.move(10, 30)

        self.lbl_pass = QLabel('Введите пароль:', self)
        self.lbl_pass.move(10, 55)
        self.lbl_pass.setFixedSize(150, 15)

        self.edit_pass = QLineEdit(self)
        self.edit_pass.setFixedSize(220, 20)
        self.edit_pass.move(10, 75)
        self.edit_pass.setEchoMode(QLineEdit.Password)
        self.lbl_ret_pass = QLabel('Повторите пароль:', self)
        self.lbl_ret_pass.move(10, 100)
        self.lbl_ret_pass.setFixedSize(150, 15)

        self.edit_rtrn_pass = QLineEdit(self)
        self.edit_rtrn_pass.setFixedSize(220, 20)
        self.edit_rtrn_pass.move(10, 120)
        self.edit_rtrn_pass.setEchoMode(QLineEdit.Password)

        self.btn_ok = QPushButton('Сохранить', self)
        self.btn_ok.move(20, 150)
        self.btn_ok.clicked.connect(self.save_data)

        self.btn_cancel = QPushButton('Выход', self)
        self.btn_cancel.move(120, 150)
        self.btn_cancel.clicked.connect(self.close)

        self.msg = QMessageBox()

        self.show()

    def save_data(self):
        '''Проверка корректности данных'''
        if not self.edit_username.text():
            self.msg.critical(self, 'Ошибка', 'Не указано имя пользователя.')
            LOGGER.debug(f'Ошибка. Не указано имя пользователя.')
            return
        elif self.edit_pass.text() != self.edit_rtrn_pass.text():
            self.msg.critical(self, 'Ошибка', 'Введённые пароли не совпадают.')
            LOGGER.debug(f'Ошибка. Введённые пароли не совпадают.')
            return
        elif self.database.check_user(self.edit_username.text()):
            self.msg.critical(self, 'Ошибка', 'Пользователь уже существует.')
            LOGGER.debug(f'Ошибка. Пользователь уже существует.')
            return
        else:
            # Генерируем хэш пароля + соль из логина
            pass_bytes = self.edit_pass.text().encode('utf-8')
            salt = self.edit_username.text().lower().encode('utf-8')
            pass_bytes = hashlib.pbkdf2_hmac('sha512', pass_bytes, salt, 10000)
            LOGGER.debug(
                f'Имя пользователя: {self.edit_username.text()}, hash: {binascii.hexlify(pass_bytes)}')
            self.database.add_user(self.edit_username.text(),
                                   binascii.hexlify(pass_bytes))
            self.msg.information(self, 'Успех',
                                 'Пользователь успешно зарегистрирован.')
            LOGGER.info('Пользователь успешно зарегистрирован.')
            # Рассылаем клиентам сообщение о необходимости обновить справичники
            self.server.service_upd_lists()
            self.close()


if __name__ == '__main__':
    app = QApplication([])
    app.setAttribute(Qt.AA_DisableWindowContextHelpButton)
    dial = RegisterUser(None)
    app.exec_()
