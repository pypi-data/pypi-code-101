# Generated by Django 2.2.2 on 2019-06-26 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SampleAppInstallation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('installed_org_uuid', models.UUIDField()),
                ('persistent_bot_token', models.TextField()),
                ('persistent_token_prefix', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
