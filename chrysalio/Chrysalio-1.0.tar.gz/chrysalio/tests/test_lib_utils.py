# -*- coding: utf-8 -*-
# pylint: disable = import-outside-toplevel
"""Tests of ``lib.utils`` functions."""

from os import walk
from os.path import join, basename, dirname, exists, relpath
from shutil import rmtree, copy
from sys import version_info
from base64 import b64encode
from datetime import date, datetime, timedelta
from filecmp import cmpfiles
from re import compile as re_compile

from unittest import TestCase

from . import TmpDirTestCase


# =============================================================================
class ULibUtilsTostr(TestCase):
    """Unit test class for :func:`lib.utils.tostr`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:lib.utils.tostr]"""
        from ..lib.utils import tostr

        text = tostr('foo')
        self.assertIsInstance(text, str)
        self.assertEqual(text, 'foo')

        text = tostr('foo'.encode('utf8'))
        self.assertIsInstance(text, str)
        self.assertEqual(text, 'foo')

        text = tostr(b'foo')
        self.assertIsInstance(text, str)
        self.assertEqual(text, 'foo')

        text = tostr(bytes('foo'.encode('utf8')))
        self.assertIsInstance(text, str)
        self.assertEqual(text, 'foo')

        text = tostr('é Ô')
        self.assertIsInstance(text, str)
        self.assertEqual(
            text, version_info > (3, 0) and 'é Ô' or 'é Ô'.encode('utf8'))


# =============================================================================
class ULibUtilsToUnicode(TestCase):
    """Unit test class for :func:`lib.utils.tounicode`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:lib.utils.unicode]"""
        from ..lib.utils import tounicode

        text = tounicode('foo')
        self.assertIsInstance(text, type(''))
        self.assertEqual(text, 'foo')

        text = tounicode('foo'.encode('utf8'))
        self.assertIsInstance(text, type(''))
        self.assertEqual(text, 'foo')

        text = tounicode(b'foo')
        self.assertIsInstance(text, type(''))
        self.assertEqual(text, 'foo')

        text = tounicode(bytes('foo'.encode('utf8')))
        self.assertIsInstance(text, type(''))
        self.assertEqual(text, 'foo')

        text = tounicode('é Ô')
        self.assertIsInstance(text, type(''))
        self.assertEqual(text, 'é Ô')


# =============================================================================
class ULibUtilsLoadGuessingEncoding(TestCase):
    """Unit test class for :func:`lib.utils.laoad_guessing_encoding`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:lib.utils.unicode]"""
        from ..lib.utils import load_guessing_encoding
        from . import TEST_LATIN1, TEST_UTF8

        self.assertIsNotNone(load_guessing_encoding(TEST_UTF8))
        self.assertIsNotNone(load_guessing_encoding(TEST_LATIN1))


# =============================================================================
class ULibUtilsCopyContent(TestCase):
    """Unit test class for :func:`lib.utils.copy_content`."""

    # -------------------------------------------------------------------------
    def tearDown(self):
        """Undo the effects of ``pyramid.testing.setUp()``."""
        from . import TEST_DIR

        super(ULibUtilsCopyContent, self).tearDown()
        if exists(TEST_DIR):
            rmtree(TEST_DIR)

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:lib.utils.copy_content]"""
        from ..lib.utils import EXCLUDED_FILES, copy_content
        from . import TEST_DIR

        # With specific excluded files
        exclude = EXCLUDED_FILES + ('hugo.txt',)
        source_dir = join(dirname(__file__), 'Texts')
        copy_content(source_dir, TEST_DIR, exclude)
        for path, dirs, files in walk(source_dir):
            for name in dirs + files:
                copy_file = join(TEST_DIR, relpath(path, source_dir), name)
                if name in exclude:
                    self.assertFalse(exists(copy_file))
                else:
                    self.assertTrue(exists(copy_file))

        # With normal excluded files
        copy_content(source_dir, TEST_DIR)
        self.assertTrue(exists(join(TEST_DIR, 'Écrits', 'XIXe', 'hugo.txt')))


# =============================================================================
class ULibUtilsCopyContentRe(TestCase):
    """Unit test class for :func:`lib.utils.copy_content_re`."""

    # -------------------------------------------------------------------------
    def tearDown(self):
        """Undo the effects of ``pyramid.testing.setUp()``."""
        from . import TEST_DIR

        super(ULibUtilsCopyContentRe, self).tearDown()
        if exists(TEST_DIR):
            rmtree(TEST_DIR)

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:lib.utils.copy_content]"""
        from ..lib.utils import copy_content_re
        from . import TEST_DIR

        source_dir = join(dirname(__file__), 'Texts')
        exclude = re_compile('(^X|1.rst$)')
        copy_content_re(source_dir, TEST_DIR, exclude)
        self.assertTrue(exists(join(TEST_DIR, 'utf8.txt')))
        self.assertFalse(exists(join(TEST_DIR, 'latin1.rst')))
        self.assertTrue(exists(join(TEST_DIR, 'Écrits')))
        self.assertFalse(exists(join(TEST_DIR, 'Écrits', 'XXe')))
        self.assertFalse(exists(join(TEST_DIR, 'Écrits', 'XIXe')))


# =============================================================================
class ULibUtilsMakeId(TestCase):
    """Unit test class for :func:`lib.utils.make_id`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:lib.utils.make_id]"""
        from ..lib.utils import make_id

        name = '12Test___Té*t.;?!'
        self.assertEqual(make_id(''), '')
        self.assertEqual(make_id(name), '12test___té*t.;?!')
        self.assertEqual(make_id(name, 'standard'), '12Test_Té_t._')
        self.assertEqual(make_id(name, 'token'), '12test_te_t._')
        self.assertEqual(make_id(name, 'token', 6), '12test')
        self.assertEqual(make_id(name, 'xmlid'), '_12test_te_t._')
        self.assertEqual(make_id(name, 'class'), '12Test_Te_t_')
        self.assertEqual(make_id(name, 'no_accent'), '12Test___Te*t.;?!')


# =============================================================================
class ULibUtilsMakeDigest(TestCase):
    """Unit test class for :func:`lib.utils.make_digest`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:lib.utils.make_digest]"""
        from ..lib.utils import make_digest, tounicode

        digest = make_digest(
            '/browse/directory/Sandbox/Écrits/XXe/de Saint Exupéry.txt')
        self.assertEqual(digest, '1d4fe4892722b034801a7bac95fd3c33')
        digest = make_digest(tounicode(
            '/browse/directory/Sandbox/Écrits/XIXe/hugo.txt'.encode('utf8')))
        self.assertEqual(digest, '34a21e0695daed8a351a54b0116c3f70')


# =============================================================================
class ULibUtilsNormalizeSpaces(TestCase):
    """Unit test class for :func:`lib.utils.normalize_spaces`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:lib.utils.normalize_spaces]"""
        from ..lib.utils import normalize_spaces

        text = 'test test1       é  _    '
        self.assertEqual(normalize_spaces(None), None)
        self.assertEqual(normalize_spaces('test  test '), 'test test')
        self.assertEqual(normalize_spaces(text), 'test test1 é _')
        self.assertEqual(normalize_spaces(text, 9), 'test test')


# =============================================================================
class ULibUtilsCamelCase(TestCase):
    """Unit test class for :func:`lib.utils.camel_case`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:lib.utils.camel_case]"""
        from ..lib.utils import camel_case

        self.assertEqual(camel_case('xml2html'), 'Xml2Html')
        self.assertEqual(camel_case('LaTeX'), 'LaTeX')
        self.assertEqual(camel_case('laTeX'), 'LaTeX')
        self.assertEqual(camel_case('my_way'), 'MyWay')
        self.assertEqual(camel_case('my way'), 'MyWay')
        self.assertEqual(camel_case('my-way'), 'My-Way')


# =============================================================================
class ULibUtilsShorten(TestCase):
    """Unit test class for :func:`lib.utils.shorten`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:lib.utils.shortent]"""
        from ..lib.utils import shorten

        self.assertEqual(shorten('12 45  7890', 10), '12 45 7890')
        self.assertEqual(shorten('12 45  789 12', 10), '12 45 789…')
        self.assertEqual(shorten('12 45  789012', 10, '...'), '12 45 7...')
        self.assertEqual(shorten('12 45  789012', 10, ''), '12 45 7890')


# =============================================================================
class ULibUtilsEncryptDecrypt(TestCase):
    """Unit test class for :func:`lib.utils.encrypt` and
    :func:`lib.utils.decrypt`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:lib.utils.encrypt/decrypt]"""
        from ..lib.utils import encrypt, decrypt

        self.assertIsNone(encrypt(None, 'seekrit'))
        self.assertEqual(encrypt('', 'seekrit'), '')
        self.assertIsNone(decrypt(None, 'seekrit'))
        self.assertEqual(decrypt('', 'seekrit'), '')

        crypted = encrypt('protectme', 'seekrit')
        self.assertEqual(len(crypted), 44)
        self.assertEqual(decrypt(crypted, 'seekrit'), 'protectme')

        crypted = encrypt(b'protectme', 'seekrit')
        self.assertEqual(decrypt(crypted, 'seekrit'), 'protectme')

        crypted = encrypt(bytes('protège moi'.encode('utf8')), 'seekrit')
        self.assertEqual(len(crypted), 44)
        self.assertEqual(decrypt(crypted, 'seekrit'), 'protège moi')

        self.assertIsNone(decrypt('foo', 'seekrit'))
        self.assertIsNone(decrypt(b64encode(b'foo'), 'seekrit'))


# =============================================================================
class ULibUtilsToken(TestCase):
    """Unit test class for :func:`lib.utils.token`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:lib.utils.token]"""
        from ..lib.utils import token

        result = token()
        self.assertTrue(len(result) > 7)
        self.assertTrue(len(result) < 17)

        result = token(32)
        self.assertEqual(len(result), 32)


# =============================================================================
class ULibUtilsExecute(TestCase):
    """Unit test class for :func:`lib.utils.execute`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:lib.utils.execute]"""
        from ..lib.utils import execute

        self.assertEqual(
            execute(['echo', 'test'], None, False), ('test', ''))
        self.assertEqual(
            execute(['nice', 'echo', 'test'], None, False), ('test', ''))
        self.assertEqual(
            execute(['echo', 'testé'], None, False), ('testé', ''))
        self.assertEqual(
            execute(['echo', '\xa9'], None, False), ('\xa9', ''))
        self.assertEqual(
            execute(['echo', 'test1', 'test2'], None, False),
            ('test1 test2', ''))

        self.assertEqual(
            execute(['echo2'], None, False), ('', '"${c}" failed: ${e}'))
        self.assertEqual(
            execute(['echo', 'test'], 'cwd', True),
            ('', '"${c}" failed: ${e}'))
        self.assertEqual(
            execute(['echo', 'test'], None, True), ('test', '"${c}" failed'))


# =============================================================================
class ULibUtilsFullUrl(TestCase):
    """Unit test class for :func:`lib.utils.full_url`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:lib.utils.full_url]"""
        from ..lib.utils import full_url

        url = 'http://hg.publiforge.org'
        new_url = full_url(url)
        self.assertEqual(new_url, url)

        new_url = full_url(url, 'foo')
        self.assertEqual(new_url, 'http://foo@hg.publiforge.org')

        new_url = full_url(url, 'foo', 'bar')
        self.assertEqual(new_url, 'http://foo:bar@hg.publiforge.org')


# =============================================================================
class ULibUtilsMimetypeGet(TestCase):
    """Unit test class for :func:`lib.utils.mimetype_get`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:lib.utils.mimetype_get]"""
        from . import TEST_XXX, TEST_CSS
        from ..lib.utils import mimetype_get

        # A directory
        mimetype, file_type = mimetype_get(dirname(__file__))
        self.assertEqual(mimetype, 'directory')
        self.assertEqual(file_type, 'directory')

        # An unknown file
        mimetype, file_type = mimetype_get(TEST_XXX)
        self.assertEqual(mimetype, 'unknown')
        self.assertEqual(file_type, 'unknown')

        # A CSS file
        mimetype, file_type = mimetype_get(TEST_CSS)
        self.assertEqual(mimetype, 'text/css')
        self.assertEqual(file_type, 'css')


# =============================================================================
class ULibUtilsDeltatimeLabel(TestCase):
    """Unit test class for :func:`lib.utils.deltatime_label`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:lib.utils.deltatime_label]"""
        from ..lib.utils import deltatime_label

        self.assertEqual(deltatime_label(lang='en'), '0 second')
        self.assertEqual(deltatime_label(days=1, lang='en'), '1 day')
        self.assertEqual(deltatime_label(days=2, lang='en'), '2 days')
        self.assertEqual(deltatime_label(hours=1, lang='en'), '1 hour')
        self.assertEqual(deltatime_label(hours=2, lang='en'), '2 hours')
        self.assertEqual(deltatime_label(minutes=1, lang='en'), '1 minute')
        self.assertEqual(deltatime_label(minutes=2, lang='en'), '2 minutes')
        self.assertEqual(deltatime_label(seconds=1, lang='en'), '1 second')
        self.assertEqual(deltatime_label(seconds=2, lang='en'), '2 seconds')

        self.assertEqual(
            deltatime_label(seconds=303, lang='en'), '5 minutes 3 seconds')

        self.assertEqual(
            deltatime_label(seconds=1, hours=25, days=1, lang='en'),
            '2 days 1 hour 1 second')


# =============================================================================
class ULibUtilsAge(TestCase):
    """Unit test class for :func:`lib.utils.age`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:lib.utils.age]"""
        from ..lib.utils import age

        self.assertEqual(age(None), '')

        mtime = datetime.now() + timedelta(seconds=12)
        self.assertEqual(age(mtime), '0 second')
        mtime = datetime.now() - timedelta(seconds=1)
        self.assertEqual(age(mtime), '1 second')
        mtime = datetime.now() - timedelta(seconds=12)
        self.assertIn('seconds', age(mtime))

        mtime = datetime.now() - timedelta(minutes=1)
        self.assertEqual(age(mtime), '1 minute')
        mtime = datetime.now() - timedelta(minutes=12)
        self.assertIn('minutes', age(mtime))

        mtime = datetime.now() - timedelta(hours=1)
        self.assertEqual(age(mtime), '1 hour')
        mtime = datetime.now() - timedelta(hours=12)
        self.assertIn('hours', age(mtime))

        mtime = datetime.now() - timedelta(days=1)
        self.assertEqual(age(mtime), '1 day')
        mtime = datetime.now() - timedelta(days=3)
        self.assertIn('days', age(mtime))

        mtime = datetime.now() - timedelta(weeks=1)
        self.assertEqual(age(mtime), '1 week')
        mtime = datetime.now() - timedelta(weeks=3)
        self.assertIn('weeks', age(mtime))

        mtime = datetime.now() - timedelta(weeks=12)
        self.assertIn('months', age(mtime))

        mtime = datetime.now() - timedelta(weeks=60)
        self.assertIn('-', age(mtime))


# =============================================================================
class ULibUtilsSizeLabel(TestCase):
    """Unit test class for :func:`lib.utils.size_label`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:lib.utils.size_label]"""
        from ..lib.i18n import _, translate
        from ..lib.utils import size_label

        # Directory, 1 element
        self.assertEqual(
            translate(size_label(1, True)),
            translate(_('${n} item', {'n': 1})))

        # Directory, several elements
        self.assertEqual(
            translate(size_label(10, True)),
            translate(_('${n} items', {'n': 10})))

        # File, bytes
        self.assertEqual(size_label(512), '512 o')

        # File, Kio
        self.assertEqual(size_label(2048), '2.0 Kio')

        # File, Mio
        self.assertEqual(size_label(3250590), '3.1 Mio')

        # File, Gio
        self.assertEqual(size_label(4831838208), '4.5 Gio')


# =============================================================================
class ULibUtilsConvertValue(TestCase):
    """Unit test class for :func:`lib.utils.convert_value`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:lib.utils.convert_value]"""
        from ..lib.utils import convert_value

        # Boolean
        self.assertIsInstance(convert_value('boolean', 'true'), bool)
        self.assertTrue(convert_value('boolean', 'foo'))
        self.assertFalse(convert_value('boolean', 'false'))
        self.assertFalse(convert_value('boolean', ''))

        # Integer
        self.assertIsInstance(convert_value('integer', '12'), int)
        self.assertEqual(convert_value('integer', '12'), 12)
        self.assertEqual(convert_value('integer', 'foo'), 0)

        # Float
        self.assertIsInstance(convert_value('decimal', '12'), float)
        self.assertIsInstance(convert_value('decimal', '3.14'), float)
        self.assertEqual(convert_value('decimal', '12'), 12.0)
        self.assertEqual(convert_value('decimal', '3.14'), 3.14)
        self.assertEqual(convert_value('decimal', 'foo'), 0.0)

        # Date/time
        self.assertIsNone(convert_value('datetime', 'foo'))
        self.assertIsInstance(
            convert_value('datetime', '2000-12-10T10:20:00'), datetime)
        self.assertEqual(
            convert_value('datetime', '1997-10-24T09:45:12'),
            datetime(1997, 10, 24, 9, 45, 12))

        # Date
        self.assertIsNone(convert_value('date', 'foo'))
        self.assertIsInstance(convert_value('date', '2000-12-10'), date)
        self.assertEqual(
            convert_value('date', '1997-10-24'), date(1997, 10, 24))

        # String
        self.assertIsInstance(convert_value('string', 'foo'), str)
        self.assertEqual(convert_value('string', 'foo'), 'foo')


# =============================================================================
class ULibUtilsCheckChrysalioJs(TmpDirTestCase):
    """Unit test class for :func:`lib.utils.check_chrysalio_js`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:lib.utils.check_chrysalio_js]"""
        from ..lib.utils import check_chrysalio_js
        from . import TEST_DIR

        js_dir = TEST_DIR
        check_chrysalio_js(join(js_dir, 'Foo'))

        cio_js_dir = join(dirname(__file__), '..', 'Static', 'Js')
        copy(join(cio_js_dir, 'jquery.js'), join(js_dir, 'jquery.js'))
        with open(join(js_dir, 'chrysalio.js'), 'w'):
            pass
        js_files = ('jquery.js', 'js.cookie.js', 'chrysalio.js')
        compare = cmpfiles(cio_js_dir, js_dir, js_files)
        self.assertEqual(compare[0], ['jquery.js'])
        self.assertEqual(compare[1], ['chrysalio.js'])
        self.assertEqual(len(compare[2]), 1)

        check_chrysalio_js(js_dir)

        compare = cmpfiles(cio_js_dir, js_dir, js_files)
        self.assertEqual(len(compare[0]), 2)
        self.assertEqual(len(compare[1]), 0)
        self.assertEqual(len(compare[2]), 1)


# =============================================================================
class ULibUtilsCheckChrysalioCss(TmpDirTestCase):
    """Unit test class for :func:`lib.utils.check_chrysalio_css`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:lib.utils.check_chrysalio_js]"""
        from ..lib.utils import check_chrysalio_css
        from . import TEST_DIR

        css_dir = TEST_DIR
        check_chrysalio_css(join(css_dir, 'Foo'))

        cio_css_dir = join(dirname(__file__), '..', 'Static', 'Css')
        copy(join(cio_css_dir, 'jquery-ui.css'),
             join(css_dir, 'jquery-ui.css'))
        with open(join(css_dir, 'jquery-ui.css'), 'w'):
            pass
        css_files = ('jquery.css', 'jquery-ui.css')
        compare = cmpfiles(cio_css_dir, css_dir, css_files)
        self.assertEqual(len(compare[0]), 0)
        self.assertEqual(compare[1], ['jquery-ui.css'])
        self.assertEqual(len(compare[2]), 1)

        check_chrysalio_css(css_dir)

        compare = cmpfiles(cio_css_dir, css_dir, css_files)
        self.assertEqual(len(compare[0]), 1)
        self.assertEqual(len(compare[1]), 0)
        self.assertEqual(len(compare[2]), 1)


# =============================================================================
class ULibUtilsCommonDirectory(TmpDirTestCase):
    """Unit test class for :func:`lib.utils.common_directory`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:lib.utils.common_directory]"""
        from . import ATTACHMENTS_DIR, TEST1_SVG, TEST5_SVG
        from ..lib.utils import common_directory

        self.assertIsNone(common_directory([]))
        self.assertIsNone(common_directory(
            [join(ATTACHMENTS_DIR, 'foo', 'bar')]))

        self.assertEqual(common_directory([TEST1_SVG]), dirname(TEST1_SVG))
        self.assertEqual(
            common_directory([TEST1_SVG, TEST5_SVG]),
            join(ATTACHMENTS_DIR, 'Users'))


# =============================================================================
class ULibUtilsHashAsdminPassword(TmpDirTestCase):
    """Unit test class for :func:`lib.utils.hash_admin_password`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:lib.utils.hash_admin_password]"""
        from . import TEST_DIR, TEST_INI
        from ..lib.utils import hash_admin_password

        copy(TEST_INI, TEST_DIR)

        hash_admin_password(TEST_DIR, (basename(TEST_INI),), 'adminpwd')
        with open(join(TEST_DIR, basename(TEST_INI)), 'r') as hdl:
            content = hdl.read()
        self.assertIn('admin.password = $2b$12$', content)


# =============================================================================
class ULibUtilsRst2Html(TestCase):
    """Unit test class for :func:`lib.utils.rst2html`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:lib.utils.rst2html]"""
        from ..lib.utils import rst2html
        self.assertEqual(
            rst2html(''), '')
        self.assertEqual(
            rst2html(None), None)
        self.assertEqual(
            rst2html('foo_'), 'foo_')
        self.assertEqual(
            rst2html('test'), 'test')
        self.assertEqual(
            rst2html('*emphasis*'), '<em>emphasis</em>')
        self.assertEqual(
            rst2html('**strong**'), '<strong>strong</strong>')
        self.assertEqual(
            rst2html('``inline literal``'),
            '<tt class="docutils literal">inline literal</tt>')
