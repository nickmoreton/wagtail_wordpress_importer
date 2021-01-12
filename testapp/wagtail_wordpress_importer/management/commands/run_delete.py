import time
import os

from django.core.management import BaseCommand, call_command
from django.conf import settings


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        self.stdout.write('This will take some time to finish ...')
        time.sleep(2)  # just so one can see the message
        call_command('delete_pages')
        call_command('delete_posts')
        call_command('delete_blogs')
        call_command('delete_atlas_case_studies')
        call_command('delete_documents')
        call_command('delete_media')
        call_command('delete_publication_types')
        call_command('delete_settings')
        call_command('delete_regions')
        call_command('delete_categories')
        call_command('delete_custom_fields')

        self.rm_data_log()
        self.rm_data_store()
        self.rm_media_store()
        self.stdout.write(self.style.SUCCESS('BOOM 💥 ALL GONE!'))

    # clean up

    def rm_data_log(self):
        log_dir = os.path.join(os.path.dirname(settings.BASE_DIR), 'log')

        if os.path.isdir(log_dir):
            self.stdout.write('Removing data log dir... ')
            self.stdout.flush()
            os.system('rm -R {}'.format(log_dir))

    def rm_data_store(self):
        data_dir = os.path.join(os.path.dirname(
            settings.BASE_DIR), 'data_store')

        if os.path.isdir(data_dir):
            self.stdout.write('Removing data store dir... ')
            self.stdout.flush()
            os.system('rm -R {}'.format(data_dir))

    def rm_media_store(self):
        media_dir = os.path.join(os.path.dirname(
            settings.BASE_DIR), 'media_store')

        if os.path.isdir(media_dir):
            self.stdout.write('Removing media store dir... ')
            self.stdout.flush()
            os.system('rm -R {}'.format(media_dir))
