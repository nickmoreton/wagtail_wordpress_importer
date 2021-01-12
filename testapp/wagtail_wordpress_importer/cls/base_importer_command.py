'''
setting this as quick work around
The media import is quite large and as the fetch happens recursively
it bombs out at 999 we need a higher amount mainly for the media
set this sys.setrecursionlimit(100000)
'''
from django.core.management import BaseCommand

from .api_fetcher import WordpressApiFetcher
from .logging import SimpleLog


class BaseImporterCommand(BaseCommand):
    '''
    The base commmand class for importing wordpress api endpoints
    For each of the endpoints you need to import sublclass BaseImporterCommand
    It basically provides a few helper methods to fetch and return json data
    You will need to implement a save_data() method to save the returned json data 
    to the database.
    '''

    ''' e.g. "https://www.england.nhs.uk" '''
    api_url = "https://www.england.nhs.uk"

    ''' e.g. "wp-json/wp/v2/pages" '''
    api_endpoint = None

    '''
    at leats one subsite is required
    root means it's not actually a subsite and is treated accordingly
    e.g. if the url is a root sub_site the final url will be like
    https://www.england.nhs.uk/wp-json/wp/v2/pages
    or if the url is a subsite the final url will be like
    https://www.england.nhs.uk/aac/wp-json/wp/v2/pages
    implmented by self.get_url(subsite)
    '''
    api_sub_sites = [
        'root',
        'aac',
        'coronavirus',
        'commissioning',
        'greenernhs',
        'improvement-hub',
        'rightcare',
        'non-executive-opportunities',
    ]

    logger = SimpleLog()

    def handle(self, *args, **options):
        if not self.api_url or not self.api_endpoint or not self.api_sub_sites:
            raise NotImplementedError(
                'api_url, api_endpoint and api_sub_sites are required properties')

        self.stdout.write('Fetching...')
        for subsite in self.api_sub_sites:
            url = self.get_url(subsite)
            self.stdout.write(url, ending=' ')
            self.fetcher = WordpressApiFetcher(url)
            if not self.fetcher._404:
                self.get_paged_results(subsite)
                self.stdout.write(self.style.SUCCESS('✅'))
            else:
                self.stdout.write(self.style.WARNING('404 '))

        self.stdout.write(self.style.SUCCESS('Finished 🏁'))
        self.stdout.write(self.style.SUCCESS('==========='))
        self.stdout.write('')

    def get_url(self, subsite=None):
        if not subsite == 'root':
            url = '/'.join([self.api_url, subsite, self.api_endpoint])
        else:
            url = '/'.join([self.api_url, self.api_endpoint])
        return url

    def get_paged_results(self, subsite):
        next_url = self.fetcher.next_url
        results = self.fetcher.get_results()

        if results:
            self.save_data(results, subsite)
        else:
            self.stdout.write(self.style.WARNING('zero results '), ending='')
            self.logger.log_message(self.fetcher.base_url,'Zero results')

        if next_url:
            self.fetcher = WordpressApiFetcher(next_url)
            self.get_paged_results(subsite)

    def save_data(self, data, subsite):
        '''
        just an example, you can implement it in any django way

        for result in data:
            self.stdout.write(next(spinner), ending="\b")
            page = ImportPage(
                these fields are from a base model
                wp_id=result.get('id'),
                date_gmt=process_date(result.get('date_gmt')),
                modified_gmt=process_date(result.get('modified_gmt')),
                sub_site=subsite,
                ...
                ...
                ...
            )
            page.save()

        '''
        raise NotImplementedError(
            'A save_data method is required in your command class!')

    class Meta:
        abstract = True
