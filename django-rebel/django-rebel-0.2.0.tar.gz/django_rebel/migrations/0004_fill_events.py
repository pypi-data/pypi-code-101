# Generated by Django 2.1.5 on 2020-03-10 17:40

from django.db import migrations
from django.db import models


def fill_events(apps, schema):
    Mail = apps.get_model("django_rebel", "Mail")

    Mail.objects.with_event_status().update(has_opened=models.F('calculated_has_opened'),
                                            has_delivered=models.F('calculated_has_delivered'),
                                            has_clicked=models.F('calculated_has_clicked'),)


class Migration(migrations.Migration):

    dependencies = [
        ('django_rebel', '0003_auto_20200310_1740'),
    ]

    operations = [
        migrations.RunPython(fill_events)
    ]
