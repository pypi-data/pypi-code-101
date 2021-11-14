from PyQt5.QtWidgets import QMainWindow, qApp, QMessageBox, QApplication, \
    QListView
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QBrush, QColor
from PyQt5.QtCore import pyqtSlot, QEvent, Qt
from Cryptodome.Cipher import PKCS1_OAEP
from Cryptodome.PublicKey import RSA
import sys
import json
import logging
import base64

sys.path.append('../')
from common.variables import TEXT, FROM_USER
from client.client_gui import Ui_MainClientWindow
from client.new_contact import AddContactDialog
from client.remove_contact import DelContactDialog

LOGGER = logging.getLogger('client')


class ClientMainWindow(QMainWindow):
    '''
    Главное окно пользователя приложения.
    Содержит логику работы клиентского модуля.
    Базовые элементы созданы при помощи QTDesigner и загружаются из
    файла client_gui.py
    '''
    def __init__(self, database, transport, keys):
        super().__init__()

        self.database = database
        self.transport = transport
        self.decrypter = PKCS1_OAEP.new(keys)

        self.ui = Ui_MainClientWindow()
        self.ui.setupUi(self)

        self.ui.menu_exit.triggered.connect(qApp.exit)
        self.ui.btn_send_msg.clicked.connect(self.send_msg)

        self.ui.btn_add_contact.clicked.connect(self.add_contact_win)
        self.ui.menu_add_contact.triggered.connect(self.add_contact_win)

        self.ui.btn_del_contact.clicked.connect(self.del_contact_win)
        self.ui.menu_rem_contact.triggered.connect(self.del_contact_win)

        self.contacts_model = None
        self.history_model = None
        self.msgs = QMessageBox()
        self.current_chat = None
        self.current_chat_key = None
        self.encryptor = None
        self.ui.list_history_msg.setHorizontalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff)
        self.ui.list_history_msg.setWordWrap(True)

        self.ui.list_contacts.doubleClicked.connect(self.select_active_user)

        self.clients_list_upd()
        self.set_disabled_input()
        self.show()

    def set_disabled_input(self):
        ''' Метод деактивации поля ввода'''
        self.ui.lbl_new_msg.setText(
            'Для выбора получателя дважды кликните на нем в окне контактов.')
        self.ui.edit_new_msg.clear()
        if self.history_model:
            self.history_model.clear()

        self.ui.btn_clr_field.setDisabled(True)
        self.ui.btn_send_msg.setDisabled(True)
        self.ui.edit_new_msg.setDisabled(True)

    def history_list_upd(self):
        '''
        Метод обновления списка отображающего историю переписки.
        '''
        list = sorted(self.database.get_history(self.current_chat),
                      key=lambda item: item[3])
        if not self.history_model:
            self.history_model = QStandardItemModel()
            self.ui.list_history_msg.setModel(self.history_model)
        self.history_model.clear()
        length = len(list)
        start_index = 0
        if length > 20:
            start_index = length - 20
        for i in range(start_index, length):
            item = list[i]
            if item[1] == 'in':
                mess = QStandardItem(
                    f'Входящее от {item[3].replace(microsecond=0)}:\n {item[2]}')
                mess.setEditable(False)
                mess.setBackground(QBrush(QColor(255, 213, 213)))
                mess.setTextAlignment(Qt.AlignLeft)
                self.history_model.appendRow(mess)
            else:
                mess = QStandardItem(
                    f'Исходящее от {item[3].replace(microsecond=0)}:\n {item[2]}')
                mess.setEditable(False)
                mess.setTextAlignment(Qt.AlignRight)
                mess.setBackground(QBrush(QColor(204, 255, 204)))
                self.history_model.appendRow(mess)
        self.ui.list_history_msg.scrollToBottom()

    def select_active_user(self):
        '''Метод обработчик события двойного клика по списку контактов.'''
        self.current_chat = self.ui.list_contacts.currentIndex().data()
        self.set_active_user()

    def set_active_user(self):
        '''Метод активации диалога между двумя клиентами.'''
        try:
            self.current_chat_key = self.transport.key_request(
                self.current_chat)
            LOGGER.debug(f'Загружен открытый ключ для {self.current_chat}')
            if self.current_chat_key:
                self.encryptor = PKCS1_OAEP.new(
                    RSA.import_key(self.current_chat_key))
        except (OSError, json.JSONDecodeError):
            self.current_chat_key = None
            self.encryptor = None
            LOGGER.debug(f'Не удалось получить ключ для {self.current_chat}')
        if not self.current_chat_key:
            self.msgs.warning(
                self, 'Ошибка',
                'Для выбранного пользователя нет ключа шифрования.')
            return
        self.ui.lbl_new_msg.setText(
            f'Введите сообщенние для {self.current_chat}:')
        self.ui.btn_clr_field.setDisabled(False)
        self.ui.btn_send_msg.setDisabled(False)
        self.ui.edit_new_msg.setDisabled(False)

        self.history_list_upd()

    def clients_list_upd(self):
        '''Метод обновления список контактов.'''
        contacts_list = self.database.get_contacts()
        self.contacts_model = QStandardItemModel()
        for i in sorted(contacts_list):
            item = QStandardItem(i)
            item.setEditable(False)
            self.contacts_model.appendRow(item)
        self.ui.list_contacts.setModel(self.contacts_model)

    def add_contact_win(self):
        '''Метод создания окна для добавления контакта'''
        global select_dialog
        select_dialog = AddContactDialog(self.transport, self.database)
        select_dialog.btn_ok.clicked.connect(
            lambda: self.add_contact_action(select_dialog))
        select_dialog.show()

    def add_contact_action(self, item):
        '''Метод обработчк нажатия кнопки "Добавить"'''
        new_contact = item.selector.currentText()
        self.add_contact(new_contact)
        item.close()

    def add_contact(self, new_contact):
        '''
        Метод добавления контакта в серверную и клиентсткую базу данных
        и последующего обновления содержимого окна
        '''
        try:
            self.transport.add_contact(new_contact)
        except OSError as err:
            if err.errno:
                self.msgs.critical(self, 'Ошибка',
                                   'Потеряно соединение с сервером!')
                self.close()
            self.msgs.critical(self, 'Ошибка', 'Таймаут соединения!')
        else:
            self.database.add_contact(new_contact)
            new_contact = QStandardItem(new_contact)
            new_contact.setEditable(False)
            self.contacts_model.appendRow(new_contact)
            LOGGER.info(f'Успешно добавлен контакт {new_contact}')
            self.msgs.information(self, 'Успех', 'Контакт успешно добавлен.')

    def del_contact_win(self):
        '''Метод создания окна для удаления контакта.'''
        global remove_dialog
        remove_dialog = DelContactDialog(self.database)
        remove_dialog.btn_ok.clicked.connect(
            lambda: self.del_contact(remove_dialog))
        remove_dialog.show()

    def del_contact(self, item):
        '''
        Метод удаления контакта из серверной и клиентсткой БД
        и обновления содержимого окна.
        '''
        selected = item.selector.currentText()
        try:
            self.transport.remove_contact(selected)
        except OSError as err:
            if err.errno:
                self.msgs.critical(self, 'Ошибка',
                                   'Потеряно соединение с сервером!')
                self.close()
            self.msgs.critical(self, 'Ошибка', 'Таймаут соединения!')
        else:
            self.database.remove_contact(selected)
            self.clients_list_upd()
            LOGGER.info(f'Успешно удалён контакт {selected}')
            self.msgs.information(self, 'Успех', 'Контакт успешно удалён.')
            item.close()
            # Если удалён активный пользователь, то деактивируем поля ввода.
            if selected == self.current_chat:
                self.current_chat = None
                self.set_disabled_input()

    def send_msg(self):
        '''
        Отправки сообщения другому клиенту.
        Реализует шифрование сообщения и отправку.
        '''
        msg_text = self.ui.edit_new_msg.toPlainText()
        self.ui.edit_new_msg.clear()
        if not msg_text:
            return
        msg_text_encrypted = self.encryptor.encrypt(
            msg_text.encode('utf8'))
        message_text_encrypted_base64 = base64.b64encode(
            msg_text_encrypted)
        try:
            self.transport.create_msg(self.current_chat,
                                      message_text_encrypted_base64.decode(
                                          'ascii'))
            pass
        except OSError as err:
            if err.errno:
                self.msgs.critical(self, 'Ошибка',
                                   'Потеряно соединение с сервером!')
                self.close()
            self.msgs.critical(self, 'Ошибка', 'Таймаут соединения!')
        except (ConnectionResetError, ConnectionAbortedError):
            self.msgs.critical(self, 'Ошибка',
                               'Потеряно соединение с сервером!')
            self.close()
        else:
            self.database.save_msg(self.current_chat, 'out', msg_text)
            LOGGER.debug(
                f'Отправлено сообщение для {self.current_chat}: {msg_text}')
            self.history_list_upd()

    @pyqtSlot(dict)
    def msg(self, msg):
        '''
        Слот обработчик получаемых сообщений, дешифрует
        сообщения и их сохраненяет в БД. Так же
        запрашивает пользователя если пришло сообщение не от текущего
        собеседника. При необходимости меняет собеседника.
        '''
        encrypted_message = base64.b64decode(msg[TEXT])
        try:
            decrypted_msg = self.decrypter.decrypt(encrypted_message)
        except (ValueError, TypeError):
            self.msgs.warning(
                self, 'Ошибка', 'Не удалось декодировать сообщение.')
            return
        self.database.save_msg(self.current_chat, 'in',
                               decrypted_msg.decode('utf8'))

        from_user = msg[FROM_USER]

        if from_user == self.current_chat:
            self.history_list_upd()
        else:
            if self.database.check_contact(from_user):
                if self.msgs.question(self, 'Новое сообщение', \
                                      f'Получено новое сообщение от {from_user}, открыть чат с ним?',
                                      QMessageBox.Yes,
                                      QMessageBox.No) == QMessageBox.Yes:
                    self.current_chat = from_user
                    self.set_active_user()
            else:
                if self.msgs.question(self, 'Новое сообщение', \
                                      f'Получено новое сообщение от {from_user}.\n Данного пользователя нет в вашем контакт-листе.\n Добавить в контакты и открыть чат с ним?',
                                      QMessageBox.Yes,
                                      QMessageBox.No) == QMessageBox.Yes:
                    self.add_contact(from_user)
                    self.current_chat = from_user
                    self.set_active_user()

    @pyqtSlot()
    def connection_lost(self):
        '''
        Слот обработчик потери соеднинения с сервером.
        Выдаёт окно предупреждение и завершает работу приложения.
        '''
        self.msgs.warning(self, 'Сбой соединения',
                          'Потеряно соединение с сервером. ')
        self.close()

    @pyqtSlot()
    def sig_205(self):
        if self.current_chat and not self.database.check_user(
                self.current_chat):
            self.msgs.warning(
                self, 'Сочувствую',
                'К сожалению собеседник был удалён с сервера.')
            self.set_disabled_input()
            self.current_chat = None
        self.clients_list_upd()

    def make_connection(self, trans_obj):
        '''Метод обеспечивающий соединение сигналов и слотов.'''
        trans_obj.new_msg.connect(self.msg)
        trans_obj.connection_lost.connect(self.connection_lost)
        trans_obj.msg_205.connect(self.sig_205)
