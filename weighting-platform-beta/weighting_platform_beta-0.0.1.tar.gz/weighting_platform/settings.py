""" Пакет содержит все настройки """
# Словарь содержит описание порядков открывания из протоколов авто согласно
# тому, с какой стороны машины подъехала (курс используется как ключ)
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent
CONF = os.path.join(BASE_DIR, 'conf.ini')


protocol_gate_description_dict = {'external':
                                      {'near': 'external', 'far': 'internal'},
                                  'internal':
                                      {'near': 'internal', 'far': 'external'}}