# -*- coding: utf-8 -*-
"""Class to divide large lists of items into pages."""

from string import Template
import re

from webhelpers2.html import literal, tags
from sqlalchemy.orm.query import Query

from ..lib.i18n import _
from ..includes.themes import theme_static_prefix

PAGE_DEFAULT_SIZE = 80
PAGE_SIZES = (('', ' '), 10, 20, 40, 80, 160, 320, 640, ('0', '∞'))


# =============================================================================
def sortable_column(
        request, label, sort, current_sorting=None):
    """Output a header of column with `sort up` and `sort down` buttons.

    :type  request: pyramid.request.Request
    :param request:
        Current request.
    :param str label:
        Label of column.
    :param str sort:
        Sort criteria.
    :param str current_sorting: (optional)
        Default current sorting.
    :rtype: webhelpers2.html.literal
    """
    current = request.params.get('sort') or current_sorting
    query_string = {}
    if request.GET:
        query_string.update(request.GET)

    html = '<a title="{0}"'.format(request.localizer.translate(
        _('Sort by ${l}', {'l': label.lower()})))
    if current and sort == current[1:]:
        html += current[0] == '+' and \
                ' class="cioSortAsc"' or ' class="cioSortDesc"'
    if current and sort == current[1:] and current[0] == '+':
        query_string['sort'] = '-{0}'.format(sort)
    else:
        query_string['sort'] = '+{0}'.format(sort)
    html += ' href="{0}"'.format(
        request.current_route_path(_query=query_string))
    html += '>{0}</a>'.format(label)

    return literal(html)


# =============================================================================
class Paging(list):
    """Divide large lists of items into pages.

    :type  request: pyramid.request.Request
    :param request:
        Current request.
    :param str paging_id:
        Paging ID.
    :type  collection: list-like object
    :param collection:
        Collection object being paged through.
    :param dict params: (optional)
        A dictionary with the following keys: ``page_size``, ``page``,
        ``sort`` and ``display``.
    :param int item_count: (optional)
        Number of items in the collection.
    :param tuple page_sizes: (optional)
        List of suggested page sizes.

    This class uses the following parameters in request: ``page_size``,
    ``page``, ``sort`` and ``display``.

    It stores its information and filters definitions in ``session['paging']``.
    This structure looks like: ``session['paging'] = (page_default_size,
    {'page_id1': {'page_size': 80, 'page': 3, 'sort': 'name',
    'display': 'cards'}, 'page_id2': {...}, ...})``
    """
    # pylint: disable = too-many-instance-attributes

    # -------------------------------------------------------------------------
    def __init__(self, request, paging_id, collection, params=None,
                 item_count=None):
        """Constructor method."""
        # Update paging session
        if params is None:
            params = self.params(request, paging_id)

        # Initialize variables
        self._request = request
        self.paging_id = paging_id
        full_list = collection
        if isinstance(collection, Query):
            full_list = _SQLAlchemyQuery(collection)
        self.item_count = item_count if item_count is not None else \
            len(full_list)
        self.page_count = ((self.item_count - 1) // (params['page_size'])) + 1\
            if params['page_size'] else 1
        if params['page'] > self.page_count:
            params['page'] = self.page_count
        self.page = max(1, params['page'])
        self.items = []
        self.page_size = params['page_size']
        self.display = params['display']

        # Compute the item list
        if self.item_count > 0:
            if self.page_size:
                first_item = (self.page - 1) * self.page_size + 1
                last_item = min(
                    first_item + self.page_size - 1, self.item_count)
            else:
                first_item = 1
                last_item = self.item_count
            try:
                self.items = full_list[first_item - 1:last_item]
            except TypeError:
                raise TypeError("You can't use type %s!" % type(full_list))

        list.__init__(self, self.items)

    # -------------------------------------------------------------------------
    @classmethod
    def params(cls, request, paging_id, default_sorting=None,
               default_display='cards'):
        """Return current paging parameters: page number, page size and
        sorting.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :param str paging_id:
            Paging ID.
        :param str default_sorting: (optional)
            Default sorting.
        :param str default_display: ('cards' or 'list', default='cards')
            Default display.
        :rtype: dict
        :return:
            The paging dictionary. See :class:`~.paging.Paging` class.
        """
        if request is None:
            return {
                'page_size': PAGE_DEFAULT_SIZE, 'page': 1,
                'sort': default_sorting, 'display': default_display}

        if 'paging' not in request.session:
            request.session['paging'] = (
                request.registry['settings']['page-size']
                if 'settings' in request.registry else PAGE_DEFAULT_SIZE, {})
        if paging_id not in request.session['paging'][1]:
            request.session['paging'][1][paging_id] = {
                'page_size': request.session['paging'][0],
                'page': 1, 'sort': default_sorting, 'display': default_display}
        params = request.session['paging'][1][paging_id]

        if 'page_size' in request.params \
           and request.params['page_size'].strip():
            params['page_size'] = int(request.params['page_size'])
        if 'page' in request.params and request.params['page'].isdigit():
            params['page'] = max(1, int(request.params['page']))
        if request.params.get('sort'):
            params['sort'] = request.params['sort']
        if params['sort'] is None:
            params['sort'] = default_sorting
        if request.params.get('display'):
            params['display'] = request.params['display']

        if request.POST:
            request.session['paging'][1][paging_id] = {
                'page_size': params['page_size'],
                'page': params['page'],
                'sort': params['sort'],
                'display': params['display']}
            params = request.session['paging'][1][paging_id]

        return params

    # -------------------------------------------------------------------------
    @classmethod
    def get_sort(cls, request, paging_id):
        """Retrieve the sort criteria from the session.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :param str paging_id:
            ID of the paging.
        :rtype: :class:`str` or ``None``
        """
        if 'paging' not in request.session or \
           paging_id not in request.session['paging'][1]:
            return None
        return request.session['paging'][1][paging_id]['sort']

    # -------------------------------------------------------------------------
    @classmethod
    def get_page(cls, request, paging_id):
        """Retrieve the current page number from the session.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :param str paging_id:
            ID of the paging.
        :rtype: int
        """
        if 'paging' not in request.session or \
           paging_id not in request.session['paging'][1]:
            return 1
        return request.session['paging'][1][paging_id]['page']

    # -------------------------------------------------------------------------
    def get_item(self, field_id, value):
        """Retrieve the first item whose field ``field_id`` has the value
        ``value``.

        :param str field_id:
            Name of the item field to search.
        :param value:
            Value to use to find the item.
        :rtype: :class:`dict` or ``None``
        """
        try:
            return next((k for k in self if k[field_id] == value))
        except (StopIteration, AttributeError, TypeError):
            return None

    # -------------------------------------------------------------------------
    def set_current_ids(self, field_id):
        """Save in ``session['paging'][1][self.paging_id]['current_ids']``
        the IDs of the items of the page.

        :param str field_id:
            Name of the item field used to store the IDs.
        """
        if self._request is None or \
           'paging' not in self._request.session or \
           self.paging_id not in self._request.session['paging'][1]:
            return
        self._request.session['paging'][1][self.paging_id][
            'current_ids'] = [getattr(k, field_id) for k in self]

    # -------------------------------------------------------------------------
    def pager(self, pager_format='~3~',
              symbol_first='&lt;&lt;', symbol_first_off='',
              symbol_last='&gt;&gt;', symbol_last_off='',
              symbol_previous='&lt;', symbol_previous_off='',
              symbol_next='&gt;', symbol_next_off=''):
        """Return string with links to other pages (e.g. '1 .. 5 6 7 [8] 9 10
        11 .. 50').

        :param str pager_format: (default='~3~')
            Format string that defines how the pager is rendered.
        :param str symbol_first: (default='&lt;&lt;')
            String to be displayed as the text for the $link_first link above.
        :param str symbol_last: (default='&gt;&gt;')
            String to be displayed as the text for the $link_last link above.
        :param str symbol_previous: (default='&lt;')
            String to be displayed as the text for the $link_previous link
            above.
        :param str symbol_next: (default='&gt;')
            String to be displayed as the text for the $link_next link above.

        Format string that defines how the pager is rendered. The string
        can contain the following $-tokens that are substituted by the
        string.Template module:

        - $first_page: number of first reachable page
        - $last_page: number of last reachable page
        - $page: number of currently selected page
        - $page_count: number of reachable pages
        - $items_per_page: maximal number of items per page
        - $first_item: index of first item on the current page
        - $last_item: index of last item on the current page
        - $item_count: total number of items
        - $link_first: link to first page (unless this is first page)
        - $link_first_off: link to first page (for first page)
        - $link_last_off: link to last page (for last page)
        - $link_previous: link to previous page (unless this is first page)
        - $link_previous_off: link to previous page (for first page)
        - $link_next_off: link to next page (for last page)

        To render a range of pages the token '~3~' can be used. The number sets
        the radius of pages around the current page.
        Example for a range with radius 3: '1 .. 5 6 7 [8] 9 10 11 .. 50'
        """
        # pylint: disable = too-many-arguments
        if self._request is None:
            return ''

        # Replace ~...~ in token format by range of pages
        result = re.sub(r'~(\d+)~', self._range, pager_format)

        # Interpolate '$' variables
        items_per_page = int(self._request.params['page_size']) \
            if self._request.params.get('page_size') else \
            self._request.session['paging'][1][self.paging_id]['page_size']
        query_string = self._request.GET.copy()
        first_item = min((self.page - 1) * self.page_size + 1, self.item_count)
        last_item = min(first_item + items_per_page - 1, self.item_count) \
            if self.page_size else self.item_count

        return literal(Template(result).safe_substitute({
            'first_page': 1,
            'last_page': self.page_count,
            'page': self.page,
            'page_count': self.page_count,
            'items_per_page': items_per_page,
            'first_item': first_item,
            'last_item': last_item,
            'item_count': self.item_count,
            'link_first': self.page > 1 and self._link(
                query_string, symbol_first, 1) or symbol_first_off,
            'link_last': self.page < self.page_count and self._link(
                query_string, symbol_last, self.page_count) or symbol_last_off,
            'link_previous': self.page > 1 and self._link(
                query_string, symbol_previous,
                self.page - 1) or symbol_previous_off,
            'link_next': self.page < self.page_count and self._link(
                query_string, symbol_next, self.page + 1) or symbol_next_off}))

    # -------------------------------------------------------------------------
    def pager_top(self, image='{theme}/images/paging_go_{action}.png'):
        """Output a string with links to first, previous, next and last pages.

        :param str image: (default={theme}/images/paging_go_{action}.png)
            Pattern for the route to navigation button images.
        :rtye: str
        """
        theme = theme_static_prefix(self._request)
        image = '<img src="{0}" alt="{1}"/>'.format(
            image.format(theme=theme, action='%s'), '%s')
        return self.pager(
            '$link_first $link_previous '
            '<span>$first_item &ndash; $last_item</span> / $item_count '
            '$link_next $link_last',
            symbol_first=literal(image % ('first', 'First')),
            symbol_first_off=literal(image % ('first_off', 'First')),
            symbol_previous=literal(image % ('previous', 'Previous')),
            symbol_previous_off=literal(image % ('previous_off', 'Previous')),
            symbol_next=literal(image % ('next', 'Next')),
            symbol_next_off=literal(image % ('next_off', 'Next')),
            symbol_last=literal(image % ('last', 'Last')),
            symbol_last_off=literal(image % ('last_off', 'Last'))) or \
            literal('&nbsp;')

    # -------------------------------------------------------------------------
    def pager_bottom(self):
        """Output a string with links to some previous and next pages.

        :rtype: str
        """
        return self.pager() or literal('&nbsp;')

    # -------------------------------------------------------------------------
    def display_modes(self, image='{theme}/images/paging_{display}.png'):
        """Output buttons to switch between cards and list mode.

        :param str image: (default={theme}/images/paging_{action}.png)
            Pattern for the route to navigation button images.
        :rtype: str
        """
        if self._request is None:
            return ''

        theme = theme_static_prefix(self._request)
        image = '<img src="{0}" alt="{1}" title="{2}"/>'.format(
            image.format(theme=theme, display='%s'), '%s', '%s')
        query_string = self._request.GET.copy()
        translate = self._request.localizer.translate
        html = literal('<span class="cioPagingDisplay">')

        if self.display == 'cards':
            html += literal(image % (
                'cards_off', 'Cards', translate(_('Display as Cards'))))
        else:
            query_string.update({'display': 'cards'})
            html += self._link(
                query_string, literal(image % (
                    'cards', 'Cards', translate(_('Display as Cards')))))
        html += ' '

        if self.display == 'list':
            html += literal(
                image % ('list_off', 'List', translate(_('Display as List'))))
        else:
            query_string.update({'display': 'list'})
            html += self._link(
                query_string, literal(
                    image % ('list', 'List', translate(_('Display as List')))))

        html += literal('</span>')
        return html

    # -------------------------------------------------------------------------
    @classmethod
    def navigator(cls, request, paging_id, item_id, url,
                  image='{theme}/images/paging_go_{action}.png'):
        """Return a piece of HTML to go to the previous and the next item.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :param str paging_id:
            Paging ID.
        :param str item_id:
            ID of the current item.
        :param str url:
            Pattern for the URL of previous and next button.
        :param str image: (default={theme}/images/paging_{action}.png)
            Pattern for the route to navigation button images.
        :rtype: str
        """
        if request is None or 'paging' not in request.session or \
           paging_id not in request.session['paging'][1] or \
           'current_ids' not in request.session['paging'][1][paging_id]:
            return ''

        current_ids = request.session['paging'][1][paging_id]['current_ids']
        if item_id not in current_ids:
            return ''
        index = current_ids.index(item_id)
        theme = theme_static_prefix(request)
        image = '<img src="{0}" alt="{1}"/>'.format(
            image.format(theme=theme, action='%s'), '%s')

        html = '<span class="cioPagingNavigator">'
        if index:
            html += '<a href="{0}">{1}</a>'.format(
                url.replace('_ID_', str(current_ids[index - 1])),
                image % ('previous', 'Previous'))
        else:
            html += image % ('previous_off', 'Previous')
        html += ' <span>{0}</span> / {1} '.format(index + 1, len(current_ids))
        if index < len(current_ids) - 1:
            html += '<a href="{0}">{1}</a>'.format(
                url.replace('_ID_', str(current_ids[index + 1])),
                image % ('next', 'Next'))
        else:
            html += image % ('next_off', 'Next')
        html += '</span>'

        return literal(html)

    # -------------------------------------------------------------------------
    def sortable_column(self, label, sort):
        """Output a header of column with `sort up` and `sort down` buttons.

        See :func:`sortable_column`.

        :param str label:
             Label of column.
        :param str sort:
             Sort criteria.
        :rtype: webhelpers2.html.literal
        """
        if self._request is None:
            return '&nbsp;'
        return sortable_column(
            self._request, label, sort,
            self._request.session['paging'][1][self.paging_id]['sort'])

    # -------------------------------------------------------------------------
    def _range(self, regex_match):
        """Return range of linked pages (e.g. '1 2 [3] 4 5 6 7 8').

        :type  regex_match: re.Match
        :param regex_match:
            A regular expressions match object containing the radius of linked
            pages around the current page in regex_match.group(1) as a string.
        :rtype: str
        """
        query_string = self._request.GET.copy()
        radius = int(regex_match.group(1))
        leftmost_page = max(1, self.page - radius)
        rightmost_page = min(self.page + radius, self.page_count)
        items = []

        if self.page != 1 and leftmost_page > 1:
            items.append(self._link(query_string, '1', 1))
        if leftmost_page > 2:
            items.append('..')
        for page in range(leftmost_page, rightmost_page + 1):
            if page == self.page:
                items.append('<span>%d</span>' % page)
            else:
                items.append(self._link(query_string, str(page), page))
        if rightmost_page < self.page_count - 1:
            items.append('..')
        if self.page != self.page_count and rightmost_page < self.page_count:
            items.append(self._link(
                query_string, str(self.page_count), self.page_count))

        return ' '.join(items)

    # -------------------------------------------------------------------------
    def _link(self, query_string, label, page_number=None):
        """Create an A-HREF tag.

        :param dict query_string:
            The current query string in a dictionary.
        :param str label:
            Text to be printed in the A-HREF tag.
        :param int page_number: (optional)
            Number of the page that the link points to.
        """
        if page_number:
            query_string.update({'page': page_number})
        return tags.link_to(
            label, self._request.current_route_path(_query=query_string))


# =============================================================================
class _SQLAlchemyQuery(object):
    """Iterable that allows to get slices from an SQLAlchemy Query object."""
    # pylint: disable = too-few-public-methods

    # -------------------------------------------------------------------------
    def __init__(self, query):
        """Contructor method."""
        self.query = query

    # -------------------------------------------------------------------------
    def __getitem__(self, records):
        """Implement evaluation of self[key]."""
        if not isinstance(records, slice):  # pragma: nocover
            raise Exception('__getitem__ without slicing not supported')
        return self.query[records]

    # -------------------------------------------------------------------------
    def __len__(self):
        """Implement the built-in function len()."""
        return self.query.count()
