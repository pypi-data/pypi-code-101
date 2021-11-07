# Generated by Django 2.2.11 on 2021-08-31 14:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('report_designer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Format',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Наименование в БД')),
                ('internal_type', models.SmallIntegerField(choices=[(0, 'Автоинкрементное'), (1, 'Автоинкрементное (64-битное)'), (2, 'Бинарное'), (3, 'Логическое'), (4, 'Строковое'), (5, 'Дата'), (6, 'Дата и время'), (7, 'Десятичное с фиксированной точностью'), (8, 'Период времени (в микросекундах)'), (9, 'Файл'), (10, 'Изображение'), (11, 'Путь до файла'), (12, 'Число с плавающей точкой'), (13, 'Целочисленное'), (14, 'Целочисленное (64-битное)'), (15, 'IP адрес'), (16, 'Логическое с нулевым значением'), (17, 'Положительное целочисленное'), (18, 'Положительное целочисленное (16-битное)'), (19, 'Название-метка'), (20, 'Целочисленное (16-битное)'), (21, 'Текстовое'), (22, 'Время'), (23, 'URL'), (24, 'UUID')], verbose_name='Тип поля')),
                ('representation', models.CharField(max_length=1000, verbose_name='Представление')),
            ],
            options={
                'verbose_name': 'Формат',
                'verbose_name_plural': 'Форматы',
                'ordering': ('-pk',),
            },
        ),
        migrations.CreateModel(
            name='Pattern',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Наименование')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата и время обновления')),
                ('is_visible_in_patterns', models.BooleanField(default=True, verbose_name='Отображать в перечне шаблонов при формировании нового шаблона')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rd_patterns', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Шаблон',
                'verbose_name_plural': 'Шаблоны',
                'ordering': ('-pk',),
            },
        ),
        migrations.CreateModel(
            name='PatternGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Группа шаблона',
                'verbose_name_plural': 'Группы шаблонов',
                'ordering': ('-pk',),
            },
        ),
        migrations.CreateModel(
            name='TableField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Наименование')),
                ('alias', models.CharField(blank=True, max_length=200, verbose_name='Псевдоним')),
                ('db_field', models.CharField(max_length=200, verbose_name='Поле таблицы БД')),
                ('is_visible', models.BooleanField(default=True, verbose_name='Отображение')),
                ('is_relation', models.BooleanField(default=False, verbose_name='Связанное поле')),
                ('db_table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fields', to='report_designer.DBTable', verbose_name='Таблица БД')),
                ('representation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tablefield_fields', to='report_designer.Format', verbose_name='Представление')),
            ],
            options={
                'verbose_name': 'Поле таблицы БД',
                'verbose_name_plural': 'Поля таблиц БД',
                'ordering': ('-pk',),
                'abstract': False,
                'unique_together': {('db_table', 'name', 'db_field')},
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000, unique=True, verbose_name='Наименование')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rd_reports', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('pattern', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='report_designer.Pattern', verbose_name='Шаблон отчета')),
            ],
            options={
                'verbose_name': 'Отчет',
                'verbose_name_plural': 'Отчеты',
                'ordering': ('-pk',),
            },
        ),
        migrations.CreateModel(
            name='PatternRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Наименование')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='report_designer.PatternRelation', verbose_name='Родительская связь')),
                ('pattern', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pattern_relations', to='report_designer.Pattern', verbose_name='Шаблон отчета')),
                ('table_field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report_designer.TableField', verbose_name='Поле таблицы')),
                ('target', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='report_designer.DBTable', verbose_name='Связанная таблица')),
            ],
            options={
                'verbose_name': 'Связь таблиц внутри шаблона',
                'verbose_name_plural': 'Связи таблиц внутри шаблонов',
                'ordering': ('-pk',),
                'unique_together': {('pattern', 'name')},
            },
        ),
        migrations.CreateModel(
            name='PatternFilter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expression', models.CharField(blank=True, max_length=2000, verbose_name='Выражение')),
                ('pattern', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pattern_filters', to='report_designer.Pattern', verbose_name='Шаблон отчета')),
                ('relation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='report_designer.PatternRelation', verbose_name='Условие связи')),
            ],
            options={
                'verbose_name': 'Условие выборки внутри шаблона',
                'verbose_name_plural': 'Условия выборки внутри шаблонов',
                'ordering': ('-pk',),
            },
        ),
        migrations.CreateModel(
            name='PatternField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Наименование')),
                ('alias', models.CharField(blank=True, max_length=200, verbose_name='Псевдоним')),
                ('expression', models.CharField(blank=True, max_length=2000, verbose_name='Выражение')),
                ('internal_type', models.SmallIntegerField(blank=True, choices=[(0, 'Автоинкрементное'), (1, 'Автоинкрементное (64-битное)'), (2, 'Бинарное'), (3, 'Логическое'), (4, 'Строковое'), (5, 'Дата'), (6, 'Дата и время'), (7, 'Десятичное с фиксированной точностью'), (8, 'Период времени (в микросекундах)'), (9, 'Файл'), (10, 'Изображение'), (11, 'Путь до файла'), (12, 'Число с плавающей точкой'), (13, 'Целочисленное'), (14, 'Целочисленное (64-битное)'), (15, 'IP адрес'), (16, 'Логическое с нулевым значением'), (17, 'Положительное целочисленное'), (18, 'Положительное целочисленное (16-битное)'), (19, 'Название-метка'), (20, 'Целочисленное (16-битное)'), (21, 'Текстовое'), (22, 'Время'), (23, 'URL'), (24, 'UUID')], null=True, verbose_name='Тип поля')),
                ('order', models.PositiveSmallIntegerField(default=0, verbose_name='Порядковый номер')),
                ('is_virtual', models.BooleanField(default=False, verbose_name='Виртуальное поле')),
                ('is_group', models.BooleanField(default=False, verbose_name='Групповое поле')),
                ('is_sort', models.BooleanField(default=False, verbose_name='Сортировочное поле')),
                ('reverse_sort', models.BooleanField(default=False, verbose_name='Обратная сортировка')),
                ('is_aggregate', models.BooleanField(default=False, help_text='Аггрегация производится для групповых полей шаблона', verbose_name='Агрегированное поле')),
                ('aggregate_function', models.CharField(blank=True, choices=[('sum', 'Сумма'), ('mean', 'Среднее'), ('max', 'Максимальное'), ('min', 'Минимальное')], max_length=20, null=True, verbose_name='Функция агрегирования')),
                ('field', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pattern_fields', to='report_designer.TableField', verbose_name='Поле таблицы БД')),
                ('pattern', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pattern_fields', to='report_designer.Pattern', verbose_name='Шаблон отчета')),
                ('relation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='report_designer.PatternRelation', verbose_name='Условие связи')),
                ('representation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='patternfield_fields', to='report_designer.Format', verbose_name='Представление')),
            ],
            options={
                'verbose_name': 'Поле шаблона отчета',
                'verbose_name_plural': 'Поля шаблонов отчетов',
                'ordering': ('order', '-pk'),
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='pattern',
            name='groups',
            field=models.ManyToManyField(related_name='patterns', to='report_designer.PatternGroup', verbose_name='Группы шаблонов'),
        ),
        migrations.AddField(
            model_name='pattern',
            name='root',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='root_table_patterns', to='report_designer.DBTable', verbose_name='Основная таблица'),
        ),
        migrations.AddField(
            model_name='pattern',
            name='tables',
            field=models.ManyToManyField(related_name='patterns', to='report_designer.DBTable', verbose_name='Таблицы БД'),
        ),
    ]
