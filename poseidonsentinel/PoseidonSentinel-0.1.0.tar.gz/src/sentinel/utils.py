from email.message import EmailMessage
import smtplib, ssl
from . import config


def send_email(subject, message):
    print('From package')
    # port = config.EMAIL_SMTP_PORT
    # smtp_server = config.EMAIL_SMTP
    # sender = config.EMAIL_UID
    # password = config.EMAIL_PWD
    # recipient = ['ecms-file-transfers@arizonapipeline.com']

    # msg = EmailMessage()
    # msg['Subject'] = subject
    # msg['From'] = sender
    # msg['To'] = recipient
    # msg.set_content(message)

    # context = ssl.create_default_context()

    # try:
    #     with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    #         server.login(sender, password)
    #         server.sendmail(sender, recipient, msg.as_string())
    #     print('Email Message Sent')
    # except Exception as e:
    #     print(f'Email did not send: {e}')