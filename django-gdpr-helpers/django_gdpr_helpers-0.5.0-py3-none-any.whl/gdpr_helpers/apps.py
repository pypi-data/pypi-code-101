from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class GdprHelpersConfig(AppConfig):
    name = "gdpr_helpers"
    verbose_name = _("Gdpr helpers")
