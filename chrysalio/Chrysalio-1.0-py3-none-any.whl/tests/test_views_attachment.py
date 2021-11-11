# pylint: disable = import-outside-toplevel
"""Tests of ``views.attachment`` functions."""

from . import DBUnitTestCase


# =============================================================================
class UViewsAttachmentAttchment(DBUnitTestCase):
    """Unit test class for testing :func:`views.attachment.attachment`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:views.attachment.attachment]"""
        from os.path import join, dirname
        from pyramid.response import FileResponse
        from pyramid.httpexceptions import HTTPNotFound
        from ..views.attachment import attachment

        self.assertRaises(HTTPNotFound, attachment, self.request)

        self.configurator.get_settings()['attachments'] = join(
            dirname(__file__), 'Attachments')
        self.request.matchdict = {'path': ('Users', 'Test1', 'test5.svg')}
        self.assertRaises(HTTPNotFound, attachment, self.request)

        self.request.matchdict = {'path': ('Users', 'Test5', 'test5.svg')}
        response = attachment(self.request)
        self.assertIsInstance(response, FileResponse)
        self.assertEqual(response.status_code, 200)


# =============================================================================
class UViewsAttachmentFavicon(DBUnitTestCase):
    """Unit test class for testing :func:`views.attachment.favicon`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:views.attachment.favicon]"""
        from os.path import join, dirname
        from pyramid.response import FileResponse
        from ..views.attachment import favicon

        response = favicon(self.request)
        self.assertIsInstance(response, FileResponse)
        self.assertEqual(response.status_code, 200)

        self.request.registry.settings['site.favicon'] = join(
            dirname(__file__), '..', 'Static', 'favicon.ico')
        response = favicon(self.request)
        self.assertIsInstance(response, FileResponse)
        self.assertEqual(response.status_code, 200)


# =============================================================================
class UViewsAttachmentRobots(DBUnitTestCase):
    """Unit test class for testing :func:`views.attachment.robots`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:views.attachment.robots]"""
        from os.path import join, dirname
        from pyramid.response import FileResponse
        from ..views.attachment import robots

        response = robots(self.request)
        self.assertIsInstance(response, FileResponse)
        self.assertEqual(response.status_code, 200)

        self.request.registry.settings['site.robots'] = join(
            dirname(__file__), '..', 'Static', 'robots.txt')
        response = robots(self.request)
        self.assertIsInstance(response, FileResponse)
        self.assertEqual(response.status_code, 200)
