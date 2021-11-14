from django.test import TestCase

from django_site_variables.helper import get_site_variable, get_many_site_variables
from django_site_variables.models import SiteVariable


class DjangoSiteSettingsTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        SiteVariable.objects.create(
            content=str(123),
            name='test1',
            value_type=SiteVariable.TYPE_NUMBER
        )
        SiteVariable.objects.create(
            content=str(True),
            name='test2',
            value_type=SiteVariable.TYPE_BOOLEAN
        )
        SiteVariable.objects.create(
            content='is_am_variable',
            name='test3',
            value_type=SiteVariable.TYPE_TEXT
        )

    def test_get_site_variable_int(self):
        self.assertEqual(get_site_variable('test1'), 123)

    def test_get_site_variable_bool(self):
        self.assertTrue(get_site_variable('test2'))

    def test_get_site_variable_str(self):
        self.assertEqual(get_site_variable('test3'), 'is_am_variable')

        print(get_many_site_variables('test1', 'test2'))
