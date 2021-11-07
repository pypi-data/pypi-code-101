# Generated by Django 2.2.11 on 2021-11-01 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report_designer', '0009_reporttablerelation_reporttablerelationcondition'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportfield',
            name='report_table_relation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='report_fields', to='report_designer.ReportTableRelation', verbose_name='Связь таблицы поля с основной таблицей отчета'),
        ),
    ]
