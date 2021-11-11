# pylint: disable = import-outside-toplevel
"""Tests of ``lib.attachment`` functions."""

from os.path import exists, join, dirname
from unittest import TestCase
from cgi import FieldStorage

from pyramid import testing
from pyramid.testing import DummyRequest

from . import TmpDirTestCase


# =============================================================================
class ULibAttachmentAttachmentUrl(TestCase):
    """Unit test class for :func:`lib.attachment.attachment_url`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:lib.attachment.attachment_url]"""
        from ..lib.attachment import attachment_url

        request = testing.DummyRequest()
        request.registry.settings = {}
        self.assertIsNone(
            attachment_url(request, 'Users', None, 'test5.svg'))
        self.assertIsNone(
            attachment_url(request, 'Users', 'Test5', None))
        self.assertIsNone(
            attachment_url(request, 'Users', 'Test5', 'test5.svg'))

        configurator = testing.setUp(settings={
            'attachments': join(dirname(__file__), 'Attachments')})
        configurator.add_route('attachment', '/attachment/*path')
        self.assertIsNone(
            attachment_url(request, 'Users', 'Test5', 'test4.svg'))
        self.assertEqual(
            attachment_url(request, 'Users', 'Test5', 'test5.svg'),
            '/attachment/Users/Test5/test5.svg')


# =============================================================================
class ULibAttachmentAttachmentUpdate(TmpDirTestCase):
    """Unit test class for :func:`lib.attachment.attachment_update`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:lib.attachment.attachment_update]"""
        from . import TEST_DIR, TEST1_SVG
        from ..lib.attachment import attachment_update

        request = DummyRequest()
        request.registry.settings = {}
        attachments_key, file_path = attachment_update(
            request, 'Users', None, FieldStorage(), 'test1.svg')
        self.assertIsNone(attachments_key)
        self.assertEqual(file_path, 'test1.svg')

        request.registry.settings = {'attachments': TEST_DIR}
        with open(TEST1_SVG, 'rb') as hdl:
            input_file = FieldStorage()
            input_file.filename = TEST1_SVG
            input_file.file = hdl
            attachments_key, file_path = attachment_update(
                request, 'Users', None, input_file)
        self.assertFalse(request.session.pop_flash('alert'))
        self.assertIsNotNone(attachments_key)
        self.assertNotEqual(attachments_key, 'Test1')
        self.assertIsNotNone(file_path)
        self.assertTrue(exists(join(
            TEST_DIR, 'Users', attachments_key, file_path)))

        with open(TEST1_SVG, 'rb') as hdl:
            input_file = FieldStorage()
            input_file.filename = TEST1_SVG
            input_file.file = hdl
            attachments_key2, file_path2 = attachment_update(
                request, 'Users', attachments_key, input_file, file_path)
        self.assertEqual(attachments_key, attachments_key2)
        self.assertNotEqual(file_path, file_path2)
        self.assertFalse(exists(join(
            TEST_DIR, 'Users', attachments_key2, file_path)))
        self.assertTrue(exists(join(
            TEST_DIR, 'Users', attachments_key2, file_path2)))

        with open(TEST1_SVG, 'rb') as hdl:
            input_file = FieldStorage()
            input_file.filename = TEST1_SVG
            input_file.file = hdl
            attachments_key, file_path = attachment_update(
                request, 'Users', 'Test1', input_file, file_path)
        self.assertEqual(attachments_key, 'Test1')
        self.assertIsNotNone(file_path)
