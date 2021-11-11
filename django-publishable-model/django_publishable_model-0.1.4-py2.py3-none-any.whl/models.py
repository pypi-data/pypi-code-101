# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext, ugettext_lazy as _

from . import managers as app_managers
from . import settings as app_settings


class PublishableModel(models.Model):
    objects = app_managers.PublishableModelManager()
    published_objects = app_managers.PublishedModelManager()
    not_published_objects = app_managers.NotPublishedModelManager()
    draft_objects = app_managers.DraftModelManager()

    PUBLICATION_STATUS_CHOICES = (
        (app_settings.PUBLICATION_STATUS_DRAFT, _("draft")),
        (app_settings.PUBLICATION_STATUS_PUBLISHED, _('published')),
    )

    status = models.CharField(_("status"), max_length=2, db_index=True,
                              choices=PUBLICATION_STATUS_CHOICES,
                              default=app_settings.PUBLICATION_STATUS_DRAFT)
    publication_start = models.DateTimeField(_("publication start"),
                                             null=True, blank=True)
    publication_end = models.DateTimeField(_("publication end"),
                                           null=True, blank=True)

    class Meta:
        abstract = True
        ordering = ['-publication_start', ]
        get_latest_by = 'publication_start'

    def get_is_actual(self):
        return all([self.publication_start and self.publication_start < timezone.now(),
                    self.publication_end is None or self.publication_end > timezone.now(),
                    self.status == app_settings.PUBLICATION_STATUS_PUBLISHED])

    is_actual = property(get_is_actual)

    def save(self, *args, **kwargs):
        if (self.status == app_settings.PUBLICATION_STATUS_PUBLISHED and not self.publication_start):
            self.publication_start = timezone.now()
        super(PublishableModel, self).save(*args, **kwargs)

    def publish(self, commit=True, update_publication_start=False):
        if self.status != app_settings.PUBLICATION_STATUS_PUBLISHED:
            self.status = app_settings.PUBLICATION_STATUS_PUBLISHED
            if update_publication_start:  # and not self.publication_start:
                self.publication_start = timezone.now()
            if commit:
                self.save()

    def unpublish(self, commit=True, update_publication_start=False, update_publication_end=False):
        if self.status != app_settings.PUBLICATION_STATUS_DRAFT:
            self.status = app_settings.PUBLICATION_STATUS_DRAFT
            if update_publication_start and self.publication_start:
                self.publication_start = None
            if update_publication_end and self.publication_end:
                self.publication_end = None
            if commit:
                self.save()
