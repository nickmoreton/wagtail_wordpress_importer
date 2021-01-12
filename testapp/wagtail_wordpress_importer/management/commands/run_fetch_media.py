import os
from urllib.parse import urlparse
from django.utils import timezone

import requests
from django.conf import settings
from django.core.management import BaseCommand
from wagtail_wordpress_importer.cls.logging import DataLog, SimpleLog
from wagtail_wordpress_importer.models import ImportMedia
from wagtail_wordpress_importer.utils import process_date


class Command(BaseCommand):

    media_store = os.path.join(os.path.dirname(
        settings.BASE_DIR), 'media_store')

    def handle(self, *args, **options):

        import_data_logger = DataLog()
        data = import_data_logger.read_data()

        if not os.path.exists(self.media_store):
            os.makedirs(self.media_store)

        media_files = ImportMedia.objects.all()
        media_files_count = media_files.count()

        self.stdout.write('This will take some time to finish ...')
        self.stdout.write(self.style.WARNING(
            '`404` and `zero results` may be shown but thats expected and they are logged 😅'))

        for media_file in media_files:
            message = 'files left: {}'.format(media_files_count)
            ending_length = len(message)
            ending = '\b'*ending_length
            self.stdout.write(message, ending=ending)

            response = requests.get(media_file.source_url)
            if not response.status_code == 200:
                message = '\nhttps://www.england.nhs.uk/wp-json/wp/v2/media/{} seems to be 404 but is listed in the API'.format(
                    media_file.wp_id)
                SimpleLog().log_message(media_file.source_url, message)
                media_file.source_404 = True
                media_file.save(response)
            else:
                self.save_media(media_file)
            media_files_count -= 1

        data['media_fetched_date'] = str(process_date(timezone.now().strftime('%Y-%m-%dT%H:%M:%S')))
        import_data_logger.write_data(data)


    def save_media(self, media_file):
        media = requests.get(media_file.source_url)

        file_name = urlparse(media_file.source_url).path.split('/')[-1]

        path_list = urlparse(media_file.source_url).path.split('/')

        dirs = '/'.join(path_list[1:-1])

        path = os.path.join(self.media_store, dirs)

        if not os.path.isdir(path):
            os.makedirs(path)

        save_path = os.path.join(path, file_name)
        absolute_path = os.path.abspath(save_path)

        with open(save_path, 'wb') as f:
            f.write(media.content)

            # get the last 3 parts for useful organisation later
            file_parts = absolute_path.split('/')[-3:]
            media_file.file_parts = file_parts
            media_file.file = absolute_path
            media_file.save()
