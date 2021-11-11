"""Provide the RedditAppMixin class."""
from credmgr.models.utils import CachedProperty


class RedditAppMixin:
    """Interface for classes that have an associated :class:`RedditApp`."""

    _editableAttrs = []

    @CachedProperty
    def redditApp(self):
        """Return the associated :class:`RedditApp`."""
        if not self._fetched:
            self._fetch()
        redditApp = self._credmgr.redditApp(id=self.redditAppId)
        return redditApp
