import json

from wagtail_wordpress_importer.cls.base_importer_command import \
    BaseImporterCommand
from wagtail_wordpress_importer.models import ImportDocument
from wagtail_wordpress_importer.utils import (html_entities, process_date,
                                              spinner, stringify_integer_list)


class Command(BaseImporterCommand):

    api_endpoint = 'wp-json/wp/v2/documents'

    def save_data(self, data, subsite):
        for result in data:
            self.stdout.write(next(spinner), ending='\b')
            try:
                obj = ImportDocument.objects.get(
                    wp_id=result.get('id'), sub_site=subsite)
            except ImportDocument.DoesNotExist:
                obj = ImportDocument(
                    wp_id=result.get('id'),
                    date_gmt=process_date(result.get('date_gmt')),
                    modified_gmt=process_date(result.get('modified_gmt')),
                    sub_site=subsite,
                    slug=result.get('slug'),
                    status=result.get('status'),
                    _type=result.get('type'),
                    author=result.get('author'),
                    link=result.get('link'),
                    title=html_entities(result.get('title')['rendered']),
                    template=result.get('template'),
                    # turns out that there are different fields now for improvement hub 😤
                    # not seen this anywhere else yet and this has changed since the first
                    # implementation
                    categories=stringify_integer_list(
                        result.get('categories', [])),
                    publication_type=stringify_integer_list(
                        result.get('publication-type', [])),
                    medical_conditions=stringify_integer_list(
                        result.get('medicalconditions', [])),
                    improvement_challenges=stringify_integer_list(
                        result.get('improvementchallenges', [])),
                    custom_fields=result.get('custom_fields'),
                )
                obj.save()
