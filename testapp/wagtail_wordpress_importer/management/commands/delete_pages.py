from django.core.management import BaseCommand
from wagtail_wordpress_importer.models import ImportPage


class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        self.stdout.write('Deleting pages... ', ending='')
        self.stdout.flush()
        ImportPage.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('✅'))
