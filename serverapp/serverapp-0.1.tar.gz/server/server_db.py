from datetime import datetime

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, \
    DateTime, String, ForeignKey, Text
from sqlalchemy.orm import mapper, sessionmaker
from sqlalchemy.sql import default_comparator


class ServerDB:
    '''
    Класс - оболочка для работы с базой данных сервера.
    Использует SQLite базу данных, реализован с помощью
    SQLAlchemy ORM и используется классический подход.
    '''
    class Users:
        '''Отображение всех зарегестрированных пользователей.'''
        def __init__(self, username, pass_hash):
            self.id = None
            self.username = username
            self.last_login = datetime.now()
            self.pass_hash = pass_hash
            self.pubkey = None

    class ActiveUsers:
        '''Отображение таблицы всех активных пользователей.'''
        def __init__(self, user_id, ip, port, login_time):
            self.id = None
            self.username = user_id
            self.ip = ip
            self.port = port
            self.login_time = login_time

    class HistoryLogin:
        '''Отображение таблицы истории входов.'''
        def __init__(self, user_id, ip, port, time_of_login):
            self.id = None
            self.username = user_id
            self.ip = ip
            self.port = port
            self.time_of_login = time_of_login

    class UsersHistory:
        '''Отображение таблицы истории действий.'''
        def __init__(self, username):
            self.id = None
            self.username = username
            self.sent = 0
            self.accepted = 0

    class UsersContacts:
        '''Отображение таблицы контактов пользователей.'''
        def __init__(self, username, contact):
            self.id = None
            self.username = username
            self.contact = contact

    def __init__(self, path):
        # Устанавливаем "прослущивание" БД
        engine = create_engine(f'sqlite:///{path}', echo=False,
                               pool_recycle=7200,
                               connect_args={'check_same_thread': False})
        self.meta = MetaData()

        # Создаем таблицы
        users = Table('users', self.meta,
                      Column('id', Integer, primary_key=True),
                      Column('username', String, unique=True),
                      Column('last_login', DateTime),
                      Column('pass_hash', String),
                      Column('pubkey', Text)
                      )

        active_users = Table('active_users', self.meta,
                             Column('id', Integer, primary_key=True),
                             Column('username', ForeignKey('users.id'),
                                    unique=True),
                             Column('ip', String),
                             Column('port', Integer),
                             Column('login_time', DateTime)
                             )

        history_login = Table('history_login', self.meta,
                              Column('id', Integer, primary_key=True),
                              Column('username', ForeignKey('users.id')),
                              Column('ip', String),
                              Column('port', Integer),
                              Column('time_of_login', DateTime)
                              )

        users_history_table = Table('history', self.meta,
                                    Column('id', Integer, primary_key=True),
                                    Column('username', ForeignKey('users.id')),
                                    Column('sent', Integer),
                                    Column('accepted', Integer)
                                    )

        users_contacts = Table('users_contacts', self.meta,
                               Column('id', Integer, primary_key=True),
                               Column('username', ForeignKey('users.id')),
                               Column('contact', ForeignKey('users.id'))
                               )

        self.meta.create_all(engine)
        # Связываем таблицы с классами
        mapper(self.Users, users)
        mapper(self.ActiveUsers, active_users)
        mapper(self.HistoryLogin, history_login)
        mapper(self.UsersHistory, users_history_table)
        mapper(self.UsersContacts, users_contacts)

        # Создаем сессию
        SESSION = sessionmaker(bind=engine)
        # Создаем объект сессии
        self.session = SESSION()

        # Очистка таблицы активных пользователей
        self.session.query(self.ActiveUsers).delete()
        self.session.commit()

    def user_login(self, username, ip, port, key):
        '''
        Метод выполняющийся при входе пользователя, записывает в базу данные о входе
        пользователя
        Обновляет открытый ключ пользователя при его изменении.
        '''
        qr = self.session.query(self.Users).filter_by(username=username)
        print(qr.count())
        if qr.count():
            user = qr.first()
            user.last_login = datetime.now()
            if user.pubkey != key:
                user.pubkey = key
        else:
            raise ValueError('Пользователь не зарегестрирован.')

        active = self.ActiveUsers(user.id, ip, port, datetime.now())
        self.session.add(active)

        history = self.HistoryLogin(user.id, ip, port, datetime.now())
        self.session.add(history)

        self.session.commit()

    def user_logout(self, username):
        '''Фиксирует в БД факт отключение пользователя.'''
        user = self.session.query(self.Users).filter_by(
            username=username).first()
        self.session.query(self.ActiveUsers).filter_by(
            username=user.id).delete()
        self.session.commit()

    def add_user(self, username, pass_hash):
        '''
        Регистрация нового пользователя.
        Принимает имя и хэш пароля, создаёт запись в таблице статистики.
        '''
        user = self.Users(username, pass_hash)
        self.session.add(user)
        self.session.commit()
        history = self.UsersHistory(user.id)
        self.session.add(history)
        self.session.commit()

    def remove_user(self, username):
        '''Удаление пользователя из базы.'''
        user = self.session.query(self.Users).filter_by(
            username=username).first()
        self.session.query(self.ActiveUsers).filter_by(
            username=user.id).delete()
        self.session.query(self.HistoryLogin).filter_by(
            username=user.id).delete()
        self.session.query(self.UsersContacts).filter_by(
            username=user.id).delete()
        self.session.query(self.UsersContacts).filter_by(
            contact=user.id).delete()
        self.session.query(self.UsersHistory).filter_by(
            username=user.id).delete()
        self.session.query(self.Users).filter_by(username=username).delete()
        self.session.commit()

    def get_hash(self, username):
        '''Получение хэша пароля пользователя.'''
        user = self.session.query(self.Users).filter_by(
            username=username).first()
        return user.pass_hash

    def get_pubkey(self, username):
        '''Получение публичного ключа пользователя.'''
        user = self.session.query(self.Users).filter_by(
            username=username).first()
        return user.pubkey

    def check_user(self, username):
        '''Проверка существования данного пользователя.'''
        if self.session.query(self.Users).filter_by(username=username).count():
            return True
        else:
            return False

    def users_list(self):
        '''Возвращающение списка всех известных пользователей со временем последнего входа.'''
        query = self.session.query(
            self.Users.username,
            self.Users.last_login
        )
        return query.all()

    '''Возвращающение списка активных пользователей.'''
    def user_active_list(self):
        query = self.session.query(
            self.Users.username,
            self.ActiveUsers.ip,
            self.ActiveUsers.port,
            self.ActiveUsers.login_time
        ).join(self.Users)
        # Возвращаем список кортежей
        return query.all()

    def login_history(self, username=None):
        '''Возвращающение истории входов.'''
        query = self.session.query(self.Users.username,
                                   self.HistoryLogin.ip,
                                   self.HistoryLogin.port,
                                   self.HistoryLogin.time_of_login,
                                   ).join(self.Users)
        if username:
            query = query.filter_by(self.Users.name == username)

        return query.all()

    def message_history(self):
        '''Возвращение статистики сообщений.'''
        query = self.session.query(
            self.Users.username,
            self.Users.last_login,
            self.UsersHistory.sent,
            self.UsersHistory.accepted
        ).join(self.Users)
        return query.all()

    # Функция счетчика переданных/полученных сообщений
    def process_msg(self, sender, recipient):
        '''Запись в таблицу статистики факта передачи сообщения.'''
        sender = self.session.query(self.Users).filter_by(
            username=sender).first().id
        recipient = self.session.query(self.Users).filter_by(
            username=recipient).first().id
        # Увеличение счетчиков
        sender_row = self.session.query(self.UsersHistory).filter_by(
            username=sender).first()
        sender_row.sent += 1
        recipient_row = self.session.query(self.UsersHistory).filter_by(
            username=recipient).first()
        recipient_row.accepted += 1

        self.session.commit()

    def add_contact(self, username, contact):
        '''Добавление контакта для пользователя.'''
        user = self.session.query(self.Users).filter_by(
            username=username).first()
        contact = self.session.query(self.Users).filter_by(
            username=contact).first()

        if not contact or self.session.query(self.UsersContacts).filter_by(
                username=user.id, contact=contact.id).count():
            return

        list = self.UsersContacts(user.id, contact.id)
        self.session.add(list)
        self.session.commit()

    def get_contacts(self, username):
        '''Возвращающение списка контактов пользователя.'''
        user = self.session.query(self.Users).filter_by(username=username).one()

        query = self.session.query(self.UsersContacts,
                                   self.Users.username).filter_by(
            username=user.id) \
            .join(self.Users, self.UsersContacts.contact == self.Users.id)

        return [contact[1] for contact in query.all()]

    def remove_contact(self, user, contact):
        '''Удаление контакта пользователя.'''
        user = self.session.query(self.Users).filter_by(username=user).first()
        contact = self.session.query(self.Users).filter_by(
            username=contact).first()
        if not contact:
            return
        self.session.query(self.UsersContacts).filter(
            self.UsersContacts.username == user.id,
            self.UsersContacts.contact == contact.id
        ).delete()
        self.session.commit()


if __name__ == '__main__':
    test_db = ServerDB('server_base.db3')
    # test_db.user_login('McG2', '192.168.1.113', 8081)
    print(test_db.check())
    # print(test_db.user_login(3, '127.0.0.1', 52884, '-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxc4H5+/Ym+08Jk3YduRY\nYsezWinHkW6tF7lz7vxStP0OkaRcbY5qCDVcNnJUHSGHrj7lAcvbuD5UtmVjfvRI\n9j8y75jPvPYr4R8/3NrRsRYUCFv1F4yWx9Jlgim+ftfXb/uVjq9PlObcP1gAWxyq\nzg5HExU7+xTyD92YalYnCMr9jejnmkh6SgTI4ERf56kyEWVCcekW+4YouX4CGiAe\nB6Lk4a7QLRk1PrK1vZhIech98/AA871CPu/UhV68OQceB2b/I3D0IDfpTJPwwhCH\nl32uafT1NHbU5pWSTgx3h0g8GKzo0HcNk8kZcqSJu9TCAP78P/d8oK/JOIQi2ePY\nyQIDAQAB\n-----END PUBLIC KEY-----'))
