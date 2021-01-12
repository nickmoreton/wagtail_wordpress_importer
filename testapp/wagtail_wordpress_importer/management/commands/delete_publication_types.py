from django.core.management import BaseCommand
from wagtail_wordpress_importer.models import ImportPublicationType


class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        self.stdout.write('Deleting publication types... ', ending='')
        self.stdout.flush()
        ImportPublicationType.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('✅'))
