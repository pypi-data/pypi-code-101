import configparser
import time

from wserver_qdk.main import WServerQDK
from weighting_platform import settings
from weighting_platform.functions import logging_functions
from weighting_platform.functions import pic_make_functions
import base64
import os

config = configparser.ConfigParser()  # создаём объекта парсера
config.read(settings.CONF)  # читаем конфиг
WSERVER_IP = config['WServer']['ip']
WSERVER_PORT = config['WServer']['port']


class WServerIntegrator(WServerQDK):
    """ Класс интегратор с WServer. """

    def __init__(self, ip='192.168.100.118', port=int(WSERVER_PORT),
                 **kwargs):
        super().__init__(ip, port, **kwargs)

    def get_polygon_id(self, login, password):
        print(locals())
        self.login = login
        self.password = password
        self.make_auth()
        response = self.get_data()
        if response['status']:
            self.polygon_id = response['info']['info']
            return self.polygon_id


class WServerActSender:
    """ Класс для отправки актов. """

    def send_act(self, wserver_qdk, auto_id, gross, tare, cargo,
                 time_in, time_out,
                 carrier_id, trash_cat_id, trash_type_id,
                 polygon_id, operator, ex_id):
        wserver_qdk.set_act(auto_id=auto_id, gross=gross, tare=tare,
                            cargo=cargo,
                            time_in=time_in, time_out=time_out,
                            carrier_id=carrier_id, trash_cat_id=trash_cat_id,
                            trash_type_id=trash_type_id, polygon_id=polygon_id,
                            operator=operator, ex_id=ex_id)


class WServerActIntegration(WServerIntegrator, WServerActSender,
                            logging_functions.PhotoSendLogger,
                            logging_functions.ActSendLogger):
    def get_act_db(self, wdb_worker, act_id):
        return wdb_worker.get_record_info(act_id)

    def send_act_photo(self, wdb_worker, act_id, photo_path):
        """
        Отправить акт и сразу за ним - фотографии брутто и тара.

        :param wdb_worker: Фреймворк для работы с БД.
        :param act_id: Номер акта в wdb.
        :param photo_path: Путь к директории, где фото лежат
        :return:
        """
        response = self.send_act_operation(wdb_worker, act_id)
        if response['info']['status']:
            wserver_act_id = response['info']['info']
            self.send_photo(photo_path, act_id, 'gross', 1, wserver_act_id,
                            wdb_worker)
            self.send_photo(photo_path, act_id, 'tare', 2, wserver_act_id,
                            wdb_worker)

    def send_act_operation(self, wdb_worker, act_id):
        act_dict = self.get_act_db(wdb_worker, act_id)
        wserver_carrier_id = wdb_worker.get_record_info(
            record_id=act_dict['carrier'], tablename='clients')['wserver_id']
        wserver_trash_type_id = wdb_worker.get_record_info(
            record_id=act_dict['trash_type'],
            tablename='trash_types')['wserver_id']
        wserver_trash_cat_id = wdb_worker.get_record_info(
            record_id=act_dict['trash_cat'],
            tablename='trash_cats')['wserver_id']
        wserver_operator = wdb_worker.get_record_info(
            record_id=act_dict['operator'],
            tablename='users')['wserver_id']
        auto_id = self.get_wserver_auto_id(wdb_worker, act_dict['auto'],
                                           self.polygon_id)
        log_id = self.log_act_send(wdb_worker, act_id)
        self.set_act(auto_id=auto_id,
                     gross=act_dict['brutto'],
                     cargo=act_dict['cargo'],
                     tare=act_dict['tara'],
                     time_in=act_dict['time_in'],
                     time_out=act_dict['time_out'],
                     carrier_id=wserver_carrier_id,
                     trash_cat_id=wserver_trash_cat_id,
                     trash_type_id=wserver_trash_type_id,
                     polygon_id=self.polygon_id,
                     operator=wserver_operator,
                     ex_id=act_dict['id'])
        response = self.get_data()
        self.log_act_get(wdb_worker, log_id, response['info']['info'])
        return response

    def encode_photo(self, photo_path):
        """ Кодирует фото в base64
        :param photo_path: Абсолютный путь до фото
        :return: Последовательность в кодировке base64"""
        with open(photo_path, 'rb') as fobj:
            photo_data = base64.b64encode(fobj.read())
        return photo_data

    def send_photo(self, photo_path, record_id, stage, photo_type,
                   wserver_act_id, wdb_worker):
        """
        Сохранить фотографии на WServer.

        :param photo_path: Оператор камеры.
        :param record_id: ID заезда, к которому относится фотография.
        :param stage: Стадия заезда (gross/tare)
        :param photo_type: Тип фото (1-брутто, 2-тара)
        :param wserver_act_id: ID акта в gdb.
        :param wdb_worker: Фреймворк для работы с БД.
        :return:
        """
        photo_path = self.generate_photo_name(photo_path, record_id, stage)
        photo_obj = self.encode_photo(photo_path)
        photo_obj_str = str(photo_obj)
        log_id = self.log_photo_send(wdb_worker, record_id, photo_path)
        self.set_photo(wserver_act_id, photo_obj_str, photo_type)
        response = self.get_data()
        self.log_photo_get(wdb_worker, log_id, response['info']['info'],
                           response['info']['status'])

    def generate_photo_name(self, pics_folder, record_id, photo_type):
        """
        Генерирует имя фотографии, сохраненной на ПК.

        :param pics_folder: Директория с фото.
        :param record_id: Номер акта фото.
        :param photo_type: Тип фото (1-брутто, 2-тара)
        :return:
        """
        pic_name = pic_make_functions.get_pic_name(record_id, photo_type)
        full_pic_name = os.path.join(pics_folder, pic_name)
        full_pic_name = full_pic_name + '.jpg'
        return full_pic_name

    def get_wserver_auto_id(self, wdb_worker, wdb_auto_id: int, polygon: int):
        """
        Получить ID авто из WServer по ID из wdb. Если такого авто нет в gdb,
        дает команду зарегать ее и вернет id только что зареганного авто.

        :param wdb_auto_id:
        :return:
        """
        auto_info = wdb_worker.get_record_info(tablename='auto',
                                               record_id=wdb_auto_id)
        auto_number = auto_info['car_number']
        self.get_auto_id(auto_number)
        response = self.get_data()
        auto_id = response['info']
        if not auto_id:
            self.set_auto(car_number=auto_number, polygon=polygon,
                          id_type='tails')

    def get_unsend_acts_id(self, gdw):
        """ Получить все id актов, не отправленных на wserver. """
        command = "SELECT id FROM records WHERE wserver_id is null"
        response = gdw.try_execute_get(command)
        if response:
            response_list = [x[0] for x in response]
            return response_list

    def act_sender_thread(self, gdw, photo_path, timing):
        """
        Отправляет акты в цикле, должен быть запущен как паралелльный поток.

        :param gdw: Фреймворк для работы с БД.
        :param photo_path: Путь к директории с фото.
        :param timing: Время, через который отправлять акты.
        :return:
        """
        while True:
            unsend_acts = self.get_unsend_acts_id(gdw)
            for act_id in unsend_acts:
                self.send_act_photo(gdw, act_id, photo_path)
                time.sleep(timing)

    def set_act(self, wserver_id): pass