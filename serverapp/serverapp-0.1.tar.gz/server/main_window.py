import sys

from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication, qApp, QLabel, \
    QTableView, QMessageBox

sys.path.append('../')
from server.new_user import RegisterUser
from server.remove_user import DelUserDialog
from server.history_window import HistoryWindow
from server.settings_window import SettingsWindow


class MainWindow(QMainWindow):
    '''Основное окно сервера.'''
    def __init__(self, database, server, config):
        super().__init__()
        self.initUI()
        self.database = database
        self.server_thread = server
        self.config = config

    def initUI(self):
        # Главное окно
        self.setFixedSize(800, 600)
        self.setWindowTitle('Мессенджер. Сервер приложения.')
        # Кнопка выхода
        btn_exit_app = QAction('Выход', self)
        btn_exit_app.setShortcut('Ctrl+Q')
        btn_exit_app.triggered.connect(qApp.quit)
        # Кнопка "Обновить"
        self.btn_active_users_list = QAction('Обновить', self)
        self.btn_active_users_list.setShortcut('F5')
        # Кнопка "История входа"
        self.history = QAction('История клиентов', self)
        # Кнопка "Настройки"
        self.settings = QAction('Настройки сервера', self)
        # Кнопка регистрации пользователя
        self.register = QAction('Регистрация пользователя', self)
        # Кнопка удаления пользователя
        self.user_remove = QAction('Удаление пользователя', self)

        self.toolbar = self.addToolBar('MainBar')
        self.toolbar.addAction(btn_exit_app)
        self.toolbar.addAction(self.btn_active_users_list)
        self.toolbar.addAction(self.history)
        self.toolbar.addAction(self.settings)
        self.toolbar.addAction(self.register)
        self.toolbar.addAction(self.user_remove)

        # Надпись
        self.top_label = QLabel('Список подключенных пользователей', self)
        self.top_label.setFixedSize(500, 15)
        self.top_label.move(15, 40)

        # Таблица
        self.table = QTableView(self)
        self.table.setFixedSize(780, 500)
        self.table.move(10, 60)

        # Инфобар
        self.statusBar()

        # Связываем кнопки с процедурами
        self.btn_active_users_list.triggered.connect(self.users_table_view)
        self.history.triggered.connect(self.show_history)
        self.settings.triggered.connect(self.server_config)
        self.register.triggered.connect(self.reg_user)
        self.user_remove.triggered.connect(self.rem_user)

        self.timer = QTimer()
        self.timer.timeout.connect(self.users_table_view)
        self.timer.start(1000)

        self.show()
        self.statusBar().showMessage('Сервер работает')

    def users_table_view(self):
        '''Заполнение таблицы активных пользователей.'''
        active_users_list = self.database.user_active_list()
        view = QStandardItemModel()
        view.setHorizontalHeaderLabels(
            ['Имя пользователя', 'IP-адрес', 'Порт', 'Время подключения'])

        # Заполняем таблицу из базы данных
        for row in active_users_list:
            username, ip, port, time = row

            username = QStandardItem(username)
            username.setEditable(False)

            ip = QStandardItem(ip)
            ip.setEditable(False)

            port = QStandardItem(str(port))
            port.setEditable(False)

            time = QStandardItem(str(time.replace(microsecond=0)))
            time.setEditable(False)

            view.appendRow([username, ip, port, time])

        self.table.setModel(view)
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()

    def show_history(self):
        '''Cоздание окна с данными по количеству сообщений клиентов.'''
        global stat_win
        stat_win = HistoryWindow(self.database)
        stat_win.show()

    def server_config(self):
        '''Cоздание окна с настройками сервера.'''
        global config_win
        config_win = SettingsWindow(self.config)

    def reg_user(self):
        '''Создание окна регистрации пользователя.'''
        global reg_window
        reg_window = RegisterUser(self.database, self.server_thread)
        reg_window.show()

    def rem_user(self):
        '''Создание окна удаления пользователя.'''
        global rem_win
        rem_win = DelUserDialog(self.database, self.server_thread)
        rem_win.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    message = QMessageBox
    dial = MainWindow()

    app.exec_()
