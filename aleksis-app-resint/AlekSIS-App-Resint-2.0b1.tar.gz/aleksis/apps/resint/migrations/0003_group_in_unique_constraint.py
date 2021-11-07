# Generated by Django 3.2.5 on 2021-07-04 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resint', '0002_permissions'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='poster',
            name='unique_site_week_year',
        ),
        migrations.AddConstraint(
            model_name='poster',
            constraint=models.UniqueConstraint(fields=('site_id', 'week', 'year', 'group'), name='unique_site_week_year'),
        ),
    ]
