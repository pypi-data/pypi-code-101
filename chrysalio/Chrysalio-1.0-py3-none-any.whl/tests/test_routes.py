# pylint: disable = import-outside-toplevel
"""Tests of ``routes`` classes and functions."""

from . import ConfiguratorTestCase


# =============================================================================
class URoutesIncludeme(ConfiguratorTestCase):
    """Unit test class for :func:`routes.includeme`."""

    # -------------------------------------------------------------------------
    def test_include_routes(self):
        """[u:routes.includeme]"""
        self.configurator.include('..routes')
        self.assertIsNotNone(
            self.configurator.registry.introspector.get('routes', 'home'))
