import json

from wagtail_wordpress_importer.cls.base_importer_command import \
    BaseImporterCommand
from wagtail_wordpress_importer.models import ImportAtlasCaseStudy
from wagtail_wordpress_importer.utils import (html_entities, process_date,
                                              spinner, stringify_integer_list)


class Command(BaseImporterCommand):

    # api_url = 'https://www.england.nhs.uk'
    api_endpoint = 'wp-json/wp/v2/atlas_case_studies'

    def save_data(self, data, subsite):
        for result in data:
            self.stdout.write(next(spinner), ending='\b')
            try:
                obj = ImportAtlasCaseStudy.objects.get(wp_id=result.get('id'), sub_site=subsite)
            except ImportAtlasCaseStudy.DoesNotExist:
                obj = ImportAtlasCaseStudy(
                    wp_id=result.get('id'),
                    date_gmt=process_date(result.get('date_gmt')),
                    modified_gmt=process_date(result.get('modified_gmt')),
                    sub_site=subsite,
                    slug=result.get('slug'),
                    status=result.get('status'),
                    _type=result.get('type'),
                    link=result.get('link'),
                    title=html_entities(result.get('title')['rendered']),
                    content=html_entities(result.get('content')['rendered']),
                    template=result.get('template'),
                    categories=stringify_integer_list(result.get('categories')),
                    regions=stringify_integer_list(result.get('region')),
                    settings=stringify_integer_list(result.get('setting')),
                    publication_type=stringify_integer_list(result.get('publication-type')),
                    custom_fields=result.get('custom_fields'),
                )
                obj.save()
