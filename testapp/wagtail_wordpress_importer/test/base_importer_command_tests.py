from django.test import SimpleTestCase
from wagtail_wordpress_importer.cls.base_importer_command import BaseImporterCommand


class SampleCommandOverridden(BaseImporterCommand):

    api_url = 'https://www.sample.com'
    api_endpoint = 'wp-json/wp/v2/sample'
    api_sub_sites = ['sample']

    def save_data(self, data, subsite):
        pass


class SampleCommandDefault(BaseImporterCommand):

    def save_data(self, data, subsite):
        pass


class BaseImporterTestCase(SimpleTestCase):

    def test_override_class_properties(self):
        self.assertEqual(SampleCommandOverridden.api_url, 'https://www.sample.com')
        self.assertEqual(SampleCommandOverridden.api_endpoint, 'wp-json/wp/v2/sample')
        self.assertEqual(len(SampleCommandOverridden.api_sub_sites), 1)
        
    def test_default_class_properties(self):
        self.assertEqual(SampleCommandDefault.api_url, 'https://www.england.nhs.uk')
        self.assertEqual(SampleCommandDefault.api_endpoint, None)
        self.assertEqual(len(SampleCommandDefault.api_sub_sites), 8)
        
