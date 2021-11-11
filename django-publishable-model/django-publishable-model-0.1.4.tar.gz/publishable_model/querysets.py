# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from . import settings as app_settings


class PublishableQuerySet(models.QuerySet):

    def published_items(self):
        now = timezone.now()
        q_pub_start = models.Q(publication_start__lte=now)
        q_pub_end = (models.Q(publication_end__gte=now) | models.Q(publication_end__isnull=True))
        q_status = models.Q(status=app_settings.PUBLICATION_STATUS_PUBLISHED)
        return self.filter(q_pub_start & q_pub_end & q_status)

    def not_published_items(self):
        now = timezone.now()
        q_pub_start = models.Q(publication_start__lte=now)
        q_pub_end = (models.Q(publication_end__gte=now) | models.Q(publication_end__isnull=True))
        q_status = models.Q(status=app_settings.PUBLICATION_STATUS_PUBLISHED)
        return self.exclude(q_pub_start & q_pub_end & q_status)

    def draft_items(self):
        q_status = models.Q(status=app_settings.PUBLICATION_STATUS_DRAFT)
        return self.filter(q_status)
