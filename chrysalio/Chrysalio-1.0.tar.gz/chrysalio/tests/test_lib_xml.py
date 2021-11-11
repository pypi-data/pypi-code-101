# -*- coding: utf-8 -*-
# pylint: disable = import-outside-toplevel
"""Tests of ``lib.xml`` classes and functions."""

from os.path import join, dirname
from io import BytesIO
from filecmp import cmpfiles
from shutil import copy
from collections import namedtuple
from json import dumps
from unittest import TestCase

from lxml import etree

from pyramid.i18n import TranslationString

from . import TmpDirTestCase


# =============================================================================
class ULibXmlLoadXml(TestCase):
    """Unit test class for :func:`lib.xml.load_xml`."""

    # -------------------------------------------------------------------------
    @classmethod
    def _call_fut(cls, filename, relaxngs='', data=None, xinclude=False):
        """Call function under test."""
        from ..lib.xml import load_xml

        if relaxngs == '':
            relaxngs = {
                'chrysalio': join(
                    dirname(__file__), '..', 'RelaxNG', 'chrysalio.rng')}
        return load_xml(filename, relaxngs, data, False, None, xinclude)

    # -------------------------------------------------------------------------
    def test_unknown_file(self):
        """[u:lib.xml.load_xml] unknown file"""
        tree = self._call_fut(join(dirname(__file__), 'Xml', 'test.usr.xml'))
        self.assertIsInstance(tree, (str, TranslationString))
        self.assertIn('Unknown file', tree)

    # -------------------------------------------------------------------------
    def test_not_well_formed(self):
        """[u:lib.xml.load_xml] not well-formed XML file"""
        from . import TEST1_USR_XML

        tree = self._call_fut(TEST1_USR_XML)
        self.assertIsInstance(tree, str)
        self.assertIn('Opening and ending tag mismatch', tree)

    # -------------------------------------------------------------------------
    def test_data_from_file(self):
        """[u:lib.xml.load_xml] XML data from file"""
        from . import TEST3_USR_XML

        with open(TEST3_USR_XML, 'r') as hdl:
            data = hdl.read()
        if not isinstance(data, bytes):
            data = bytes(data.encode())
        data = etree.parse(BytesIO(data))
        tree = self._call_fut(TEST3_USR_XML, data=data, xinclude=True)
        self.assertNotIsInstance(tree, (str, TranslationString))
        # pylint: disable = no-member
        self.assertEqual(tree.getroot().findtext('user/password'), 'user1pwd')

    # -------------------------------------------------------------------------
    def test_data_from_string(self):
        """[u:lib.xml.load_xml] XML data from string"""
        tree = self._call_fut(
            'test.xml', data='<chrysalio version="1.0"></chrysalio>')
        self.assertNotIsInstance(tree, (str, TranslationString))
        # pylint: disable = no-member
        self.assertEqual(tree.getroot().tag, 'chrysalio')

        tree = self._call_fut(
            'test.xml', data='<chrysalio version="1.0"></chrysalio>')
        self.assertNotIsInstance(tree, (str, TranslationString))
        self.assertEqual(tree.getroot().tag, 'chrysalio')

        tree = self._call_fut(
            'test.xml',
            data=bytes('<chrysalio version="1.0"></chrysalio>'.encode(
                'utf8')))
        self.assertNotIsInstance(tree, (str, TranslationString))
        self.assertEqual(tree.getroot().tag, 'chrysalio')

    # -------------------------------------------------------------------------
    def test_without_relaxng(self):
        """[u:lib.xml.load_xml] without Relax NG"""
        from . import TEST3_USR_XML

        tree = self._call_fut(TEST3_USR_XML, relaxngs=None)
        self.assertNotIsInstance(tree, str)

    # -------------------------------------------------------------------------
    def test_incorrect_xinclude(self):
        """[u:lib.xml.load_xml] incorrect xinclude"""

        data = \
            '<chrysalio version="1.0"'\
            '         xmlns:xi="http://www.w3.org/2001/XInclude">'\
            '  <xi:include href="chrysalio.inc.xml"/>'\
            '</chrysalio>'
        tree = self._call_fut('test.xml', data=data, xinclude=True)
        self.assertIsInstance(tree, str)
        self.assertIn('could not load chrysalio.inc.xml', tree)

    # -------------------------------------------------------------------------
    def test_invalid(self):
        """[u:lib.xml.load_xml] invalid XML file"""
        from . import TEST2_USR_XML

        tree = self._call_fut(TEST2_USR_XML)
        self.assertIsInstance(tree, (str, TranslationString))
        self.assertTrue('Line' in tree)


# =============================================================================
class ULibXmlValidateXml(TestCase):
    """Unit test class for :func:`lib.xml.validate_xml`."""

    # -------------------------------------------------------------------------
    @classmethod
    def _call_fut(cls, filename, relaxngs=None, noline=False):
        """Call function under test."""
        from ..lib.xml import validate_xml

        tree = etree.parse(filename)
        if not relaxngs:
            relaxngs = {
                'chrysalio':
                join(dirname(__file__), '..', 'RelaxNG', 'chrysalio.rng')}
        return validate_xml(tree, relaxngs, noline)

    # -------------------------------------------------------------------------
    def test_invalid(self):
        """[u:lib.xml.validate_xml] invalid XML file"""
        from . import TEST2_USR_XML

        error = self._call_fut(TEST2_USR_XML)
        self.assertIsInstance(error, (str, TranslationString))
        self.assertIn('Line', error)

    # -------------------------------------------------------------------------
    def test_valid(self):
        """[u:lib.xml.validate_xml] valid XML file"""
        from . import TEST3_USR_XML

        error = self._call_fut(TEST3_USR_XML)
        self.assertIsNone(error)

        error = self._call_fut(
            TEST3_USR_XML, relaxngs={
                'chrysalio, version=1.0':
                join(dirname(__file__), '..', 'RelaxNG', 'chrysalio.rng')})
        self.assertIsNone(error)

    # -------------------------------------------------------------------------
    def test_unknown_notfound(self):
        """[u:lib.xml.validate_xml] Relax NG not found"""
        from . import TEST3_USR_XML

        error = self._call_fut(
            TEST3_USR_XML, relaxngs={
                'chrysalio': join(dirname(__file__), 'Xml', 'chrysalio0.rng')})
        self.assertIsInstance(error, str)
        self.assertIn('failed to load', error)

    # -------------------------------------------------------------------------
    def test_unknown_relaxng(self):
        """[u:lib.xml.validate_xml] unknown Relax NG"""
        from . import TEST3_USR_XML

        error = self._call_fut(
            TEST3_USR_XML, relaxngs={
                'chrysalio0': join(dirname(__file__), 'Xml', 'chrysalio0.rng'),
                'chrysalio, version=0.1':
                join(dirname(__file__), 'Xml', 'chrysalio.rng')})
        self.assertIsInstance(error, (str, TranslationString))
        self.assertIn('Relax NG not found', error)

    # -------------------------------------------------------------------------
    def test_invalid_relaxng(self):
        """[u:lib.xml.validate_xml] invalid Relax NG"""
        from . import TEST3_USR_XML

        error = self._call_fut(
            TEST3_USR_XML, relaxngs={
                'chrysalio': join(dirname(__file__), 'Xml', 'chrysalio.rng')})
        self.assertIsInstance(error, str)
        self.assertIn('no matching definition', error)


# =============================================================================
class ULibXmlRelaxng4Validation(TestCase):
    """Unit test class for :func:`lib.xml.relaxng4validation`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:lib.xml.relaxng4validation]"""
        from ..lib.xml import relaxng4validation

        # None as Relax NG
        relaxngs = relaxng4validation(None)
        self.assertIsNone(relaxngs)

        # No namespace, no version
        relaxngs = relaxng4validation({
            'root': 'article',
            'file': join(dirname(__file__), '..', 'RelaxNG', 'article.rng')})
        self.assertIn('article', relaxngs)

        # No namespace, version
        relaxngs = relaxng4validation({
            'root': 'chrysalio', 'version': '1.0',
            'file': join(dirname(__file__), '..', 'RelaxNG', 'chrysalio.rng')})
        self.assertIn('chrysalio, version=1.0', relaxngs)

        # Namespace, no version
        relaxngs = relaxng4validation({
            'namespace': 'http://ns.chrysal.io/cioskeleton',
            'root': 'cioskeleton',
            'file': join(
                dirname(__file__), '..', 'RelaxNG', 'cioskeleton.rng')})
        self.assertIn(
            '{http://ns.chrysal.io/cioskeleton}cioskeleton', relaxngs)

        # Namespace, version
        relaxngs = relaxng4validation({
            'namespace': 'http://ns.chrysal.io/cioprocessor',
            'root': 'cioprocessor', 'version': '1.0',
            'file': join(
                dirname(__file__), '..', 'RelaxNG', 'cioprocessor.rng')})
        self.assertIn(
            '{http://ns.chrysal.io/cioprocessor}cioprocessor, version=1.0',
            relaxngs)


# =============================================================================
class ULibXmlLoadXsl(TestCase):
    """Unit test class for :func:`lib.xml.load_xsl`."""

    # -------------------------------------------------------------------------
    @classmethod
    def _call_fut(cls, filename):
        """Call function under test."""
        from ..lib.xml import load_xslt
        return load_xslt(filename)

    # -------------------------------------------------------------------------
    def test_unknown_xsl(self):
        """[u:lib.xml.load_xsl] unknown XSL file"""
        xslt = self._call_fut(join(dirname(__file__), 'Xml', 'transform0.xsl'))
        self.assertIsInstance(xslt, str)
        self.assertIn('Error reading file', xslt)

    # -------------------------------------------------------------------------
    def test_valid_xsl(self):
        """[u:lib.xml.load_xsl] valid XSL file"""
        from . import TRANSFORM_XSL

        xslt = self._call_fut(TRANSFORM_XSL)
        self.assertNotIsInstance(xslt, str)


# =============================================================================
class ULibXmlCreateEntireXml(TestCase):
    """Unit test class for :func:`lib.xml.create_entire_xml`."""

    # -------------------------------------------------------------------------
    @classmethod
    def _call_fut(cls, elements):
        """Call function under test."""
        from ..lib.xml import create_entire_xml

        relaxng = {
            'root': 'chrysalio', 'version': '1.0',
            'file': join(dirname(__file__), '..', 'RelaxNG', 'chrysalio.rng')}

        return create_entire_xml(relaxng, elements)

    # -------------------------------------------------------------------------
    def test_invalid_element(self):
        """[u:lib.xml.create_entire_xml] invalid element"""
        user_elt = etree.XML(
            '<user>'
            '  <login>test2</login>'
            '  <password>test2pass</password>'
            '  <firstname>Sophie</firstname>'
            '  <lastname>FONFEC</lastname>'
            '  <email>test2_chrysal.io</email>'
            '</user>')

        error = self._call_fut([user_elt])
        # pylint: disable = protected-access
        self.assertNotIsInstance(error, etree._Element)
        # pylint: enable = protected-access
        self.assertIn('email failed to validate', error)

    # -------------------------------------------------------------------------
    def test_one_element(self):
        """[u:lib.xml.create_entire_xml] one element"""
        user_elt = etree.XML(
            '<user>'
            '  <login>test1</login>'
            '  <password>test1pass</password>'
            '  <firstname>Édith</firstname>'
            '  <lastname>AVULEUR</lastname>'
            '  <email>test1@chrysal.io</email>'
            '</user>')

        root_elt = self._call_fut([user_elt])
        # pylint: disable = protected-access
        self.assertIsInstance(root_elt, etree._Element)
        # pylint: enable = protected-access
        # pylint: disable = no-member
        self.assertEqual(root_elt.tag, 'chrysalio')
        self.assertEqual(root_elt.get('version'), '1.0')
        self.assertEqual(root_elt.findtext('user/login'), 'test1')
        self.assertEqual(root_elt.findtext('user/firstname'), 'Édith')

    # -------------------------------------------------------------------------
    def test_several_elements(self):
        """[u:lib.xml.create_entire_xml] several elements"""
        profile_elt = etree.XML(
            '<profile id="user_manager">'
            '  <label xml:lang="en">User manager</label>'
            '  <principals>'
            '    <principal>user.creator</principal>'
            '  </principals>'
            '</profile>')
        user1_elt = etree.XML(
            '<user>'
            '  <login>test1</login>'
            '  <password>test1pass</password>'
            '  <firstname>Édith</firstname>'
            '  <lastname>AVULEUR</lastname>'
            '  <email>test1@chrysal.io</email>'
            '</user>')
        user2_elt = etree.XML(
            '<user>'
            '  <login>test2</login>'
            '  <password>test2pass</password>'
            '  <firstname>Sophie</firstname>'
            '  <lastname>FONFEC</lastname>'
            '  <email>test2@chrysal.io</email>'
            '</user>')

        root_elt = self._call_fut([profile_elt, user1_elt, user2_elt])
        # pylint: disable = protected-access
        self.assertIsInstance(root_elt, etree._Element)
        # pylint: enable = protected-access
        # pylint: disable = no-member
        self.assertEqual(len(root_elt.findall('*')), 2)
        self.assertIsNotNone(root_elt.find('profiles'))
        self.assertIsNotNone(root_elt.find('users'))
        self.assertEqual(len(root_elt.findall('profiles/*')), 1)
        self.assertEqual(len(root_elt.findall('users/*')), 2)

    # -------------------------------------------------------------------------
    def test_settings_element(self):
        """[u:lib.xml.create_entire_xml] settings element"""
        settings_elt = etree.XML(
            '<settings>'
            '  <title>Chrysalio – Test</title>'
            '  <email>admin@chrysal.io</email>'
            '  <password-min-length>8</password-min-length>'
            '  <language>en</language>'
            '  <page-size>80</page-size>'
            '  <download-max-size>10485760</download-max-size>'
            '  <theme>Default</theme>'
            '</settings>')
        profile_elt = etree.XML(
            '<profile id="user_manager">'
            '  <label xml:lang="en">User manager</label>'
            '  <principals>'
            '    <principal>user.creator</principal>'
            '  </principals>'
            '</profile>')

        root_elt = self._call_fut([settings_elt, profile_elt])
        # pylint: disable = protected-access
        self.assertIsInstance(root_elt, etree._Element)
        # pylint: enable = protected-access
        # pylint: disable = no-member
        self.assertEqual(root_elt.tag, 'chrysalio')
        self.assertEqual(root_elt.get('version'), '1.0')
        self.assertEqual(root_elt.findtext(
            'settings/title'), 'Chrysalio – Test')

    # -------------------------------------------------------------------------
    def test_module(self):
        """[u:lib.xml.create_entire_xml] with a module"""
        skeleton_elt = etree.XML(
            '<module id="chrysalio.modules.cioskeleton" inactive="true">'
            '  <cioskeleton xmlns="http://ns.chrysal.io/chrysalio/skeleton"'
            '              version="1.0">'
            '    <bones>'
            '      <bone id="foot">'
            '        <label>Foot</label>'
            '      </bone>'
            '    </bones>'
            '  </cioskeleton>'
            '</module>')
        root = self._call_fut([skeleton_elt])
        self.assertTrue(root.xpath('module'))
        self.assertTrue(
            root.xpath('module[@id="chrysalio.modules.cioskeleton"]'))

        ldap_elt = etree.XML(
            '<module id="chrysalio.modules.ldap" inactive="true"/>')
        root_elt = self._call_fut([ldap_elt, skeleton_elt])
        self.assertTrue(root_elt.xpath('modules'))
        self.assertTrue(root_elt.xpath(
            'modules/module[@id="chrysalio.modules.ldap"]'))
        self.assertTrue(root_elt.xpath(
            'modules/module[@id="chrysalio.modules.cioskeleton"]'))

    # -------------------------------------------------------------------------
    def test_namespace_element(self):
        """[u:lib.xml.create_entire_xml] with namespace"""
        from ..lib.xml import create_entire_xml

        namespace = 'http://ns.chrysal.io/cioskeleton'
        relaxng = {
            'namespace': namespace, 'root': 'cioskeleton', 'version': '1.0',
            'file': join(
                dirname(__file__), '..', 'modules', 'cioskeleton', 'RelaxNG',
                'cioskeleton.rng')}
        skeleton_elt = etree.XML(
            '<bone id="hand">'
            '  <label>Hand</label>'
            '  <attachments key="Hand">'
            '    <picture>hand.png</picture>'
            '  </attachments>'
            '</bone>')

        root_elt = create_entire_xml(relaxng, (skeleton_elt,))
        # pylint: disable = protected-access
        self.assertIsInstance(root_elt, etree._Element)
        # pylint: enable = protected-access
        # pylint: disable = no-member
        self.assertEqual(root_elt.tag, '{{{0}}}cioskeleton'.format(namespace))
        self.assertEqual(root_elt.get('version'), '1.0')
        self.assertTrue(root_elt.xpath(
            'ns0:bones/ns0:bone[@id="hand"]', namespaces={'ns0': namespace}))


# =============================================================================
class ULibXmlI18nXmlText(TestCase):
    """Unit test class for :func:`lib.xml.i18n_xml_text`."""

    # -------------------------------------------------------------------------
    @classmethod
    def _call_fut(cls, root_elt=None, xpath='label'):
        """Call function under test."""
        from . import I18N_XML
        from ..lib.xml import i18n_xml_text

        if root_elt is None:
            tree = etree.parse(I18N_XML)
            root_elt = tree.getroot().find('profile')
        return i18n_xml_text(root_elt, xpath)

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:lib.xml.i18n_xml_text]"""
        labels = self._call_fut()
        self.assertIsInstance(labels, dict)
        self.assertIn('en', labels)
        self.assertIn('fr', labels)
        self.assertEqual(labels['en'], 'Profile Manager')


# =============================================================================
class ULibXmlDb2xmlI18nLabels(TestCase):
    """Unit test class for :func:`lib.xml.db2xml_i18n_labels`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:lib.xml.db2xml_i18n_labels]"""
        from ..lib.xml import db2xml_i18n_labels

        dbitem = namedtuple(
            'DBItem', 'i18n_label i18n_description')(
                i18n_label=dumps({
                    'en': 'Item label', 'fr': "Libellé de l'élément"}),
                i18n_description={'en': 'Item description'})
        root_elt = etree.Element('root')

        db2xml_i18n_labels(dbitem, root_elt, 1)
        self.assertEqual(len(root_elt.xpath('label')), 2)
        self.assertEqual(len(root_elt.xpath('description')), 1)


# =============================================================================
class ULibXmlXmlWrap(TestCase):
    """Unit test class for :func:`lib.xml.xml_wrap`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:lib.xml.xml_wrap]"""
        from ..lib.xml import xml_wrap

        result = xml_wrap(
            'Lorèm ipsum dolor sit amet, consectetur adipiscing elit. '
            'Sed in ultricies ex, ut sollicitudin velit. Praesent semper '
            'venenatis pellentesque.', 2)
        self.assertEqual(
            result,
            '\n      Lorèm ipsum dolor sit amet, consectetur adipiscing '
            'elit. Sed in ultricies\n'
            '      ex, ut sollicitudin velit. Praesent semper venenatis '
            'pellentesque.\n    ')


# =============================================================================
class ULibXmlCheckChrysalioRng(TmpDirTestCase):
    """Unit test class for :func:`lib.xml.check_chrysalio_rng`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:lib.xml.check_chrysalio_rng]"""
        from ..lib.xml import check_chrysalio_rng
        from . import TEST_DIR

        relaxng_dir = TEST_DIR
        cio_relaxng_dir = join(dirname(__file__), '..', 'RelaxNG')
        copy(join(cio_relaxng_dir, 'chrysalio.rnc'),
             join(relaxng_dir, 'chrysalio.rnc'))
        with open(join(relaxng_dir, 'chrysalio.rng'), 'w'):
            pass
        compare = cmpfiles(
            cio_relaxng_dir, relaxng_dir, ('chrysalio.rnc', 'chrysalio.rng'))
        self.assertEqual(compare[0], ['chrysalio.rnc'])
        self.assertEqual(compare[1], ['chrysalio.rng'])
        self.assertEqual(len(compare[2]), 0)

        check_chrysalio_rng(relaxng_dir)

        compare = cmpfiles(
            cio_relaxng_dir, relaxng_dir, ('chrysalio.rnc', 'chrysalio.rng'))
        self.assertEqual(len(compare[0]), 2)
        self.assertEqual(len(compare[1]), 0)
        self.assertEqual(len(compare[2]), 0)
