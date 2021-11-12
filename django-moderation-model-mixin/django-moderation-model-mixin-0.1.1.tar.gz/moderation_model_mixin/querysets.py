# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals


from django.db.models.query import QuerySet

from moderation_model_mixin import settings


class ModerableQuerySet(QuerySet):
    def moderated(self):
        return self.exclude(moderation_state=settings.MODERATION_STATE_QUEUED)

    def not_moderated(self):
        return self.filter(moderation_state=settings.MODERATION_STATE_QUEUED)

    def rejected(self):
        return self.filter(moderation_state=settings.MODERATION_STATE_REJECTED)

    def not_rejected(self):
        return self.exclude(moderation_state=settings.MODERATION_STATE_REJECTED)

    def accepted(self):
        return self.filter(moderation_state=settings.MODERATION_STATE_ACCEPTED)
