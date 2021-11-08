"""
  @Project     : sentry-dingtalk
  @Time        : 2021/07/12 17:34:35
  @File        : plugin.py
  @Author      : Jedore and Henryhaoson
  @Software    : VSCode
  @Desc        :
"""


import requests
import six
from sentry import tagstore
from sentry.plugins.bases import notify
from sentry.utils import json
from sentry.utils.http import absolute_uri
from sentry.integrations import FeatureDescription, IntegrationFeatures
from sentry_plugins.base import CorePluginMixin
from django.conf import settings


class DingTalkPlugin(CorePluginMixin, notify.NotificationPlugin):
    title = "DingTalk"
    slug = "dingtalk"
    description = "Post notifications to Dingtalk."
    conf_key = "dingtalk"
    required_field = "webhook"
    author = "Henryhaoson"
    author_url = "https://github.com/Henryhaoson/sentry-dingtalk"
    version = "2.0.4"
    resource_links = [
        ("Report Issue", "https://github.com/Henryhaoson/sentry-dingtalk/issues"),
        ("View Source", "https://github.com/Henryhaoson/sentry-dingtalk"),
    ]

    feature_descriptions = [
        FeatureDescription(
            """
                Configure rule based Dingtalk notifications to automatically be posted into a
                specific channel.
                """,
            IntegrationFeatures.ALERT_RULE,
        )
    ]

    def is_configured(self, project):
        return bool(self.get_option("webhook", project))

    def get_config(self, project, **kwargs):
        return [
            {
                "name": "webhook",
                "label": "webhook",
                "type": "url",
                "placeholder": "https://oapi.dingtalk.com/robot/send?access_token=**********",
                "required": True,
                "help": "Your custom DingTalk webhook",
                "default": self.set_default(project, "webhook", "DINGTALK_WEBHOOK"),
            },
            {
                "name": "ats",
                "label": "@成员",
                "type": "string",
                "placeholder": "填写钉钉手机号",
                "required": False,
                "help": "Optional - 填写钉钉手机号，会 @ 对应成员",
                "default": self.set_default(
                    project, "ats", ""
                ),
            },
        ]

    def set_default(self, project, option, env_var):
        if self.get_option(option, project) != None:
            return self.get_option(option, project)
        if hasattr(settings, env_var):
            return six.text_type(getattr(settings, env_var))
        return None

    def notify(self, notification, raise_exception=False):
        event = notification.event
        user = event.get_minimal_user()
        user_id = user.id
        release = event.release
        group = event.group
        project = group.project
        self._post(group, user_id, release, project)

    def _post(self, group, userId, release, project):
        webhook = self.get_option("webhook", project)
        ats_str = self.get_option("ats", project)

        issue_link = group.get_absolute_url(params={"referrer": "dingtalk"})

        payload = f"## Error: [{group.title}]({issue_link}) \n\n"
        payload = f"{payload} #### UserId: [{userId}](https://admin.shanbay.com/jetty/users/{userId}) \n\n"
        payload = f"{payload} #### Project: {project.name} \n\n"
        payload = f"{payload} #### release: {release} \n\n"
        payload = f"{payload} > Detail: {group.message} \n\n"
        payload = f"{payload} @{ats_str} \n\n"

        headers = {
            "Content-type": "application/json",
            "Accept": "text/plain",
            "charset": "utf8"
        }

        data = {
            "msgtype": "markdown",
            "markdown": {
                "title": group.title,
                "text": payload,
            },
            "at": {
                "atMobiles": [ats_str],
                "isAtAll": "false"
            }
        }

        requests.post(webhook, data=json.dumps(data), headers=headers)
