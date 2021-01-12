from django.core.management import BaseCommand
from wagtail_wordpress_importer.models import ImportCategory


class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        self.stdout.write('Deleting categories... ', ending='')
        self.stdout.flush()
        ImportCategory.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('✅'))
