# Generated by Django 3.2.4 on 2021-07-17 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bom', '0040_alter_organization_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='subscription_quantity',
            field=models.IntegerField(default=0),
        ),
    ]
