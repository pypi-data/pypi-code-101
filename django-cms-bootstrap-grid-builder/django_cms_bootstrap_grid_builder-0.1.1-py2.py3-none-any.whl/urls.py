# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views


app_name = 'bootstrap_grid_builder'
urlpatterns = [
    url(r'', TemplateView.as_view(template_name="base.html")),
    ]
