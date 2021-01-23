from django.contrib import admin
from wagtail_wordpress_importer.models import ImportPost

from .admin_base import AdminBase


class ImportPostAdmin(AdminBase):

    endpoint = 'posts'

    model = ImportPost
    list_display = (
        'truncate_title',
        'truncate_content',
        'truncate_excerpt',
        'sub_site',
        'slug',
        'status',
        '_type',
        'get_live_link',
        'get_wordpress_api_link',
        'author',
        'featured_media',
        'comment_status',
        'ping_status',
        'sticky',
        'template',
        '_format',
        'categories',
        'tags',
        'pprint_custom_fields',
        'date_gmt',
        'modified_gmt',
    )
    list_filter = ('sub_site',)
    search_fields = ('wp_id', 'title')


admin.site.register(ImportPost, ImportPostAdmin)
