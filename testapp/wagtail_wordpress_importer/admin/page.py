from django.contrib import admin
from wagtail_wordpress_importer.models import ImportPage, ImportPageCustomField

from .admin_base import AdminBase


class ImportPageCustomInline(admin.TabularInline):
    model = ImportPageCustomField
    readonly_fields = ('field',)
    extra = 0

class ImportPageAdmin(AdminBase):

    endpoint = 'pages'

    model = ImportPage
    list_display = (
        'truncate_title',
        'truncate_content',
        'truncate_excerpt',
        'sub_site',
        'parent',
        'slug',
        'status',
        '_type',
        'get_live_link',
        'author',
        'featured_media',
        'comment_status',
        'ping_status',
        'template',
        'pprint_custom_fields',
        'get_wordpress_api_link',
        'date_gmt',
        'modified_gmt',
    )
    list_filter = ('sub_site', 'template')
    search_fields = ('wp_id', 'title')

    inlines = (ImportPageCustomInline,)


admin.site.register(ImportPage, ImportPageAdmin)


class ImportPageCustomAdmin(AdminBase):

    model = ImportPageCustomField
    ordering = ()
    list_display = ('field','page',)
    list_filter = ('field__fields_group__title',)




admin.site.register(ImportPageCustomField, ImportPageCustomAdmin)
