# -*- coding: utf-8 -*-
# pylint: disable = import-outside-toplevel
"""Tests of ``lib.mailing.Mailing`` class."""

from os.path import basename
from email.mime.text import MIMEText
from unittest import TestCase

from pyramid.testing import DummyRequest


# =============================================================================
class ULibMailingMailing(TestCase):
    """Unit test class for :class:`lib.mailing.Mailing`."""

    # -------------------------------------------------------------------------
    def test_is_valid(self):
        """[u:lib.mailing.Mailing.is_valid]"""
        from ..lib.mailing import Mailing

        self.assertTrue(Mailing.is_valid('foo@chrysal.io'))
        self.assertFalse(Mailing.is_valid('@chrysal.io'))
        self.assertFalse(Mailing.is_valid('foochrysal.io'))
        self.assertFalse(Mailing.is_valid('foo @ chrysal.io'))

    # -------------------------------------------------------------------------
    def test_send(self):
        """[u:lib.mailing.Mailing.send]"""
        from ..lib.utils import decrypt
        from ..lib.mailing import Mailing

        request = DummyRequest()
        request.registry.settings = {'smtp.host':  'chrysalio'}
        email = MIMEText('Hello World!')
        email['From'] = 'admin@chrysal.io'
        email['To'] = 'test@chrysal.io'
        email['Subject'] = '[Chrysalio] Hello'

        # Socket error
        error = Mailing(request).send(email)
        self.assertTrue(
            ('Connection refused' in error) or
            ('Name or service not known' in error) or
            ('No address associated with hostname' in error) or
            ('Temporary failure' in error) or
            ('Connection timed out' in error))

        # Socket error with SSL
        request.registry.settings['smtp.host'] = 'chrysalio'
        request.registry.settings['smtp.ssl'] = 'true'
        error = Mailing(request).send(email)
        self.assertTrue(
            ('Connection refused' in error) or
            ('Name or service not known' in error) or
            ('No address associated with hostname' in error) or
            ('Temporary failure' in error) or
            ('Connection timed out' in error))

        # Connection
        request.registry.settings['smtp.host'] = 'mail.gandi.net'
        request.registry.settings['smtp.ssl'] = 'true'
        request.registry.settings['smtp.user'] = 'test@chrysal.io'
        request.registry.settings['smtp.password'] = decrypt(
            'CQLanGWkUonUrXKYheoQBo0vEtoFMlGuklBS5wIqj/U=', 'warehouse')
        error = Mailing(request).send(email)
        if error:
            return

        # Bad authentication
        request.registry.settings['smtp.password'] = 'foo'
        error = Mailing(request).send(email)
        self.assertIn('authentication failed', error)

    # -------------------------------------------------------------------------
    def test_mailing(self):
        """[u:lib.mailing.Mailing.mailing]"""
        from . import EMAIL_HTML, EMAIL_TEXT, TEST1_SVG
        from ..lib.mailing import Mailing

        request = DummyRequest()
        request.registry.settings = {'smtp.host': 'chrysalio'}
        email_template = {'subject': 'Test', 'from': 'admin@chrysal.io'}
        recipient = {
            'to': 'test1@chrysal.io',
            'first_name': 'Édith',
            'last_name': 'AVULEUR'}

        errors = Mailing(request).mailing(email_template, [recipient])
        self.assertIsInstance(errors, tuple)
        self.assertEqual(len(errors), 1)
        self.assertEqual(errors[0], 'No available template.')

        email_template['html_template'] = EMAIL_HTML
        errors = Mailing(request).mailing(email_template, [recipient])
        self.assertIsInstance(errors, tuple)
        self.assertEqual(len(errors), 1)
        self.assertTrue(
            ('Connection refused' in errors[0]) or
            ('Name or service not known' in errors[0]) or
            ('No address associated with hostname' in errors[0]) or
            ('Temporary failure' in errors[0]) or
            ('Connection timed out' in errors[0]))

        del email_template['html_template']
        email_template['text_template'] = EMAIL_TEXT
        errors = Mailing(request).mailing(email_template, [recipient])
        self.assertTrue(
            ('Connection refused' in errors[0]) or
            ('Name or service not known' in errors[0]) or
            ('No address associated with hostname' in errors[0]) or
            ('Temporary failure' in errors[0]) or
            ('Connection timed out' in errors[0]))

        email_template['html_template'] = EMAIL_HTML
        recipient['attachments'] = ((basename(TEST1_SVG), TEST1_SVG),)
        errors = Mailing(request).mailing(email_template, [recipient])
        self.assertTrue(
            ('Connection refused' in errors[0]) or
            ('Name or service not known' in errors[0]) or
            ('No address associated with hostname' in errors[0]) or
            ('Temporary failure' in errors[0]) or
            ('Connection timed out' in errors[0]))
