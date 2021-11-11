"""Function to import and export database from and into XML files."""

from ..relaxng import RELAXNG_CIOLDAP
from .dbldap import DBLdap


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
    if only is not None and only != 'ldap':
        return []

    ldap_elt = root_elt.find(
        '{{{0}}}ldap'.format(RELAXNG_CIOLDAP['namespace']))
    if ldap_elt is None:
        return []
    error = DBLdap.xml2db(dbsession, ldap_elt)
    return [error] if error is not None else []


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
    dbldap = dbsession.query(DBLdap).first()
    if dbldap is not None:
        root_elt.append(dbldap.db2xml())
