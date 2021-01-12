from django.contrib import admin
from wagtail_wordpress_importer.models import ImportAtlasCaseStudy

from .admin_base import AdminBase


class ImportAtlasCaseStudyAdmin(AdminBase):

    endpoint = 'atlas_case_studies'

    model = ImportAtlasCaseStudy

    list_display = (
        'truncate_title',
        'truncate_content',
        'sub_site',
        'slug',
        'status',
        '_type',
        'get_live_link',
        'template',
        'categories',
        'regions',
        'settings',
        'publication_type',
        'pprint_custom_fields',
        'get_wordpress_api_link',
        'date_gmt',
        'modified_gmt',
    )
    list_filter = ('sub_site',)
    search_fields = ('wp_id', 'title')


admin.site.register(ImportAtlasCaseStudy, ImportAtlasCaseStudyAdmin)
