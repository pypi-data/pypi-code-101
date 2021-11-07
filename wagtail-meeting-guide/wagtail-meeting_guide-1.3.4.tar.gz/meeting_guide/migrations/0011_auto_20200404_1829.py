# Generated by Django 2.2.5 on 2020-04-04 22:29

from django.db import migrations, models
import meeting_guide.validators


class Migration(migrations.Migration):

    dependencies = [
        ('meeting_guide', '0010_auto_20200322_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='venmo',
            field=models.TextField(blank=True, default='', help_text='Example: @aa-tbc', max_length=17, validators=[meeting_guide.validators.VenmoUsernameValidator()], verbose_name='Venmo Account'),
        ),
    ]
