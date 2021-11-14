import os

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, \
    QFileDialog, QMessageBox


class SettingsWindow(QDialog):
    '''Окно настроек приложения сервера.'''
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.initUI()

    def initUI(self):
        '''Настройки окна'''
        self.setFixedSize(365, 245)
        self.setWindowTitle('Настройки сервера')
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setModal(True)

        # Путь до БД

        # Подпись
        self.db_label = QLabel('Путь до базы данных', self)
        self.db_label.setFixedSize(240, 15)
        self.db_label.move(10, 10)
        # Поле ввода пути файла
        self.db_path_input = QLineEdit(self)
        self.db_path_input.setFixedSize(295, 20)
        self.db_path_input.move(10, 30)
        self.db_path_input.setReadOnly(True)
        # Кнопка
        self.db_path_btn = QPushButton('...', self)
        self.db_path_btn.setFixedSize(30, 25)
        self.db_path_btn.move(310, 27)

        # Название БД
        self.db_name_label = QLabel('Название базы данных:', self)
        self.db_name_label.setFixedSize(245, 20)
        self.db_name_label.move(10, 70)

        self.db_name_input = QLineEdit(self)
        self.db_name_input.setFixedSize(120, 20)
        self.db_name_input.move(225, 70)

        # IP-адрес
        self.ip_label = QLabel('Допустимый для приема IP-адреса:', self)
        self.ip_label.setFixedSize(247, 30)
        self.ip_label.move(10, 103)

        self.ip_label2 = QLabel('(пустое, если ограничений нет)', self)
        self.ip_label2.setFixedSize(247, 30)
        self.ip_label2.move(10, 120)

        self.ip_input = QLineEdit(self)
        self.ip_input.setFixedSize(120, 20)
        self.ip_input.move(225, 110)

        # Порт
        self.port_label = QLabel('Номер порта для соединения:', self)
        self.port_label.setFixedSize(247, 30)
        self.port_label.move(10, 150)

        self.port_input = QLineEdit(self)
        self.port_input.setFixedSize(120, 20)
        self.port_input.move(225, 157)

        # Кнопка сохранить
        self.save_btn = QPushButton('Сохранить', self)
        self.save_btn.move(205, 200)

        # Кнопка отменить
        self.cancel_btn = QPushButton('Отменить', self)
        self.cancel_btn.move(75, 200)
        self.cancel_btn.clicked.connect(self.close)

        self.db_path_btn.clicked.connect(self.open_file_dialog)

        self.show()

        self.db_path_input.insert(self.config['SETTINGS']['Database_path'])
        self.db_name_input.insert(self.config['SETTINGS']['Database_file'])
        self.port_input.insert(self.config['SETTINGS']['Default_port'])
        self.ip_input.insert(self.config['SETTINGS']['Listen_Address'])
        self.save_btn.clicked.connect(self.save_server_config)

    def open_file_dialog(self):
        '''Обработчик открытия окна выбора папки.'''
        global dialog
        dialog = QFileDialog(self)
        path = dialog.getExistingDirectory()
        path = path.replace('/', '\\')
        self.db_path_input.insert(path)

    def save_server_config(self):
        '''
        Сохранение настроек.
        Проверяет правильность введённых данных и
        если всё правильно сохраняет ini файл.
        '''
        global config_window
        msg = QMessageBox()
        self.config['SETTINGS']['Database_path'] = self.db_path_input.text()
        self.config['SETTINGS']['Database_file'] = self.db_name_input.text()
        try:
            port = int(self.port_input.text())
        except ValueError:
            msg.warning(self, 'Ошибка', 'Порт должен быть числом')
        else:
            self.config['SETTINGS']['Listen_Address'] = self.ip_input.text()
            if 1023 < port < 65536:
                self.config['SETTINGS']['Default_port'] = str(port)
                dir_path = os.getcwd()
                dir_path = os.path.join(dir_path, '..')
                with open(f"{dir_path}/{'server.ini'}", 'w') as conf:
                    self.config.write(conf)
                    msg.information(
                        self, 'OK', 'Настройки успешно сохранены!')
            else:
                msg.warning(
                    self, 'Ошибка', 'Порт должен быть от 1024 до 65536')
