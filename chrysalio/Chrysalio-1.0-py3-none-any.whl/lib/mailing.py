# -*- coding: utf-8 -*-
"""Function to manage e-mails."""

from re import match
from smtplib import SMTP, SMTP_SSL
from smtplib import SMTPSenderRefused, SMTPRecipientsRefused, SMTPConnectError
from smtplib import SMTPHeloError, SMTPAuthenticationError, SMTPException
from socket import error as socket_error
from email import encoders
from email.charset import QP, Charset
from email.mime.nonmultipart import MIMENonMultipart
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import formatdate

from chameleon import PageTemplateFile, PageTextTemplateFile

from pyramid.asset import abspath_from_asset_spec
from pyramid.i18n import TranslationString

from .i18n import _
from .log import log_error


# =============================================================================
class Mailing(object):
    """Class to send one or several mails.

    :type  request: pyramid.request.Request
    :param request:
        Current request.
    """

    # -------------------------------------------------------------------------
    def __init__(self, request):
        """Constructor method."""
        self._request = request
        self._domain = 'chrysalio'

    # -------------------------------------------------------------------------
    @classmethod
    def is_valid(cls, email):
        """Check the validity of an email address.

        :param str email:
            Address to check.
        :rtype: bool
        """
        return match(
            r'^[a-zA-Z0-9._%-]+@[a-zA-Z0-9._%-]+\.[a-zA-Z]{2,6}$', email)

    # -------------------------------------------------------------------------
    def send(self, email):
        """Send an email.

        :type  email: email.message.Message
        :param email:
            MIME type object to send.
        :rtype: :class:`str` or ``None``
        """
        settings = self._request.registry.settings
        try:
            if settings.get('smtp.ssl') == 'true':
                smtp = SMTP_SSL(
                    settings.get('smtp.host', 'localhost'),
                    int(settings.get('smtp.port', 465)))
            else:
                smtp = SMTP(
                    settings.get('smtp.host', 'localhost'),
                    int(settings.get('smtp.port', 25)))
        except SMTPConnectError as error:  # pragma: nocover
            log_error(self._request, error)
            return error
        except socket_error as error:
            log_error(self._request, error.strerror or error)
            return error.strerror or error

        if settings.get('smtp.user') and settings.get('smtp.password'):
            try:
                smtp.login(settings['smtp.user'], settings['smtp.password'])
            except (SMTPHeloError, SMTPAuthenticationError,
                    SMTPException) as error:
                smtp.quit()
                log_error(self._request, str(error))
                return str(error)

        try:
            smtp.sendmail(email['From'], email['To'], email.as_string())
        except (SMTPSenderRefused,
                SMTPRecipientsRefused) as error:  # pragma: nocover
            log_error(self._request, error)
            return error
        finally:
            smtp.quit()
        return None

    # -------------------------------------------------------------------------
    def mailing(self, email_template, recipients):
        """Send an e-mail to several users according to a HTML and a text
        template.

        :param dict email_template:
            A dictionary containing the e-mail parameters. The keys of this
            dictionary are: ``subject``, ``from``, ``text_template``,
            ``html_tempalte``, ``attachments``. ``subject`` can be overridden
            by the user dictionary.
        :param list recipients:
            A list of recipients to whom to send the e-mail. Each recipient is
            a dictionary containing at least the ``to`` key. It is passed to
            the Chameleon ``html`` and ``text`` templates.
        :rtype: tuple
        :return:
            List of errors.
        """
        # Prepare templates
        templates = {}
        if 'html_template' in email_template:
            path = email_template['html_template']
            templates['html'] = (
                PageTemplateFile(abspath_from_asset_spec(path)),
                ':' in path and path.partition(':')[0] or 'chrysalio')
        if 'text_template' in email_template:
            path = email_template['text_template']
            templates['text'] = (
                PageTextTemplateFile(abspath_from_asset_spec(path)),
                ':' in path and path.partition(':')[0] or 'chrysalio')
        if not templates:
            log_error(self._request, 'No available template.')
            return (_('No available template.'),)
        translate = self._request.localizer.translate
        email_template['subject'] = translate(email_template['subject'])
        email_template['locale_name'] = self._request.locale_name
        email_template['_'] = self._template_translate

        # Browse recipients
        errors = set()
        for recipient in recipients:
            context = email_template.copy()
            context.update(recipient)
            if 'attachments' in email_template or 'attachments' in recipient:
                email = MIMEMultipart()
                email.preamble = \
                    'This is a multi-part message in MIME format.\n'
                email.attach(self._mime_text(templates, context))
                for item in tuple(recipient.get('attachments', '')) + tuple(
                        email_template.get('attachments', '')):
                    part = MIMEBase('application', 'octet-stream')
                    with open(item[1], 'rb') as hdl:
                        part.set_payload(hdl.read())
                        encoders.encode_base64(part)
                    part.add_header(
                        'Content-Disposition',
                        'attachment; filename= {0}'.format(item[0]))
                    email.attach(part)
            else:
                email = self._mime_text(templates, context)

            email['Subject'] = context['subject']
            email['From'] = email_template['from']
            email['To'] = recipient['to']
            email['Date'] = formatdate()
            errors.add(self.send(email))

        return errors and errors != set((None,)) and tuple(errors)

    # -------------------------------------------------------------------------
    def _mime_text(self, templates, context):
        """Return a simple or a multi-part MIME object according to
        ``templates``.

        :param dict templates:
            A dictionary with keys ``text`` and/or ``html``.
        :param dict context:
            Parameters for templates.
        :rtype: :class:`email.mime.multipart.MIMEMultipart` or
            :class:`email.mime.text.MIMETest`
        """
        if len(templates) > 1:
            mime = MIMEMultipart('alternative')
            mime.preamble = 'This is a multi-part message in MIME format.\n'
            self._domain = templates['text'][1]
            mime.attach(self._mime_quoted_printable(
                templates['text'][0](**context)))
            self._domain = templates['html'][1]
            mime.attach(self._mime_quoted_printable(
                templates['html'][0](**context), 'html'))

        elif 'html' in templates:
            self._domain = templates['html'][1]
            mime = self._mime_quoted_printable(
                templates['html'][0](**context), 'html')

        else:
            self._domain = templates['text'][1]
            mime = self._mime_quoted_printable(
                templates['text'][0](**context))

        # Save HTML part in a file
        # if 'html' in templates:
        #     from os.path import dirname, join
        #     self._domain = templates['html'][1]
        #     with open(join(dirname(__file__),
        #                    '..', '..', 'email~.html'), 'w') as hdl:
        #         hdl.write(templates['html'][0](**context))

        return mime

    # -------------------------------------------------------------------------
    @classmethod
    def _mime_quoted_printable(cls, payload, subtype='plain'):
        """Encode MIMEText as quoted printables.

        :param str payload:
            Text to encode
        :param str subtype: (default='plain')
            Subtype for the text.
        :rtype: email.mime.nonmultipart.MIMENonMultipart
        """
        charset = Charset('utf-8')
        charset.header_encoding = QP
        charset.body_encoding = QP
        mime = MIMENonMultipart('text', subtype, charset='utf-8')
        mime.set_payload(payload, charset)
        return mime

    # -------------------------------------------------------------------------
    def _template_translate(self, text, mapping=None, domain=None):
        """Translation from a string for templating system."""
        return self._request.localizer.translate(TranslationString(
            text, mapping=mapping, domain=domain or self._domain))
