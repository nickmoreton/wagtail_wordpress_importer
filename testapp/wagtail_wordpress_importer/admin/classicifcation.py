from django.contrib import admin
from wagtail_wordpress_importer.models import (ImportCategory,
                                               ImportPublicationType,
                                               ImportRegion, ImportSetting)

from .admin_base import AdminBase


class ImportCategoryAdmin(AdminBase):

    endpoint = 'categories'

    model = ImportCategory
    list_display = (
        'name',
        'slug',
        'get_live_link',
        'truncate_description',
        'parent',
        'taxonomy',
        'count',
        'get_wordpress_api_link',
        'sub_site',
    )
    list_filter = ('sub_site',)
    search_fields = ('wp_id', 'title')


admin.site.register(ImportCategory, ImportCategoryAdmin)


class ImportRegionAdmin(AdminBase):

    endpoint = 'region'

    model = ImportRegion
    list_display = (
        'name',
        'slug',
        'get_live_link',
        'truncate_description',
        'parent',
        'taxonomy',
        'count',
        'get_wordpress_api_link',
        'sub_site',
    )
    list_filter = ('sub_site',)
    ordering = ('wp_id',)


admin.site.register(ImportRegion, ImportRegionAdmin)


class ImportSettingAdmin(AdminBase):

    endpoint = 'setting'

    model = ImportSetting
    list_display = (
        'name',
        'slug',
        'get_live_link',
        'truncate_description',
        'parent',
        'taxonomy',
        'count',
        'get_wordpress_api_link',
        'sub_site',
    )
    list_filter = ('sub_site',)
    ordering = ('wp_id',)


admin.site.register(ImportSetting, ImportSettingAdmin)


class ImportPublicationTypeAdmin(AdminBase):

    endpoint = 'publication-type'

    model = ImportPublicationType
    list_display = (
        'name',
        'slug',
        'get_live_link',
        'truncate_description',
        'parent',
        'taxonomy',
        'count',
        'get_wordpress_api_link',
        'sub_site',
    )
    list_filter = ('sub_site',)
    ordering = ('wp_id',)


admin.site.register(ImportPublicationType, ImportPublicationTypeAdmin)
