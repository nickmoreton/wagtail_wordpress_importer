import json

from wagtail_wordpress_importer.cls.base_importer_command import \
    BaseImporterCommand
from wagtail_wordpress_importer.models import ImportPost
from wagtail_wordpress_importer.utils import (html_entities, process_date,
                                              spinner, stringify_integer_list)


class Command(BaseImporterCommand):
    
    api_endpoint = 'wp-json/wp/v2/posts'

    def save_data(self, data, subsite):
        for result in data:
            self.stdout.write(next(spinner), ending='\b')
            try:
                obj = ImportPost.objects.get(
                    wp_id=result.get('id'), sub_site=subsite)
            except ImportPost.DoesNotExist:
                obj = ImportPost(
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
                    excerpt=html_entities(result.get('excerpt')['rendered']),
                    author=result.get('author'),
                    featured_media=result.get('featured_media'),
                    comment_status=result.get('comment_status'),
                    ping_status=result.get('ping_status'),
                    sticky=result.get('sticky'),
                    template=result.get('template'),
                    _format=result.get('format'),
                    categories=stringify_integer_list(result.get('categories')),
                    tags=stringify_integer_list(result.get('tags')),
                    custom_fields=result.get('custom_fields'),
                )
                obj.save()
