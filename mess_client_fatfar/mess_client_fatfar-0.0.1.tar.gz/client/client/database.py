"""Структура базы данных клиента"""

import datetime
import os

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime, Text
from sqlalchemy.orm import mapper, sessionmaker
from sqlalchemy.sql import default_comparator

from common.variables import *


class ClientDB:
    """
    Класс - оболочка для работы с базой данных клиента.
    Использует SQLite базу данных, реализован с помощью
    SQLAlchemy ORM и используется классический подход.
    """
    class KnownUsers:
        """
        Класс - отображение для таблицы всех пользователей.
        """

        def __init__(self, user):
            self.id = None
            self.username = user

    class MessageHist:
        """
        Класс - отображение для таблицы статистики переданных сообщений.
        """

        def __init__(self, from_user, to_user, message):
            self.id = None
            self.from_user = from_user
            self.to_user = to_user
            self.message = message
            self.date = datetime.datetime.now()

    class Contacts:
        """
        Класс - отображение для таблицы контактов.
        """

        def __init__(self, contact):
            self.id = None
            self.name = contact

    # конструктор класса
    def __init__(self, name):
        # Создаём движок базы данных, поскольку разрешено несколько
        # клиентов одновременно, каждый должен иметь свою БД
        # Поскольку клиент мультипоточный необходимо отключить
        # проверки на подключения с разных потоков,
        # иначе sqlite3.ProgrammingError
        path = os.getcwd()
        filename = f'client_{name}.db3'
        self.database_engine = create_engine(
            f'sqlite:///{os.path.join(path, filename)}',
            echo=False,
            pool_recycle=7200,
            connect_args={
                'check_same_thread': False})

        self.metadata = MetaData()

        users = Table('known_users', self.metadata,
                      Column('id', Integer, primary_key=True),
                      Column('username', String)
                      )

        history = Table('message_hist', self.metadata,
                        Column('id', Integer, primary_key=True),
                        Column('from_user', String),
                        Column('to_user', String),
                        Column('message', Text),
                        Column('date', DateTime),
                        )
        contacts = Table('contacts', self.metadata,
                         Column('id', Integer, primary_key=True),
                         Column('name', String, unique=True)
                         )

        self.metadata.create_all(self.database_engine)
        mapper(self.KnownUsers, users)
        mapper(self.MessageHist, history)
        mapper(self.Contacts, contacts)

        Session = sessionmaker(bind=self.database_engine)
        self.session = Session()

        # Необходимо очистить таблицу контактов, т.к. при запуске они
        # подгружаются с сервера.
        self.session.query(self.Contacts).delete()
        self.session.commit()

    def add_contact(self, contact):
        """Метод, добавляющий контакт в базу данных."""
        if not self.session.query(
                self.Contacts).filter_by(
                name=contact).count():
            contact_row = self.Contacts(contact)
            self.session.add(contact_row)
            self.session.commit()

    def contacts_clear(self):
        """Метод, очищающий таблицу со списком контактов."""
        self.session.query(self.Contacts).delete()

    def del_contact(self, contact):
        """Метод, удаляющий определённый контакт."""
        self.session.query(self.Contacts).filter_by(name=contact).delete()

    def add_users(self, users_list):
        """Метод, заполняющий таблицу известных пользователей."""
        self.session.query(self.KnownUsers).delete()
        for user in users_list:
            user_row = self.KnownUsers(user)
            self.session.add(user_row)
        self.session.commit()

    def save_message(self, from_user, to_user, message):
        """Метод, сохраняющий сообщение в базе данных."""
        message_row = self.MessageHist(from_user, to_user, message)
        self.session.add(message_row)
        self.session.commit()

    def get_contacts(self):
        """Метод, возвращающий список всех контактов."""
        return [contact[0]
                for contact in self.session.query(self.Contacts.name).all()]

    def get_users(self):
        """Метод, возвращающий список всех известных пользователей."""
        return [user[0]
                for user in self.session.query(self.KnownUsers.username).all()]

    def check_user(self, user):
        """Метод, проверяющий существует ли пользователь."""
        if self.session.query(
                self.KnownUsers).filter_by(
                username=user).count():
            return True
        else:
            return False

    def check_contact(self, contact):
        """Метод, проверяющий существует ли контакт."""
        if self.session.query(self.Contacts).filter_by(name=contact).count():
            return True
        else:
            return False

    def get_history(self, from_user):
        """Метод, возвращающий историю сообщений с определённым пользователем."""
        query = self.session.query(
            self.MessageHist).filter_by(
            from_user=from_user)
        return [(history_row.from_user,
                 history_row.to_user,
                 history_row.message,
                 history_row.date) for history_row in query.all()]


if __name__ == '__main__':
    trial_db = ClientDB('test1')
    for i in ['test3', 'test4', 'test5']:
        trial_db.add_contact(i)
    trial_db.add_contact('test2')
    trial_db.add_users(['test1', 'test2', 'test3', 'test4', 'test5'])
    trial_db.save_message(
        'test1',
        'test2',
        f"Hello! It's me. Testing message dated on {datetime.datetime.now()}!")
    trial_db.save_message(
        'test2',
        'test1',
        f"Hello! I'm another testing message dated on {datetime.datetime.now()}!")
    print(trial_db.get_contacts())
    print(trial_db.get_users())
    print(trial_db.check_contact('test11'))
    print(trial_db.check_user('test1'))
    print(trial_db.check_user('test12'))
    # print(trial_db.get_history('test2'))
    # print(trial_db.get_history('test15'))
    trial_db.del_contact('test5')
    print(trial_db.get_contacts())
    print(sorted(trial_db.get_history('test2'), key=lambda item: item[3]))
