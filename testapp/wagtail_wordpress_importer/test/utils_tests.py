from django.test import SimpleTestCase
from wagtail_wordpress_importer.utils import process_date, stringify_integer_list, html_entities


class TestUtilsTestCase(SimpleTestCase):

    def test_utils_process_date(self):
        date_string = '2020-01-31T13:37:59'
        date_processed = str(process_date(date_string))
        self.assertEqual(date_processed, '2020-01-31 13:37:59+00:00')

    def test_stringify_integer_list(self):
        integers = [200, 300, 500]
        interger_list = stringify_integer_list(integers)
        self.assertEqual(interger_list, '200,300,500')

    def test_html_entities(self):
        excerpt = 'Primary Care Network: &#8216;Drive thru&#8217; services offering a safe alternative to immunisation clinics'
        corrected = html_entities(excerpt)
        self.assertNotIn(corrected, '&#8216;')
