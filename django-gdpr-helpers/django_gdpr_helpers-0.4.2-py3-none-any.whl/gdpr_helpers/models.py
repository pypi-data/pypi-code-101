from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _

from .managers import LegalReasonGroupManager, LegalReasonManager, PrivacyLogManager


class PrivacyLog(models.Model):
    """A new log will be created when a user accept some flags"""

    content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")
    created = models.DateTimeField(_("Data creazione"), auto_now_add=True)

    objects = PrivacyLogManager()

    def __str__(self):
        return f"{self.content_type} privacy-log {self.created}"

    class Meta:
        verbose_name = _("Privacy log")
        verbose_name_plural = _("Privacy logs")


class LegalReasonGroup(models.Model):
    """
    Group LegalReason by a common key to use in specific form,
    es: contact form, registration form, lead form etc.
    """

    where = models.CharField(_("Posizione del gruppo"), max_length=100, unique=True)

    objects = LegalReasonGroupManager()

    def get_as_form_fields(self):
        fields = []
        for reason in self.legal_reasons.get_as_form_fields():
            fields.append(reason)
        return fields

    def __str__(self):
        return gettext(f"For use in {self.where}")

    class Meta:
        verbose_name = _("Gruppo ragioni legali")
        verbose_name_plural = _("Gruppi ragioni legali")


class LegalReason(models.Model):
    """Register the legal reason, it will be used for flags and privacy-policy page"""
    slug = models.SlugField(_("Slug del consenso"), unique=True)
    flag_text = models.TextField(_("Testo da mostrare nella spunta"))
    privacy_description = models.TextField(
        _("Descrizione per pagina privacy"), blank=True, null=True
    )
    required = models.BooleanField(_("Obbligatorio"), default=False)
    active = models.BooleanField(_("Attivo"), default=False)
    legal_group = models.ForeignKey(
        LegalReasonGroup,
        verbose_name=_("Gruppo di ragioni legali"),
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="legal_reasons",
    )

    objects = LegalReasonManager()

    @property
    def field_name(self):
        return f"privacy_{self.slug}"

    def __str__(self):
        return self.flag_text

    class Meta:
        verbose_name = _("Ragione legale")
        verbose_name_plural = _("Ragioni legali")


class PrivacyEvent(models.Model):
    """Register user consent"""

    privacy_log = models.ForeignKey(
        PrivacyLog,
        on_delete=models.PROTECT,
        verbose_name=_("Privacy log"),
        related_name="event",
    )
    legal_reason = models.ForeignKey(
        LegalReason,
        on_delete=models.PROTECT,
        verbose_name=_("Ragione legale"),
        related_name="event",
    )
    accepted = models.BooleanField(_("Accetata"), default=False)

    def __str__(self):
        return f"{self.legal_reason} {self.accepted}"

    class Meta:
        verbose_name = _("Evento privacy")
        verbose_name_plural = _("Eventi privacy")
