import json

from django.contrib import admin
from django.utils.safestring import mark_safe
from wagtail_wordpress_importer.models import ImportMedia
from wagtail_wordpress_importer.utils import get_json_field_style

from .admin_base import AdminBase


class ImportMediaAdmin(AdminBase):

    endpoint = 'media'

    model = ImportMedia
    list_display = (
        'truncate_title',
        'truncate_description',
        'slug',
        'status',
        'source_404',
        '_type',
        'get_live_link',
        'template',
        'caption',
        'alt_text',
        'file',
        'file_parts',
        'media_type',
        'mime_type',
        'pprint_media_details',
        'sub_site',
        'author',
        'comment_status',
        'ping_status',
        'get_wordpress_api_link',
        'date_gmt',
        'modified_gmt',
    )
    list_filter = ('sub_site', 'source_404', 'media_type', 'mime_type')
    search_fields = ('wp_id', 'title')

    def pprint_media_details(self, obj):
        if obj.media_details:
            return mark_safe('''
            <pre class="pprint-json">{}</pre>
            {}
            '''.format(json.dumps(obj.media_details, indent=1), get_json_field_style()))
        return obj.media_details

    pprint_media_details.short_description = 'Media Details'


admin.site.register(ImportMedia, ImportMediaAdmin)
