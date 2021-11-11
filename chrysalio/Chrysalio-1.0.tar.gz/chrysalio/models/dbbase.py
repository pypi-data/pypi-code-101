"""Database main objects, functions and constants."""

from os import makedirs
from os.path import join, exists
from shutil import copy2
from json import loads

from ..lib.i18n import translate_field


# =============================================================================
class DBBaseClass(object):
    """Base class for prime SQLAlchemy table."""

    suffix = 'cio'
    attachments_dir = None
    _settings_tabs = None

    # -------------------------------------------------------------------------
    def label(self, request):
        """Return a translated label.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :rtype: str
        """
        # pylint: disable = no-member
        return translate_field(request, loads(self.i18n_label)) \
            if hasattr(self, 'i18n_label') else ''

    # -------------------------------------------------------------------------
    def description(self, request):
        """Return a translated description.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :rtype: str
        """
        # pylint: disable = no-member
        return translate_field(request, self.i18n_description) \
            if hasattr(self, 'i18n_description') else ''

    # -------------------------------------------------------------------------
    def attachments2directory(self, attachments, directory):
        """Copy from attachments directory the file corresponding to the user.

        :param str attachments:
            Absolute path to the attachments directory.
        :param str directory:
            The backup directory.
        """
        # pylint: disable = no-member
        if not self.attachments_dir or \
           not hasattr(self, 'attachments_key') or \
           not self.attachments_key or \
           not hasattr(self, 'picture') or not self.picture:
            return

        picture = join(
            attachments, self.attachments_dir, self.attachments_key,
            self.picture)
        if not exists(picture):
            return

        destination = join(
            directory, self.attachments_dir, self.attachments_key)
        if not exists(destination):
            makedirs(destination)
        copy2(picture, destination)

    # -------------------------------------------------------------------------
    @classmethod
    def settings_tabs(cls, request):
        """Return a tuple of tab labels to view or edit the object.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :rtype: tuple
        """
        # pylint: disable = unused-argument
        return cls._settings_tabs
