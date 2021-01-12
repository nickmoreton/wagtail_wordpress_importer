from wagtail_wordpress_importer.cls.base_importer_command import \
    BaseImporterCommand
from wagtail_wordpress_importer.models import ImportCategory
from wagtail_wordpress_importer.utils import html_entities, spinner


class Command(BaseImporterCommand):

    # api_url = 'https://www.england.nhs.uk'
    api_endpoint = 'wp-json/wp/v2/categories'

    def save_data(self, data, subsite):
        for result in data:
            self.stdout.write(next(spinner), ending='\b')
            try:
                obj = ImportCategory.objects.get(wp_id=result.get('id'), sub_site=subsite)
            except ImportCategory.DoesNotExist:
                obj = ImportCategory(
                    wp_id=result.get('id'),
                    count=result.get('count'),
                    description=html_entities(result.get('description')),
                    link=result.get('link'),
                    name=html_entities(result.get('name')),
                    slug=result.get('slug'),
                    taxonomy=result.get('taxonomy'),
                    parent=result.get('parent'),
                    sub_site=subsite,
                )
                obj.save()
