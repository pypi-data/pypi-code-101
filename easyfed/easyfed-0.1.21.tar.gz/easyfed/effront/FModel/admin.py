from django.contrib import admin
from FModel.models import Clients
from django.contrib.sessions.models import Session
# Register your models here.
admin.site.register(Clients)
admin.site.register(Session)