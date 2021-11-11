"""Function to import and export database from and into XML files."""

from lxml import etree

from ....models.populate import element2db
from ..relaxng import RELAXNG_CIOSKELETON
from .dbbone import DBBone


# =============================================================================
def xml2db(dbsession, root_elt, only=None, error_if_exists=True, modules=None):
    """Load an XML configuration file for an included module.

    :type  dbsession: sqlalchemy.orm.session.Session
    :param dbsession:
        SQLAlchemy session.
    :type  root_elt: lxml.etree.Element
    :param root_elt:
        XML element with the namespace of the module.
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
    # pylint: disable = unused-argument
    return element2db(
        dbsession, root_elt, only, error_if_exists, {
            'tag': 'bone', 'class': DBBone, 'relaxng': RELAXNG_CIOSKELETON})


# =============================================================================
def db2xml(dbsession, root_elt):
    """Return a list of XML elements.

    :type  dbsession: sqlalchemy.orm.session.Session
    :param dbsession:
        SQLAlchemy session.
    :type  root_elt: lxml.etree._Element
    :param root_elt:
        XML element with the namespace of the module.
    """
    dbbones = dbsession.query(DBBone).order_by('bone_id').all()
    if dbbones:
        bones_elt = etree.SubElement(root_elt, 'bones')
        for dbbone in dbbones:
            bones_elt.append(dbbone.db2xml())
