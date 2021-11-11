# -*- coding: utf-8 -*-
"""SQLAlchemy-powered model definitions for modules."""

from pkg_resources import get_distribution

from sqlalchemy import Column, String, Boolean
from webhelpers2.html import literal
import colander

from ...lib.i18n import _
from ...includes.themes import theme_static_prefix
from ...models import DBDeclarativeClass, MODULE_LEN


MODULES_SUFFIX = 'ciomod'


# =============================================================================
class DBModule(DBDeclarativeClass):
    """SQLAlchemy-powered module class."""

    __tablename__ = 'modules'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    module_id = Column(String(MODULE_LEN), primary_key=True)
    inactive = Column(Boolean(name='inactive'), default=True)

    suffix = MODULES_SUFFIX

    # -------------------------------------------------------------------------
    @classmethod
    def table4view(cls, request):
        """Generate the modules table.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :rtype: webhelpers2.html.literal
        """
        translate = request.localizer.translate
        if 'modules' not in request.registry or \
           not request.registry['modules']:
            return translate(_('No module.'))
        names = {k: translate(request.registry['modules'][k].name)
                 for k in request.registry['modules']}

        html = '<table>\n<thead>\n'\
            '<tr><th>{active}</th><th>{name}</th><th>{version}</th>'\
            '<th>{depends}</th><th class="cioActions">{actions}</th></tr>\n'\
            '</thead>\n<tbody>\n'.format(
                active=translate(_('Active')), name=translate(_('Name')),
                version=translate(_('Version')),
                depends=translate(_('Dependencies')),
                actions=translate(_('Actions')))
        for module_id in request.registry['modules']:
            module = request.registry['modules'][module_id]
            dependencies = ', '.join(
                [names[k] for k in module.dependencies if k in names]) \
                if module.dependencies else ''
            actions = module.configuration_route(request) or ''
            if actions:
                actions = '<a href="{0}">'\
                    '<img src="{1}{2}" alt="configuration"/></a>'.format(
                        actions, theme_static_prefix(request),
                        '/images/action_configure.png')
            html += '<tr><td>{active}</td><td title="{id}">{name}</td>'\
                '<td>{version}</td><td>{depends}</td>'\
                '<td class="cioActions">{actions}</td></tr>\n'.format(
                    active='' if module_id in request.registry['modules_off']
                    else '✔', id=module_id, name=translate(module.name),
                    version=get_distribution(module_id.split('.')[0]).version,
                    depends=dependencies, actions=actions)
        html += '</tbody>\n</table>\n'

        return literal(html)

    # -------------------------------------------------------------------------
    @classmethod
    def settings_schema(cls, request):
        """Return a Colander schema to edit modules.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :rtype: tuple
        :return:
            A tuple such as ``(schema, defaults)``.
        """
        schema = colander.SchemaNode(colander.Mapping())
        for module_id in request.registry['modules']:
            schema.add(colander.SchemaNode(
                colander.Boolean(), name=module_id, missing=False))

        # Defaults
        defaults = {}
        for module_id in request.registry['modules']:
            if module_id not in request.registry['modules_off']:
                defaults[module_id] = True

        return schema, defaults

    # -------------------------------------------------------------------------
    @classmethod
    def table4edit(cls, request, form):
        """Generate the modules table for edition.

        :type  request: pyramid.request.Request
        :param request:
            Current request.
        :type  form: .lib.form.Form
        :param form:
            Current form object.
        :rtype: webhelpers2.html.literal
        """
        translate = request.localizer.translate
        if 'modules' not in request.registry or \
           not request.registry['modules']:
            return translate(_('No module.'))
        names = {k: translate(request.registry['modules'][k].name)
                 for k in request.registry['modules']}

        html = '<table>\n<thead>\n'\
            '<tr><th>{selected}</th><th>{name}</th><th>{version}</th>'\
            '<th>{depends}</th></tr>\n</thead>\n<tbody>\n'.format(
                selected=translate(_('Active')), name=translate(_('Name')),
                version=translate(_('Version')),
                depends=translate(_('Dependencies')))
        for module_id in request.registry['modules']:
            module = request.registry['modules'][module_id]
            dependencies = ', '.join(
                [names[k] for k in module.dependencies if k in names]) \
                if module.dependencies else ''
            html += '<tr><td>{selected}</td>'\
                '<td><label for="{cid}" title="{id}">{name}</label></td>'\
                '<td>{version}</td><td>{depends}</td></tr>\n'.format(
                    selected=form.custom_checkbox(module_id),
                    name=translate(module.name),
                    cid=module_id.replace('.', ''), id=module_id,
                    version=get_distribution(module_id.split('.')[0]).version,
                    depends=dependencies)
        html += '</tbody>\n</table>\n'

        return literal(html)
