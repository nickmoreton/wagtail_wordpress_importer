from django.contrib import admin
from wagtail_wordpress_importer.models import ImportBlog

from .admin_base import AdminBase


class ImportBlogAdmin(AdminBase):

    endpoint = 'blogs'

    model = ImportBlog
    list_display = (
        'truncate_title',
        'truncate_content',
        'sub_site',
        'author',
        'slug',
        'status',
        '_type',
        'get_live_link',
        'featured_media',
        'comment_status',
        'ping_status',
        'template',
        'categories',
        'pprint_custom_fields',
        'guest_authors',
        'get_wordpress_api_link',
        'date_gmt',
        'modified_gmt',
    )
    list_filter = ('sub_site',)
    search_fields = ('wp_id', 'title')


admin.site.register(ImportBlog, ImportBlogAdmin)
