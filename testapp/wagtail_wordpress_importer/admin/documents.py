import json

from django.contrib import admin
from django.utils.safestring import mark_safe
from wagtail_wordpress_importer.models import ImportDocument
from wagtail_wordpress_importer.utils import get_json_field_style

from .admin_base import AdminBase


class ImportDocumentAdmin(AdminBase):

    endpoint = 'documents'

    model = ImportDocument
    list_display = (
        'truncate_title',
        'sub_site',
        'author',
        'slug',
        'status',
        '_type',
        'get_live_link',
        'template',
        'categories',
        'publication_type',
        'medical_conditions',
        'improvement_challenges',
        'pprint_custom_fields',
        'get_wordpress_api_link',
        'date_gmt',
        'modified_gmt',
    )
    list_filter = ('sub_site',)
    search_fields = ('wp_id', 'title')


admin.site.register(ImportDocument, ImportDocumentAdmin)
