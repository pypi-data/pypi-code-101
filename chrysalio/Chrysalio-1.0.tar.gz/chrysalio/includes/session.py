"""Pyramid session functionality."""

from pyramid.session import SignedCookieSessionFactory
from pyramid.session import JSONSerializer, PickleSerializer
from pyramid.config import Configurator


# =============================================================================
def includeme(configurator):
    """Function to include session from Pyramid.

    :type  configurator: pyramid.config.Configurator
    :param configurator:
        Object used to do configuration declaration within the application.
    """
    if isinstance(configurator, Configurator):
        configurator.set_session_factory(
            SignedCookieSessionFactory(
                configurator.get_settings().get(
                    'site.uid', 'chrysalio_sekret'),
                serializer=JSONSerializerWithPickleFallback()))


# =============================================================================
class JSONSerializerWithPickleFallback(object):
    """To support upcoming changes to ISession in Pyramid 2.0."""

    # -------------------------------------------------------------------------
    def __init__(self):
        """Constructor method."""
        self.json = JSONSerializer()
        self.pickle = PickleSerializer()

    # -------------------------------------------------------------------------
    def dumps(self, value):
        """Serialize obj to a JSON formatted str."""
        return self.json.dumps(value)

    # -------------------------------------------------------------------------
    def loads(self, value):
        """Deserialize s (a str, bytes or bytearray instance containing a JSON
        document) to a Python object.
        """
        try:
            return self.json.loads(value)
        except ValueError:  # pragma: nocover
            return self.pickle.loads(value)
