from datetime import datetime, timedelta
import jwt
from monitoring_db_license_generator.settings.service_settings import *


def create_lic():
    dt = datetime.now() + timedelta(days=2)
    encoded_token = jwt.encode({'client_name': CLIENT_NAME, 'exp': dt}, SECRET, algorithm='HS256')
    print(encoded_token)

