from django.core.management import BaseCommand
from wagtail_wordpress_importer.models import ImportPost


class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        self.stdout.write('Deleting posts... ', ending='')
        self.stdout.flush()
        ImportPost.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('✅'))
