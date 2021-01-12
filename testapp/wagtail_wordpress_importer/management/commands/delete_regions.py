from django.core.management import BaseCommand
from wagtail_wordpress_importer.models import ImportRegion


class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        self.stdout.write('Deleting regions... ', ending='')
        self.stdout.flush()
        ImportRegion.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('✅'))
