"""Various functions to manage attachments."""

from os import makedirs, remove, close
from os.path import join, exists, splitext, basename
from tempfile import mkdtemp, mkstemp


# =============================================================================
def attachment_url(request, category, key, filename):
    """Return the URL of an attachement file or ``None`` if it does not exist
    or attachments are not activated.

    :type  request: pyramid.request.Request
    :param request:
        Current request.
    :param str category:
        Category of attachement (e.g. Users).
    :param str key:
        Key to access to the attachments.
    :param str filename:
        Name of file to retrieve.
    :rtype: str
    """
    if not key or not filename:
        return None
    attachments = request.registry.settings.get('attachments')
    if not attachments:
        return None

    attachment = join(attachments, category, key, filename)
    if not exists(attachment):
        return None

    return request.route_path('attachment', path=(category, key, filename))


# =============================================================================
def attachment_update(request, category, key, field, replace=None, prefix=''):
    """Update the content of the attachment directory.

    :type  request: pyramid.request.Request
    :param request:
        Current request.
    :param str category:
        Category of attachement (e.g. Users).
    :param str key:
        Key to access to the attachments.
    :type  field: cgi.FieldStorage
    :param field:
        File to retrieve.
    :param str replace: (optional)
        File to delete before adding the new file.
    :param str prefix: (optional)
        Prefix for newly created attachment key.
    :rtype: tuple
    :return:
        A tuple such as ``(attachments_key, file_path)``.
    """
    # Directory for attachments
    attachments = request.registry.settings.get('attachments')
    if not attachments:
        return key, replace
    attachments = join(attachments, category)
    if not exists(attachments):
        try:
            makedirs(attachments)
        except (OSError, IOError):  # pragma: nocover
            request.session.flash(('Permission refused.'), 'alert')
            return key, replace

    # Personal attachment directory
    try:
        if key is None:
            key = basename(mkdtemp(prefix=prefix, dir=attachments))
        attachments = join(attachments, key)
        if not exists(attachments):
            makedirs(attachments)
    except (OSError, IOError):  # pragma: nocover
        request.session.flash(('Permission refused.'), 'alert')
        return key, replace

    # Remove old file
    if replace and exists(join(attachments, replace)):
        try:
            remove(join(attachments, replace))
        except (OSError, IOError):  # pragma: nocover
            request.session.flash(('Permission refused.'), 'alert')
            return key, replace

    # Copy new file
    try:
        hdl, filename = mkstemp(
            suffix=splitext(field.filename)[1], prefix='',
            dir=attachments)
        close(hdl)
        with open(filename, 'wb') as hdl:
            hdl.write(field.file.read())
    except (OSError, IOError):  # pragma: nocover
        request.session.flash(('Permission refused.'), 'alert')
        return key, None

    return key, basename(filename)
