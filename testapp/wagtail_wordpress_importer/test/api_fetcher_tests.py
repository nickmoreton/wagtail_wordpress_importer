from django.test import SimpleTestCase
from wagtail_wordpress_importer.cls.api_fetcher import WordpressApiFetcher

class ApiFetcherTestCase(SimpleTestCase):

    def test_get_page_headers(self):

        api_fetcher = WordpressApiFetcher(
            base_url='https://www.england.nhs.uk/wp-json/wp/v2/pages?page=1'
        )
        self.assertEqual(api_fetcher.content_type,
                         'application/json; charset=UTF-8')
        self.assertGreater(api_fetcher.total_results, 0)
        self.assertGreater(api_fetcher.total_pages, 0)

    def test_parse_headers_link(self):
        # page 1
        api_fetcher_one = WordpressApiFetcher(
            base_url='https://www.england.nhs.uk/wp-json/wp/v2/pages?page=1'
        )
        expected_next = 'https://www.england.nhs.uk/wp-json/wp/v2/pages?page=2'
        self.assertEqual(api_fetcher_one.next_url, expected_next)

        expected_prev = None
        self.assertEqual(api_fetcher_one.prev_url, expected_prev)

        # page 2
        api_fetcher_two = WordpressApiFetcher(
            base_url='https://www.england.nhs.uk/wp-json/wp/v2/pages?page=2'
        )
        expected_next = 'https://www.england.nhs.uk/wp-json/wp/v2/pages?page=3'
        self.assertEqual(api_fetcher_two.next_url, expected_next)

        expected_prev = 'https://www.england.nhs.uk/wp-json/wp/v2/pages?page=1'
        self.assertEqual(api_fetcher_two.prev_url, expected_prev)

        # last page
        api_fetcher_get_last = WordpressApiFetcher(
            base_url='https://www.england.nhs.uk/wp-json/wp/v2/pages?page=1'
        )
        last_page = api_fetcher_get_last.total_pages

        api_fetcher_last_page = WordpressApiFetcher(
            base_url='https://www.england.nhs.uk/wp-json/wp/v2/pages?page={}'.format(
                last_page)
        )
        expected_next = None
        self.assertEqual(api_fetcher_last_page.next_url, expected_next)

        expected_previous = 'https://www.england.nhs.uk/wp-json/wp/v2/pages?page={}'.format(
            last_page-1)
        self.assertEqual(api_fetcher_last_page.prev_url, expected_previous)

    def test_get_page_headers_subsite(self):

        api_fetcher = WordpressApiFetcher(
            base_url='https://www.england.nhs.uk/aac/wp-json/wp/v2/pages?page=1'
        )
        self.assertEqual(api_fetcher.content_type,
                         'application/json; charset=UTF-8')
        self.assertGreater(api_fetcher.total_results, 0)
        self.assertGreater(api_fetcher.total_pages, 0)

    def test_parse_headers_link_subsite(self):
        # page 1
        api_fetcher_one = WordpressApiFetcher(
            base_url='https://www.england.nhs.uk/aac/wp-json/wp/v2/pages?page=1'
        )
        expected_next = 'https://www.england.nhs.uk/aac/wp-json/wp/v2/pages?page=2'
        self.assertEqual(api_fetcher_one.next_url, expected_next)

        expected_prev = None
        self.assertEqual(api_fetcher_one.prev_url, expected_prev)

        # page 2
        api_fetcher_two = WordpressApiFetcher(
            base_url='https://www.england.nhs.uk/aac/wp-json/wp/v2/pages?page=2'
        )
        expected_next = 'https://www.england.nhs.uk/aac/wp-json/wp/v2/pages?page=3'
        self.assertEqual(api_fetcher_two.next_url, expected_next)

        expected_prev = 'https://www.england.nhs.uk/aac/wp-json/wp/v2/pages?page=1'
        self.assertEqual(api_fetcher_two.prev_url, expected_prev)

        # last page
        api_fetcher_get_last = WordpressApiFetcher(
            base_url='https://www.england.nhs.uk/aac/wp-json/wp/v2/pages?page=1'
        )
        last_page = api_fetcher_get_last.total_pages

        api_fetcher_last_page = WordpressApiFetcher(
            base_url='https://www.england.nhs.uk/aac/wp-json/wp/v2/pages?page={}'.format(
                last_page)
        )
        expected_next = None
        self.assertEqual(api_fetcher_last_page.next_url, expected_next)

        expected_previous = 'https://www.england.nhs.uk/aac/wp-json/wp/v2/pages?page={}'.format(
            last_page-1)
        self.assertEqual(api_fetcher_last_page.prev_url, expected_previous)

