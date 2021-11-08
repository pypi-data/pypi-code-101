from copy import copy
from operator import eq

from django.db.models import Count

from report_designer.core.tables import (
    AbstractTable,
    CellTypeCenter,
    CellTypeDateTime,
    CellTypeBooleanIcon,
    AbstractBaseTable,
    CellTypeEmpty,
)


class ReportsTable(AbstractTable):
    """
    Таблица списка отчетов
    """

    def create_header(self, header):
        level_0 = [
            header('Наименование'),
            header('Основная таблица'),
            header('Группы'),
            header('Автор'),
            header('Дата и время обновления'),
        ]
        return [level_0]

    def create_cells(self, obj):
        cell = self.cell_class
        url = obj.get_detail_url()
        return [
            cell(obj.name, cell_type=CellTypeCenter, url=url),
            cell(obj.root, cell_type=CellTypeCenter, url=url),
            cell(obj.get_groups_names, cell_type=CellTypeCenter, url=url),
            cell(obj.author, cell_type=CellTypeCenter, url=url),
            cell(obj.updated, cell_type=CellTypeDateTime, url=url),
        ]


class ReportFieldsTable(AbstractTable):
    """
    Таблица списка полей отчетов
    """

    js_sortable_class = 'js-report-fields-table'

    def create_header(self, header):
        level_0 = [
            header('Наименование'),
            header('Псевдоним'),
            header('Представление'),
            header('Виртуальное'),
            header('Групповое'),
            header('Сортировочное'),
            header('Обратная сортировка'),
            header('Агрегированное'),
        ]
        return [level_0]

    def create_cells(self, obj):
        cell = self.cell_class
        base_attrs = {
            'link_class': 'js-rd-ajax-load-modal-btn',
            'url': obj.get_edit_url(),
            'link_html_attrs': {'data-modal-lg': True}
        }
        return [
            cell(obj.name, cell_type=CellTypeCenter, **base_attrs),
            cell(obj.alias, cell_type=CellTypeCenter, **base_attrs),
            cell(obj.representation and obj.representation.name or None, cell_type=CellTypeCenter, **base_attrs),
            cell(obj.is_virtual, cell_type=CellTypeBooleanIcon, **base_attrs),
            cell(obj.is_group, cell_type=CellTypeBooleanIcon, **base_attrs),
            cell(obj.is_sort, cell_type=CellTypeBooleanIcon, **base_attrs),
            cell(obj.reverse_sort, cell_type=CellTypeBooleanIcon, **base_attrs),
            cell(obj.is_aggregate, cell_type=CellTypeBooleanIcon, **base_attrs),
        ]

    def get_row_data_attrs(self, obj):
        data_attrs = super().get_row_data_attrs(obj)
        data_attrs.update({
            'pk': obj.pk,
            'order': obj.order,
            'change-order-url': obj.get_change_order_url(),
        })
        return data_attrs


class ReportTableRelationTable(AbstractTable):
    """
    Таблица списка связей таблиц отчета
    """

    def create_header(self, header):
        level_0 = [
            header('Наименование'),
            # header('Родительская связь'),
            header('Таблица отчета'),
            header('Количество условий'),
        ]
        return [level_0]

    def create_cells(self, obj):
        cell = self.cell_class
        base_attrs = {
            'link_class': 'js-rd-ajax-load-modal-btn',
            'url': obj.get_edit_url(),
            'link_html_attrs': {'data-modal-lg': True}
        }
        return [
            cell(obj.name, cell_type=CellTypeCenter, **base_attrs),
            # cell(obj.parent and obj.parent.name or None, cell_type=CellTypeCenter, **base_attrs),
            cell(obj.report_table.db_table.alias, cell_type=CellTypeCenter, **base_attrs),
            cell(obj.conditions_count, cell_type=CellTypeCenter, **base_attrs),
        ]

    def get_row_data_attrs(self, obj):
        return super().get_row_data_attrs(obj)

    def get_objs(self):
        return super().get_objs().annotate(conditions_count=Count('from_report_table_relations'))


class ReportGeneratedTable(AbstractBaseTable):
    """
    Таблица списка связей таблиц отчета
    """

    def __init__(self, objs=None, *args, **kwargs):
        self.handler = kwargs.pop('handler', None)
        self.count_tables = self.handler and len(self.handler.columns_names) or 0
        self.is_grouped = self.handler and bool(self.handler.group_fields) or False
        super().__init__(objs, *args, **kwargs)

    def create_table(self):
        if self.handler:
            super().create_table()

    def create_header(self, header):
        level_0 = [header(column_name) for column_name in self.handler.columns_names]
        return [level_0, ]

    def create_body(self):
        """
        Создание тела таблицы
        """
        previous_index = ()
        for index, group in self.get_objs():
            if index:
                # Текущий level. Получен путем нахождение первого
                # расхождения индекса группы и предыдущего текущего индекса
                level = sum(eq(*item) for item in zip(previous_index, tuple(index)))
                self.create_header_group_rows(index, level)
                previous_index = index

            # Значения
            group_values = group.tolist()
            if not group_values:
                continue

            if self.is_grouped:
                for values in group_values:
                    row = self.create_row(values)
                    self._add_row(row)
            else:
                row = self.create_row(group_values)
                self._add_row(row)

    def create_header_group_rows(self, index, level):
        """
        Создание ячеек шапки группы
        """
        # Ячейки шапки группы
        cell = self.cell_class
        row = self.row_class
        cells = [cell(None, cell_type=CellTypeEmpty)] * (self.count_tables - 1)

        if not isinstance(index, (tuple, list,)):
            index = (index,)
        for i, name in enumerate(index[level:]):
            row_cells = copy(cells)
            row_cells.insert(i + level, cell(name))
            self._add_row(row(row_cells))

    def create_row(self, values):
        """
        Формирование строки тела таблицы
        """
        cells = self.create_cells(values)
        return self.row_class(cells)

    def get_objs(self):
        if self.is_grouped:
            for group_by in self.handler.builder.groups:
                index, group = group_by
                yield index, group.values
        else:
            for row in self.handler.builder.dataframe.values:
                yield None, row

    def create_cells(self, values):
        cell = self.cell_class
        return [
            *([cell(None)] * (self.count_tables - len(values))),
            *[cell(value) for value in values],
        ]
