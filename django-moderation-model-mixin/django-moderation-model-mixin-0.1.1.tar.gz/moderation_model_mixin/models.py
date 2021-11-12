# -*- coding: utf-8 -*-
import logging

from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import Q
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from moderation_model_mixin import signals, managers, settings


logger = logging.getLogger(__name__)


class ModerationModelMixin(models.Model):
    SEND_MODERATION_SIGNAL_ON_SAVE = True

    objects = managers.ModerableEntryManager()
    published_objects = managers.AcceptedModerableEntryManager()
    moderated_objects = managers.ModeratedModerableEntryManager()
    accepted_objects = managers.AcceptedModerableEntryManager()
    rejected_objects = managers.RejectedModerableEntryManager()
    not_moderated_objects = managers.NotModeratedModerableEntryManager()
    not_rejected_objects = managers.NotRejectedModerableEntryManager()

    MODERATION_STATE_CHOICES = ((settings.MODERATION_STATE_QUEUED, _("Not Moderated")),
                                (settings.MODERATION_STATE_ACCEPTED, _("Accepted")),
                                (settings.MODERATION_STATE_REJECTED, _("Rejected")))

    moderation_date = models.DateTimeField(_("Moderation Date"), blank=True, null=True)
    moderation_state = models.IntegerField(_("Moderation State"), choices=MODERATION_STATE_CHOICES,
                                           default=settings.MODERATION_STATE_QUEUED)

    class Meta:
        abstract = True

    @property
    def is_moderated(self):
        return self.moderation_state != settings.MODERATION_STATE_QUEUED

    @property
    def is_rejected(self):
        return self.moderation_state == settings.MODERATION_STATE_REJECTED

    @property
    def is_accepted(self):
        return self.moderation_state == settings.MODERATION_STATE_ACCEPTED

    def is_acceptable(self):
        return not self.is_moderated

    def is_rejectable(self):
        return not self.is_rejected

    def save(self, *args, **kwargs):
        send_signals = kwargs.pop('send_signal', True) and self.SEND_MODERATION_SIGNAL_ON_SAVE
        if self.is_moderated and not self.moderation_date:
            self.moderation_date = timezone.now()
        if send_signals:
            is_accepted_modified = False
            is_rejected_modified = False
            try:
                old_instance = self.__class__.objects.get(pk=self.pk)
                if not old_instance.is_rejected and self.is_rejected:
                    is_rejected_modified = True
                if not old_instance.is_accepted and self.is_accepted:
                    is_accepted_modified = True
            except self.__class__.DoesNotExist:
                pass
            super(ModerationModelMixin, self).save(*args, **kwargs)
            if is_accepted_modified:
                signals.set_accepted.send(sender=self.__class__, instance=self, explicit=False)
            if is_rejected_modified:
                signals.set_rejected.send(sender=self.__class__, instance=self, explicit=False)
        else:
            super(ModerationModelMixin, self).save(*args, **kwargs)

    @property
    def is_actual(self):
        return not self.is_rejected

    @property
    def is_sharable(self):
        return self.is_accepted

    def set_accepted(self, commit=True, **kwargs):
        self.moderation_state = settings.MODERATION_STATE_ACCEPTED
        if commit:
            self.save(send_signal=False)
            signals.set_accepted.send(sender=self.__class__, instance=self, explicit=True)

    set_accepted.alters_data = True

    def set_rejected(self, commit=True, **kwargs):
        self.moderation_state = settings.MODERATION_STATE_REJECTED
        if commit:
            self.save(send_signal=False)
            signals.set_rejected.send(sender=self.__class__, instance=self, explicit=True)

    set_rejected.alters_data = True

    def get_previous(self, queryset=None):
        if queryset is None:
            queryset = self.__class__.published_objects.all()
        if hasattr(self, 'created'):
            qs = queryset.order_by('-moderation_date', '-created')
            qs = qs.filter(Q(moderation_date__lt=self.moderation_date) |
                           (Q(moderation_date=self.moderation_date) & Q(created__lt=self.created)))
        else:
            qs = queryset.order_by('-moderation_date')
            qs = qs.filter(moderation_date__lt=self.moderation_date)
        if qs.count():
            return qs[0:1].get()
        return None

    def get_next(self, queryset=None):
        if queryset is None:
            queryset = self.__class__.published_objects.all()
        if hasattr(self, 'created'):
            qs = queryset.order_by('moderation_date', 'created')
            qs = qs.filter(Q(moderation_date__gt=self.moderation_date) |
                           (Q(moderation_date=self.moderation_date) &
                            Q(created__gt=self.created)))
        else:
            qs = queryset.order_by('moderation_date')
            qs = qs.filter(moderation_date__gt=self.moderation_date)
        if qs.count():
            return qs[0:1].get()
        return None

