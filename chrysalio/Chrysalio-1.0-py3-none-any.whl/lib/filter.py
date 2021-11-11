# -*- coding: utf-8 -*-
"""Class to manage a filter to select items among a collection."""

from collections import OrderedDict
from json import loads
from re import sub

from webhelpers2.html import literal
from sqlalchemy.sql import text

from pyramid.httpexceptions import HTTPForbidden
from .i18n import _, translate_field
from .utils import shorten


OPERATORS = OrderedDict((('AND', _('AND')), ('OR', _('OR'))))
COMPARISONS = OrderedDict((
    ('=', '='), ('!=', '≠'), ('>', '>'), ('>=', _('≥')), ('<', '<'),
    ('<=', _('≤'))))


# =============================================================================
class Filter(object):
    """A class to manage filters.

    :type  request: pyramid.request.Request
    :param request:
        Current request.
    :param str filter_id:
        Filter ID.
    :param list inputs:
        A list of inputs like
        ``((key, label, is_static, available_values),...)``.
    :param list initials: (optional)
        Initial conditions.
    :param str remove: (optional)
        Number of the condition to remove from the previous filter.
    :type  comparisons: collections.OrderedDict
    :param comparisons: (optional)
        Customize list of comparaisons.

    For ``inputs`` the ``available_values`` field must be:

    * ``None`` for a string value
    * ``''`` for a string value with auto-completion
    * ``True`` for a boolean value
    * ``0`` for an integer value
    * a ``list`` of value/label for closed list of values.

    A filter is a list of AND-conditions.
    Each AND-condition is a list of OR-conditions.
    An OR-condition is a tuple such as ``(key, comparison, value)``.

    The ``comparison`` is one of the items of ``comparisons`` and can be
    ``'='``, ``'!='``, ``'>'``, ``'>='``, ``'<'`` or ``'<='``.
    The ``value`` can be a boolean, a string or a
    :class:`~pyramid.i18n.TranslationString` instance.

    For instance, the filter:

    ``(id=2 OR id>5) AND active AND group!='Foo'`` is stored as:

    ``[[('id', '=', 2), ('id', '>', 5)], [('active', '=', True)],
    [('group', '!=', 'Foo')]]``
    """

    # -------------------------------------------------------------------------
    def __init__(
            self, request, filter_id, inputs, initials=None, remove=None,
            comparisons=None):
        """Constructor method."""
        # pylint: disable = too-many-arguments
        self.uid = filter_id
        self._request = request
        self._inputs = OrderedDict(
            [(k[0], (k[1], k[2], k[3])) for k in inputs])
        self._comparisons = comparisons \
            if comparisons is not None else COMPARISONS

        # Retrieve last filter
        if 'filters' not in request.session:
            request.session['filters'] = {}
        self._conditions = request.session['filters'].get(filter_id) or []

        # Append initial conditions
        if filter_id not in request.session['filters'] \
           and initials is not None:
            for condition in initials:
                self.append_condition(*condition)

        # Remove obsolete conditions
        if remove is not None:
            self.remove_condition(remove)

        # Append new conditions
        if 'filter' in request.POST:
            for key in self._inputs:
                if self._inputs[key][1] and \
                   request.POST.get('filter_value_{0}'.format(key)):
                    self.append_condition(
                        key, request.POST.get(
                            'filter_comparison_{0}'.format(key), '='),
                        request.POST['filter_value_{0}'.format(key)],
                        request.POST.get(
                            'filter_operator_{0}'.format(key), 'AND'))
            self.append_condition(
                request.POST.get('filter_key'),
                request.POST.get('filter_comparison', '='),
                request.POST.get('filter_value'),
                request.POST.get('filter_operator', 'AND'))

    # -------------------------------------------------------------------------
    def __str__(self):
        """String representation."""
        return str(self._conditions)

    # -------------------------------------------------------------------------
    def is_empty(self):
        """Return ``True`` if a filter is empty."""
        return not bool(self._conditions)

    # -------------------------------------------------------------------------
    def clear(self):
        """Clear filter."""
        self._conditions = []
        self._request.session['filters'][self.uid] = []

    # -------------------------------------------------------------------------
    def append_condition(self, key, comparison, value, operator='AND'):
        """Append an AND-condition to the filter.

        :param str key:
            The key to use.
        :param str comparison: (``'='``, ``'!='``, ``'>'``, ``'<'``,...)
            How to compare.
        :type  value: :class:`str`, :class:`bool` or
            :class:`~pyramid.i18n.TranslationString`
        :param value:
            The value of the filter. It is optional for boolean filter and its
            default value is ``True``.
        :param str operator: ('AND' or 'OR', default='AND')
            The operator to use to complete the filter.
        """
        if not key or not value or key not in self._inputs or \
           comparison not in self._comparisons or operator not in OPERATORS:
            return
        if self._inputs[key][2] is True:
            value = True
        elif self._inputs[key][2] == 0:
            value = int(sub(r'[^\d-]+', '', value) or '0')
        condition = (key, comparison, value)
        if self._conditions and operator == 'OR':
            if condition not in self._conditions[-1]:
                self._conditions[-1].append(condition)
        elif [condition] not in self._conditions:
            self._conditions.append([condition])
        self._request.session['filters'][self.uid] = self._conditions

    # -------------------------------------------------------------------------
    def remove_condition(self, index):
        """Remove one AND-condition of the filter.

        :param str index:
            Index of the AND-condition to remove.
        """
        if index is None or not index.isdigit():
            return
        index = int(index)
        if index < 0 or index >= len(self._conditions):
            return
        del self._conditions[index]
        self._request.session['filters'][self.uid] = self._conditions

    # -------------------------------------------------------------------------
    def html_conditions(self):
        """An HTML representation of the current conditions.

        :rtype: webhelpers2.html.literal
        """
        if not self._conditions:
            return ''

        html = ''
        for and_num, and_condition in enumerate(self._conditions):
            if and_num:
                html += ' <strong>{0}</strong> '.format(
                    self._request.localizer.translate(OPERATORS['AND']))
            html += '<span class="cioFilterCondition">'\
                '<input type="submit" value="X" name="crm!{0}.x"/>'.format(
                    and_num)
            for or_num, or_condition in enumerate(and_condition):
                if or_num:
                    html += ' <strong>{0}</strong> '.format(
                        self._request.localizer.translate(OPERATORS['OR']))
                condition = self._inputs[or_condition[0]]
                html += '<span>{0}{1}'.format(
                    condition[2] is True and or_condition[1] == '!=' and
                    self._request.localizer.translate(_('EXCEPT')) + ' ' or '',
                    self._request.localizer.translate(condition[0]))
                if isinstance(condition[2], (list, tuple)):
                    html += ' {0} {1}'.format(
                        self._comparisons[or_condition[1]],
                        self._request.localizer.translate(
                            dict(condition[2]).get(
                                or_condition[2], or_condition[2])))
                elif condition[2] is not True:
                    html += ' {0} {1}'.format(
                        self._comparisons[or_condition[1]], or_condition[2])
                html += '</span>'
            html += '</span> '
        return literal(html)

    # -------------------------------------------------------------------------
    def html_inputs(self, form, tag='span'):
        """An HTML representation of the current inputs.

        :type  form: .lib.form.Form
        :param form:
            Current form.
        :param str tag: (Default='div')
            Tag which wraps each input line.
        :rtype: webhelpers2.html.literal
        """
        # Static inputs
        html = ''
        has_static = False
        inputs = []
        translate = self._request.localizer.translate
        for key in self._inputs:
            if self._conditions or not self._inputs[key][1]:
                inputs.append((key, self._inputs[key][0]))
                continue
            has_static = True
            html += literal(
                '<{0} class="cioFilterInput cioFilterInputStatic">'
                '<span>'.format(tag))
            html += literal('<span class="cioFilterNoOp"> </span>')
            html += literal(
                '<span class="cioFilterKey" title="{0}">'
                '<span>{1}</span></span>'.format(
                    translate(_('Filter name')),
                    translate(self._inputs[key][0])))
            html += self._html_select_comparison(form, key)
            html += self._html_select_value(form, key)
            html += literal('</span></{0}>'.format(tag))
        if not inputs:
            return literal(html)

        # Dynamic inputs
        html += literal('<{0} class="cioFilterInput"><span>'.format(tag))
        key = self._request.POST.get('filter_key') or \
            not has_static and inputs[0][0]
        if self._conditions:
            html += literal('<span class="cioFilterOp">') + \
                form.select('filter_operator', None, OPERATORS.items()) + \
                literal('</span>')
        else:
            html += literal('<span class="cioFilterNoOp"> </span>')
        if has_static:
            inputs.insert(0, ('', ' '))
        html += literal('<span class="cioFilterKey" title="{0}">'.format(
            translate(_('Filter name')))) + form.select(
                'filter_key', None, inputs, True) + literal('</span>')
        html += self._html_select_comparison(form, key, 'filter_comparison')
        html += self._html_select_value(form, key, 'filter_value')
        html += literal('</span></{0}>'.format(tag))

        return html

    # -------------------------------------------------------------------------
    def sql(self, dbquery, table_name, ignored=None):
        """Complete a SqlAlchemy query with of the current filter.

        :param sqlalchemy.orm.query.Query dbquery:
            SqlAlchemy query to complete.
        :param str table_name:
            Name of the default SQL table.
        :param list ignored: (optional)
            List of and-conditions that must be ignored. They should be
            processed by the caller, probably because of joins.
        :rtype: sqlalchemy.orm.query.Query
        """
        and_conditions = self._sql_remove_ignored(ignored)
        if not and_conditions:
            return dbquery

        like = 'ILIKE' if dbquery.session.bind.dialect.name == 'postgresql' \
            else 'LIKE'
        for and_num, and_condition in enumerate(and_conditions):
            clause = '('
            params = {}
            for or_num, or_condition in enumerate(and_condition):
                if or_num:
                    clause += ' OR '
                available_values = self._inputs[or_condition[0]][2]
                if or_condition[1] == '=' and available_values in (None, ''):
                    comparison = like
                elif or_condition[1] == '!=' and available_values in (
                        None, ''):
                    comparison = 'NOT {0}'.format(like)
                else:
                    comparison = or_condition[1]
                value = True if available_values is True else or_condition[2]
                clause += '{0}.{1} {2} :p{3}{4:02d}'.format(
                    table_name, or_condition[0], comparison, and_num, or_num)
                params['p{0}{1:02d}'.format(and_num, or_num)] = \
                    '%{0}%'.format(value) if like in comparison else value
            clause += ')'
            dbquery = dbquery.filter(text(clause).bindparams(**params))

        return dbquery

    # -------------------------------------------------------------------------
    @classmethod
    def sql_autocomplete(
            cls, request, table_class, where=None, limit=10, width=0):
        """suggest terms for auto-completion in SQL

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :param table_class:
            SQLAlchemy table class to query.
        :param dict where: (optional)
            WHERE clause for the query.
        :param int limit: (default=10)
            Limit for the search.
        :param int width: (default=25)
            Shorten the length of each suggestion.
        :rtype: list
        """
        field = request.params.get('field')
        if not request.is_xhr or not hasattr(table_class, field):
            raise HTTPForbidden()

        value = '%{0}%'.format(request.params.get('value'))
        dbquery = request.dbsession.query(getattr(table_class, field)).filter(
            getattr(table_class, field).ilike(value))
        if where is not None:
            dbquery = dbquery.filter_by(**where)
        data = [k[0] for k in dbquery.group_by(field).limit(limit)]

        if field == 'i18n_label':
            data = [translate_field(request, loads(k)) for k in data]
        if width:
            data = [shorten(k, width, '') for k in data]
        return data

    # -------------------------------------------------------------------------
    def whoosh(self):
        """Return the current filter in Whoosh query language.

        :rtype: tuple
        :return:
            a tuple search as ``(fieldnames, query)``.
        """
        # pylint: disable = too-many-branches
        fieldnames = set()
        clause = ''
        for and_num, and_condition in enumerate(self._conditions):
            if and_num:
                clause += ' AND '
            clause += '('
            for or_num, or_condition in enumerate(and_condition):
                if or_num:
                    clause += ' OR '
                fieldnames.add(or_condition[0])
                comparison = or_condition[1]
                if or_condition[2] is True:
                    clause += '{0}{1}:TRUE'.format(
                        comparison == '!=' and 'NOT ' or '', or_condition[0])
                elif comparison == '=' and not isinstance(
                        or_condition[2], (int, float, bool)) and \
                        ' ' in or_condition[2]:
                    clause += '{0}:"{1}"'.format(
                        or_condition[0], or_condition[2])
                elif comparison == '=':
                    clause += '{0}:({1})'.format(
                        or_condition[0], or_condition[2])
                elif comparison == '!=' and not isinstance(
                        or_condition[2], (int, float, bool)) \
                        and ' ' in or_condition[2]:
                    clause += 'NOT {0}:"{1}"'.format(
                        or_condition[0], or_condition[2])
                elif comparison == '!=':
                    clause += 'NOT {0}:({1})'.format(
                        or_condition[0], or_condition[2])
                elif comparison == '>':
                    clause += '{0}:{{{1} TO}}'.format(
                        or_condition[0], or_condition[2])
                elif comparison == '>=':
                    clause += '{0}:[{1} TO]'.format(
                        or_condition[0], or_condition[2])
                elif comparison == '<':
                    clause += '{0}:{{TO {1}}}'.format(
                        or_condition[0], or_condition[2])
                elif comparison == '<=':
                    clause += '{0}:[TO {1}]'.format(
                        or_condition[0], or_condition[2])
            clause += ')'

        return tuple(fieldnames), clause

    # -------------------------------------------------------------------------
    def _html_select_comparison(self, form, key, name=None):
        """HTML form select to choose the comparison operator of a condition.

        :type  form: .lib.form.Form
        :param form:
            Current form.
        :param str key:
            Current condition key.
        :param str name: (optional)
            Name of the form select.
        :rtype: webhelpers2.html.literal
        """
        html = literal('<span class="cioFilterComparison" title="{0}">'.format(
            self._request.localizer.translate(_('Comparison'))))
        if name is None:
            name = 'filter_comparison_{0}'.format(key)
        if key and self._inputs[key][2] not in (None, 0):
            return html + form.select(
                name, None, (('=', '='), ('!=', '≠'))) + literal('</span>')
        return html + form.select(name, None, self._comparisons.items()) + \
            literal('</span>')

    # -------------------------------------------------------------------------
    def _html_select_value(self, form, key, name=None):
        """HTML form select to choose the value of a condition.

        :type  form: .lib.form.Form
        :param form:
            Current form.
        :param str key:
            Current condition key.
        :param str name: (optional)
            Name of the form select.
        :rtype: webhelpers2.html.literal
        """
        html = literal('<span class="cioFilterValue" title="{0}">'.format(
            self._request.localizer.translate(_('Filter value'))))
        if name is None:
            name = 'filter_value_{0}'.format(key)
        if key and self._inputs[key][2] is True:
            return html + form.custom_checkbox(name) + literal('</span>')
        if key and self._inputs[key][2] not in (None, '', 0):
            return html + form.select(
                name, None, self._inputs[key][2]) + literal('</span>')
        if key and self._inputs[key][2] == '':
            return html + form.text(
                name, placeholder=self._request.localizer.translate(
                    _('filter here...')), class_='cioAutocomplete') + literal(
                        '</span>')
        return html + form.text(
            name, placeholder=self._request.localizer.translate(
                _('filter here...'))) + literal('</span>')

    # -------------------------------------------------------------------------
    def _sql_remove_ignored(self, ignored):
        """Remove ignored conditions.

        :param list ignored:
            List of and-conditions that must be ignored. They should be
            processed by the caller, probably because of joins.
        :rtype: list
        """
        if ignored is None:
            return self._conditions

        and_conditions = []
        for and_condition in self._conditions:
            new_and_conditions = []
            for or_condition in and_condition:
                if or_condition[0] not in ignored:
                    new_and_conditions.append(or_condition)
            if new_and_conditions:
                and_conditions.append(new_and_conditions)

        return and_conditions
