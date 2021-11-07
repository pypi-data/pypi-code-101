from typing import Any, cast

from django.apps import AppConfig, apps
from django.utils.translation import gettext_lazy as _
from injector import Injector

from ninja_extra.modules import NinjaExtraModule
from ninja_extra.shortcuts import fail_silently


class NinjaExtraConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "ninja_extra"
    verbose_name = _("Django Ninja Extra")
    injector: Injector

    def ready(self) -> None:
        self.injector = Injector([NinjaExtraModule])
        # get django_injector is available and registered
        django_injector_app = fail_silently(
            apps.get_app_config, app_label="django_injector"
        )
        app = cast(Any, django_injector_app)
        if app:
            app.ready()
            self.injector = app.injector
