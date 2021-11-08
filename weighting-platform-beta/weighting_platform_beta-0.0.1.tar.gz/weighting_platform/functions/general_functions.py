""" Содержит общие, многоразовые функции"""
import datetime
import re
import uuid

from wsqluse.wsqluse import Wsqluse

from weighting_platform import cfg
from weighting_platform.functions import logging_functions


def form_point_name(course: str, point_type_str: str):
    """ Формирует название точки доступа, который передается в QSB, что бы тот его
    открыл. Как правилr, оно состоит из направления (course) который передает
    QSB (оно может быть external или internal). Название точки формируется
    сложиение направления и слова point_type_str, т.е должно получиться что-то типа:
    EXTERNAL_GATE или INTERNAL_PHOTOCELL"""
    gate_name_full = '_'.join((course.upper(), point_type_str.upper()))
    return gate_name_full


def get_change_percent(first_weight, second_weight):
    """ Вернуть процент изменения second_weight относительно first_weight """
    difference = second_weight - first_weight
    percent = difference / first_weight * 100
    return abs(percent)


def if_dlinnomer_moved(first_weight, second_weight, min_percent=30):
    """ Возвращает True, если понимает, что машина переместилась по весам
    (весы изменились более чем на min_percent процентов) """
    percent = get_change_percent(first_weight, second_weight)
    if percent >= min_percent:
        return True


def send_round_status(stage, status=None, timer=None, weight=None):
    """ Отправляет статус заезда (stage) и дополнительную информацию для
     отображения статуса заезда.
    STAGE - BEFORE_WEIGHING; WEIGHING; AFTER_WEIGHING
    INFO - """
    info = {'STAGE': stage.upper(),
            'STATUS': status.upper(),
            'TIMER': timer,
            'WEIGHT': weight}
    send_status(info)


def send_status(*msg):
    """ Используется в других функциях для вывода статуса в стандартный поток,
    либо для отправки статуса выполнения клиентам """
    save_current_round_info(**msg[0])
    global sql_shell
    logging_functions.fix_event(sql_shell, cfg.current_round)
    info = {'status': True, 'info': cfg.current_round,
            'core_method': 'round_status'}
    print("ROUND_STATUS", info)
    cfg.qodex_pi.broadcast_sending(info)


def save_current_round_info(**kwargs):
    """ Сохраняет информацию о текущем раунде взвешивания в модуль cfg """
    for k, v in kwargs.items():
        cfg.current_round[k] = v
    return cfg.current_round


def clear_current_round():
    cfg.current_round = {'record_id': None, 'has_gross': None, 'auto_id': None}


sql_shell = Wsqluse('wdb', 'watchman', 'hect0r1337', 'localhost')


def update_last_events(sql_shell, car_id: int, carrier: int, trash_type: int, trash_cat: int,
                       polygon: int, date=None):
    """Обновляет информацию в таблице last_events, в wdb, добавляя данные в  polygon"""
    if not date:
        date = datetime.datetime.now()
    command = "INSERT INTO last_events (car_id, carrier, trash_type, trash_cat, date, polygon) " \
              "VALUES ({}, {}, {}, {}, '{}', {}) ON CONFLICT (car_id) DO UPDATE " \
              "SET carrier={}, trash_type={}, trash_cat={}, date='{}', polygon={}"
    command = command.format(car_id, carrier, trash_type, trash_cat, date, polygon,
                             carrier, trash_type, trash_cat, date, polygon)
    response = sql_shell.try_execute(command)
    return response


def get_mac_ar():
    """Получить мак адрес AR"""
    mac_ar = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
    return mac_ar


def send_mac_ar(wserver_qdk, active:bool):
    """Отправляет мак адрес на wserver_qdk и получает ответ о легитимности"""
    mac_ar = get_mac_ar()
    wserver_qdk.check_legit(mac_addr=mac_ar)
    response = wserver_qdk.get_data()
    return response


"""
def self_destroy_func():
    Удаление ПО если не легитимный запуск
    active = send_mac_ar(wserver_qdk)
    if not active:
        path = os.getcwd()
        shutil.rmtree(path)
"""
