from django.http import response
import requests


class WordpressApiFetcher:

    def __init__(self, base_url=''):
        self._404 = False
        self.base_url = base_url
        self.get_page_headers()

    def get_page_headers(self):
        r = requests.get(self.base_url)
        if not r.status_code == 200:
            self._404 = True
        else:
            self.content_type = r.headers['Content-Type']
            self.total_results = int(r.headers['x-wp-total'])
            self.total_pages = int(r.headers['x-wp-totalpages'])
            self.next_url, self.prev_url = self.parse_headers_link(
                r.headers['link'])

    def parse_headers_link(self, header=''):
        # the raw headers link is
        '''
        link: 
            <https://www.england.nhs.uk/wp-json/wp/v2/pages?page=9>; rel='prev', 
            <https://www.england.nhs.uk/wp-json/wp/v2/pages?page=11>; rel='next'
        '''
        next_url = None
        prev_url = None

        links = header.split(',')

        '''
        
        middle
        ['<https://www.england.nhs.uk/wp-json/wp/v2/pages?page=9>; rel='prev'', 
        ' <https://www.england.nhs.uk/wp-json/wp/v2/pages?page=11>; rel='next'']
        end
        ['<https://www.england.nhs.uk/wp-json/wp/v2/pages?page=*>; rel='prev'']
        start
        ['<https://www.england.nhs.uk/wp-json/wp/v2/pages?page=1>; rel='next'']
        
        '''

        for link in links:
            if 'rel="prev"' in link:  # the previous page
                prev_url = self._parse_link(link)
            if 'rel="next"' in link:  # the next page
                next_url = self._parse_link(link)

        return next_url, prev_url

    def _parse_link(self, link):
        link = link.split(';')[0]
        link = link.replace('<', '')
        link = link.replace('>', '')
        return link.strip()

    def get_results(self):
        results = requests.get(self.base_url).json()
        if results:
            return results
