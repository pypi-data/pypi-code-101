from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver

from ucamlookup.models import LookupGroup
from ucamlookup.utils import (return_title_by_groupid,
                              return_visibleName_by_crsid)


@receiver(pre_save, sender=User)
def add_user_attrs(instance, **kwargs):
    user = instance
    if user is not None:

        # It is tempting to populate the Django User first name, last name,
        # and email from lookup, but given their visibility setting this seems
        # not to be always feasible. That's why we rely on the lookup visible name
        # for comms with the users so that's retrieved and stored in User last name
        # attribute.
        user.last_name = return_visibleName_by_crsid(user.username)[:30]

        # Email is required to 'social_core.pipeline.social_auth.associate_by_email'
        # social auth pipeline to associate the social user to the existing Django User.
        # So, it should be populated. We use the canonical email format: crsid@cam.ac.uk.
        user.email = user.username + '@cam.ac.uk'

        # If first_name is not set, social_core.pipeline.user.user_details
        # social auth pipeline will update it and eventually we may end up with
        # confusing information where there are redundant details in Django
        # User first name and last name. Set it to '' to prevent this.
        user.first_name = ''


@receiver(pre_save, sender=LookupGroup)
def add_title_to_group(instance, **kwargs):
    group = instance
    if group is not None:
        group.name = return_title_by_groupid(group.lookup_id)[:80]
