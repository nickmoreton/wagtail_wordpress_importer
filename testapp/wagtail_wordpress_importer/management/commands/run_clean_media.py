import os

from django.conf import settings
from django.core.management import BaseCommand
from wagtail_wordpress_importer.models import ImportMedia


class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        self.stdout.write('Removing media files... ', ending='')
        self.stdout.flush()
        media_files = ImportMedia.objects.all()

        for media_file in media_files:
            if media_file.file:
                full_path = media_file.file
                os.system('rm {}'.format(full_path))
                media_file.file = ''
                media_file.save()
        self.stdout.write(self.style.SUCCESS('✅'))
