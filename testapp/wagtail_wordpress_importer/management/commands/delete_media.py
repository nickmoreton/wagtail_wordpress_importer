from django.core.management import BaseCommand
from wagtail_wordpress_importer.models import ImportMedia


class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        self.stdout.write('Deleting media... ', ending='')
        self.stdout.flush()
        ImportMedia.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('✅'))
