"""Form validation and rendering library."""

from re import sub as re_sub

import colander
from webhelpers2.html import tags, HTML, literal

from pyramid.csrf import get_csrf_token, new_csrf_token

from .i18n import _


# =============================================================================
def get_action(request, silent=False):
    """Return a tuple such as ``(action, items)`` where ``action`` is a
    string such as ``<act><?|!><item_id>`` and ``items`` is a list of
    selected items in a list form.

    :type  request: pyramid.request.Request
    :param request:
        Current request.
    :param bool silent: (default=False)
        If ``True``, no alert emitted.
    :rtype: tuple
    :return: (tuple)
        A tuple such as ``(action, items)``.

    Each submit button returns a string such as ``<act><?|!><item_id>.x`` where
    ``<item_id>`` is the item identifier or ``#`` for all selected items,
    ``<?|!>`` means respectively *confirm* or *proceed* and ``<act>`` is the
    action to do.

    Checkbox inputs return string such as ``#<item_id>``.

    For instance, ``del!#`` and ``['#user1', '#user2']`` means "delete
    ``user1`` and ``user2``". ``del!user1`` means "delete ``user1`` and only
    this one".
    """
    action = ''
    items = []
    for param in request.POST:
        if not isinstance(param, str):
            param = param.decode('utf8')  # pragma: nocover
        if param[0] == '#':
            items.append(param[1:])
        elif param[-2:] == '.x':
            if param[-3:-2] == '#':
                action = param[0:-2]
            else:
                return param[0:-2], (param[4:-2],)
    if '#' in action and not items:
        if not silent:
            request.session.flash(_('Select items!'), 'alert')
        action = ''
    return action, items


# =============================================================================
class SameAs(object):
    # pylint: disable = too-few-public-methods
    """This class implements a ``colander`` validator to check if to fields are
    identical.

    :type  request: pyramid.request.Request
    :param request:
        Current request.
    :param str reference:
        Name of the field to compare with.
    :type  message: :class:`str` or :class:`~pyramid.i18n.TranslationString`
    :param message: (optional)
        Error message.
    """

    # -------------------------------------------------------------------------
    def __init__(self, request, reference, message=None):
        """Constructor method."""
        self._request = request
        self._reference = reference
        self._message = message or _('The two fields are not identical.')

    # -------------------------------------------------------------------------
    def __call__(self, node, value):
        """This method raises a :class:`colander.Invalid` instance as an
        exception value is not same as ``self.reference``.

        :type node: colander.SchemaNode
        :type value: cstruct
        """
        if self._request.POST.get(self._reference) != value:
            raise colander.Invalid(node, self._message)


# =============================================================================
def button(url, label='', src=None, title=None, class_='cioButton'):
    """Output a link on a label and an image with a button aspect.

    :param str url:
        Target URL.
    :param str label: (optional)
        Label for roll over and ``alt``.
    :param str src: (optional)
        Image path.
    :param str title: (optional)
        Label for roll over.
    :param str class_: (default='cioButton')
        The class attribute.
    :rtype: str
        HTML tag.
    """
    if class_ == 'cioButton' and not label and src:
        class_ = None
    return literal('<a href="{0}"{1}{2}>{3}{4}</a> '.format(
        literal.escape(url), ' title="{0}"'.format(title) if title else '',
        ' class="{0}"'.format(class_) if class_ else '',
        src and '<img src="%s" alt="%s"/>' % (src, label or title) or '',
        label))


# =============================================================================
def grid_item(name, label, content, required=False, hint=None, error=None,
              title=None, clear=False, class_=None):
    """Display an item with label, hint and error message.

    :param str name:
        Input ID.
    :param str label:
        Label.
    :param str content:
        HTML content.
    :param bool required: (default=False)
        Indicate if this field is required.
    :param str hint: (optional)
        Help message.
    :param str error: (optional)
        Error message.
    :param str title: (optional)
        Title for the hover effect.
    :param bool clear: (default=False)
        If ``True``, add a ``<div class="cioClear"/>`` at the end.
    :param str class_: (optional)
        The class attribute.
    :rtype: str

    This ouputs a structure such as:

    .. code-block:: html

        <div class="[class_]">
          <label for="[name]"><strong>[label]<span>*</span></strong></label>
          <tag title="[title]">
            [content]
            <em> [hint]</em>
            <strong> [form.error(name)]</strong>
          </tag>
          <div class="cioClear"></div>
        </div>
    """
    # pylint: disable = too-many-arguments
    if not content:
        return ''
    if error:
        class_ = '{0} cioError'.format(class_) if class_ else 'cioError'
    return literal(
        '<div{class_}>'
        '<label{name}><strong>{label}{required}</strong></label>'
        '<div{title}>{content}{hint}{error}</div>{clear}</div>'.format(
            class_=' class="{0}"'.format(class_) if class_ else '',
            name=' for="{0}"'.format(name.replace(':', '')) if name else '',
            label=label or '',
            required=HTML.span('*') if required else '',
            title=' title="{0}"'.format(title) if title else '',
            content=content,
            hint=HTML.em(' {0}'.format(hint)) if hint else '',
            error=HTML.strong(' {0}'.format(error)) if error else '',
            clear=clear and '<div class="cioClear"></div>' or ''))


# =============================================================================
class Form(object):
    """Form validation class."""
    # pylint: disable = too-many-public-methods

    # -------------------------------------------------------------------------
    def __init__(self, request, schema=None, defaults=None, obj=None,
                 force_defaults=False):
        """Constructor method."""
        # pylint: disable = too-many-arguments
        self.values = defaults \
            if defaults and (not request.POST or force_defaults) else {}
        self._request = request
        self._schema = schema
        self._errors = {}
        self._special = [[], []]
        self._validated = False
        if obj is not None and schema is not None and not request.POST:
            for field in [k.name for k in schema]:
                if hasattr(obj, field):
                    self.values[field] = getattr(obj, field)

    # -------------------------------------------------------------------------
    def validate(self, obj=None):
        """Check if the form is validated.

        :param object obj: (optional)
            Object to fill.
        :rtype: bool
        :return:
             ``True`` if validated.
        """
        # Something to do?
        if not self._request.POST:
            return False
        if self._validated:
            return not self._errors

        # Schema validation
        params = dict(self._request.POST.items())
        if self._schema:
            try:
                self.values = self._schema.deserialize(params)
            except colander.Invalid as err:
                self._errors = {}
                for child in err.children:
                    self._errors[child.node.name] = child.messages()
        else:
            self.values.update(params)

        # Fill object
        if obj is not None and not self._errors:
            for field in self.values:
                if hasattr(obj, field):
                    setattr(obj, field, self.values[field])

        self._validated = True
        return len(self._errors) == 0

    # -------------------------------------------------------------------------
    def has_error(self, name=None):
        """Return ``True`` if field ``name`` has an error.

        :param str name: (optional)
            Input ID.
        :rtype: bool
        """
        return bool(name is None and self._errors) or name in self._errors

    # -------------------------------------------------------------------------
    def set_error(self, name, message):
        """Set an error message for field ``name``.

        :param str name:
            Input ID.
        :param str message:
            Error message.
        """
        if name in self._errors:
            self._errors[name].append(message)
        else:
            self._errors[name] = [message]

    # -------------------------------------------------------------------------
    def error(self, name):
        """Return error message for field ``name``.

        :param str name:
            Input ID.
        :rtype: str
        :return:
            Translated error message.
        """
        if name not in self._errors:
            return ''
        return ' ; '.join([self._request.localizer.translate(error)
                           for error in self._errors[name]])

    # -------------------------------------------------------------------------
    def static(self, name):
        """The field ``name`` will not be updated by the form.

        :param str name:
            Name of field to set static.
        """
        if name not in self._special[0]:
            self._special[0].append(name)

    # -------------------------------------------------------------------------
    def forget(self, prefix):
        """Fields beginning by ``prefix`` are forgotten when the page is
        refreshed.

        :param str prefix:
            Prefix to select fields.
        """
        if prefix not in self._special[1]:
            self._special[1].append(prefix)

    # -------------------------------------------------------------------------
    @classmethod
    def make_safe_id(cls, name):
        """Make a string safe for including in an id attribute

        :param str name:
            String to transform.
        :rtype: str
        """
        return re_sub(r'(?!-)\W', '', re_sub(
            r'\s', '_', name.replace('?', '0').replace('!', '1'), )).lower()

    # -------------------------------------------------------------------------
    def begin(self, url=None, multipart=False, **attrs):
        """Ouput the ``<form>`` tag.

        :param str url: (optional)
            URL to submit form, by default, the current URL.
        :param bool multipart: (default=False)
            If set to ``True``, the enctype is set to ``multipart/form-data``.
        :param dict attrs:
            Keyworded arguments for ``webhelpers2.html.tags`` object.
        :rtype: str
        :return:
            HTML tag.
        """
        token = get_csrf_token(self._request) or new_csrf_token(self._request)
        html = tags.form(
            url or self._request.path_qs, 'post', multipart, **attrs)
        html += HTML.div(self.hidden('csrf_token', token), class_="cioHidden")
        return html

    # -------------------------------------------------------------------------
    @classmethod
    def end(cls):
        """Ouput the ``</form>`` tag."""
        return tags.end_form()

    # -------------------------------------------------------------------------
    @classmethod
    def submit(cls, name, label=None, class_='cioButton', **attrs):
        """Output a submit button with the label as the caption.

        :param str name:
            Input ID.
        :param str label: (optional)
            Button caption.
        :param str class_: (default='cioButton')
            The class attribute.
        :param dict attrs:
            Keyworded arguments for ``webhelpers2.html.tags`` object.
        :rtype: str
        :return:
            HTML tag.
        """
        return tags.submit(
            name, label, cls.make_safe_id(name), class_=class_, **attrs)

    # -------------------------------------------------------------------------
    @classmethod
    def submit_image(cls, name, label, src, **attrs):
        """Output an image submit button.

        :param str name:
            Input ID.
        :param str label:
            Label for roll over and ``alt``.
        :param str src:
            Image path.
        :param dict attrs:
            Keyworded arguments for ``webhelpers2.html.tags`` object.
        :rtype: str
        :return:
            HTML tag.
        """
        return HTML.tag(
            'input', type='image', name=name, id=cls.make_safe_id(name),
            src=src, title=label or name, alt=label or name, **attrs)

    # -------------------------------------------------------------------------
    @classmethod
    def submit_cancel(cls, label, src, **attrs):
        """Output a cancel submit button.

        :param str label:
            Label for roll over and ``alt``.
        :param str src:
            Image path.
        :param dict attrs:
            Keyworded arguments for ``webhelpers2.html.tags`` object.
        :rtype: str
        :return:
            HTML tag.
        """
        return HTML.tag(
            'input', type='image', name='ccl!', id='ccl', src=src, title=label,
            alt=label, **attrs)

    # -------------------------------------------------------------------------
    @classmethod
    def button(cls, url, label='', src=None, title=None, class_='cioButton'):
        """Output a link on a label and an image with a button aspect.

        See :func:`button`.
        """
        return button(url, label, src, title, class_)

    # -------------------------------------------------------------------------
    @classmethod
    def default_button(cls, name):
        """Create an invisible button to catch the Enter signal for the input
        submit we want to be the default one.

        :param str name:
            ID of the input submit to activate.
        """
        return literal(
            '<button type="submit" name="{0}" class="cioDefaultButton">'
            '</button>'.format(name))

    # -------------------------------------------------------------------------
    @classmethod
    def grid_item(cls, label, content, required=False, hint=None, error=None,
                  title=None, clear=False, class_='cioFormItem'):
        """Output an item with label, hint and error message.

        See :func:`grid_item`.
        """
        # pylint: disable = too-many-arguments
        return grid_item(
            None, label, content, required, hint, error, title, clear,
            class_)

    # -------------------------------------------------------------------------
    def hidden(self, name, value=None, **attrs):
        """Output a hidden field.

        :param str name:
            Input ID.
        :param str value: (optional)
            Hidden value.
        :param dict attrs:
            Keyworded arguments for ``webhelpers2.html.tags`` object.
        :rtype: str
        :return:
            HTML tag.
        """
        return tags.hidden(name, self._value(name, value), **attrs)

    # -------------------------------------------------------------------------
    def text(self, name, value=None, **attrs):
        """Output a standard text field.

        :param str name:
            Input ID.
        :param str value: (optional)
            Default value.
        :param dict attrs:
            Keyworded arguments for ``webhelpers2.html.tags`` object.
        :rtype: str
        :return:
             HTML tag.
        """
        return tags.text(name, self._value(name, value), **attrs)

    # -------------------------------------------------------------------------
    def password(self, name, value=None, **attrs):
        """Output a password field.

        This method takes the same options as text().
        """
        return tags.password(name, self._value(name, value), **attrs)

    # -------------------------------------------------------------------------
    def checkbox(self, name, value='1', checked=False, autosubmit=False,
                 **attrs):
        """Output a check box.

        :param str name:
            Input ID.
        :param str value: (default='1')
            The value to return to the application if the box is checked.
        :param bool checked: (default=False)
            ``True`` if the box should be initially checked.
        :param bool autosubmit: (default=False)
            If ``True``, it adds ``class="cioAutoSubmit"`` attribute.
        :param dict attrs:
            Keyworded arguments for ``webhelpers2.html.tags`` object.
        :rtype: str
        :return:
            HTML tag.
        """
        if autosubmit:
            attrs['class_'] = '{0} cioAutoSubmit'.format(attrs['class_']) \
                if 'class_' in attrs else 'cioAutoSubmit'
        return tags.checkbox(
            name, value, checked or self._value(name), **attrs)

    # -------------------------------------------------------------------------
    def custom_checkbox(
            self, name, value='1', checked=False, autosubmit=False,
            class_=None, **attrs):
        """Output a check box followed by an empty label to customize the
        aspect of the box.

        :param str name:
            Input ID.
        :param str value: (default='1')
            The value to return to the application if the box is checked.
        :param bool checked: (default=False)
            ``True`` if the box should be initially checked.
        :param bool autosubmit: (default=False)
            If ``True``, it adds ``class="cioAutoSubmit"`` attribute.
        :param str class_: (default='cioCustomCheckbox')
            The class attribute.
        :param dict attrs:
            Keyworded arguments for ``webhelpers2.html.tags`` object.
        :rtype: str
        :return:
            HTML tag.
        """
        if class_ is None:
            class_ = 'cioCustomCheckbox'
        attrs['class_'] = class_
        if autosubmit:
            attrs['class_'] = '{0} cioAutoSubmit'.format(attrs['class_'])
        return literal('{0}{1}'.format(
            tags.checkbox(name, value, checked or self._value(name), **attrs),
            '<label for="{0}" class="{1}"> </label>'.format(
                self.make_safe_id(name), class_)))

    # -------------------------------------------------------------------------
    def radio(self, name, value, checked=False, autosubmit=False, **attrs):
        """Output a radio button.

        :param str name:
            Input ID.
        :param str value:
            The value to return to the application if the radio is checked.
        :param bool checked: (default=False)
            ``True`` if the box should be initially checked.
        :param bool autosubmit: (default=False)
            If ``True``, it adds ``class="cioAutoSubmit"`` attribute.
        :param dict attrs:
            Keyworded arguments for ``webhelpers2.html.tags`` object.
        :rtype: str
        :return:
            HTML tag.
        """
        if autosubmit:
            attrs['class_'] = '{0} cioAutoSubmit'.format(attrs['class_']) \
                if 'class_' in attrs else 'cioAutoSubmit'
        return tags.radio(
            name, value, checked or value == self._value(name), **attrs)

    # -------------------------------------------------------------------------
    def select(self, name, selected_values, options, autosubmit=False,
               **attrs):
        """Output a dropdown selection box.

        :param str name:
            Input ID.
        :type  selected_value: :class:`str` or :class:`list`
        :param selected_value:
            A string or list of strings or integers giving the value(s) that
            should be preselected.
        :type options:
            (list of :class:`str`, :class:`int` or ``(value, label)`` pairs)
        :param options:
            The label will be shown on the form; the option will be returned to
            the application if that option is chosen. If you pass a ``string``
            or ``int`` instead of a ``2-tuple``, it will be used for both the
            value and the label.
        :param bool autosubmit: (default=False)
            If ``True``, it adds ``class="cioAutoSubmit"`` attribute.
        :param dict attrs:
            Keyworded arguments for ``webhelpers2.html.tags`` object.
        :rtype: str
        :return:
            HTML tag.
        """
        if not options:
            return ''
        opts = []
        translate = self._request.localizer.translate
        for opt in options:
            if isinstance(opt, tuple):
                opts.append(
                    tags.Option(translate(opt[1]), '{0}'.format(opt[0])))
            else:
                opts.append(tags.Option('{0}'.format(opt)))
        if autosubmit:
            attrs['class_'] = '{0} cioAutoSubmit'.format(attrs['class_']) \
                if 'class_' in attrs else 'cioAutoSubmit'
        return tags.select(
            name, '{0}'.format(self._value(name, selected_values)),
            tags.Options(opts), **attrs)

    # -------------------------------------------------------------------------
    def upload(self, name, value=None, **attrs):
        """Output a file upload field.

        :param str name:
            Input ID.
        :param str value: (optional)
            Default value.
        :param dict attrs:
            Keyworded arguments for ``webhelpers2.html.tags`` object.
        :rtype: str
        :return:
            HTML tag.
        """
        return tags.file(name, self._value(name, value) or None, **attrs)

    # -------------------------------------------------------------------------
    def textarea(self, name, content='', **attrs):
        """Output a text input area.

        :param str name:
            Input ID.
        :param str content: (optional)
            Default value.
        :param dict attrs:
            Keyworded arguments for ``webhelpers2.html.tags`` object.
        :rtype: str
        :return:
            HTML tag.
        """
        return tags.textarea(name, self._value(name, content), **attrs)

    # -------------------------------------------------------------------------
    def grid_text(self, name, label, required=False, hint=None, title=None,
                  clear=False, class_='cioFormItem', **attrs):
        """Output a standard text field in a CSS grid layout.

        :param str name:
            Input ID.
        :param str label:
            Label.
        :param bool required: (default=False)
            Indicate if this field is required.
        :param str hint: (optional)
            Help message.
        :param str title: (optional)
            Title for the hover effect.
        :param bool clear: (default=False)
            If ``True``, add a ``<div class="cioClear"/>`` at the end.
        :param str class_: (default='cioFormItem')
            The class attribute.
        :param dict attrs:
            Keyworded arguments for ``webhelpers2.html.tags`` object.
        :rtype: str
        :return:
            Output a grid layout.
        """
        # pylint: disable = too-many-arguments
        return grid_item(
            name, label, self.text(name, **attrs), required, hint,
            self.error(name), title=title, clear=clear, class_=class_)

    # -------------------------------------------------------------------------
    def grid_password(self, name, label, required=False, hint=None, title=None,
                      clear=False, class_='cioFormItem', **attrs):
        """Output a password field in a CSS grid layout.

        This method takes the same options as grid_text().
        """
        # pylint: disable = too-many-arguments
        return grid_item(
            name, label, self.password(name, **attrs), required, hint,
            self.error(name), title=title, clear=clear, class_=class_)

    # -------------------------------------------------------------------------
    def grid_checkbox(self, name, label, required=False, hint=None, title=None,
                      clear=False, class_='cioFormItem', **attrs):
        """Output a check box in a CSS grid layout.

        :param str name:
            Input ID.
        :param str label:
            Label.
        :param bool required: (default=False)
            Indicate if this field is required.
        :param str hint: (optional)
            Help message.
        :param str title: (optional)
            Title for the hover effect.
        :param bool clear: (default=False)
            If ``True``, add a ``<div class="cioClear"/>`` at the end.
        :param str class_: (default='cioFormItem')
            The class attribute.
        :param dict attrs:
            Keyworded arguments for ``webhelpers2.html.tags`` object.
        :rtype: str
        :return:
            Output a grid layout.
        """
        # pylint: disable = too-many-arguments
        return grid_item(
            name, label, self.checkbox(name, **attrs), required, hint,
            self.error(name), title=title, clear=clear, class_=class_)

    # -------------------------------------------------------------------------
    def grid_custom_checkbox(
            self, name, label, required=False, hint=None, title=None,
            clear=False, class_='cioFormItem', **attrs):
        """Output a custom check box in a CSS grid layout.

        :param str name:
            Input ID.
        :param str label:
            Label.
        :param bool required: (default=False)
            Indicate if this field is required.
        :param str hint: (optional)
            Help message.
        :param str title: (optional)
            Title for the hover effect.
        :param bool clear: (default=False)
            If ``True``, add a ``<div class="cioClear"/>`` at the end.
        :param str class_: (default='cioFormItem')
            The class attribute.
        :param dict attrs:
            Keyworded arguments for ``webhelpers2.html.tags`` object.
        :rtype: str
        :return:
            Output a grid layout.
        """
        # pylint: disable = too-many-arguments
        return grid_item(
            name, label, self.custom_checkbox(name, **attrs), required, hint,
            self.error(name), title=title, clear=clear, class_=class_)

    # -------------------------------------------------------------------------
    def grid_select(self, name, label, options, autosubmit=False,
                    required=False, hint=None, title=None, clear=False,
                    class_='cioFormItem', **attrs):
        """Output a dropdown selection box in a CSS grid layout.

        :param str name:
            Input ID.
        :param str label:
            Label.
        :type options:
            (list of :class:`str`, :class:`int` or ``(value, label)`` pairs)
        :param options:
            Values in the dropdown list.
        :param bool autosubmit: (default=False)
            If ``True``, it adds ``onchange="submit()"`` attribute.
        :param bool required: (default=False)
            Indicate if this field is required.
        :param str hint: (optional)
            Help message.
        :param str title: (optional)
            Title for the hover effect.
        :param bool clear: (default=False)
            If ``True``, add a ``<div class="cioClear"/>`` at the end.
        :param str class_: (default='cioFormItem')
            The class attribute.
        :param dict attrs:
            Keyworded arguments for ``webhelpers2.html.tags`` object.
        :rtype: str
        :return:
            Output a grid layout.
        """
        # pylint: disable = too-many-arguments
        if not options:
            return ''
        return grid_item(
            name, label, self.select(name, None, options, autosubmit, **attrs),
            required, hint, self.error(name), title=title, clear=clear,
            class_=class_)

    # -------------------------------------------------------------------------
    def grid_upload(self, name, label, required=False, hint=None, title=None,
                    clear=False, class_='cioFormItem', **attrs):
        """Output a file upload field in a CSS grid layout.

        :param str name:
            Input ID.
        :param str label:
            Label.
        :param bool required: (default=False)
            Indicate if this field is required.
        :param str hint: (optional)
            Help message.
        :param str title: (optional)
            Title for the hover effect.
        :param bool clear: (default=False)
            If ``True``, add a ``<div class="cioClear"/>`` at the end.
        :param str class_: (default='cioFormItem')
            The class attribute.
        :param dict attrs:
            Keyworded arguments for ``webhelpers2.html.tags`` object.
        :rtype: str
        :return:
            Output a grid layout.
        """
        # pylint: disable = too-many-arguments
        return grid_item(
            name, label, self.upload(name, **attrs), required, hint,
            self.error(name), title=title, clear=clear, class_=class_)

    # -------------------------------------------------------------------------
    def grid_textarea(self, name, label, required=False, hint=None, title=None,
                      clear=False, class_='cioFormItem', **attrs):
        """Output a text input area in a CSS grid layout.

        :param str name:
            Input ID.
        :param str label:
            Label.
        :param bool required: (default=False)
            Indicate if this field is required.
        :param str hint: (optional)
            Help message.
        :param str title: (optional)
            Title for the hover effect.
        :param bool clear: (default=False)
            If ``True``, add a ``<div class="cioClear"/>`` at the end.
        :param str class_: (default='cioFormItem')
            The class attribute.
        :param dict attrs:
            Keyworded arguments for ``webhelpers2.html.tags`` object.
        :rtype: str
        :return:
            Output a grid layout.
        """
        # pylint: disable = too-many-arguments
        return grid_item(
            name, label, self.textarea(name, **attrs), required, hint,
            self.error(name), title=title, clear=clear, class_=class_)

    # -------------------------------------------------------------------------
    def _value(self, name, default=None):
        """Return the best value for the field ``name``.

        :param str name:
            Input ID.
        :param str default: (optional)
            Default value.
        :rtype: str
        """
        special = name in self._special[0] or [
            True for k in self._special[1] if name.startswith(k)]
        if not special and name in self._request.POST:
            return self._request.POST[name]
        if name in self.values:
            return self.values[name]
        return default
