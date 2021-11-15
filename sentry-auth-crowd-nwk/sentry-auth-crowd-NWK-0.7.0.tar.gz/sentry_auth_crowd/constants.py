# -*- coding: utf-8 -*-
from django.conf import settings

CROWD_URL = getattr(settings, 'CROWD_URL', None)
CROWD_APP_NAME = getattr(settings, 'CROWD_APP_NAME', None)
CROWD_APP_PASSWORD = getattr(settings, 'CROWD_APP_PASSWORD', None)
