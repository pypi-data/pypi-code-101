# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils import formats
from django.utils.safestring import mark_safe
from django.utils.translation import ungettext, ugettext_lazy as _
from django.utils import timezone
from django.utils.timezone import localtime, get_current_timezone

from .. import settings as app_settings
from .admin_filters import IsPublishedFilter


class PublishableModelAdmin(admin.ModelAdmin):
    publication_field = 'status'
    date_hierarchy = 'publication_start'
    actions = ['make_published', 'make_unpublished']
    DISPLAY_PUBLICATION_START = False
    DISPLAY_PUBLICATION_END = False
    DISPLAY_PUBLICATION_DATES = False

    def get_list_filter(self, request):
        """ Override get_list_filter to allow final user to filter on published or draft items """
        list_filter = list(super(PublishableModelAdmin, self).get_list_filter(request))
        list_filter.append(IsPublishedFilter)
        return list_filter

    def get_list_display(self, request):
        """ Override get_list_display to show publication fields in change_list.html """
        list_display = list(super(PublishableModelAdmin, self).get_list_display(request))
        if 'display_actual_status' not in list_display:
            list_display.append('display_actual_status')
        if self.DISPLAY_PUBLICATION_START and 'display_publication_start' not in self.list_display:
            list_display.append('display_publication_start')
        if self.DISPLAY_PUBLICATION_END and 'display_publication_end' not in self.list_display:
            list_display.append('display_publication_end')
        if self.DISPLAY_PUBLICATION_DATES and 'display_publication_dates' not in self.list_display:
            list_display.append('display_publication_dates')
        return list_display

    # ===========================================
    # List Display Fields
    # ===========================================
    def display_actual_status(self, obj):
        return obj.is_actual

    display_actual_status.short_description = _('is published')
    display_actual_status.boolean = True

    def display_publication_start(self, obj=None):
        return formats.date_format(localtime(obj.publication_start, get_current_timezone()),
                                   "SHORT_DATETIME_FORMAT")

    display_publication_start.short_description = _('Publication Start Date')
    display_publication_start.admin_order_field = 'publication_start'

    def display_publication_end(self, obj=None):
        return formats.date_format(localtime(obj.publication_end, get_current_timezone()),
                                   "SHORT_DATETIME_FORMAT")

    display_publication_end.short_description = _('Publication End Date')
    display_publication_end.admin_order_field = 'publication_end'

    @mark_safe
    def display_publication_dates(self, obj):
        dt = ""
        if obj and obj.id:
            if obj.publication_start:
                dt += "{0} {1}" \
                      "".format(_("From"), formats.date_format(localtime(obj.publication_start, get_current_timezone()),
                                                               "SHORT_DATETIME_FORMAT"))
                if obj.publication_end:
                    dt += "<br>{0} {1}" \
                          "".format(_("To"), formats.date_format(localtime(obj.publication_end, get_current_timezone()),
                                                                 "SHORT_DATETIME_FORMAT"))
        return mark_safe(dt)

    display_publication_dates.short_description = _("Publication Dates")
    display_publication_dates.admin_order_field = 'publication_start'

    # ===========================================
    # Actions
    # ===========================================
    def make_published(self, request, queryset):
        rows_updated = queryset.update(
            status=app_settings.PUBLICATION_STATUS_PUBLISHED,
            publication_start=timezone.now(),
            publication_end=None)
        self.message_user(request, ungettext('%(count)d entries was published',
                                             '%(count)d entries where published',
                                             rows_updated) % {'count': rows_updated})

    make_published.short_description = _('Publish selected entries')

    def make_unpublished(self, request, queryset):
        rows_updated = queryset.update(
            status=app_settings.PUBLICATION_STATUS_DRAFT,
            publication_start=None,
            publication_end=None)
        self.message_user(request, ungettext('%(count)d entries was unpublished',
                                             '%(count)d entries where unpublished',
                                             rows_updated) % {'count': rows_updated})

    make_unpublished.short_description = _('Unpublish selected entries')
