from sqlalchemy import create_engine, MetaData, Table, Column, Integer, \
    DateTime, String, ForeignKey, Text
from sqlalchemy.orm import mapper, sessionmaker
from sqlalchemy.sql import default_comparator
import sys
import os

sys.path.append('../')
from datetime import datetime


class ClientDB:
    '''
    Класс - оболочка для работы с БД SQLite>.
    Реализован с помощью SQLAlchemy ORM.
    '''
    class AllKnowUsers:
        '''
        Класс "Все известные пользователи"
        '''
        def __init__(self, username):
            self.id = None
            self.username = username

    class Contacts:
        '''
        Класс "Контакты"
        '''
        def __init__(self, username):
            self.id = None
            self.username = username

    class MsgHistory:
        '''
        Класс "История сообщений"
        '''
        def __init__(self, contact, direction, message):
            self.id = None
            self.contact = contact
            self.direction = direction
            self.message = message
            self.date = datetime.now()

    def __init__(self, username):
        path = os.getcwd()
        self.engine = create_engine(f'sqlite:///client_{username}.db3',
                                    echo=False, pool_recycle=7200,
                                    connect_args={'check_same_thread': False})

        self.meta = MetaData()

        # Таблица "Известные пользователи"
        all_know_users = Table('all_know_users', self.meta,
                               Column('id', Integer, primary_key=True),
                               Column('username', String, unique=True)
                               )

        # Таблица "Контакты"
        contacts = Table('contacts', self.meta,
                         Column('id', Integer, primary_key=True),
                         Column('username', String, unique=True)
                         )
        # Таблица "История сообщений"
        msg_history = Table('msg_history', self.meta,
                            Column('id', Integer, primary_key=True),
                            Column('contact', String),
                            Column('direction', String),
                            Column('message', Text),
                            Column('date', DateTime)
                            )

        self.meta.create_all(self.engine)

        mapper(self.AllKnowUsers, all_know_users)
        mapper(self.Contacts, contacts)
        mapper(self.MsgHistory, msg_history)

        Session = sessionmaker(bind=self.engine)
        self.session = Session()

        # Таблица контактов каждый раз очищается и подгружается с сервера
        self.session.query(self.Contacts).delete()
        self.session.commit()


    def add_contact(self, contact):
        '''
        Метод добавления контакта в БД
        '''
        if not self.session.query(self.Contacts).filter_by(
                username=contact).count():
            contact_el = self.Contacts(contact)
            self.session.add(contact_el)
            self.session.commit()

    def remove_contact(self, contact):
        '''
        Метод удаления контакта из БД
        '''
        self.session.query(self.Contacts).filter_by(username=contact).delete()

    def contacts_clear(self):
        '''
        Метод очищающий таблицу контактов
        '''
        self.session.query(self.Contacts).delete()

    def add_users(self, users):
        '''
        Метод добавление известных пользователей
        '''
        self.session.query(self.AllKnowUsers).delete()
        for user in users:
            user_el = self.AllKnowUsers(user)
            self.session.add(user_el)
        self.session.commit()

    def get_users(self):
        '''
        Метод получения списка известных пользователей
        '''
        return [user[0] for user in
                self.session.query(self.AllKnowUsers.username).all()]

    def save_msg(self, contact, direction, message):
        '''
        Метод сохранения сообщений
        '''
        msg_el = self.MsgHistory(contact, direction, message)
        self.session.add(msg_el)
        self.session.commit()

    def get_contacts(self):
        '''
        Метод получение списка контактов
        '''
        return [contact[0] for contact in
                self.session.query(self.Contacts.username).all()]

    def check_user(self, user):
        '''
        Метод проверки наличия пользователя в списке известных
        '''
        if self.session.query(self.AllKnowUsers).filter_by(
                username=user).count():
            return True
        else:
            return False

    def check_contact(self, contact):
        '''
        Метод проверки наличия пользователя в контактах
        '''
        if self.session.query(self.Contacts).filter_by(
                username=contact).count():
            return True
        else:
            return False

    def get_history(self, contact):
        '''Метод получения истории переписки'''
        query = self.session.query(self.MsgHistory).filter_by(contact=contact)
        return [(
                history_row.contact, history_row.direction, history_row.message,
                history_row.date) for history_row in query.all()]


if __name__ == '__main__':
    test_db = ClientDB('test1')
    for i in ['test3', 'test4', 'test5']:
        test_db.add_contact(i)
    test_db.add_contact('test4')
    test_db.add_users(['test1', 'test2', 'test3', 'test4', 'test5'])
    test_db.save_msg('test2', 'in',
                     f'Привет! я тестовое сообщение от {datetime.now()}!')
    test_db.save_msg('test2', 'out',
                     f'Привет! я другое тестовое сообщение от {datetime.now()}!')
    print(test_db.get_contacts())
    print(test_db.get_users())
    print(test_db.check_user('test1'))
    print(test_db.check_user('test10'))
    print(sorted(test_db.get_history('test2'), key=lambda item: item[3]))
    test_db.remove_contact('test4')
    print(test_db.get_contacts())
