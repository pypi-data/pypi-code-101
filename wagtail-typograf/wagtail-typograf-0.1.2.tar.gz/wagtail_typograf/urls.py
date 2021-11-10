from django.conf.urls import url
from .views import typograf_api

app_name = "wagtail_typograf"

urlpatterns = [
    url(r"^typograf/", typograf_api, name="typograf"),
]
