import abc
import json
import mimetypes
from operator import itemgetter

from django.contrib.auth.decorators import login_required
from django.contrib.postgres.aggregates import StringAgg
from django.db import transaction
from django.db.models import (
    Value,
    F,
    BooleanField,
    Case,
    When,
    Func,
    CharField,
)
from django.db.models.functions import Cast, Concat
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.functional import cached_property
from django.views import View
from django.views.generic import DetailView, TemplateView
from django.views.generic.edit import FormMixin

from report_designer.builder import ReportDataHandler
from report_designer.consts import Functions
from report_designer.core.utils import order_by_list
from report_designer.core.views import (
    TitleMixin,
    AjaxContentListView,
    ParentMixin,
    ObjectActionAjaxView,
    DynamicContentTableBaseView,
    CreateAjaxView,
    ActionGroupMixin,
    UpdateAjaxView,
    BreadcrumbsListMixin,
    BackUrlDetailMixin,
    BreadcrumbsDetailMixin,
    Select2BaseListView,
    AjaxResponseMixin,
    CustomDeleteView,
    CustomTemplateView,
    TableMixin,
)
from report_designer.models import (
    Report,
    DBTable,
    TableField,
    ReportField,
    ReportFieldRelation,
    ReportTableRelation,
    ReportTable,
)
from report_designer.reports.actions import (
    ReportListActionGroup,
    ReportDropdownActionGroup,
    ReportAddFieldActionGroup,
    ReportTableRelationActionGroup,
    ReportAddVirtualFieldActionGroup,
    ReportGenerateActionGroup,
    ReportExcelActionGroup,
)
from report_designer.reports.filters import (
    ReportFilterSet,
    ReportFieldsFilterSet,
    ReportTableRelationFilterSet,
)
from report_designer.reports.forms import (
    ReportCreateForm,
    ReportCreateByReportForm,
    ReportUpdateForm,
    ReportTableRelationCreateUpdateForm,
    ReportTableRelationConditionsFormsetManager,
    ReportFieldUpdateForm,
    ReportVirtualFieldCreateUpdateForm,
    ReportGenerateForm,
)
from report_designer.reports.report_handler import ReportCloneHandler
from report_designer.reports.tables import (
    ReportsTable,
    ReportFieldsTable,
    ReportTableRelationTable,
    ReportGeneratedTable,
)


# endregion Базовые миксины


class ReportBreadcrumbsListMixin(BreadcrumbsListMixin):
    """
    Хлебные крошки отчетов
    """

    title_breadcrumb = 'Список отчетов'


class ReportBreadcrumbsDetailBaseMixin(BreadcrumbsDetailMixin, ReportBreadcrumbsListMixin):
    """
    Хлебные крошки отчета
    """

    pass


class ReportsDynamicContentTableBaseView(ParentMixin, DynamicContentTableBaseView):
    """
    Базовое представление для динамических список на странице отчета
    """

    parent_model = Report
    is_paginate = False

    def get_content_url_kwargs(self):
        content_url_kwargs = super().get_content_url_kwargs()
        content_url_kwargs.update(pk=self.parent.pk)
        return content_url_kwargs


# endregion Базовые миксины


# region Список отчетов


@method_decorator(login_required, name='dispatch')
class ReportListView(ReportBreadcrumbsListMixin, DynamicContentTableBaseView):
    """
    Представление: Список отчетов
    """

    model = Report
    filterset_class = ReportFilterSet
    table_class = ReportsTable
    title = 'Отчеты'
    ajax_content_name = 'reports'
    action_group_classes = (ReportListActionGroup,)


# endregion Список отчетов


# region Создание / редактирование отчета


class ReportCreateUpdateMixin:
    """
    Миксин создания / редактирования отчета
    """

    model = Report

    def get_success_redirect_url(self):
        return self.object.get_detail_url()


class BaseReportCreateView(ReportCreateUpdateMixin, CreateAjaxView):
    """
    Базовое представление: Создание отчета
    """

    title = 'Создание отчета'
    form_class = ReportCreateForm

    def set_object_additional_values(self, obj):
        super().set_object_additional_values(obj)
        obj.author = self.request.user


@method_decorator(login_required, name='dispatch')
class ReportCreateView(BaseReportCreateView):
    """
    Представление: Создание отчета
    """

    form_class = ReportCreateForm

    def after_save(self, **kwargs):
        super().after_save(**kwargs)
        self.object.report_tables.create(report=self.object, db_table=self.object.root, is_root=True)


@method_decorator(login_required, name='dispatch')
class ReportCreateByReportView(BaseReportCreateView):
    """
    Представление: Создание отчета на основании другого отчета
    """

    form_class = ReportCreateByReportForm

    def after_save(self, **kwargs):
        super().after_save(**kwargs)
        form = kwargs.get('form')
        ReportCloneHandler(form.cleaned_data.get('report'), self.object).run()


@method_decorator(login_required, name='dispatch')
class ReportUpdateView(ReportCreateUpdateMixin, UpdateAjaxView):
    """
    Представление: Редактирование отчета
    """

    title = 'Редактирование отчета'
    form_class = ReportUpdateForm


# endregion Создание / редактирование отчета


# region Просмотр отчета


@method_decorator(login_required, name='dispatch')
class ReportDetailView(
    BackUrlDetailMixin,
    ReportBreadcrumbsDetailBaseMixin,
    ActionGroupMixin,
    TitleMixin,
    DetailView,
):
    """
    Представление: Просмотр отчета
    """

    model = Report
    template_name = 'report_designer/reports/detail.html'
    context_object_name = 'report'
    action_group_classes = (
        ReportDropdownActionGroup,
        ReportAddFieldActionGroup,
        ReportTableRelationActionGroup,
        ReportAddVirtualFieldActionGroup,
    )

    def get_title(self):
        return f'Отчет "{self.object.name}"'


@method_decorator(login_required, name='dispatch')
class ReportExportExcelView(View):
    """
    Экспорт отчета в Excel
    """

    model = Report

    def get(self, request, *args, **kwargs):
        report = get_object_or_404(Report, pk=self.request.GET.get('report'))

        # Построение шаблона
        handler = ReportDataHandler(report)
        handler.run()

        # Подготовка файла
        filename = f'{report.name}.xlsx'
        content_type = mimetypes.guess_type(filename)[0]
        response = FileResponse(streaming_content=handler.builder.excel(), content_type=content_type)
        response['Content-Disposition'] = "attachment; filename*=utf-8''{}".format(filename)
        return response


# endregion Просмотр отчета


# region Редактирование списка таблиц в отчете


class BaseTreeListView(AjaxContentListView):
    """
    Базовое представления для вывода дерева
    """

    is_paginate = False
    is_only_ajax = True
    is_subtree = False
    template_name = 'report_designer/reports/blocks/tables_tree_branch.html'
    context_object_name = 'tree_branches'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data.update(
            {
                'is_subtree': self.is_subtree,
            }
        )
        return context_data


class ExpressionsMixin:
    """
    Миксин для полей для составления выражений
    """

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data.update({'is_expression': self.is_expression})
        return context_data

    @property
    def is_expression(self):
        """
        Неперносимыое (кликабельное) поле
        """
        return 'is_expression' in self.request.GET


class DBTablesBaseTreeListView(ParentMixin, BaseTreeListView):
    """
    Базовое представление: Список таблиц БД / в отчете
    """

    queryset = DBTable.objects.available()
    context_object_name = 'tree_branches'
    parent_model = Report
    kwargs_parent_fk = 'report_pk'
    parent_context_name = 'report'
    is_processed = False

    def get_queryset(self):
        # Аннотация параметров для списка таблиц
        # 1). PK для URL загрузки полей
        # 2). Title из alias
        # 3). Существование связи для URL загрузки полей
        return (
            super()
            .get_queryset()
            .annotate(
                related_table_pk=F('pk'),
                title=F('alias'),
                is_relation=Value(True, output_field=BooleanField()),
            )
        )

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data.update({'is_processed': self.is_processed})
        return context_data


class ActionTablesMixin:
    """
    Миксин добавления URL действия с таблицами
    """

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data.update({'action_url': self.get_action_tables_url()})
        return context_data

    @abc.abstractmethod
    def get_action_tables_url(self):
        """
        URL для действия с таблицами
        """
        raise NotImplementedError


@method_decorator(login_required, name='dispatch')
class DBTablesTreeListView(ActionTablesMixin, DBTablesBaseTreeListView):
    """
    Представление: Список таблиц БД
    """

    def get_action_tables_url(self):
        return reverse_lazy('report_designer:reports:add-table', kwargs={'pk': self.parent.pk})


@method_decorator(login_required, name='dispatch')
class ReportDBTablesTreeListView(ActionTablesMixin, DBTablesBaseTreeListView):
    """
    Представление: Список таблиц в отчете
    """

    is_processed = True

    def get_queryset(self):
        # Доступны таблицы, добавленные в отчет
        return super().get_queryset().for_report(self.parent)

    def get_action_tables_url(self):
        return reverse_lazy('report_designer:reports:remove-table', kwargs={'pk': self.parent.pk})


@method_decorator(login_required, name='dispatch')
class TableFieldsListView(ExpressionsMixin, ParentMixin, BaseTreeListView):
    """
    Представление: Список таблиц БД / в отчете
    """

    queryset = TableField.objects.is_visible()
    parent_model = DBTable
    parent_field = 'db_table'
    is_subtree = True

    def get_queryset(self):
        queryset = super().get_queryset()

        # Цепочка связи
        chain = self.request.GET.get('chain', '')
        if self.is_processed:
            # Аннотация хеша цепочки связей полей отчета
            chain_kwargs = Func(
                StringAgg(
                    Cast(
                        Case(When(report_fields__report__pk=self.report.pk, then=F('report_fields__relations'))),
                        output_field=CharField(),
                    ),
                    delimiter=',',
                ),
                function='md5',
            )
            # Поля таблиц БД в полях очтета
            fields_in_report_fields = self.report.report_fields.values_list('field', flat=True)

            # Условие принадлежности поля к отчету
            condition = (
                chain
                and When(chain=Value(chain), then=Value(True))
                or When(pk__in=fields_in_report_fields, chain__isnull=True, then=Value(True))
            )
            is_exists_in_report_kwargs = Case(condition, default=Value(False), output_field=BooleanField())
            queryset = queryset.annotate(chain=chain_kwargs).annotate(is_exists_in_report=is_exists_in_report_kwargs)

        # Аннотации для составления выражений
        if self.is_expression:
            # Аннотация параметров поля
            field = Functions.Keywords.FIELD
            queryset = queryset.annotate(
                expression_field_name=Value(field, output_field=CharField()),
                expression_field_display_name=Value(
                    Functions.Keywords.DISPLAY_NAMES.get(field), output_field=CharField()
                ),
                expression_field_value=F('db_field'),
                expression_field_is_editable=Value(False, output_field=BooleanField()),
            )
        return queryset.with_related_tables(self.parent).with_title().order_by('is_relation', 'related_table_pk', 'pk')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data.update(
            {
                'report': self.report,
                'is_processed': self.is_processed,
            }
        )
        return context_data

    @property
    def is_processed(self):
        """
        Переносимые поля
        """
        return 'is_processed' in self.request.GET

    @cached_property
    def report(self):
        """
        Отчет
        """
        return get_object_or_404(Report, pk=self.kwargs.get('report_pk'))


class ReportDBTableChangeBaseView(ObjectActionAjaxView):
    """
    Базовое представление: Добавление / удаление таблицы в отчете
    """

    model = Report
    join_errors = True
    dependents = (('ajax_contents', 'report_tables'),)

    @cached_property
    def table(self):
        """
        Добавляемая таблица
        """
        return get_object_or_404(DBTable.objects.available(), pk=self.request.POST.get('table'))


@method_decorator(login_required, name='dispatch')
class ReportDBTableAddView(ReportDBTableChangeBaseView):
    """
    Представление: Добавление таблицы в отчет
    """

    title = 'Добавление таблицы в отчет'

    def valid_action(self):
        is_valid = super().valid_action()
        if self.object.report_tables.filter(db_table=self.table).exists():
            self.add_error(f'Таблица "{self.table.alias}" уже добавлена в отчет')
            is_valid = False
        return is_valid

    def action(self):
        super().action()
        self.object.report_tables.create(db_table=self.table, order=self.object.table_next_order)


@method_decorator(login_required, name='dispatch')
class ReportDBTableRemoveView(ReportDBTableChangeBaseView):
    """
    Представление: Удаление таблицы из отчета
    """

    title = 'Удаление таблицы из отчета'

    def valid_action(self):
        is_valid = super().valid_action()
        if not self.object.report_tables.filter(db_table=self.table).exists():
            self.add_error(f'Таблица "{self.table.alias}" не существует в отчете')
            is_valid = False
        if self.table == self.object.root:
            self.add_error(f'Таблица "{self.table.alias}" является основной таблицей отчета')
            is_valid = False
        return is_valid

    def action(self):
        super().action()
        # Удаление таблицы из отчета
        report_table = self.object.report_tables.filter(db_table=self.table)
        order = report_table.first().order
        report_table.delete()

        # Изменение порядка таблиц
        self.object.report_tables.filter(order__gt=order).update(order=F('order') - 1)


# endregion Редактирование списка таблиц в отчете


# region Список связей таблиц отчета


@method_decorator(login_required, name='dispatch')
class ReportTableRelationsListView(ReportsDynamicContentTableBaseView):
    """
    Представление: Список связей таблиц отчета
    """

    queryset = ReportTableRelation.objects.all()
    parent_field = 'report_table__report'
    table_class = ReportTableRelationTable
    filterset_class = ReportTableRelationFilterSet
    ajax_content_name = 'report_table_relations'

    def get_filterset_kwargs(self, filterset_class):
        filterset_kwargs = super().get_filterset_kwargs(filterset_class)
        filterset_kwargs.update({'report': self.parent})
        return filterset_kwargs


class ReportTableRelationCreateUpdateMixin(ParentMixin):
    """
    Миксин: Создание / редактирование связи таблицы отчета
    """

    template_name = 'report_designer/reports/create_table_relation.html'
    parent_model = Report
    kwargs_parent_fk = 'report_pk'
    model = ReportTableRelation
    title = 'Создание связи таблицы отчета'
    form_class = ReportTableRelationCreateUpdateForm
    formset_managers = (ReportTableRelationConditionsFormsetManager,)
    dependents = (('dynamic_contents', 'report_table_relations'),)

    def get_form_kwargs(self):
        form_kwargs = super().get_form_kwargs()
        form_kwargs.update(report=self.parent)
        return form_kwargs

    def get_formset_managers_kwargs(self, **kwargs):
        formset_managers_kwargs = super().get_formset_managers_kwargs(**kwargs)
        formset_managers_kwargs.update(kwargs_relation_conditions={'report': self.parent})
        return formset_managers_kwargs


@method_decorator(login_required, name='dispatch')
class ReportTableRelationCreateView(ReportTableRelationCreateUpdateMixin, CreateAjaxView):
    """
    Представление: Создание связи таблицы отчета
    """

    title = 'Создание связи таблицы отчета'

    def after_save(self, **kwargs):
        super().after_save(**kwargs)
        # Если связь для таблицы первая
        if self.object.report_table.relations.count() == 1:
            # Обновление связей таблиц для полей, не имеющих этих связей
            report_fields = self.parent.report_fields.filter(
                report_table_relation__isnull=True,
                field__db_table=self.object.report_table.db_table,
            )
            report_fields.update(report_table_relation=self.object)


@method_decorator(login_required, name='dispatch')
class ReportTableRelationUpdateView(ReportTableRelationCreateUpdateMixin, UpdateAjaxView):
    """
    Представление: Создание связи таблицы отчета
    """

    title = 'Редактирование связи таблицы отчета'


# endregion Список связей таблиц отчета


# region Список полей в отчете


@method_decorator(login_required, name='dispatch')
class ReportFieldsListView(ReportsDynamicContentTableBaseView):
    """
    Представление: Список полей отчета
    """

    queryset = ReportField.objects.order_by('order')
    parent_field = 'report'
    table_class = ReportFieldsTable
    filterset_class = ReportFieldsFilterSet
    ajax_content_name = 'report_fields'


@method_decorator(login_required, name='dispatch')
class ReportFieldsDeleteView(CustomDeleteView):
    """
    Представление: Удаление поля отчета
    """

    model = ReportField
    dependents = (('ajax_contents', 'report_fields'),)


@method_decorator(login_required, name='dispatch')
class ReportTableRelationsDeleteView(CustomDeleteView):
    """
    Представление: Удаление поля отчета
    """

    model = ReportTableRelation
    dependents = (('dynamic_contents', 'report_table_relations'),)


@method_decorator(login_required, name='dispatch')
class ReportFieldsAddView(ObjectActionAjaxView):
    """
    Представление: Добавление полей в отчет
    """

    model = Report
    dependents = (
        ('ajax_contents', 'report_tables'),
        ('dynamic_contents', 'report_fields'),
    )

    @transaction.atomic
    def action(self):
        # Создание полей отчета
        table_fields_ids = list(map(itemgetter(-1), self.fields_with_relations))

        # Список полей, отсортированных в полученном порядке
        fields = order_by_list(TableField.objects.filter(pk__in=table_fields_ids), 'pk', table_fields_ids)

        # Последний порядковый номер поля в отчете
        order = self.object.field_next_order

        # Связи таблиц внутри шаблона
        report_tables_ids = self.object.report_tables.values_list('id', flat=True)
        relations_tables_queryset = ReportTableRelation.objects.filter(report_table_id__in=report_tables_ids).distinct()
        relations_tables_map = dict(relations_tables_queryset.values_list('report_table__db_table_id', 'id'))

        # Связи полей и поля
        relations_report_fields, report_fields = [], []
        for index, field in enumerate(fields):
            # Добавление поля отчета
            report_field = ReportField(
                name=field.name,
                alias=field.alias,
                representation=field.representation,
                report=self.object,
                field=field,
                order=order + index,
            )
            # Добавление связи с таблицей
            report_table_relation = relations_tables_map.get(field.db_table.pk)
            if report_table_relation:
                report_field.report_table_relation_id = report_table_relation
            report_fields.append(report_field)
        objs = ReportField.objects.bulk_create(report_fields)

        # Добавление связей поля
        for report_field, chain in zip(objs, self.fields_with_relations):
            for relation_order, table_field_id in enumerate(chain[:-1]):
                relations_report_fields.append(
                    ReportFieldRelation(order=relation_order, report_field=report_field, table_field_id=table_field_id)
                )
        ReportFieldRelation.objects.bulk_create(relations_report_fields)

    @cached_property
    def fields_with_relations(self):
        """
        Список цепочек полей
        """
        fields_chains = self.request.POST.get('fields_chains[]')
        if not fields_chains:
            return {}
        return json.loads(fields_chains)


@method_decorator(login_required, name='dispatch')
class ReportFieldChangeOrderView(ObjectActionAjaxView):
    """
    Представление: Изменение порядка поля
    """

    title = 'Изменение порядка поля'
    error_message = 'Групповые поля должны находиться перед остальными полями'
    join_errors = True
    model = ReportField

    def valid_action(self):
        # Отчет и новый порядковый номер
        report, new = self.object.report, int(self.request.POST.get('order'))

        # Количество групповых полей шаблона
        report_group_fields_count = report.report_fields.filter(is_group=True).count()
        if self.object.is_group:
            if new >= report_group_fields_count:
                self.add_error(self.error_message)
        else:
            if new < report_group_fields_count:
                self.add_error(self.error_message)
        return not bool(self._errors)

    def action(self):
        self.object.reorder(int(self.request.POST.get('order')))


class ReportFieldMixin:
    """
    Миксин полей шаблона
    """

    is_virtual = False
    model = ReportField
    template_name = 'report_designer/reports/processing_report_field.html'
    dependents = (('dynamic_contents', 'report_fields'),)

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data.update(is_virtual=self.is_virtual)
        return context_data


@method_decorator(login_required, name='dispatch')
class ReportFieldUpdateView(ReportFieldMixin, UpdateAjaxView):
    """
    Представление: Редактирование полей отчета
    """

    title = 'Редактирование поля отчета'
    form_class = ReportFieldUpdateForm

    def get_title(self):
        return f'{super().get_title()} "{self.object.name}"'

    def before_save(self):
        super().before_save()
        self.group_field_next_order = self.object.report.group_field_next_order

    def after_save(self, **kwargs):
        super().after_save(**kwargs)
        form = kwargs.get('form')
        if 'is_group' in form.changed_data:
            self.object.reorder(self.group_field_next_order - int(not self.object.is_group))

    def set_object_additional_values(self, obj):
        super().set_object_additional_values(obj)
        if obj.is_group:
            obj.is_sort = True


# endregion Список полей в отчете


# region Списки для составления выражений


@method_decorator(login_required, name='dispatch')
class ReportFunctionsDBTablesTreeListView(ExpressionsMixin, DBTablesBaseTreeListView):
    """
    Представление: Список таблиц в отчете
    """

    def get_queryset(self):
        # Таблицы отчета
        report_tables_ids = self.parent.report_tables.all().values_list('pk', flat=True)

        # Связи таблиц
        relations = ReportTableRelation.objects.filter(report_table_id__in=report_tables_ids)

        # Построение вырыражения для связей
        db_table_template = 'report_table__db_table'
        table_template, SEP = f'{db_table_template}__table__%s', Value('_')
        relations = relations.annotate(
            report_table_relation_lookup=Concat(
                table_template % 'app_label', SEP, table_template % 'model', SEP, Cast('pk', output_field=CharField())
            )
        ).values_list('name', 'pk', 'report_table_relation_lookup')

        # Аннотация имени связей
        name_whens, lookup_whens = [], []
        for name, pk, lookup in relations:
            name_whens.append(When(report_tables__relations__pk=pk, then=Value(name)))
            lookup_whens.append(When(report_tables__relations__pk=pk, then=Value(lookup)))

        # Доступны таблицы, добавленные в отчет
        return (
            super()
            .get_queryset()
            .for_report(self.parent)
            .annotate(
                report_table_relation_name=Case(*name_whens, default=Value(''), output_field=CharField()),
                report_table_relation_lookup=Case(*lookup_whens, default=Value(''), output_field=CharField()),
            )
        )


@method_decorator(login_required, name='dispatch')
class FunctionsListView(AjaxResponseMixin, TemplateView):
    """
    Представление: список функций конструктора отчетов
    """

    template_name = 'report_designer/reports/blocks/functions_tree_branch.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data.update(tree_branches=Functions.create_tree_for_template())
        return context_data


# endregion Списки для составления выражений


# region Виртуальные поля


class ReportVirtualFieldMixin(ParentMixin, ReportFieldMixin):
    """
    Миксин: Создание/Редактирование виртуального поля
    """

    is_virtual = True
    parent_model = Report
    kwargs_parent_fk = 'report_pk'
    form_class = ReportVirtualFieldCreateUpdateForm

    def set_object_additional_values(self, obj):
        super().set_object_additional_values(obj)
        if obj.is_group:
            obj.is_sort = True


@method_decorator(login_required, name='dispatch')
class ReportVirtualFieldCreateView(ReportVirtualFieldMixin, CreateAjaxView):
    """
    Представление: Создание виртуального поля
    """

    title = 'Создание виртуального поля'

    def set_object_additional_values(self, obj):
        super().set_object_additional_values(obj)
        obj.report = self.parent
        obj.is_virtual = True
        obj.order = self.parent.field_next_order


@method_decorator(login_required, name='dispatch')
class ReportVirtualFieldUpdateView(ReportVirtualFieldMixin, UpdateAjaxView):
    """
    Представление: Редактирование виртуального поля
    """

    title = 'Редактирование виртуального поля'


# endregion Виртуальные поля


# region Генерация шаблона


@method_decorator(login_required, name='dispatch')
class ReportGenerateView(ReportBreadcrumbsDetailBaseMixin, FormMixin, CustomTemplateView):
    """
    Представление: генерация шаблона
    """

    title = 'Формирование отчета'
    template_name = 'report_designer/reports/report_generate.html'
    form_class = ReportGenerateForm
    action_group_classes = (
        ReportGenerateActionGroup,
        ReportExcelActionGroup,
    )


@method_decorator(login_required, name='dispatch')
class ReportGeneratedTableView(TableMixin, AjaxResponseMixin, TemplateView):
    """
    Сгенерированная таблица отчета
    """

    table_class = ReportGeneratedTable
    template_name = 'report_designer/core/dynamic_tables/table.html'

    def get_table_kwargs(self):
        table_kwargs = super().get_table_kwargs()
        if self.report:
            table_kwargs.update({'handler': self.generated_report})
        return table_kwargs

    @cached_property
    def report(self):
        """
        Отчет
        """
        return Report.objects.filter(pk=self.request.GET.get('report')).first()

    @cached_property
    def generated_report(self):
        """
        Сгенерированный отчет
        """
        report = ReportDataHandler(self.report)
        report.run()
        return report


# endregion Генерация шаблона


@method_decorator(login_required, name='dispatch')
class TableFieldsListSelect2View(ParentMixin, Select2BaseListView):
    """
    Загрузка полей select2
    """

    parent_model = Report
    queryset = TableField.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.table:
            return queryset.none()
        return (
            queryset.available_for_report(self.parent)
            .filter(db_table=self.table)
            .values()
            .annotate(name=Case(When(alias__exact='', then=F('name')), default=F('alias')))
            .distinct()
        )

    @cached_property
    def table(self):
        """
        Таблица
        """
        # Обработка родительской связи
        if 'relation' in self.request.GET:
            relation = self.request.GET.get('relation')
            if relation:
                relation = ReportTableRelation.objects.filter(report_table__report=self.parent, pk=relation).first()
                return relation.report_table.db_table if relation else None
            return self.parent.root

        # Обработка связываемой таблицы
        table = self.request.GET.get('table')
        if not table:
            return
        table = ReportTable.objects.filter(report=self.parent, pk=table).first()
        return table.db_table if table else None
