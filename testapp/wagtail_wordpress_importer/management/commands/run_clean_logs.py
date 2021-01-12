import os

from django.conf import settings
from django.core.management import BaseCommand


class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        self.stdout.write('Removing logs... ', ending='')
        self.stdout.flush()
        log_path = os.path.join(settings.BASE_DIR, 'wagtail_wordpress_importer/log')
        rm  = 'rm {}/*.log'.format(log_path)
        os.system('rm {}/*.log'.format(log_path))
        self.stdout.write(self.style.SUCCESS('✅'))
