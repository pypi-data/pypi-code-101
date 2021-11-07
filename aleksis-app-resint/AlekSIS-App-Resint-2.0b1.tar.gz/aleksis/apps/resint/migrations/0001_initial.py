# Generated by Django 3.2.4 on 2021-06-30 18:23

import aleksis.apps.resint.models
import calendarweek.calendarweek
import django.contrib.sites.managers
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='PosterGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extended_data', models.JSONField(default=dict, editable=False)),
                ('slug', models.SlugField(help_text="If you use 'example', the filename will be 'example.pdf'.", verbose_name='Slug used in URL name')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('publishing_day', models.PositiveSmallIntegerField(choices=[(0, 'Montag'), (1, 'Dienstag'), (2, 'Mittwoch'), (3, 'Donnerstag'), (4, 'Freitag'), (5, 'Samstag'), (6, 'Sonntag')], verbose_name='Publishing weekday')),
                ('publishing_time', models.TimeField(verbose_name='Publishing time')),
                ('default_pdf', models.FileField(help_text='This PDF file will be shown if there is no current PDF.', upload_to='default_posters/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])], verbose_name='Default PDF')),
                ('show_in_menu', models.BooleanField(default=True, verbose_name='Show in menu')),
                ('public', models.BooleanField(default=False, verbose_name='Show for not logged-in users')),
                ('site', models.ForeignKey(default=1, editable=False, on_delete=django.db.models.deletion.CASCADE, to='sites.site')),
            ],
            options={
                'verbose_name': 'Poster group',
                'verbose_name_plural': 'Poster groups',
            },
            managers=[
                ('objects', django.contrib.sites.managers.CurrentSiteManager()),
            ],
        ),
        migrations.CreateModel(
            name='Poster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extended_data', models.JSONField(default=dict, editable=False)),
                ('week', models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'), (20, '20'), (21, '21'), (22, '22'), (23, '23'), (24, '24'), (25, '25'), (26, '26'), (27, '27'), (28, '28'), (29, '29'), (30, '30'), (31, '31'), (32, '32'), (33, '33'), (34, '34'), (35, '35'), (36, '36'), (37, '37'), (38, '38'), (39, '39'), (40, '40'), (41, '41'), (42, '42'), (43, '43'), (44, '44'), (45, '45'), (46, '46'), (47, '47'), (48, '48'), (49, '49'), (50, '50'), (51, '51'), (52, '52')], default=calendarweek.calendarweek.CalendarWeek.current_week, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(53)], verbose_name='Calendar week')),
                ('year', models.PositiveSmallIntegerField(default=aleksis.apps.resint.models._get_current_year, verbose_name='Year')),
                ('pdf', models.FileField(upload_to='posters/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])], verbose_name='PDF')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posters', to='resint.postergroup', verbose_name='Poster group')),
                ('site', models.ForeignKey(default=1, editable=False, on_delete=django.db.models.deletion.CASCADE, to='sites.site')),
            ],
            options={
                'verbose_name': 'Poster',
                'verbose_name_plural': 'Posters',
            },
            managers=[
                ('objects', django.contrib.sites.managers.CurrentSiteManager()),
            ],
        ),
        migrations.AddConstraint(
            model_name='postergroup',
            constraint=models.UniqueConstraint(fields=('site_id', 'name'), name='unique_site_name'),
        ),
        migrations.AddConstraint(
            model_name='postergroup',
            constraint=models.UniqueConstraint(fields=('site_id', 'slug'), name='unique_site_slug'),
        ),
        migrations.AddConstraint(
            model_name='poster',
            constraint=models.UniqueConstraint(fields=('site_id', 'week', 'year'), name='unique_site_week_year'),
        ),
    ]
