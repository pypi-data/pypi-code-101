"""CioLDAP secutity functionalities."""

from ...lib.i18n import _
from ...lib.config import update_acl


PRINCIPALS_CIOLDAP = (
    ('cioldap', _('CioLDAP module management'), (
        ('viewer', _('View CioLDAP configuration'), ('cioldap-view',)),
        ('editor', _('Edit or view CioLDAP configuration'), (
            'cioldap-edit', 'cioldap-view'))
    )),
)


# =============================================================================
def includeme(configurator):
    """Function to include security.

    :type  configurator: :class:`pyramid.config.Configurator`
    :param configurator:
        Object used to do configuration declaration within the application.
    """
    update_acl(configurator, PRINCIPALS_CIOLDAP)
