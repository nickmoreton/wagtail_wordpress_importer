from django.core.management import BaseCommand
from wagtail_wordpress_importer.models import CustomFieldsGroup


class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        self.stdout.write('Deleting custom field groups... ', ending='')
        self.stdout.flush()
        CustomFieldsGroup.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('✅'))
