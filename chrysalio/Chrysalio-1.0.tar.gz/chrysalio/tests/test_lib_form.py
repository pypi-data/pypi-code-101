# -*- coding: utf-8 -*-
# pylint: disable = import-outside-toplevel
"""Tests of ``lib.form`` functions and class methods."""

from unittest import TestCase


# =============================================================================
class ULibFormGetAction(TestCase):
    """Unit test class for :func:`lib.form.get_action`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:lib.form.get_action]"""
        from sys import version_info
        from pyramid.testing import DummyRequest
        from ..lib.form import get_action

        request = DummyRequest(POST={})
        action, items = get_action(request)
        self.assertEqual(action, '')
        self.assertEqual(len(items), 0)

        request = DummyRequest(POST={'run!1.x': '8'})
        action, items = get_action(request)
        self.assertEqual(action, 'run!1')
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0], '1')

        request = DummyRequest(POST={
            'run!éÔ.x'.encode('utf8'): '8'})
        action, items = get_action(request)
        item = 'run!éÔ' if version_info > (3, 0) else 'run!éÔ'.encode('utf8')
        self.assertEqual(action, item)
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0], item[4:])

        request = DummyRequest(POST={'run!#.x': '8'})
        action = get_action(request)[0]
        self.assertEqual(action, '')
        self.assertTrue(request.session.pop_flash('alert'))

        request = DummyRequest(POST={'run!#.x': '8', '#1': '1', '#2': '1'})
        action, items = get_action(request)
        self.assertEqual(action, 'run!#')
        self.assertEqual(len(items), 2)
        self.assertIn(items[0], ('1', '2'))

        request = DummyRequest(POST={
            'run!#.x': '8', bytes('#éÔ'.encode('utf8')): '1'})
        action, items = get_action(request)
        self.assertEqual(len(items), 1)
        self.assertEqual(
            items[0], version_info > (3, 0) and 'éÔ' or 'éÔ'.encode('utf8'))


# =============================================================================
class ULibFormSameAs(TestCase):
    """Unit test class for :class:`lib.form.SameAs`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:lib.form.SameAs]"""
        from colander import Invalid
        from pyramid.testing import DummyRequest
        from ..lib.form import SameAs

        same_as = SameAs(DummyRequest(), 'foo')
        self.assertRaises(Invalid, same_as, 'login', 'bar')


# =============================================================================
class ULibFormButton(TestCase):
    """Unit test class for :func:`lib.form.button`."""

    # -------------------------------------------------------------------------
    def test_with_no_label(self):
        """[u:lib.form.button] with no label"""
        from ..lib.form import button
        from webhelpers2.html import literal

        test_button = button(url='url', src='src')
        expected_result = \
            literal('<a href="url"><img src="src" alt="None"/></a> ')
        self.assertEqual(test_button, expected_result)

    # -------------------------------------------------------------------------
    def test_regular_button(self):
        """[u:lib.form.button] regular button"""
        from ..lib.form import button
        from webhelpers2.html import literal

        test_button = button(
            url='url', label='label', src='src', title='title', class_='value')
        expected_result = \
            literal('<a href="url" title="title" class="value">'
                    '<img src="src" alt="label"/>label</a> ')
        self.assertEqual(test_button, expected_result)


# =============================================================================
class ULibFormGridItem(TestCase):
    """Unit test class for :func:`lib.form.grid_item`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:lib.form.grid_item]"""
        from ..lib.form import grid_item

        self.assertFalse(grid_item(None, 'label', None))
        self.assertEqual(
            grid_item(
                None, 'label', 'html', True, 'help', 'erreur', clear=True),
            '<div class="cioError">'
            '<label><strong>label<span>*</span></strong></label>'
            '<div>html<em> help</em><strong> erreur</strong></div>'
            '<div class="cioClear"></div></div>')
        self.assertEqual(
            grid_item(
                None, 'label', 'html', False, 'help', 'erreur',
                class_='noClass'),
            '<div class="noClass cioError">'
            '<label><strong>label</strong></label>'
            '<div>html<em> help</em><strong> erreur</strong></div></div>')


# =============================================================================
class ULibFormForm(TestCase):
    """Unit test class for :class:`lib.form.Form`."""
    # pylint: disable = too-many-public-methods

    # -------------------------------------------------------------------------
    def setUp(self):
        """Set up test application."""
        from pyramid.testing import setUp
        from pyramid.csrf import SessionCSRFStoragePolicy

        self.configurator = setUp()
        self.configurator.set_csrf_storage_policy(SessionCSRFStoragePolicy())

    # -------------------------------------------------------------------------
    def tearDown(self):
        """Undo the effects of ``pyramid.testing.setUp()``."""
        from pyramid.testing import tearDown

        tearDown()

    # -------------------------------------------------------------------------
    @classmethod
    def schema(cls):
        """Return a simple Colander schema."""
        from colander import Mapping, SchemaNode, String, Boolean, Length

        schema = SchemaNode(Mapping())
        schema.add(SchemaNode(String(), name='login', validator=Length(min=2)))
        schema.add(SchemaNode(Boolean(), name='remember', missing=False))
        return schema

    # -------------------------------------------------------------------------
    def test_init(self):
        """[u:lib.form.Form.__init__]"""
        from collections import namedtuple
        from pyramid.testing import DummyRequest
        from ..lib.form import Form

        request = DummyRequest()
        form = Form(request)
        self.assertFalse(form.values)

        form = Form(request, self.schema())
        self.assertFalse(form.values)

        form = Form(request, self.schema(), defaults={'login': 'user1'})
        self.assertIn('login', form.values)
        self.assertEqual(form.values['login'], 'user1')

        user = namedtuple('User', 'login')(login='user1')
        form = Form(request, self.schema(), obj=user)
        self.assertIn('login', form.values)
        self.assertEqual(form.values['login'], 'user1')

    # -------------------------------------------------------------------------
    def test_validate_request_no_post(self):
        """[u:lib.form.Form.validate] request with no post"""
        from pyramid.testing import DummyRequest
        from ..lib.form import Form

        form = Form(DummyRequest())
        self.assertFalse(form.validate())

    # -------------------------------------------------------------------------
    def test_validate_ko(self):
        """[u:lib.form.Form.validate] KO"""
        from colander import Mapping, SchemaNode, String, Boolean, Length
        from pyramid.testing import DummyRequest
        from ..lib.form import Form

        schema = SchemaNode(Mapping())
        schema.add(SchemaNode(String(), name='login', validator=Length(min=2)))
        schema.add(SchemaNode(Boolean(), name='remember'))

        form = Form(
            DummyRequest(POST={'login': 'user1'}), schema=schema)
        self.assertFalse(form.validate())

        form = Form(
            DummyRequest(POST={'login': 'u', 'remember': False}),
            schema=schema)
        self.assertFalse(form.validate())

    # -------------------------------------------------------------------------
    def test_validate_ok(self):
        """[u:lib.form.Form.validate] OK"""
        from pyramid.testing import DummyRequest
        from ..lib.form import Form

        form = Form(DummyRequest(POST={'login': 'user1'}))
        form.validate()
        self.assertTrue(form.validate())
        self.assertNotIn('remember', form.values)
        self.assertIn('login', form.values)
        self.assertEqual(form.values['login'], 'user1')

        form = Form(
            DummyRequest(POST={'login': 'user1'}), schema=self.schema())
        self.assertTrue(form.validate())
        self.assertIn('remember', form.values)
        self.assertFalse(form.values['remember'])
        self.assertIn('login', form.values)
        self.assertEqual(form.values['login'], 'user1')

        class User(object):
            """Dummy user class."""
            # pylint: disable = too-few-public-methods
            login = None
            remember = False

        form = Form(
            DummyRequest(POST={'login': 'user1', 'remember': True}),
            schema=self.schema())
        user = User()
        self.assertTrue(form.validate(user))
        self.assertIn('remember', form.values)
        self.assertTrue(form.values['remember'])
        self.assertEqual(user.login, 'user1')
        self.assertTrue(user.remember)

    # -------------------------------------------------------------------------
    def test_has_error(self):
        """[u:lib.form.Form.has_error]"""
        from pyramid.testing import DummyRequest
        from ..lib.form import Form

        form = Form(
            DummyRequest(POST={'remember': True}), schema=self.schema())
        form.validate()
        self.assertTrue(form.has_error())
        self.assertTrue(form.has_error('login'))
        self.assertFalse(form.has_error('remember'))

    # -------------------------------------------------------------------------
    def test_set_error(self):
        """[u:lib.form.Form.set_error]"""
        from pyramid.testing import DummyRequest
        from ..lib.form import Form

        form = Form(DummyRequest())
        form.set_error('login', 'required')
        self.assertTrue(form.has_error('login'))

        form = Form(
            DummyRequest(POST={'remember': True}), schema=self.schema())
        form.validate()
        form.set_error('login', 'required login')
        self.assertTrue(form.has_error('login'))

    # -------------------------------------------------------------------------
    def test_error(self):
        """[u:lib.form.Form.error]"""
        from pyramid.testing import DummyRequest
        from ..lib.form import Form

        form = Form(
            DummyRequest(POST={'remember': True}), schema=self.schema())
        form.validate()
        self.assertEqual(form.error('login'), 'Required')
        self.assertFalse(form.error('remember'))

    # -------------------------------------------------------------------------
    def test_static(self):
        """[u:lib.form.Form.static]"""
        from pyramid.testing import DummyRequest
        from ..lib.form import Form

        form = Form(
            DummyRequest(POST={'login': 'user2'}),
            schema=self.schema(), defaults={'login': 'user1'})
        form.static('login')
        input_text = str(form.text('login', 'user1'))
        self.assertIn('user1', input_text)
        self.assertNotIn('user2', input_text)

    # -------------------------------------------------------------------------
    def test_forget(self):
        """[u:lib.form.Form.forget]"""
        from pyramid.testing import DummyRequest
        from ..lib.form import Form

        form = Form(
            DummyRequest(POST={'login': 'user1'}), schema=self.schema())
        form.forget('l')
        input_text = str(form.text('login'))
        self.assertNotIn('user1', input_text)

    # -------------------------------------------------------------------------
    def test_make_safe_id(self):
        """[u:lib.form.Form.make_safe_id]"""
        from ..lib.form import Form

        self.assertEqual(Form.make_safe_id('~Publidoc'), 'publidoc')
        self.assertEqual(Form.make_safe_id('#12'), '12')

    # -------------------------------------------------------------------------
    def test_begin(self):
        """[u:lib.form.Form.begin]"""
        from pyramid.csrf import new_csrf_token
        from pyramid.testing import DummyRequest
        from ..lib.form import Form

        form = Form(DummyRequest())
        html = str(form.begin(url='/login', multipart=True))
        self.assertTrue(html.startswith(
            '<form action="/login" enctype="multipart/form-data"'
            ' method="post">'))

        request = DummyRequest()
        token = new_csrf_token(request)
        form = Form(request)
        html = str(form.begin(url='/login'))
        self.assertEqual(
            html,
            '<form action="/login" method="post"><div class="cioHidden">'
            '<input id="csrf_token" name="csrf_token" type="hidden" '
            'value="{0}" /></div>'.format(token))

    # -------------------------------------------------------------------------
    def test_end(self):
        """[u:lib.form.Form.end]"""
        from pyramid.testing import DummyRequest
        from ..lib.form import Form

        html = str(Form(DummyRequest()).end())
        self.assertEqual(html, '</form>')

    # -------------------------------------------------------------------------
    def test_submit(self):
        """[u:lib.form.Form.submit]"""
        from pyramid.testing import DummyRequest
        from ..lib.form import Form

        html = Form(DummyRequest()).submit('foo', 'Foo')
        self.assertIn('id="foo"', html)
        self.assertIn('value="Foo"', html)
        self.assertIn('class="cioButton"', html)

        html = Form(DummyRequest()).submit('foo', class_='mainButton')
        self.assertIn('class="mainButton"', html)

    # -------------------------------------------------------------------------
    def test_submit_image(self):
        """[u:lib.form.Form.submit_image]"""
        from pyramid.testing import DummyRequest
        from ..lib.form import Form

        html = Form(DummyRequest()).submit_image('foo', '', 'Images/foo.png')
        self.assertIn('type="image"', html)
        self.assertIn('name="foo"', html)
        self.assertIn('title="foo"', html)

        html = Form(DummyRequest()).submit_image(
            'foo', 'My "Foo"', 'Images/foo.png')
        self.assertIn('title="My &#34;Foo&#34;', html)

        html = Form(DummyRequest()).submit_image(
            'foo', 'éÔ', 'Images/foo.png')
        self.assertIn('title="éÔ"', html)

    # -------------------------------------------------------------------------
    def test_submit_cancel(self):
        """[u:lib.form.Form.submit_cancel]"""
        from pyramid.testing import DummyRequest
        from ..lib.form import Form

        html = Form(DummyRequest()).submit_cancel(
            'Cancel', 'Images/cancel.png')
        self.assertIn('type="image"', html)
        self.assertIn('name="ccl!"', html)
        self.assertIn('title="Cancel"', html)

    # -------------------------------------------------------------------------
    def test_button(self):
        """[u:lib.form.Form.button]"""
        from pyramid.testing import DummyRequest
        from ..lib.form import Form

        html = Form(DummyRequest()).button(
            'http://localhost/foo', 'My Foo')
        self.assertIn('href="http://localhost/foo"', html)
        self.assertIn('class="cioButton"', html)

    # -------------------------------------------------------------------------
    def test_default_button(self):
        """[u:lib.form.Form.default_button]"""
        from pyramid.testing import DummyRequest
        from ..lib.form import Form

        html = Form(DummyRequest()).default_button('filter')
        self.assertIn('name="filter"', html)

    # -------------------------------------------------------------------------
    def test_grid_item(self):
        """[u:lib.form.Form.grid_item]"""
        from webhelpers2.html import literal
        from pyramid.testing import DummyRequest
        from ..lib.form import Form

        html = Form(DummyRequest()).grid_item(
            'My label', literal('<input type="test" id="foo">'),
            required=True, hint='éÔ', error='ôÉ')
        self.assertIn('<em> éÔ</em>', html)
        self.assertIn('<strong> ôÉ</strong>', html)
        self.assertIn('<span>*</span>', html)

    # -------------------------------------------------------------------------
    def test_hidden(self):
        """[u:lib.form.Form.hidden]"""
        from pyramid.testing import DummyRequest
        from ..lib.form import Form

        html = Form(DummyRequest()).hidden('foo', 'éÔ')
        self.assertIn('type="hidden"', html)
        self.assertIn('id="foo"', html)
        self.assertIn('value="éÔ"', html)

    # -------------------------------------------------------------------------
    def test_text(self):
        """[u:lib.form.Form.text]"""
        from pyramid.testing import DummyRequest
        from ..lib.form import Form

        html = Form(DummyRequest()).text('foo', 'éÔ')
        self.assertIn('type="text"', html)
        self.assertIn('id="foo"', html)
        self.assertIn('value="éÔ"', html)

    # -------------------------------------------------------------------------
    def test_password(self):
        """[u:lib.form.Form.password]"""
        from pyramid.testing import DummyRequest
        from ..lib.form import Form

        html = Form(DummyRequest()).password('password', 'seekrit')
        self.assertIn('type="password"', html)
        self.assertIn('id="password"', html)
        self.assertIn('value="seekrit"', html)

    # -------------------------------------------------------------------------
    def test_checkbox(self):
        """[u:lib.form.Form.checkbox]"""
        from pyramid.testing import DummyRequest
        from ..lib.form import Form

        html = Form(DummyRequest()).checkbox('foo', 'éÔ')
        self.assertIn('type="checkbox"', html)
        self.assertIn('value="éÔ"', html)
        self.assertNotIn('checked="checked"', html)

        html = Form(DummyRequest()).checkbox('foo', checked=True)
        self.assertIn('checked="checked"', html)

        html = Form(DummyRequest()).checkbox('foo', autosubmit=True)
        self.assertIn('class="cioAutoSubmit"', html)

        html = Form(DummyRequest(POST={'foo': '1'})).checkbox('foo')
        self.assertIn('checked="checked"', html)

    # -------------------------------------------------------------------------
    def test_custom_checkbox(self):
        """[u:lib.form.Form.custom_checkbox]"""
        from pyramid.testing import DummyRequest
        from ..lib.form import Form

        html = Form(DummyRequest()).custom_checkbox('foo')
        self.assertIn('cioCustomCheckbox', html)
        self.assertIn('label', html)
        self.assertIn('type="checkbox"', html)
        self.assertIn('value="1"', html)
        self.assertNotIn('checked="checked"', html)

        html = Form(DummyRequest()).custom_checkbox('foo', checked=True)
        self.assertIn('checked="checked"', html)

        html = Form(DummyRequest()).custom_checkbox('foo', autosubmit=True)
        self.assertIn('class="cioCustomCheckbox cioAutoSubmit"', html)

        html = Form(DummyRequest(POST={'foo': '1'})).custom_checkbox('foo')
        self.assertIn('checked="checked"', html)

    # -------------------------------------------------------------------------
    def test_radio(self):
        """[u:lib.form.Form.radio]"""
        from pyramid.testing import DummyRequest
        from ..lib.form import Form

        html = Form(DummyRequest()).radio('foo', 'éÔ')
        self.assertIn('type="radio"', html)
        self.assertIn('value="éÔ"', html)
        self.assertNotIn('checked="checked"', html)

        html = Form(DummyRequest()).radio('foo', 'bar', checked=True)
        self.assertIn('checked="checked"', html)

        html = Form(DummyRequest()).radio('foo', 'bar', autosubmit=True)
        self.assertIn('class="cioAutoSubmit"', html)

        html = Form(DummyRequest(POST={'foo': 'éÔ'})).radio('foo', 'éÔ')
        self.assertIn('checked="checked"', html)

    # -------------------------------------------------------------------------
    def test_select(self):
        """[u:lib.form.Form.select]"""
        from pyramid.testing import DummyRequest
        from ..lib.form import Form

        html = Form(DummyRequest()).select('foo', 'b', None)
        self.assertEqual(html, '')

        html = Form(DummyRequest()).select(
            'foo', 'b', ('', 'a', 'b', 'é'), autosubmit=True)
        self.assertIn('<select', html)
        self.assertIn('id="foo"', html)
        self.assertIn('class="cioAutoSubmit"', html)
        self.assertIn('<option></option>', html)
        self.assertIn('<option>a</option>', html)
        self.assertIn('<option selected="selected">b</option>', html)
        self.assertIn('<option>é</option>', html)

        html = Form(DummyRequest()).select('foo', None, (1, 2))
        self.assertIn('<option>1</option>', html)
        self.assertIn('<option>2</option>', html)

        html = Form(DummyRequest()).select(
            'foo', 'b', (('', ''), ('a', 'A'), ('b', 'B'), ('é', 'É')))
        self.assertIn('<option value="a">A</option>', html)
        self.assertIn('<option selected="selected" value="b">B</option>', html)
        self.assertIn('<option value="é">É</option>', html)

        html = Form(DummyRequest()).select(
            'foo', None, ((1, 'One'), (2, 'Two')))
        self.assertIn('<option value="1">One</option>', html)

    # -------------------------------------------------------------------------
    def test_upload(self):
        """[u:lib.form.Form.upload]"""
        from pyramid.testing import DummyRequest
        from ..lib.form import Form

        html = Form(DummyRequest()).upload('upload_file')
        self.assertIn('type="file"', html)
        self.assertIn('id="upload_file"', html)

    # -------------------------------------------------------------------------
    def test_textarea(self):
        """[u:lib.form.Form.textarea]"""
        from pyramid.testing import DummyRequest
        from ..lib.form import Form

        html = Form(DummyRequest()).textarea('foo')
        self.assertIn('<textarea', html)
        self.assertIn('id="foo"', html)

    # -------------------------------------------------------------------------
    def test_grid_text(self):
        """[u:lib.form.Form.grid_text]"""
        from pyramid.testing import DummyRequest
        from ..lib.form import Form

        html = Form(DummyRequest()).grid_text('foo', 'éÔ', clear=True)
        self.assertIn('<div class="cioFormItem">', html)
        self.assertIn('<label for="foo">', html)
        self.assertIn('type="text"', html)
        self.assertIn('<strong>éÔ</strong>', html)
        self.assertIn('<div class="cioClear">', html)

    # -------------------------------------------------------------------------
    def test_grid_password(self):
        """[u:lib.form.Form.grid_password]"""
        from pyramid.testing import DummyRequest
        from ..lib.form import Form

        html = Form(DummyRequest()).grid_password('password', 'Password')
        self.assertIn('<div class="cioFormItem">', html)
        self.assertIn('<label for="password">', html)
        self.assertIn('type="password"', html)
        self.assertIn('<strong>Password</strong>', html)
        self.assertNotIn('<div class="cioClear">', html)

    # -------------------------------------------------------------------------
    def test_grid_checkbox(self):
        """[u:lib.form.Form.grid_checkbox]"""
        from pyramid.testing import DummyRequest
        from ..lib.form import Form

        html = Form(DummyRequest()).grid_checkbox('foo', 'éÔ')
        self.assertIn('<div class="cioFormItem">', html)
        self.assertIn('<label for="foo">', html)
        self.assertIn('type="checkbox"', html)
        self.assertIn('<label for="foo">', html)

    # -------------------------------------------------------------------------
    def test_grid_custom_checkbox(self):
        """[u:lib.form.Form.grid_checkbox]"""
        from pyramid.testing import DummyRequest
        from ..lib.form import Form

        html = Form(DummyRequest()).grid_custom_checkbox('foo', 'éÔ')
        self.assertIn('<div class="cioFormItem">', html)
        self.assertIn('cioCustomCheckbox', html)

    # -------------------------------------------------------------------------
    def test_grid_select(self):
        """[u:lib.form.Form.grid_select]"""
        from pyramid.testing import DummyRequest
        from ..lib.form import Form

        html = Form(DummyRequest()).grid_select('foo', 'b', None)
        self.assertEqual(html, '')

        html = Form(DummyRequest()).grid_select(
            'foo', 'éÔ', ('', 'a', 'b', 'é'), autosubmit=True, required=True,
            hint='Ôé', clear=True)
        self.assertIn('<div class="cioFormItem">', html)
        self.assertIn('<label for="foo">', html)
        self.assertIn('<select', html)
        self.assertIn('<span>*</span>', html)
        self.assertIn('<div class="cioClear">', html)

    # -------------------------------------------------------------------------
    def test_grid_upload(self):
        """[u:lib.form.Form.grid_upload]"""
        from pyramid.testing import DummyRequest
        from ..lib.form import Form

        html = Form(DummyRequest()).grid_upload('foo', 'éÔ')
        self.assertIn('<div class="cioFormItem">', html)
        self.assertIn('<label for="foo">', html)
        self.assertIn('type="file"', html)

    # -------------------------------------------------------------------------
    def test_grid_textarea(self):
        """[u:lib.form.Form.grid_texarea]"""
        from pyramid.testing import DummyRequest
        from ..lib.form import Form

        html = Form(DummyRequest()).grid_textarea('foo', 'éÔ')
        self.assertIn('<div class="cioFormItem">', html)
        self.assertIn('<label for="foo">', html)
        self.assertIn('<textarea', html)
        self.assertIn('id="foo"', html)

    # -------------------------------------------------------------------------
    def test_values(self):
        """[u:lib.form.Form.values]"""
        from pyramid.testing import DummyRequest
        from ..lib.form import Form

        request = DummyRequest()
        request.POST['foo'] = 'éÔ'
        html = Form(request).text('foo')
        self.assertIn('value="éÔ"', html)

        form = Form(request)
        form.values['bar'] = 'ôÉ'
        html = form.text('bar')
        self.assertIn('value="ôÉ"', html)
