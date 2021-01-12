import json
import sys

from wagtail_wordpress_importer.cls.base_importer_command import \
    BaseImporterCommand
from wagtail_wordpress_importer.models import ImportMedia
from wagtail_wordpress_importer.utils import (html_entities, process_date,
                                              spinner, stringify_integer_list)


class Command(BaseImporterCommand):

    # there's a lot of files in this one
    sys.setrecursionlimit(10000)

    api_endpoint = 'wp-json/wp/v2/media'

    def save_data(self, data, subsite):
        for result in data:
            self.stdout.write(next(spinner), ending='\b')
            try:
                obj = ImportMedia.objects.get(
                    wp_id=result.get('id'), sub_site=subsite)
            except ImportMedia.DoesNotExist:
                obj = ImportMedia(
                    wp_id=result.get('id'),
                    date_gmt=process_date(result.get('date_gmt')),
                    modified_gmt=process_date(result.get('modified_gmt')),
                    sub_site=subsite,
                    slug=result.get('slug'),
                    status=result.get('status'),
                    _type=result.get('type'),
                    link=result.get('link'),
                    title=html_entities(result.get('title')['rendered']),
                    author=result.get('author'),
                    comment_status=result.get('comment_status'),
                    ping_status=result.get('ping_status'),
                    template=result.get('template'),
                    description=html_entities(
                        result.get('description')['rendered']),
                    caption=html_entities(result.get('caption')['rendered']),
                    alt_text=html_entities(result.get('alt_text')),
                    media_type=result.get('media_type'),
                    mime_type=result.get('mime_type'),
                    media_details=result.get('media_details'),
                    source_url=result.get('source_url'),
                    post=result.get('post') or 0,
                    file_parts='',
                )
                obj.save()
