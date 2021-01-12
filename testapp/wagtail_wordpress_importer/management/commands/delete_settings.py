from django.core.management import BaseCommand
from wagtail_wordpress_importer.models import ImportSetting


class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        self.stdout.write('Deleting settings... ', ending='')
        self.stdout.flush()
        ImportSetting.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('✅'))
