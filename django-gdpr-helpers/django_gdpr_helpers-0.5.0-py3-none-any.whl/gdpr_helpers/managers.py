from django import forms
from django.apps import apps
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import gettext_lazy as _


class LegalReasonManager(models.Manager):
    def get_legal_reasons(self):
        """Return a queryset of active Legal Reasons"""
        return self.filter(active=True)

    def get_as_form_fields(self):
        """Return a list of dict of Legal Reasons fields (booleanField)"""
        fields = []
        for reason in self.get_legal_reasons():
            if reason.required:
                fields.append(
                    {
                        "field_name": reason.field_name,
                        "field": forms.BooleanField(label=reason.flag_text),
                    }
                )
            else:
                fields.append(
                    {
                        "field_name": reason.field_name,
                        "field": forms.TypedChoiceField(
                            label=reason.flag_text,
                            coerce=lambda x: x == "True",
                            choices=((True, _("Accetto")), (False, _("Rifiuto"))),
                            widget=forms.RadioSelect,
                        ),
                    }
                )
        return fields


class LegalReasonGroupManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().prefetch_related("legal_reasons")


class PrivacyLogManager(models.Manager):
    def _lazy_load_models(self):
        """Lazy load the models so we don't get circular imports problems"""
        self.legal_reason = apps.get_model("gdpr_helpers", "LegalReason")
        self.privacy_log = apps.get_model("gdpr_helpers", "PrivacyLog")
        self.privacy_event = apps.get_model("gdpr_helpers", "PrivacyEvent")

    def create_log(self, content_object, cleaned_data):
        self._lazy_load_models()
        """Create a new Log using data from a form"""
        privacy_log = self.privacy_log(content_object=content_object)
        privacy_log.save()
        for reason in self.legal_reason.objects.get_legal_reasons():
            if reason.field_name in cleaned_data:
                self.privacy_event.objects.create(
                    privacy_log=privacy_log,
                    legal_reason=self.legal_reason.objects.get(
                        slug=reason.field_name.split("privacy_")[1]
                    ),
                    accepted=cleaned_data[reason.field_name],
                )
        return privacy_log

    def get_privacy_logs_for_object(self, object_instance):
        """Return last privacy log for object"""
        self._lazy_load_models()
        content_type = ContentType.objects.get_for_model(object_instance)
        return self.prefetch_related("event").filter(content_type=content_type, object_id=object_instance.id).order_by("-created").first()

    def get_consents_for_object(self, object_instance):
        consents = []
        log = self.get_privacy_logs_for_object(object_instance)
        if log:
            for event in log.event.all():
                consents.append(
                    {
                        "slug": event.legal_reason.slug,
                        "accepted": event.accepted,
                        "given_at": event.privacy_log.created
                    }
                )
        return consents
