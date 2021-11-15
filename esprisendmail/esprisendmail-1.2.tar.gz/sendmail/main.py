#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
    :platform: Unix
    :synopsis: Mail sender to notify ESPRI users.

"""

import os
import re
import sys
from argparse import ArgumentParser
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP

from jinja2 import Environment, FileSystemLoader, select_autoescape
from yaml import safe_load, YAMLError

# Make a regular expression for validating an e-mail address
MAIL_SYNTAX = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


class Mail(object):
    """
    Class handling e-mail content.

    """

    def __init__(self, sender, template):

        # Sender.
        self.sender = re.fullmatch(MAIL_SYNTAX, sender).string

        # Recipient.
        self.recipients = list()

        # Template.
        self.tmpl = template

        # Subject.
        self.subject = None

        # Message.
        self.body = None

    def __enter__(self):
        """
        Returns the alert context depending on its type.

        """
        if not self.tmpl:
            ctx = dict()

            # Prompt user to get recipients.
            ctx['recipients'] = []
            while True:
                recipient = str(input('Add a recipients address (let empty to stop): '))
                if len(recipient.strip()):
                    ctx['recipients'].append(recipient)
                else:
                    break

            # Prompt user to get subject severity flag.
            ctx['severity'] = input('Severity flag to prepend to the subject of the email: ')

            # Prompt user to get e-mail subject.
            ctx['subject'] = input('Subject of the email: ')

            # Prompt user to get e-mail message.
            ctx['message'] = input('Message of the email: ')

            # Prompt user to get start and end date and time.
            ctx['date'] = dict()
            ctx['date']['from'] = input(
                'Start date and time in the format "DD-MM-YYYY HH:MM" (let empty to set starting date now): ')
            ctx['date']['to'] = input(
                'End date and time in the format "DD-MM-YYYY HH:MM" (let empty to set end date unknown): ')

            # Prompt user to get affected data paths.
            ctx['affected_data'] = []
            while True:
                path = str(input('Add an affected data path (optional - let empty to stop): '))
                if len(path.strip()):
                    ctx['affected_data'].append(path)
                else:
                    break

            # Prompt user to get affected server urls.
            ctx['affected_servers'] = []
            while True:
                url = str(input('Add an affected server url (optional - let empty to stop): '))
                if len(url.strip()):
                    ctx['affected_servers'].append(url)
                else:
                    break

        # If template selected get information from it.
        else:
            with open(os.path.join(os.path.dirname(__file__), 'contents', '{}.yaml'.format(self.tmpl)),
                      "r") as yaml_file:
                try:
                    # Load YAML content
                    ctx = safe_load(yaml_file)
                except YAMLError as error:
                    print(error)

        # Check recipients address syntax.
        for recipient in ctx['recipients']:
            self.recipients.append(re.fullmatch(MAIL_SYNTAX, recipient).string)

        # Prepend severity flag to subject
        self.subject = '[{}] {}'.format(ctx['severity'].upper(), ctx['subject'])

        # Convert dates into datetime objects if exists and reformat.
        if ctx['date']['from']:
            ctx['date']['from'] = datetime.strptime(ctx['date']['from'], '%d-%m-%Y %H:%M')
        else:
            ctx['date']['from'] = datetime.now()
        ctx['date']['from'] = ctx['date']['from'].strftime('%A, %d %B %Y, %I:%M %p')

        if ctx['date']['to']:
            ctx['date']['to'] = datetime.strptime(ctx['date']['to'], '%d-%m-%Y %H:%M')
            ctx['date']['to'] = ctx['date']['to'].strftime('%A, %d %B %Y, %I:%M %p')
        else:
            ctx['date']['to'] = 'Unknown'

        # Instantiate Jinja template environment.
        env = Environment(
            loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')),
            autoescape=select_autoescape())

        # Get appropriate template // TODO: select template according to available choices.
        template = env.get_template('info.html')

        # Rendering the HTML Jinja template with YAML context.
        self.body = template.render(ctx)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def generate(self):
        """
        Generate HTML body to be sent through SMTP

        """
        message = MIMEMultipart()
        message['Subject'] = self.subject
        message['From'] = self.sender
        message['To'] = ', '.join(self.recipients)
        message.attach(MIMEText(self.body, "html"))
        return message.as_string()


def get_args():
    """
    Returns parsed command-line arguments.

    """
    # Argument parser.
    parser = ArgumentParser(
        prog='ESPRI info sender',
        description='CLI to send mail alerts to ESPRI users',
        add_help=True)
    parser.add_argument(
        '-v', '--version',
        action='version',
        version='1.0',
        help='Program version.')
    parser.add_argument(
        '-t', '--template',
        default=None,
        nargs='?',
        choices=get_alert_types(),
        type=str,
        help="""
             Choose a type of alert with pre-configured context. Available types are: {}.
             If no type (the default), the mail context is prompted for interactively.
             
             """.format(', '.join(get_alert_types())))
    return parser.parse_args()


def get_alert_types():
    """
    Returns the different types of mail to send.

    """
    contents_path = os.path.join(os.path.dirname(__file__), 'contents')
    return [os.path.splitext(i)[0] for i in os.listdir(contents_path)]


def main():
    """
    Run main program

    """
    # Get command-line arguments.
    args = get_args()

    # Get SMTP configuration.
    with open(os.path.join(os.path.dirname(__file__), 'smtp.yaml')) as yaml_file:
        try:
            smtp = safe_load(yaml_file)
        except YAMLError as error:
            print(error)

    # SMTP server connection.
    server = SMTP(host=smtp['host'],
                  port=smtp['port'])
    server.starttls()

    # SMTP server authentication.
    sender = input('Enter your login address: ')
    server.login(user=sender,
                 password=input('Enter your password: '))

    # Create & send email.
    with Mail(sender=sender, template=args.template) as mail:

        # Send mail.
        server.sendmail(from_addr=mail.sender,
                        to_addrs=mail.recipients,
                        msg=mail.generate())
        # Success.
        print('E-mail notification sent. Summary:')
        print('Sender: {}'.format(mail.sender))
        print('Subject: {}'.format(mail.subject))
        print('Recipients: {}'.format(', '.join(mail.recipients)))

    # Close SMTP server connection.
    server.quit()


if __name__ == "__main__":
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
    main()
