"""Provide the OwnerMixin class."""
from credmgr.models.utils import CachedProperty


class OwnerMixin:
    """Interface for classes that have an owner."""

    _editableAttrs = []

    @CachedProperty
    def owner(self):
        """Get the owner of the object."""
        if not self._fetched:
            self._fetch()
        user = self._credmgr.user(id=self.ownerId)
        return user
