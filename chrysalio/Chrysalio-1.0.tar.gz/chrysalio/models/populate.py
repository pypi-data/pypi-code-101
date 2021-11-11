"""Function to import and export database from and into XML files."""

from os.path import join, basename, exists, splitext, relpath
from tempfile import mkdtemp
from shutil import rmtree
from zipfile import ZIP_DEFLATED, ZipFile, LargeZipFile, BadZipfile
from cgi import FieldStorage

from lxml import etree
from sqlalchemy.exc import ProgrammingError

from pyramid.response import Response, FileResponse

from ..lib.i18n import _
from ..lib.utils import scandir, walk
from ..lib.xml import load_xml, validate_xml, create_entire_xml
from ..lib.xml import relaxng4validation
from .dbsettings import DBSettings
from .dbprofile import DBProfile
from .dbuser import DBUser
from .dbgroup import DBGroup


# =============================================================================
def xml2db(dbsession, tree, only=None, error_if_exists=True, modules=None):
    """Load an XML configuration file into the database.

    :type  dbsession: sqlalchemy.orm.session.Session
    :param dbsession:
        SQLAlchemy session.
    :type  tree: lxml.etree.ElementTree
    :param tree:
        Content of the XML document.
    :param str only: (optional)
        If not ``None``, only the items of type ``only`` are loaded.
    :param bool error_if_exists: (default=True)
        It returns an error if an item already exists.
    :type  modules: collections.OrderedDict
    :param modules: (optional)
        Dictionary of modules to use to complete the loading.
    :rtype: list
    :return:
        A list of error messages.
    """
    # Load settings
    if only is None or only == 'settings':
        DBSettings.xml2db(dbsession, tree.find('settings'))

    # Load profiles
    errors = element2db(dbsession, tree, only, error_if_exists, {
        'tag': 'profile', 'class': DBProfile})
    profiles = [k[0] for k in dbsession.query(DBProfile.profile_id)]

    # Load users
    errors += element2db(dbsession, tree, only, error_if_exists, {
        'tag': 'user', 'class': DBUser, 'kwargs': {'profiles': profiles}})
    users = dict(dbsession.query(DBUser.login, DBUser.user_id))

    # Load groups
    errors += element2db(dbsession, tree, only, error_if_exists, {
        'tag': 'group', 'class': DBGroup,
        'kwargs': {'profiles': profiles, 'users': users}})

    # Load tables from modules
    errors += module_xml2db(dbsession, tree, only, error_if_exists, modules)

    return [k for k in errors if k is not None]


# =============================================================================
def element2db(dbsession, tree, only, error_if_exists, element):
    """Load XML elements into the database according to an XPath.

    :type  dbsession: sqlalchemy.orm.session.Session
    :param dbsession:
        SQLAlchemy session.
    :type  tree: lxml.etree.ElementTree
    :param tree:
        Content of the configuration file.
    :param str only:
        If not ``None``, only the items of type ``only`` are loaded.
    :param bool error_if_exists:
        It returns an error if an item already exists.
    :param dict element:
        A dictionary with keys ``tag``, ``class`` and, possibly, ``kwargs``,
        ``relaxng`` representing the element to insert into the database.
    :rtype: list
    :return:
        A list of error messages.
    """
    if only is not None and only != element['tag']:
        return []

    # Without namespace
    errors = []
    relaxng = element.get('relaxng')
    namespace = relaxng.get('namespace') if relaxng is not None else None
    if namespace is None:
        for elt in tree.xpath('{0}|{0}s/{0}'.format(element['tag'])):
            errors.append(element['class'].xml2db(
                dbsession, elt, error_if_exists, element.get('kwargs')))
        return errors

    # With namespace
    must_validate = tree.xpath('namespace-uri()') != namespace
    for root_elt in tree.xpath(
            '//ns0:{0}'.format(relaxng['root']),
            namespaces={'ns0': namespace}):
        if must_validate:
            error = validate_xml(
                etree.ElementTree(root_elt), relaxng4validation(relaxng))
            if error is not None:
                errors.append(error)
                continue
        for elt in root_elt.xpath(
                './/ns0:{0}s/ns0:{0}|ns0:{0}'.format(element['tag']),
                namespaces={'ns0': namespace}):
            errors.append(element['class'].xml2db(
                dbsession, elt, error_if_exists, element.get('kwargs')))

    return [k for k in errors if k is not None]


# =============================================================================
def module_xml2db(dbsession, tree, only, error_if_exists, modules):
    """Load elements from included modules.

    :type  dbsession: sqlalchemy.orm.session.Session
    :param dbsession:
        SQLAlchemy session.
    :type  tree: lxml.etree.ElementTree
    :param tree:
        Content of the configuration file.
    :param str only:
        If not ``None``, only the items of type ``only`` are loaded.
    :param bool error_if_exists:
        It returns an error if an item already exists.
    :type  modules: :class:`collections.OrderedDict` or ``None``
    :param modules:
        Dictionary of modules to use to complete the loading.
    :rtype: list
    :return:
        A list of error messages.
    """
    if modules is None:
        return []

    errors = []
    for module_id in modules:
        errors += modules[module_id].module_xml2db(
            dbsession, tree, only, error_if_exists)
    return errors


# =============================================================================
def db2xml(dbsession, modules=None):
    """Return a list of XML elements.

    :type  dbsession: sqlalchemy.orm.session.Session
    :param dbsession:
        SQLAlchemy session.
    :type  modules: collections.OrderedDict
    :param modules: (optional)
        Dictionary of modules to use to complete the loading.
    :rtype: list
    """
    elements = []

    # General settings
    elements.append(DBSettings.db2xml(dbsession))

    # Profiles
    for dbprofile in dbsession.query(DBProfile).order_by('profile_id'):
        elements.append(dbprofile.db2xml(dbsession))

    # Users
    for dbuser in dbsession.query(DBUser).order_by('login'):
        if dbuser.user_id != 1 or dbuser.status != 'administrator':
            elements.append(dbuser.db2xml(dbsession))

    # Groups
    for dbgroup in dbsession.query(DBGroup).order_by('group_id'):
        elements.append(dbgroup.db2xml(dbsession))

    # Save tables of included modules
    elements += module_db2xml(dbsession, modules)

    return [k for k in elements if k is not None]


# =============================================================================
def module_db2xml(dbsession, modules):
    """Return a list of XML elements from included modules.

    :type  dbsession: sqlalchemy.orm.session.Session
    :param dbsession:
        SQLAlchemy session.
    :type  modules: :class:`collections.OrderedDict` or ``None``
    :param modules:
        Dictionary of modules to use to complete the loading.
    :rtype: list
    """
    if modules is None:
        return []

    elements = []
    for module_id in modules:
        elements += modules[module_id].module_db2xml(dbsession)
    return elements


# =============================================================================
def web2db(request, _xml2db, only=None, relaxngs=None, error_if_exists=True):
    """Read XML or ZIP files from Web and load them into the database.

    :type  request: pyramid.request.Request
    :param request:
        Current request.
    :param _xml2db:
        Function to load an XML configuration file.
    :param str only: (optional)
        If not ``None``, only the items of type ``only`` are loaded.
    :param dict relaxngs: (optional)
        Dictionary of extra Relax NG files.
    :param bool error_if_exists: (default=True)
        It returns an error if an item already exists.
    """
    def _web2db_xml(filename, data):
        """Sub function to load an XML file."""
        tree = load_xml(filename, relaxngs, data=data)
        # pylint: disable = protected-access
        if not isinstance(tree, etree._ElementTree):
            errors.append(tree)
            return
        # pylint: enable = protected-access
        try:
            errors.extend(_xml2db(
                request.dbsession, tree, only=only,
                error_if_exists=error_if_exists,
                modules=request.registry.get('modules')))
        except ProgrammingError as error:  # pragma: nocover
            errors.append(error)

    # RelaxNG
    relaxngs = {} if relaxngs is None else relaxngs
    relaxngs.update(relaxng4validation(request.registry['relaxng']))

    # Browse files
    errors = []
    attachments = request.registry.settings.get('attachments')
    for field_storage in request.POST.getall('file'):
        if not isinstance(field_storage, FieldStorage):
            continue

        # XML file
        ext = splitext(field_storage.filename)[1]
        if ext == '.xml':
            _web2db_xml(field_storage.filename, field_storage.file.read())
            continue

        # Not a ZIP file
        if ext != '.zip':
            errors.append(_('Format must be ZIP or XML!'))
            continue

        # ZIP file
        try:
            with ZipFile(field_storage.file, 'r') as zip_file:
                for zip_info in zip_file.infolist():
                    if splitext(zip_info.filename)[1] == '.xml':
                        _web2db_xml(
                            zip_info.filename,
                            zip_file.read(zip_info.filename))
                    elif attachments:
                        zip_file.extract(zip_info, attachments)
        except BadZipfile:
            errors.append(_('It is not a ZIP file!'))
            continue

    # Push errors into session
    for err in errors:
        request.session.flash(err, 'alert')


# =============================================================================
def db2web(request, dbitems, filename, relaxng=None):
    """Convert SqlAlchemy items into an XML file and its attachments embedded
    in a Pyramid response.

    :type  request: pyramid.request.Request
    :param request:
        Current request.
    :param list dbitems:
        A list of SqlAlchemy objects with a method db2xml() and a
        method attachments2directory().
    :param str filename:
        The name of the downloaded file.
    :param dict relaxng: (optional)
        A dictionary describing the Relax NG used by
        func:`.lib.xml.create_entire_xml`.
    :rtype: pyramid.response.Response
    :return:
        An object :class:`~pyramid.response.Response` or ``None``.
    """
    # pylint: disable = too-many-locals
    # Create the XML file
    root_elt = create_entire_xml(
        relaxng or request.registry['relaxng'],
        [k.db2xml(request.dbsession) for k in dbitems])
    # pylint: disable = protected-access
    if not isinstance(root_elt, etree._Element):  # pragma: nocover
        return Response(body=root_elt)
    # pylint: enable = protected-access

    # Collect attachments
    attachments = request.registry.settings.get('attachments')
    tmp_dir = None
    if attachments and exists(attachments):
        tmp_dir = mkdtemp(
            prefix=request.registry.settings['site.uid'],
            dir=request.registry.settings.get('temporary'))
        container = join(tmp_dir, 'Container')
        for dbitem in dbitems:
            dbitem.attachments2directory(attachments, container)

    # Return a XML file
    if not tmp_dir or not tuple(scandir(tmp_dir)):
        if tmp_dir:
            rmtree(tmp_dir)
        response = Response(
            body=etree.tostring(
                root_elt, pretty_print=True, encoding='utf-8',
                xml_declaration=True),
            content_type='application/xml')
        response.headerlist.append((
            'Content-Disposition', 'attachment; filename="{0}"'.format(
                filename)))
        return response

    # Return a ZIP file
    # pylint: disable = consider-using-with
    zip_file = ZipFile(
        join(tmp_dir, '{0}.zip'.format(splitext(filename)[0])), 'w',
        ZIP_DEFLATED)
    zip_file.writestr(
        filename, etree.tostring(
            root_elt, encoding='utf-8', xml_declaration=True,
            pretty_print=True))
    for root, unused_, files in walk(container):
        for name in files:
            name = join(root, name)
            try:
                zip_file.write(name, relpath(name, container))
            except LargeZipFile:  # pragma: nocover
                zip_file.close()
                rmtree(tmp_dir)
                return Response(request.localizer.translate(
                    _('This file is too big!')))
            except IOError as error:  # pragma: nocover
                zip_file.close()
                rmtree(tmp_dir)
                return Response(error)
    filename = zip_file.filename
    zip_file.close()

    response = FileResponse(
        filename, request=request, content_type='application/zip')
    response.headers['Content-Disposition'] = \
        'attachment; filename="{0}"'.format(basename(filename))
    rmtree(tmp_dir)
    return response
