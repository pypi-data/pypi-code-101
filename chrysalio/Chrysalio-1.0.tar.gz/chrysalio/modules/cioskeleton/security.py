"""CioSkeleton secutity functionalities."""

from ...lib.i18n import _
from ...lib.config import update_acl


PRINCIPALS_CIOSKELETON = (
    ('mode', _('Mode management'), (
        ('skeleton', _('Access to skeleton mode'), ('mode-skeleton',)),
    )),
    ('bone', _('Bone management'), (
        ('viewer', _('View bone'), ('bone-view',)),)))


# =============================================================================
def includeme(configurator):
    """Function to include security.

    :type  configurator: pyramid.config.Configurator
    :param configurator:
        Object used to do configuration declaration within the application.
    """
    update_acl(configurator, PRINCIPALS_CIOSKELETON)
