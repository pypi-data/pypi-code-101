# Generated by Django 2.1.4 on 2019-01-14 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_rebel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mail',
            name='email_from',
            field=models.CharField(db_index=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='mail',
            name='email_to',
            field=models.CharField(db_index=True, max_length=256),
        ),
    ]
