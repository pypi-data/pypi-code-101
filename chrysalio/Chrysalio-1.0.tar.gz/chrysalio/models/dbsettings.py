"""SQLAlchemy-powered model definitions for settings."""

from os.path import basename
from datetime import datetime

from sqlalchemy import Column, String
from sqlalchemy.exc import OperationalError, ProgrammingError
from lxml import etree
from webhelpers2.html import HTML, literal
import colander

from ..lib.i18n import _
from ..lib.utils import tounicode, deltatime_label, size_label
from ..lib.config import settings_get_list
from ..lib.paging import PAGE_DEFAULT_SIZE, PAGE_SIZES
from . import DBDeclarativeClass, ID_LEN, EMAIL_LEN, LABEL_LEN
from .dbbase import DBBaseClass

SETTINGS_DEFAULTS = {
    'language': 'en', 'password-min-length': 8, 'remember-me': 5184000,
    'page-size': PAGE_DEFAULT_SIZE, 'download-max-size': 10485760,
    'clipboard-size': 10, 'theme': ''}


# =============================================================================
class DBSettings(DBDeclarativeClass, DBBaseClass):
    """SQLAlchemy-powered settings class."""

    suffix = 'cioset'
    settings_defaults = SETTINGS_DEFAULTS
    _settings_tabs = (_('Parameters'), _('Information'))

    __tablename__ = 'settings'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    key = Column(String(ID_LEN), primary_key=True)
    value = Column(String(128))

    # -------------------------------------------------------------------------
    @classmethod
    def exists(cls, dbsession):
        """Check if table ``settings`` exists and has at least one item.

        :type  dbsession: sqlalchemy.orm.session.Session
        :param dbsession:
            SQLAlchemy session (for testing).
        :rtype: bool
        """
        try:
            setting = dbsession.query(cls).first()
        except (OperationalError, ProgrammingError, UnicodeEncodeError):
            return False
        return setting is not None

    # -------------------------------------------------------------------------
    @classmethod
    def xml2db(cls, dbsession, settings_elt):
        """Load settings from a XML element.

        :type  dbsession: sqlalchemy.orm.session.Session
        :param dbsession:
            SQLAlchemy session.
        :type  settings_elt: lxml.etree.Element
        :param settings_elt:
            Profile XML element.
        """
        if settings_elt is None:
            return

        # Clean up old settings
        for dbsetting in dbsession.query(cls):
            dbsession.delete(dbsetting)

        # Fill settings table
        dbsession.add(cls(
            key='populate', value=datetime.now().isoformat(' ').split('.')[0]))
        for elt in settings_elt.iterchildren(tag=etree.Element):
            dbsession.add(cls(
                key=elt.tag,
                value=elt.text[:128] if elt.text is not None else None))

    # -------------------------------------------------------------------------
    @classmethod
    def db2xml(cls, dbsession):
        """Serialize settings to a XML representation.

        :type  dbsession: sqlalchemy.orm.session.Session
        :param dbsession:
            SQLAlchemy session.
        :rtype: lxml.etree.Element
        """
        settings_elt = etree.Element('settings')

        # Key/value from database
        for dbsetting in dbsession.query(cls):
            if dbsetting.key != 'populate':
                etree.SubElement(settings_elt, dbsetting.key).text = \
                    dbsetting.value

        return settings_elt if len(settings_elt) + 1 > 1 else None

    # -------------------------------------------------------------------------
    @classmethod
    def db2dict(cls, settings, dbsession, default_email):
        """Return a dictionary containing settings.

        :param dict settings:
            Pyramid settings.
        :type  dbsession: sqlalchemy.orm.session.Session
        :param dbsession:
            SQLAlchemy session (for testing).
        :param str default_email:
            Default email for the site, usually the administrator email.
        :rtype: dict
        """
        try:
            dbsettings = dbsession.query(cls).all()
        except (OperationalError, ProgrammingError, UnicodeEncodeError):
            dbsettings = []

        # Default settings
        settings_dict = cls.settings_defaults.copy()
        if len(dbsettings) < 2:
            settings_dict['title'] = tounicode(settings.get(
                'site.title', settings['site.uid']))
            settings_dict['email'] = default_email
            if 'pyramid.default_locale_name' in settings:
                settings_dict['language'] = settings[
                    'pyramid.default_locale_name']
            settings_dict['populate'] = datetime.now().isoformat(
                ' ').split('.')[0]
            return settings_dict

        # ... or customized settings
        for dbsetting in dbsettings:
            settings_dict[dbsetting.key] = dbsetting.value
        settings_dict['password-min-length'] = int(
            settings_dict['password-min-length'])
        settings_dict['remember-me'] = int(settings_dict['remember-me'])
        settings_dict['page-size'] = int(settings_dict['page-size'])
        settings_dict['download-max-size'] = int(
            settings_dict['download-max-size'])
        settings_dict['clipboard-size'] = int(settings_dict['clipboard-size'])
        if 'chrysalio.includes' not in settings or \
           'chrysalio.includes.themes' not in settings['chrysalio.includes']:
            settings_dict['theme'] = ''

        return settings_dict

    # -------------------------------------------------------------------------
    @classmethod
    def tab4view(cls, request, tab_index, form):
        """Generate the tab content for settings.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :param int index:
            Index of the tab.
        :type  form: .lib.form.Form
        :param tuple principals:
            Groups of principals.
        :rtype: webhelpers2.html.literal
        """
        if tab_index == 0:
            return cls._tab4view_parameters(request, form)
        if tab_index == 1:
            return cls._tab4view_information(request, form)
        return ''

    # -------------------------------------------------------------------------
    @classmethod
    def _tab4view_parameters(cls, request, form):
        """Generate the parameters tab.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :type  form: .lib.form.Form
        :param form:
            Current form object.
        :rtype: webhelpers2.html.literal
        """
        translate = request.localizer.translate
        html = HTML.h3(translate(_('Site')))
        html += form.grid_item(
            translate(_('Title:')), request.registry['settings']['title'],
            clear=True)
        html += form.grid_item(
            translate(_('Email:')),
            request.registry['settings'].get('email'), clear=True)

        html += HTML.h3(translate(_('Default values')))
        html += form.grid_item(
            translate(_('Language:')),
            request.registry['settings']['language'], clear=True)
        html += form.grid_item(
            translate(_('Password length:')),
            request.registry['settings']['password-min-length'], clear=True)
        html += form.grid_item(
            translate(_('Remember me:')),
            deltatime_label(
                request.registry['settings']['remember-me'],
                lang=request.locale_name),
            clear=True)
        html += form.grid_item(
            translate(_('Lines per page:')),
            request.registry['settings']['page-size'], clear=True)
        if request.registry['settings']['download-max-size']:
            html += form.grid_item(
                translate(_('Maximum size of download:')),
                size_label(request.registry['settings']['download-max-size']),
                clear=True)
        html += form.grid_item(
            translate(_('Clipboard size:')),
            request.registry['settings']['clipboard-size'], clear=True)
        lang = request.session.get('lang', 'en')
        html += form.grid_item(
            translate(_('Theme:')), request.registry['themes'][
                request.registry['settings']['theme']]['name'].get(
                    lang, request.registry['settings']['theme']),
            clear=True)

        return html

    # -------------------------------------------------------------------------
    @classmethod
    def _tab4view_information(cls, request, form, readonly_message=False):
        """Generate the information tab.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :type  form: .lib.form.Form
        :param form:
            Current form object.
        :param bool readonly_message:
            If ``True`` add a `Read Only` message.
        :rtype: webhelpers2.html.literal
        """
        translate = request.localizer.translate

        html = ''
        if readonly_message:
            html = HTML.div(
                translate(_('You cannot modify these values.')),
                class_='cioAlert')

        html += HTML.h3(translate(_('Site')))
        html += form.grid_item(
            translate(_('Identifier:')),
            request.registry.settings['site.uid'], clear=True)
        html += form.grid_item(
            translate(_('Application version:')), request.registry['version'],
            clear=True)
        html += form.grid_item(
            translate(_('Configuration version:')),
            request.registry.settings.get('site.version'), clear=True)

        html += HTML.h3(translate(_('Database')))
        html += form.grid_item(
            translate(_('Name:')),
            basename(request.dbsession.bind.url.database), clear=True)
        html += form.grid_item(
            translate(_('Type:')), request.dbsession.bind.name, clear=True)
        html += form.grid_item(
            translate(_('Last loading:')),
            request.registry['settings']['populate'], clear=True)

        html += HTML.h3(translate(_('Resources')))
        html += form.grid_item(
            translate(_('Log:')),
            translate(_('active')) if request.registry.get('log_activity')
            else translate(_('inactive')), clear=True)
        html += form.grid_item(
            translate(_('Languages:')), ', '.join(settings_get_list(
                request.registry.settings, 'languages', ['en'])),
            clear=True)
        lang = request.session.get('lang', 'en')
        themes = sorted([
            request.registry['themes'][k]['name'].get(lang, k)
            for k in request.registry['themes']])
        html += form.grid_item(
            translate(_('Themes:')), ', '.join(themes), clear=True)

        return html

    # -------------------------------------------------------------------------
    @classmethod
    def settings_schema(cls, request):
        """Return a Colander schema to edit settings.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :rtype: tuple
        :return:
            A tuple such as ``(schema, defaults)``.
        """
        # Site
        schema = colander.SchemaNode(colander.Mapping())
        schema.add(colander.SchemaNode(
            colander.String(), name='title',
            validator=colander.Length(max=LABEL_LEN)))
        schema.add(colander.SchemaNode(
            colander.String(), name='email',
            validator=colander.All(
                colander.Length(max=EMAIL_LEN), colander.Email())))

        # Default values
        schema.add(colander.SchemaNode(
            colander.String(), name='language',
            validator=colander.OneOf(settings_get_list(
                request.registry.settings, 'languages', ['en']))))
        schema.add(colander.SchemaNode(
            colander.Integer(), name='password-min-length',
            validator=colander.Range(min=4)))
        schema.add(colander.SchemaNode(
            colander.Integer(), name='remember-me',
            validator=colander.Range(min=3600)))
        schema.add(colander.SchemaNode(
            colander.Integer(), name='page-size',
            validator=colander.OneOf(PAGE_SIZES[1:-1])))
        schema.add(colander.SchemaNode(
            colander.Integer(), name='download-max-size',
            validator=colander.Range(min=0)))
        schema.add(colander.SchemaNode(
            colander.Integer(), name='clipboard-size',
            validator=colander.Range(min=1)))
        if len(request.registry['themes']) > 1:
            schema.add(colander.SchemaNode(
                colander.String(), name='theme',
                validator=colander.OneOf(request.registry['themes'])))

        return schema, request.registry['settings']

    # -------------------------------------------------------------------------
    @classmethod
    def tab4edit(cls, request, tab_index, form):
        """Generate the tab content for edition.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :param int tab_index:
            Index of the tab.
        :type  form: .lib.form.Form
        :param form:
            Current form object.
        :rtype: webhelpers2.html.literal
        """
        if tab_index == 0:
            return cls._tab4edit_parameters(request, form)
        if tab_index == 1:
            return cls._tab4view_information(request, form, True)
        return ''

    # -------------------------------------------------------------------------
    @classmethod
    def _tab4edit_parameters(cls, request, form):
        """Generate the parameters tab for edition.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :type  form: .lib.form.Form
        :param form:
            Current form object.
        :rtype: webhelpers2.html.literal
        """
        translate = request.localizer.translate
        html = HTML.h3(translate(_('Site')))
        html += form.grid_text(
            'title', translate(_('Title:')), maxlength=LABEL_LEN,
            required=True, clear=True)
        html += form.grid_text(
            'email', translate(_('Email:')), maxlength=EMAIL_LEN,
            required=True, clear=True)

        html += HTML.h3(translate(_('Default values')))
        html += form.grid_select(
            'language', translate(_('Language:')),
            sorted(settings_get_list(
                request.registry.settings, 'languages', ['en'])),
            required=True, clear=True)
        html += form.grid_text(
            'password-min-length', translate(_('Password length:')),
            maxlength=2, required=True, clear=True)
        html += form.grid_text(
            'remember-me', translate(_('Remember me:')),
            maxlength=8, required=True, clear=True)
        html += form.grid_select(
            'page-size', translate(_('Lines per page:')), PAGE_SIZES[:-1],
            required=True, clear=True)
        html += form.grid_text(
            'download-max-size', translate(_('Maximum size of download:')),
            maxlength=10, required=True, clear=True)
        html += form.grid_text(
            'clipboard-size', translate(_('Clipboard size:')),
            maxlength=2, required=True, clear=True)
        if len(request.registry['themes']) > 1:
            lang = request.session.get('lang', 'en')
            themes = [(i, j['name'].get(lang, i))
                      for i, j in request.registry['themes'].items()]
            html += form.grid_select(
                'theme', translate(_('Theme:')),
                sorted(themes, key=lambda k: k[1]), clear=True)

        return literal(html)
