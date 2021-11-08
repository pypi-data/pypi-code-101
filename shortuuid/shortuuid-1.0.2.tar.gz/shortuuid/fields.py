from django.db import models
from django.utils.translation import gettext_lazy as _


class ShortUUIDField(models.CharField):
    description = _("A short UUID.")

    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = 104
        super().__init__(*args, **kwargs)
