"""Localization management."""

from sys import exit as sys_exit
from os.path import dirname, join
from locale import getdefaultlocale
from json import dumps, loads

import colander

from pyramid.i18n import TranslationStringFactory, make_localizer
from pyramid.exceptions import ConfigurationError

from .config import settings_get_list


_ = TranslationStringFactory('chrysalio')


# =============================================================================
def locale_negotiator(request):
    """Locale negotiator to figure out the language to use.

    :type  request: pyramid.request.Request
    :param request:
        Current request.
    :rtype: str
    """
    if request.session.get('lang'):
        return request.session['lang']
    return request.accept_language.lookup(
        settings_get_list(
            request.registry.settings, 'languages', ['en']),
        default_tag=request.registry['settings']['language'])


# =============================================================================
def add_translation_dirs(configurator, package):
    """Add one or more translation directory paths to the current configuration
    state according to settings and package name.

    :type  configurator: pyramid.config.Configurator
    :param configurator:
        Object used to do configuration declaration within the application.
    :param str package:
        Name of the calling package.
    """
    dirs = ['chrysalio:Locale', 'colander:locale']
    if package != 'chrysalio':
        dirs.insert(0, ('{0}:Locale'.format(package)))
    if configurator.get_settings().get('translation_dirs'):
        dirs = settings_get_list(
            configurator.get_settings(), 'translation_dirs') + dirs
    try:
        configurator.add_translation_dirs(*dirs)
    except (ImportError, ConfigurationError) as error:
        sys_exit('*** Translation directories: {0}'.format(error))


# =============================================================================
def translate(text, lang=None, request=None):
    """Return ``text`` translated.

    :param str text:
        Text to translate.
    :param str lang: (optional)
        Language to use.
    :type  request: pyramid.request.Request
    :param request: (optional)
        Current request to find the current language.
    :rtype: str
    """
    if lang is None and request is not None:
        lang = request.session.get('lang') \
            or request.locale_name or request.registry['settings']['language']
    return make_localizer(
        lang or getdefaultlocale()[0] or 'en',
        (join(dirname(__file__), '..', 'Locale'),)).translate(text)


# =============================================================================
def translate_field(request, i18n_fields, default=''):
    """Return the best translation according to user language.

    :type  request: pyramid.request.Request
    :param request:
        Current request.
    :param dict i18n_fields:
        Dictionary of avalaible translations.
    :param str default:
        Default label.
    :rtype: str
    """
    if not i18n_fields:
        return ''
    return \
        'lang' in request.session and i18n_fields.get(request.session['lang'])\
        or i18n_fields.get(request.locale_name) \
        or i18n_fields.get(request.registry['settings']['language']) \
        or i18n_fields.get(request.registry.settings.get(
            'pyramid.default_locale_name', 'en')) \
        or i18n_fields.get('en') or default


# =============================================================================
def record_format_i18n(record):
    """Update record by converting label and description entries into a
    dictionary with languages as key.

    :param dict record:
        Dictionary to process.
    :rtype: bool
    :return:
        ``True`` if a label has been found.
    """
    labels = loads(record['i18n_label']) if 'i18n_label' in record else {}
    descriptions = record.get('i18n_description', {})

    for k in tuple(record.keys()):
        if k.startswith('label_'):
            labels[k[6:]] = record[k]
            del record[k]
        elif k.startswith('description_'):
            descriptions[k[12:]] = record[k]
            del record[k]

    if not labels:
        return False

    record['i18n_label'] = dumps(labels, ensure_ascii=False)
    if descriptions:
        record['i18n_description'] = descriptions
    return True


# =============================================================================
def view_i18n_labels(
        request, form, dbitem, with_label=True, with_description=True):
    """Return HTML input to edit i18n labels.

    :type  request: pyramid.request.Request
    :param request:
        Current request.
    :param dbitem:
        Current SqlAlchemy object.
    :param bool with_label: (default=True)
       If ``True``, produce input fields for labels.
    :param bool with_description: (default=True)
       If ``True``, produce input fields for descriptions.
    :rtype: webhelpers2.html.literal
    """
    html = ''
    local_translate = request.localizer.translate

    if with_label and dbitem.i18n_label:
        labels = loads(dbitem.i18n_label)
        for lang in sorted(labels):
            html += form.grid_item(
                local_translate(_('Label (${l}):', {'l': lang})), labels[lang],
                clear=True)

    if with_description and dbitem.i18n_description:
        if dbitem.i18n_description:
            for lang in sorted(dbitem.i18n_description):
                html += form.grid_item(
                    local_translate(_('Description (${l}):', {'l': lang})),
                    dbitem.i18n_description[lang], clear=True)

    return html


# =============================================================================
def schema_i18n_labels(request, schema, label_len=0, description_len=0,
                       prefix='', required=True):
    """Update the Colander schema with fields for label ans, possibly, for
    descriptions of each available language.

    :type  request: pyramid.request.Request
    :param request:
        Current request.
    :type  schema: colander.SchemaNode
    :param schema:
       Current Colander schema.
    :param int label_len: (optional)
       Maximum length of label. If ``0``, no field is produced.
    :param int description_len: (optional)
       Maximum length of description. If ``0``, no field is produced.
    :param str prefix: (optional)
       A prefix for the name of field.
    :param bool required: (default=True)
       ``True`` if the label in default language is required.
    """
    default_lang = request.registry['settings']['language']

    # Label
    if label_len:
        for lang in sorted(settings_get_list(
                request.registry.settings, 'languages', ('en',))):
            if lang == default_lang and required:
                schema.add(colander.SchemaNode(
                    colander.String(),
                    name='{0}label_{1}'.format(prefix, lang),
                    validator=colander.Length(max=label_len)))
            else:
                schema.add(colander.SchemaNode(
                    colander.String(),
                    name='{0}label_{1}'.format(prefix, lang),
                    validator=colander.Length(max=label_len), missing=None))

    # Description
    if description_len:
        for lang in sorted(settings_get_list(
                request.registry.settings, 'languages', ('en',))):
            schema.add(colander.SchemaNode(
                colander.String(),
                name='{0}description_{1}'.format(prefix, lang),
                validator=colander.Length(max=description_len), missing=None))


# =============================================================================
def defaults_i18n_labels(
        dbitem, with_label=True, with_description=True, prefix=''):
    """Return a dictionary of default values for labels.

    :param dbitem:
        Current SqlAlchemy object.
    :param bool with_label: (default=True)
       If ``True``, produce input fields for labels.
    :param bool with_description: (default=True)
       If ``True``, produce input fields for descriptions.
    :param str prefix: (optional)
       A prefix for the name of field.
    """
    defaults = {}

    if with_label and dbitem.i18n_label:
        labels = loads(dbitem.i18n_label)
        for lang in labels:
            defaults['{0}label_{1}'.format(prefix, lang)] = labels[lang]

    if with_description and dbitem.i18n_description:
        for lang in dbitem.i18n_description:
            defaults['{0}description_{1}'.format(prefix, lang)] = \
                dbitem.i18n_description[lang]

    return defaults


# =============================================================================
def edit_i18n_labels(
        request, form, label_len=0, description_len=0, prefix=''):
    """Return HTML input to edit i18n labels.

    :type  request: pyramid.request.Request
    :param request:
        Current request.
    :param int label_len: (optional)
       Maximum length of label. If ``0``, no field is produced.
    :param int description_len: (optional)
       Maximum length of description. If ``0``, no field is produced.
    :param str prefix: (optional)
       A prefix for the name of field.
    :rtype: webhelpers2.html.literal
    """
    html = ''
    default_lang = request.registry['settings']['language']
    local_translate = request.localizer.translate

    # Label
    if label_len:
        for lang in sorted(settings_get_list(
                request.registry.settings, 'languages', ('en',))):
            html += form.grid_text(
                '{0}label_{1}'.format(prefix, lang),
                local_translate(_('Label (${l}):', {'l': lang})),
                required=lang == default_lang,
                maxlength=label_len, clear=True)

    # Description
    if description_len:
        for lang in sorted(settings_get_list(
                request.registry.settings, 'languages', ('en',))):
            html += form.grid_text(
                '{0}description_{1}'.format(prefix, lang),
                local_translate(_('Description (${l}):', {'l': lang})),
                maxlength=description_len, clear=True)

    return html
