# -*- coding: utf-8 -*-
from django.db import models

from .querysets import PublishableQuerySet


class PublishableModelManager(models.Manager):
    use_for_related_fields = True

    def get_queryset(self):
        return PublishableQuerySet(self.model, using=self._db)


class PublishedModelManager(PublishableModelManager):

    def get_queryset(self):
        return super(PublishedModelManager, self).get_queryset().published_items()


class NotPublishedModelManager(PublishableModelManager):

    def get_queryset(self):
        return super(NotPublishedModelManager, self).get_queryset().not_published_items()


class DraftModelManager(PublishableModelManager):

    def get_queryset(self):
        return super(DraftModelManager, self).get_queryset().draft_items()
