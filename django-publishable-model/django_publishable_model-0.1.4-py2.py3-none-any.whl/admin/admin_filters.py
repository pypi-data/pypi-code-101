# -*- coding: utf-8 -*-
from django.utils.translation import ugettext, ugettext_lazy as _
from django.contrib import messages
from django.contrib.admin.filters import SimpleListFilter


class SimpleBooleanListFilter(SimpleListFilter):
    title = ''  # _('Your Filter Label')
    parameter_name = ''  # 'your_filter_key'
    is_legacy = True
    LOOKUP_CHOICES = (
        ('1', _('Yes')),
        ('0', _('No')),
    )

    def lookups(self, request, model_admin):
        return self.LOOKUP_CHOICES

    def get_allowed_values(self):
        return dict(self.LOOKUP_CHOICES).keys()

    def get_true_queryset_values(self, queryset):
        raise NotImplementedError()

    def get_false_queryset_values(self, queryset):
        raise NotImplementedError()

    def queryset(self, request, queryset):
        _value = self.value()
        if _value in self.get_allowed_values():
            if bool(int(_value)):
                return self.get_true_queryset_values(queryset)
            else:
                return self.get_false_queryset_values(queryset)
        if self.value():
            messages.add_message(request, messages.WARNING,
                                 _("Impossible to filter with the argument '{0}' for the key '{1}'"
                                   "").format(self.value(), self.title))
        return queryset


class IsPublishedFilter(SimpleBooleanListFilter):
    title = _('Published')
    parameter_name = 'is_published'

    def get_true_queryset_values(self, queryset):
        return queryset.published_items()

    def get_false_queryset_values(self, queryset):
        return queryset.draft_items()
