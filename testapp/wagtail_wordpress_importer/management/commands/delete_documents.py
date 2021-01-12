from django.core.management import BaseCommand
from wagtail_wordpress_importer.models import ImportDocument


class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        self.stdout.write('Deleting documents... ', ending='')
        self.stdout.flush()
        ImportDocument.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('✅'))
