import os
import re
import json
import logging
import boto3
import requests

from importlib import import_module

from alira.instance import Instance
from alira.modules.redis import RedisModule, ServiceException

from botocore.exceptions import ClientError, EndpointConnectionError

from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException


PIPELINE_EMAIL_MODULE_NAME = "alira.modules.notification.email"
PIPELINE_SMS_MODULE_NAME = "alira.modules.notification.sms"


class Notification(RedisModule):
    def __init__(
        self,
        module_id: str,
        model_identifier: str,
        configuration_directory: str,
        redis_server: str = None,
        filtering: str = None,
    ):
        super().__init__(
            module_id=module_id,
            model_identifier=model_identifier,
            configuration_directory=configuration_directory,
            redis_server=redis_server,
        )

        self.filtering = self._load_function(filtering)

    def _load_template(self, instance: Instance, template_file):
        try:
            with open(
                os.path.join(self.configuration_directory, template_file),
                encoding="UTF-8",
            ) as file:
                template = file.read()

            variables_pattern = re.compile(r"\[\[([A-Za-z0-9_.]+)\]\]")

            variables = variables_pattern.findall(template)
            for variable in variables:
                template = template.replace(
                    f"[[{variable}]]", str(instance.get_attribute(variable, default=""))
                )

            return template

        except FileNotFoundError:
            logging.info(f"Template file {template_file} not found")
            return None
        except Exception as e:
            logging.exception(e)
            return None


class EmailNotification(Notification):
    def __init__(
        self,
        model_identifier: str,
        configuration_directory: str,
        sender: str,
        recipients: list,
        subject: str,
        template_html_filename: str,
        template_text_filename: str,
        redis_server: str = None,
        filtering: str = None,
        provider=None,
        **kwargs,
    ):
        super().__init__(
            module_id=PIPELINE_EMAIL_MODULE_NAME,
            model_identifier=model_identifier,
            configuration_directory=configuration_directory,
            redis_server=redis_server,
            filtering=filtering,
        )

        self.sender = sender
        self.recipients = recipients
        self.template_html_filename = template_html_filename
        self.template_text_filename = template_text_filename
        self.subject = subject

        self.provider = provider or AwsSesEmailNotificationProvider(**kwargs)

    def run(self, instance: Instance, **kwargs) -> dict:
        if self.filtering and not self.filtering(instance):
            logging.info(
                f"The instance didn't pass the filtering criteria. Instance: {instance}"
            )
            return {"status": "SKIPPED"}

        if not hasattr(self.provider, "send_email") or not callable(
            self.provider.send_email
        ):
            logging.info("The specified provider is not valid")
            return {
                "status": "FAILURE",
                "message": "Specified provider is not valid",
            }

        template_text = self._load_template(instance, self.template_text_filename)
        if not template_text:
            logging.info("Couldn't load the template text file")
            return {
                "status": "FAILURE",
                "message": "Couldn't load the template text file",
            }

        template_html = self._load_template(instance, self.template_html_filename)
        if not template_html:
            logging.info("Couldn't load the template html file")
            return {
                "status": "FAILURE",
                "message": "Couldn't load the template html file",
            }

        logging.info(
            f"Sending an email with provider {self.provider.__class__.__name__}"
        )

        arguments = {
            "sender": self.sender,
            "recipients": self.recipients,
            "subject": self.subject,
            "template_text": template_text,
            "template_html": template_html,
        }

        try:
            queue = self.get_redis_queue()
            if queue:
                queue.enqueue(self.provider.send_email, **arguments)
            else:
                self.provider.send_email(
                    sender=self.sender,
                    recipients=self.recipients,
                    subject=self.subject,
                    template_text=template_text,
                    template_html=template_html,
                )
        except Exception as e:
            logging.exception("There was an error sending the notification email")

        return {"status": "SUCCESS"}


class SmsNotification(Notification):
    def __init__(
        self,
        model_identifier: str,
        configuration_directory: str,
        sender: str,
        recipients: list,
        template_text_filename: str,
        redis_server: str = None,
        filtering: str = None,
        image: str = None,
        provider=None,
        **kwargs,
    ):
        super().__init__(
            module_id=PIPELINE_SMS_MODULE_NAME,
            model_identifier=model_identifier,
            configuration_directory=configuration_directory,
            redis_server=redis_server,
            filtering=filtering,
        )

        self.sender = sender
        self.recipients = recipients
        self.template_text_filename = template_text_filename
        self.image = image

        self.provider = provider or TwilioSmsNotificationProvider(**kwargs)

    def run(self, instance: Instance, **kwargs):
        if self.filtering and not self.filtering(instance):
            logging.info(
                f"The instance didn't pass the filtering criteria. Instance: {instance}"
            )
            return {"status": "SKIPPED"}

        if not hasattr(self.provider, "send_sms") or not callable(
            self.provider.send_sms
        ):
            logging.info("The specified provider is not valid")
            return {
                "status": "FAILURE",
                "message": "Specified provider is not valid",
            }

        template_text = self._load_template(instance, self.template_text_filename)
        if not template_text:
            logging.info("Couldn't load the template text file")
            return {
                "status": "FAILURE",
                "message": "Couldn't load the template text file",
            }

        logging.info(f"Sending SMS with provider {self.provider.__class__.__name__}")

        image_url = instance.get_attribute(self.image, default=None)
        logging.info(f"Image included in message: {image_url}")

        arguments = {
            "sender": self.sender,
            "recipients": self.recipients,
            "message": template_text,
            "image": image_url,
        }

        try:
            queue = self.get_redis_queue()
            if queue:
                queue.enqueue(self.provider.send_sms, **arguments)
            else:
                self.provider.send_sms(**arguments)
        except Exception as e:
            logging.exception("There was an error sending the SMS")

        return {"status": "SUCCESS"}


class SocketIO(object):
    def __init__(
        self,
        model_identifier: str,
        endpoint: str,
        event: str = "dispatch",
        **kwargs,
    ):
        self.model_identifier = model_identifier
        self.endpoint = endpoint
        self.event = event

    def run(self, instance: Instance, **kwargs):
        payload = {
            "message": "pipeline-new-instance",
            "data": instance.__dict__,
            "pipeline_id": self.model_identifier,
        }

        self.emit(self.event, payload)

        return None

    def emit(self, event: str, payload=None):
        if not self.endpoint:
            return

        logging.info(
            f"Sending Socket IO notification to {self.endpoint}. Namespace: {self.model_identifier}"
        )

        payload["event"] = event
        payload["namespace"] = self.model_identifier

        try:
            requests.post(
                url=self.endpoint,
                data=json.dumps(payload),
                headers={"Content-type": "application/json"},
            )
        except Exception:
            logging.exception("There was an error sending the socket io notification")


class TwilioSmsNotificationProvider(object):
    def __init__(self, account_sid: str, auth_token: str, **kwargs):
        self.account_sid = account_sid
        self.auth_token = auth_token

    def send_sms(
        self,
        sender: str,
        recipients: list,
        message: str,
        image: str = None,
        **kwargs,
    ):
        logging.info("Sending message using Twilio")

        for phone_number in recipients:
            try:
                logging.info(
                    f"Sending message to '{phone_number}': Message -> '{message}'..."
                )
                self.send_message(sender, phone_number, message, image)

            except TwilioRestException as e:
                raise ServiceException(e)
            except Exception as e:
                print(e)
                logging.exception(e)

        return None

    def send_message(
        self,
        phone_number_origin: str,
        phone_number_dest: str,
        message: str,
        media_url: str = None,
    ):
        client = Client(self.account_sid, self.auth_token)
        arguments = {
            "to": phone_number_dest,
            "from_": phone_number_origin,
            "body": message,
        }

        if media_url:
            arguments["media_url"] = [media_url]

        return client.messages.create(**arguments)


class AwsSesEmailNotificationProvider(object):
    def __init__(
        self, aws_access_key: str, aws_secret_key: str, aws_region_name: str, **kwargs
    ):
        self.aws_access_key = aws_access_key
        self.aws_secret_key = aws_secret_key
        self.aws_region_name = aws_region_name

    def send_email(
        self,
        sender: str,
        recipients: list,
        subject: str,
        template_text: str,
        template_html: str,
    ):
        payload = {
            "Destination": {"ToAddresses": recipients},
            "Message": {
                "Body": {
                    "Html": {"Charset": "UTF-8", "Data": template_html},
                    "Text": {"Charset": "UTF-8", "Data": template_text},
                },
                "Subject": {"Charset": "UTF-8", "Data": subject},
            },
            "Source": sender,
        }

        try:
            logging.info(
                (
                    "Sending an email using AWS SES Service... \n"
                    f"Sender: {sender}\n"
                    f"Recipients: {recipients}\n"
                    f"Subject: {subject}"
                )
            )

            client = boto3.client(
                "ses",
                aws_access_key_id=self.aws_access_key,
                aws_secret_access_key=self.aws_secret_key,
                region_name=self.aws_region_name,
            )

            client.send_email(**payload)

        except EndpointConnectionError as e:
            logging.exception(e)

            raise ServiceException(e)
        except ClientError as e:
            logging.exception(e)
        except Exception as e:
            logging.exception(e)
