# -*- coding: utf-8 -*-
from cpskin.core.utils import remove_behavior


def imported_profile(event):
    profile_id = event.profile_id
    if profile_id == "profile-collective.contact.core:default":
        remove_behavior(
            "organization", "collective.contact.core.behaviors.IContactDetails"
        )
