"""Clipboard management."""

from pyramid.config import Configurator

from ..lib.i18n import _
from ..lib.panel import PANEL_ITEM_PREFIX, Panel
from ..models.dbsettings import SETTINGS_DEFAULTS


CLIPBOARD_LABEL_MAX_LENGTH = 96
CLIPBOARD_LABEL_MAX_ITEMS = 8


# =============================================================================
def includeme(configurator):
    """Function to include themes.

    :type  configurator: pyramid.config.Configurator
    :param configurator:
        Object used to do configuration declaration within the application.
    """
    if isinstance(configurator, Configurator):
        if 'panels' not in configurator.registry:
            configurator.registry['panels'] = {}
        if 'clipboard' not in configurator.registry['panels']:
            Clipboard.register(configurator.registry, Clipboard)


# =============================================================================
class Clipboard(Panel):
    """Class to manage clipboard and clipboard panel.

    See: :class:`.lib.panel.Panel`
    """

    uid = 'clipboard'
    label = _('Clipboard')
    icon = '/images/panel_clipboard.png'
    template = 'chrysalio:Templates/panel_clipboard.pt'
    need_form = True

    # -------------------------------------------------------------------------
    @classmethod
    def is_empty(cls, request):
        """Return ``True`` if the clipboard is empty.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :rtype: bool
        """
        return bool(not request.session.get('clipboard'))

    # -------------------------------------------------------------------------
    @classmethod
    def entries(cls, request):
        """Return the list of entries.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :rtype: list
        """
        return request.session['clipboard'] \
            if 'clipboard' in request.session else []

    # -------------------------------------------------------------------------
    @classmethod
    def push(cls, request, domain, cut, data, preview):
        """Push a new entry in the clipboard buffer.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :param str domain:
            Domain of the entry (ex.: ``'warehouse/file'``).
        :param bool cut:
            ``True`` if it is a `cut` operation.
        :param data:
            Content of this entry. It  depends on the domain.
        :type  preview: webhelpers2.html.literal
        :param preview:
            Representation of the entry in the clipboard.
        """
        # Ajust size
        if 'clipboard' not in request.session:
            request.session['clipboard'] = []
        request.session['clipboard'] = request.session['clipboard'][
            :request.registry['settings'].get(
                'clipboard-size', SETTINGS_DEFAULTS['clipboard-size']) - 1]

        # Push the new entry in the buffer
        request.session['clipboard'].insert(0, (domain, cut, data, preview))

    # -------------------------------------------------------------------------
    @classmethod
    def selection(cls, request, domains):
        """Return entries selected in the clipboard and compatible with almost
        one domain of ``domains``.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :param list domains:
            List of accepted formats of the entry.
        :rtype: list
        """
        if 'clipboard' not in request.session \
           or not request.session['clipboard']:
            return ()

        # Selected entries
        entries = []
        kept_nums = []
        requested_nums = cls._requested_numbers(request, domains)
        for num in requested_nums:
            entries.append(request.session['clipboard'][num])
            if not request.session['clipboard'][num][1]:
                kept_nums.append(num)

        # Reorganization of the buffer
        my_buffer = []
        for num in kept_nums:
            my_buffer.append(request.session['clipboard'][num])
        for num in range(len(request.session['clipboard'])):
            if num not in requested_nums:
                my_buffer.append(request.session['clipboard'][num])
        request.session['clipboard'] = my_buffer

        return entries

    # -------------------------------------------------------------------------
    @classmethod
    def _requested_numbers(cls, request, domains):
        """Return a list of numbers of entry requested and compatible with
        ``domains``.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :param list domains:
            List of accepted formats of the entry.
        :rtype: list
        """
        selected = []
        size = len(request.session['clipboard'])

        # Selected in the clipboard panel
        for num in request.params:
            if num.startswith(PANEL_ITEM_PREFIX):
                num = int(num[len(PANEL_ITEM_PREFIX):])
                if num < size and \
                   request.session['clipboard'][num][0] in domains:
                    selected.append(num)
        if selected:
            return selected

        # The first compatible entry
        for num in range(size):
            if request.session['clipboard'][num][0] in domains:
                selected.append(num)
                break
        return selected
