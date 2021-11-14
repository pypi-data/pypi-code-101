from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DjangoSiteConfigConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_site_variables'
    verbose_name = _('Site variables')
