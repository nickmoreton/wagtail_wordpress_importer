from django.core.management import BaseCommand
from wagtail_wordpress_importer.models import ImportBlog


class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        self.stdout.write('Deleting blogs... ', ending='')
        self.stdout.flush()
        ImportBlog.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('✅'))
