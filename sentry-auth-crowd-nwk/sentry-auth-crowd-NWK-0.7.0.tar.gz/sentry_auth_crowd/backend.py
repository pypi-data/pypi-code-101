# -*- coding: utf-8 -*-
import logging

from django.contrib.auth.backends import ModelBackend
from django.db import transaction

from sentry.models import User, UserEmail, Organization, OrganizationMember
from sentry.models import OrganizationMemberTeam, Team
from sentry.models import AuditLogEntry, AuditLogEntryEvent

import crowd

from .constants import CROWD_URL, CROWD_APP_NAME, CROWD_APP_PASSWORD

def new_user(username, success):
    # see https://github.com/getsentry/sentry/blob/master/src/sentry/auth/helper.py
    name = success['name']
    email = success['email']
    with transaction.atomic():
        user = User.objects.create(
            username=username,
            email=email,
            name=name,
            is_managed=True,
        )

        organization = Organization.get_default()
        om = OrganizationMember.objects.create(
            organization=organization,
            role=organization.default_role,
            user=user,
            flags=OrganizationMember.flags['sso:linked'],
        )

        AuditLogEntry.objects.create(
            organization=organization,
            actor=user,
            # TODO attribute request ip
            #ip=
            target_object=om.id,
            target_user=om.user,
            event=AuditLogEntryEvent.MEMBER_ADD,
            data=om.get_audit_log_data(),
        )
        return user


class SentryCrowdBackend(ModelBackend):
    """
    Mimick email backend and authenticate against Crowd server.

    Auto create account if not exists already.
    """
    # According to https://github.com/getsentry/sentry/blob/21.9.0/src/sentry/conf/server.py
    # Only email backend is supported by "default"
    # See https://github.com/getsentry/sentry/blob/21.9.0/src/sentry/utils/auth.py 
    # for structure of Email backend.
    def __init__(self, *args, **kwargs):
        self._crowd = crowd.CrowdServer(CROWD_URL, CROWD_APP_NAME, CROWD_APP_PASSWORD)
        super(SentryCrowdBackend, self).__init__(*args, **kwargs)

    def authenticate(self, request, username=None, password=None):
        success = self._crowd.auth_user(username, password)
        if success:
            try:
                user = User.objects.filter(is_active=True).exclude(password='!').get(username=username)
            except User.DoesNotExist:
                user = new_user(username, success)
            return user
        return None

    def user_can_authenticate(self, user):
        return True