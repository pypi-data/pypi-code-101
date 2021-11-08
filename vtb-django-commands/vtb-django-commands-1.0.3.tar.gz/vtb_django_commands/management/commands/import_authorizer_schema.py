import json
from typing import List, Dict, Any

from asgiref.sync import async_to_sync  # noqa
from django.conf import settings
from django.core.management import BaseCommand
from vtb_authorizer_utils.config import import_service_from_dict, ImportServiceResult
from vtb_authorizer_utils.gateway import AuthorizerGateway
from vtb_django_utils.keycloak_utils import keycloak_config


class Command(BaseCommand):
    """
    Импорт конфигурации сервиса из json файла в authorizer
    Пример Json
    {
      "state-service": {
        "title": "Сервис состояний",
        "description": "",
        "url": "http://dev-kong-service.apps.d0-oscp.corp.dev.vtb/state-service",
        "resource_types": {
          "inventories": {
            "title": "Объекты инфраструктуры",
            "description": "",
            "actions": "post"
          }
        },
        "resource_rules": [
          {
            "http_method": "POST",
            "url_pattern": "/api/v1/tag-manager/organizations/{id}/inventories/",
            "access_type": "members",
            "operation_name": "Список объектов инфраструктуры",
            "resource_action_code": "state-service:inventories:post"
          }
        ]
      }
    }
    """
    help = "Register service configuration"

    def add_arguments(self, parser):
        parser.add_argument('--file', help='File with json service configuration', required=True)

    def handle(self, *args, **options):
        file = options['file']

        authorizer_base_url = settings.AUTHORIZER_BASE_URL
        redis_url = settings.REDIS_CONNECTION_STRING

        gateway = AuthorizerGateway(authorizer_base_url, keycloak_config, redis_url)

        with open(file, encoding="utf-8") as json_file:
            cfg = json.load(json_file)

            import_service(gateway, cfg)

            self.stdout.write('Success')


@async_to_sync
async def import_service(gateway: AuthorizerGateway,
                         cfg: Dict[str, Any]) -> List[ImportServiceResult]:
    """ Загрузка конфигурации ресурсных типов и правил для сервиса в виде словаря """
    return await import_service_from_dict(gateway, cfg)
