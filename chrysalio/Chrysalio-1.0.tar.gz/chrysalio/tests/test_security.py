# pylint: disable = import-outside-toplevel
"""Tests of ``security`` classes and functions."""

# pylint: disable = unused-import
from ..models.dbgroup import DBGroup  # noqa
# pylint: enable = unused-import
from . import ConfiguratorTestCase, DBUnitTestCase


# =============================================================================
class USecurityIncludeme(ConfiguratorTestCase):
    """Unit test class for :func:`subscribers.includeme`."""

    # -------------------------------------------------------------------------
    def test_include_security(self):
        """[u:security.includeme]"""
        self.configurator.include('..security')
        authorization_policy = self.configurator.introspector.get(
            'authorization policy', None)
        self.assertIsNotNone(authorization_policy)

        authentication_policy = self.configurator.introspector.get(
            'authentication policy', None)
        self.assertIsNotNone(authentication_policy)

        root_factory = self.configurator.introspector.get(
            'root factories', None).get('factory')
        self.assertGreater(len(root_factory.__acl__), 6)


# =============================================================================
class USecuritySessionAuthenticationPolicy(DBUnitTestCase):
    """Unit test class for :class:`subscribers.SessionAuthenticationPolicy`."""

    # -------------------------------------------------------------------------
    def test_authenticated_userid(self):
        """[u:security.SessionAuthenticationPolicy.authenticated_userid]"""
        from ..security import SessionAuthenticationPolicy

        authentication_policy = SessionAuthenticationPolicy(
            secret='-', hashalg='sha512', cookie_name='CIO_AUTH')

        user_id = authentication_policy.authenticated_userid(self.request)
        self.assertIsNone(user_id)

        self.add_user({
            'login': 'test1', 'last_name': 'Mr Test 1', 'password': 'test1pwd',
            'email': 'test1@chrysal.io'})
        self.configurator.testing_securitypolicy('test1', permissive=True)
        user_id = authentication_policy.authenticated_userid(self.request)
        self.assertEqual(user_id, 1)

        self.request.session['user'] = {'login': 'test1', 'user_id': 2}
        user_id = authentication_policy.authenticated_userid(self.request)
        self.assertEqual(user_id, 2)

        self.add_user({
            'login': 'test2', 'last_name': 'Mr Test 2', 'password': 'test2pwd',
            'email': 'test2@chrysal.io', 'password_mustchange': True})
        self.configurator.testing_securitypolicy('test2', permissive=True)
        self.assertIsNone(
            authentication_policy.authenticated_userid(self.request))

    # -------------------------------------------------------------------------
    def test_effective_principals(self):
        """[u:security.SessionAuthenticationPolicy.effective_principals]"""
        from ..security import SessionAuthenticationPolicy

        authentication_policy = SessionAuthenticationPolicy(
            secret='-', hashalg='sha512', cookie_name='CIO_AUTH')

        principals = authentication_policy.effective_principals(self.request)
        self.assertEqual(len(principals), 1)
        self.assertEqual(principals[0], 'system.Everyone')

        self.add_user({
            'login': 'test2', 'last_name': 'Mr Test 2', 'password': 'test2pwd',
            'email': 'test2@chrysal.io'})
        self.configurator.testing_securitypolicy('test2', permissive=True)
        principals = authentication_policy.effective_principals(self.request)
        self.assertEqual(len(principals), 2)
        self.assertEqual(principals[1], 'system.Authenticated')
