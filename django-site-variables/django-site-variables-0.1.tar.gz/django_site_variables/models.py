from django.db import models
from django.utils.translation import gettext_lazy as _


class SiteVariableManager(models.Manager):

    def __init__(self, value_type: int):
        self.value_type = value_type
        super().__init__()

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(value_type=self.value_type)


class SiteVariable(models.Model):
    """
    SiteVariable model
    """
    TYPE_TEXT = 0
    TYPE_BOOLEAN = 1
    TYPE_NUMBER = 2
    VALUE_TYPE_CHOICES = (
        (TYPE_TEXT, _('Text')),
        (TYPE_BOOLEAN, _('Boolean')),
        (TYPE_NUMBER, _('Number')),
    )

    name = models.SlugField(_('name'), max_length=128, db_index=True, unique=True)
    content = models.TextField(_('value'))

    value_type = models.PositiveSmallIntegerField(_('value type'), default=TYPE_TEXT, choices=VALUE_TYPE_CHOICES)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('site variable')
        verbose_name_plural = _('site variables')


class SiteVariableText(SiteVariable):
    objects = SiteVariableManager(SiteVariable.TYPE_TEXT)

    class Meta:
        proxy = True
        verbose_name = _('string')
        verbose_name_plural = _('strings')


class SiteVariableBoolean(SiteVariable):
    objects = SiteVariableManager(SiteVariable.TYPE_BOOLEAN)

    class Meta:
        proxy = True
        verbose_name = _('boolean value')
        verbose_name_plural = _('boolean values')


class SiteVariableNumber(SiteVariable):
    objects = SiteVariableManager(SiteVariable.TYPE_NUMBER)

    class Meta:
        proxy = True
        verbose_name = _('number value')
        verbose_name_plural = _('number values')
