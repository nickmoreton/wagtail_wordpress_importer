from django.core.management import BaseCommand
from wagtail_wordpress_importer.models import ImportAtlasCaseStudy


class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        self.stdout.write('Deleting atlas case studies... ', ending='')
        self.stdout.flush()
        ImportAtlasCaseStudy.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('✅'))
