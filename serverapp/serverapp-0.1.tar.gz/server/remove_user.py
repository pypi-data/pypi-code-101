from PyQt5.QtWidgets import QDialog, QLabel, QComboBox, QPushButton, QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem


class DelUserDialog(QDialog):
    '''
    Диалог выбора контакта для удаления.
    '''
    def __init__(self, database, server):
        super().__init__()
        self.database = database
        self.server = server

        self.setFixedSize(255, 120)
        self.setWindowTitle('Удаление пользователя')
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setModal(True)

        self.lbl_select = QLabel(
            'Выберите пользователя для удаления:', self)
        self.lbl_select.setFixedSize(250, 20)
        self.lbl_select.move(10, 10)

        self.selector = QComboBox(self)
        self.selector.setFixedSize(225, 20)
        self.selector.move(10, 40)

        self.btn_ok = QPushButton('Удалить', self)
        self.btn_ok.setFixedSize(100, 30)
        self.btn_ok.move(127, 75)
        self.btn_ok.clicked.connect(self.remove_user)

        self.btn_cancel = QPushButton('Отмена', self)
        self.btn_cancel.setFixedSize(100, 30)
        self.btn_cancel.move(17, 75)
        self.btn_cancel.clicked.connect(self.close)

        self.all_users()

    def all_users(self):
        '''Заполнение списка пользователей.'''
        self.selector.addItems([item[0]
                                for item in self.database.users_list()])

    def remove_user(self):
        '''Обработчик удаления пользователя.'''
        self.database.remove_user(self.selector.currentText())
        if self.selector.currentText() in self.server.names:
            sock = self.server.names[self.selector.currentText()]
            del self.server.names[self.selector.currentText()]
            self.server.remove_client(sock)
        #Обновление списков клиентов
        self.server.service_upd_lists()
        self.close()

if __name__ == '__main__':
    app = QApplication([])
    dial = DelUserDialog()
    app.exec_()