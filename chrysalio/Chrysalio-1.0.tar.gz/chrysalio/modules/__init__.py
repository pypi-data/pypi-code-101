"""Base class for modules."""

from os.path import dirname
from configparser import ConfigParser

from lxml import etree

from pyramid.httpexceptions import HTTPForbidden

from ..lib.i18n import _
from ..lib.utils import tounicode


# =============================================================================
class Module(object):
    """Base class for included modules.

    :param str config_ini:
        Absolute path to the configuration file (e.g. development.ini).
    """

    name = None
    implements = ()
    dependencies = ()
    relaxng = None
    xml2db = None
    db2xml = None
    areas = None
    _DBModule = None  # In order to avoid always loading module table

    # -------------------------------------------------------------------------
    def __init__(self, config_ini):
        """Constructor method."""
        # pylint: disable = unused-argument
        self.uid = self.__class__.__module__
        if self.name is None:
            self.name = self.uid
        if self.areas is None:
            self.areas = {self.uid: self.name}

    # -------------------------------------------------------------------------
    @classmethod
    def register(cls, environment, module_class):
        """Method to register the module.

        :type  environment: :class:`pyramid.config.Configurator` or
            :class:`dict`
        :param environment:
            Object used to do configuration declaration within the application
            or a ScriptRegistry to simulate the application registry.
        :param module_class:
            Module class.
        """
        # Server mode (environment == configurator)
        if hasattr(environment, 'registry'):
            if 'modules' in environment.registry:
                module = module_class(environment.get_settings()['__file__'])
                environment.registry['modules'][module.uid] = module

        # Populate/backup/execute mode (environment == ScriptRegistry)
        else:
            module = module_class(environment.settings['__file__'])
            environment['modules'][module.uid] = module

    # -------------------------------------------------------------------------
    @classmethod
    def check_conflicts(cls, includes, modules):
        """Check conflicts between modules. Return a list of IDs of avaliable
        modules and IDs of implemented functionalities.

        :param list includes:
            List of available `includes`.
        :type  modules: collections.OrderedDict
        :param modules:
            Dictionary of available modules.
        :rtype: tuple
        :return:
           A tuple such as ``(implementation_list, error)``.
        """
        implementations = {k: k for k in includes}
        for module_id in modules:
            for implementation in modules[module_id].implements:
                if implementation in implementations:
                    return (), _(
                        '*** Modules ${m1} and ${m2} implement the same '
                        'functionality "${f}".', {
                            'm1': implementations[implementation],
                            'm2': module_id, 'f': implementation})
                implementations[implementation] = module_id
        return implementations.keys(), None

    # -------------------------------------------------------------------------
    def check_dependencies(self, implementations):
        """Check dependencies.

        :param list implementations:
            List containing the IDs of available `includes` plus the IDS
            of functionalities implemented by each available module.
        :rtype: :class:`pyramid.i18n.TranslationString` or ``None``
        """
        for dependency in self.dependencies:
            if dependency not in implementations:
                return _(
                    '*** Dependency "${d}" is missing!', {'d': dependency})
        return None

    # -------------------------------------------------------------------------
    def check_activations(self, modules_off):
        """Check activations.

        :param set modules_off:
            Set of inactive modules.
        :rtype: bool
        :return:
             ``True`` if an activation occurs.
        """
        if self.uid in modules_off:
            return False

        activation = False
        for dependency in self.dependencies:
            if dependency in modules_off:
                modules_off.remove(dependency)
                activation = True
        return activation

    # -------------------------------------------------------------------------
    def module_xml2db(self, dbsession, tree, only, error_if_exists):
        """Load an XML configuration file for the module.

        :type  dbsession: sqlalchemy.orm.session.Session
        :param dbsession:
            SQLAlchemy session.
        :type  tree: lxml.etree.ElementTree
        :param tree:
            Content of the XML document.
        :param str only:
            If not ``None``, only the items of type ``only`` are loaded.
        :param bool error_if_exists:
            It returns an error if an item already exists.
        :rtype: list
        :return:
            A list of error messages.
        """
        # Module activation
        module_elt = None
        if self._DBModule is not None:
            module_elt = tree.xpath(
                'module[@id="{0}"]|modules/module[@id="{0}"]'.format(
                    self.uid))
            if module_elt:
                dbmodule = dbsession.query(self._DBModule).filter_by(
                    module_id=self.uid).first()
                inactive = module_elt[0].get('inactive') in ('true', '1')
                if inactive and dbmodule is None:
                    # pylint: disable = not-callable
                    dbsession.add(
                        self._DBModule(module_id=self.uid, inactive=True))
                elif not inactive and dbmodule:
                    dbsession.delete(dbmodule)

        # Module settings
        # pylint: disable = unsubscriptable-object
        if self.relaxng is None or self.xml2db is None or (
                module_elt and len(module_elt[0]) + 1 == 1):
            return []
        if module_elt:
            root_elt = module_elt[0].xpath(
                'ns0:{0}'.format(self.relaxng['root']),
                namespaces={'ns0': self.relaxng.get('namespace')})
        else:
            root_elt = tree.xpath(
                '/ns0:{0}'.format(self.relaxng['root']),
                namespaces={'ns0': self.relaxng.get('namespace')})
        if not root_elt:
            return []

        return self.xml2db[0](dbsession, root_elt[0], only, error_if_exists)

    # -------------------------------------------------------------------------
    def module_db2xml(self, dbsession):
        """Return a list of XML elements of the module.

        :type  dbsession: sqlalchemy.orm.session.Session
        :param dbsession:
            SQLAlchemy session.
        :rtype: list
        :return:
            A list of XML elements.
        """
        module_elt = etree.Element('module')
        module_elt.set('id', self.uid)
        inactive = False

        # Module activation
        if self._DBModule is not None:
            dbmodule = dbsession.query(self._DBModule).filter_by(
                module_id=self.uid).first()
            inactive = dbmodule is not None and dbmodule.inactive
            if inactive:
                module_elt.set('inactive', 'true')

        # Module settings
        # pylint: disable = unsubscriptable-object
        if self.relaxng is None or self.db2xml is None:
            return [module_elt] if inactive else []
        root_elt = etree.SubElement(
            module_elt,
            etree.QName(self.relaxng['namespace'], self.relaxng['root']).text,
            nsmap={None: self.relaxng['namespace']},
            version=self.relaxng['version'])
        self.db2xml[0](dbsession, root_elt)

        return [module_elt]

    # -------------------------------------------------------------------------
    def populate(self, args, registry, dbsession):
        """Method called by populate script to complete the operation.

        :type  args: argparse.Namespace
        :param args:
            Command line arguments.
        :param dict registry:
            Dictionary registry.
        :type  dbsession: sqlalchemy.orm.session.Session
        :param dbsession:
            SQLAlchemy session.
        :rtype: :class:`pyramid.i18n.TranslationString` or ``None``
        :return:
            Error message or ``None``.
        """

    # -------------------------------------------------------------------------
    def backup(self, args, registry, dbsession, directory):
        """Method called by backup script to complete the operation.

        :type  args: argparse.Namespace
        :param args:
            Command line arguments.
        :param dict registry:
            Dictionary registry.
        :type  dbsession: sqlalchemy.orm.session.Session
        :param dbsession:
            SQLAlchemy session.
        :param str directory:
            Path to the backup directory.
        :rtype: :class:`pyramid.i18n.TranslationString` or ``None``
        :return:
            Error message or ``None``.
        """

    # -------------------------------------------------------------------------
    def activate(self, registry, dbsession):
        """Method to activate the module.

        :type  registry: pyramid.registry.Registry
        :param registry:
            Application registry.
        :type  dbsession: sqlalchemy.orm.session.Session
        :param dbsession:
            SQLAlchemy session.
        """

    # -------------------------------------------------------------------------
    def deactivate(self, registry, dbsession):
        """Method to deactivate the module.

        :type  registry: pyramid.registry.Registry
        :param registry:
            Application registry.
        :type  dbsession: sqlalchemy.orm.session.Session
        :param dbsession:
            SQLAlchemy session.
        """

    # -------------------------------------------------------------------------
    @classmethod
    def check_activated(cls, request, module_id):
        """Check if the module is active and raise an HTTPForbidden exception
        if not.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :param str module_id:
            ID of checked module.
        """
        if 'modules' not in request.registry or \
           module_id not in request.registry['modules'] or \
           module_id in request.registry['modules_off']:
            raise HTTPForbidden(comment=_(
                'The module "${i}" is not activated.', {'i': module_id}))

    # -------------------------------------------------------------------------
    def configuration_route(self, request):
        """Return the route to configure this module.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        """

    # -------------------------------------------------------------------------
    def _settings(self, config_ini, section=None):
        """Method to retrieve the settings of the module.

        :param str config_ini:
            Absolute path to the configuration file.
        :param str section: (optional)
            Section in INI file.
        :rtype: dict
        """
        if section is None:
            section = self.__class__.__name__.replace('Module', '')
        config = ConfigParser({'here': dirname(config_ini)})
        config.read(tounicode(config_ini), encoding='utf8')
        if not config.has_section(section):
            return config.defaults()
        return dict(config.items(section))
