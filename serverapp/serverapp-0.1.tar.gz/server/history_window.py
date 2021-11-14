from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QTableView, QDialog, QPushButton


class HistoryWindow(QDialog):
    '''
    Окно со статистикой пользователей
    '''
    def __init__(self, database):
        super().__init__()
        self.database = database
        self.initUI()

    def initUI(self):
        '''Основное окно'''
        self.setFixedSize(800, 500)
        self.setWindowTitle('История клиентов')
        self.setAttribute(Qt.WA_DeleteOnClose)

        # Список
        self.table = QTableView(self)
        self.table.setFixedSize(780, 450)
        self.table.move(10, 5)

        # Кнопка закрытия
        self.btn_close = QPushButton('Закрыть', self)
        self.btn_close.move(350, 460)
        self.btn_close.clicked.connect(self.close)

        self.create_history()

    def create_history(self):
        '''Заполнение таблицы статистикой сообщений.'''
        history_list = self.database.message_history()

        list = QStandardItemModel()
        list.setHorizontalHeaderLabels(
            ['Клиент', 'Последний вход', 'Отправлено', 'Получено'])
        for el in history_list:
            username, last_login, sent, recvd = el
            username = QStandardItem(username)
            username.setEditable(False)
            last_login = QStandardItem(str(last_login.replace(microsecond=0)))
            last_login.setEditable(False)
            sent = QStandardItem(str(sent))
            sent.setEditable(False)
            recvd = QStandardItem(str(recvd))
            recvd.setEditable(False)

            list.appendRow([username, last_login, sent, recvd])

        self.table.setModel(list)
        self.table.resizeColumnsToContents()
