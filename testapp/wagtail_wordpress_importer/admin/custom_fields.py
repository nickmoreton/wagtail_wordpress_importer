import json

from django.contrib import admin
from django.utils.safestring import mark_safe
from wagtail_wordpress_importer.models import (CustomField, CustomFieldsGroup,
                                               CustomFieldsGroupLocation)
from wagtail_wordpress_importer.models.custom_fields import (
    CustomFieldsLayout, CustomFieldsLayoutSubField,
    CustomFieldSubFieldsSubField)

from .admin_base import AdminBase
from wagtail_wordpress_importer.utils import get_json_field_style

''' inlines '''


class CustomFieldsGroupLocationInline(admin.TabularInline):
    model = CustomFieldsGroupLocation
    extra = 0
    readonly_fields = ('_key', '_value', '_index')


class CustomFieldInline(admin.TabularInline):
    model = CustomField
    extra = 0
    readonly_fields = (
        'key',
        'label',
        '_type',
        'layout',
        'sub_site',
        'name',
        'is_layout',
        'sub_fields',
        'layouts'
    )


class CustomFieldsSubFieldsInline(admin.TabularInline):
    model = CustomFieldSubFieldsSubField
    extra = 0
    readonly_fields = ('_key', '_value', '_index')


class CustomFieldsLayoutSubFieldsInline(admin.TabularInline):
    model = CustomFieldsLayoutSubField
    extra = 0
    readonly_fields = ('_key', '_value', '_index')


''' admins '''


class CustomFieldsGroupAdmin(AdminBase):

    endpoint = 'groups'

    model = CustomFieldsGroup
    list_display = (
        'key',
        'title',
        'description',
        'pprint_location',
        'get_wordpress_api_link',
        'sub_site',
        'has_layout',
    )
    search_fields = ('title', 'key')
    ordering = ('key',)
    list_filter = ('sub_site', 'has_layout')
    # list_per_page = 25
    inlines = (CustomFieldInline, CustomFieldsGroupLocationInline,)

    def pprint_location(self, obj):
        if obj.location:
            return mark_safe('''
            <pre class="pprint-json">{}</pre>
            {}
            '''.format(json.dumps(obj.location, indent=1), get_json_field_style()))
        return obj.layouts

    pprint_location.short_description = 'Locations'

    def get_wordpress_api_link(self, obj):
        sub_site = ''
        if not obj.sub_site == 'root':
            sub_site = obj.sub_site.replace('pages-', '') + '/'
        return mark_safe(
            '<a href="https://www.england.nhs.uk/{}wp-json/custom_fields/v1/{}/{}" target="_blank">{}</a>'
            .format(sub_site, self.get_endpoint_name(), obj.key, obj.key))
    get_wordpress_api_link.short_description = 'WP-API'


admin.site.register(CustomFieldsGroup, CustomFieldsGroupAdmin)


class CustomFieldsFieldAdmin(AdminBase):
    endpoint = 'fields'

    list_display = (
        'key',
        'fields_group',
        'sub_site',
        'usage_count',
        '_type',
        'get_wordpress_api_link',
        'is_layout',
        'pprint_sub_fields',
        'pprint_layouts',
    )
    list_filter = ('sub_site', 'fields_group__title', 'is_layout')
    ordering = ('-usage_count', 'key',)
    search_fields = ('fields_group__title', 'key', '_type')
    # list_per_page = 25
    # inlines = (CustomFieldsSubFieldsInline,)

    def truncate_sub_fields(self, obj):
        return str(obj.sub_fields)[:100]

    truncate_sub_fields.short_decription = 'sub fields'

    def truncate_layouts(self, obj):
        return str(obj.layouts)[:100]

    truncate_layouts.short_decription = 'layouts'

    def get_wordpress_api_link(self, obj):
        sub_site = ''
        if not obj.sub_site == 'root':
            sub_site = obj.sub_site.replace('pages-', '') + '/'
        return mark_safe(
            '<a href="https://www.england.nhs.uk/{}wp-json/custom_fields/v1/{}/{}" target="_blank">{}</a>'
            .format(sub_site, self.get_endpoint_name(),  obj.key, obj.key))
    get_wordpress_api_link.short_description = 'WP-API'

    def pprint_sub_fields(self, obj):
        if obj.sub_fields:
            return mark_safe('''
            <pre class="pprint-json">{}</pre>
            {}
            '''.format(json.dumps(obj.sub_fields, indent=1), get_json_field_style()))
        return obj.sub_fields

    pprint_sub_fields.short_description = 'Sub Fields'
    
    def pprint_layouts(self, obj):
        if obj.layouts:
            return mark_safe('''
            <pre class="pprint-json">{}</pre>
            {}
            '''.format(json.dumps(obj.layouts, indent=1), get_json_field_style()))
        return obj.layouts

    pprint_layouts.short_description = 'Layouts'


admin.site.register(CustomField, CustomFieldsFieldAdmin)


class CustomFieldsLayoutAdmin(AdminBase):

    list_display = (
        'fields_group',
        'sub_site',
        'key',
        'label',
        'name',
        'display',
        'pprint_sub_fields',
    )
    search_fields = ('name', )
    list_filter = ('sub_site', 'display', ('fields_group', admin.RelatedOnlyFieldListFilter))
    ordering = ('key',)
    # list_per_page = 25
    inlines = (CustomFieldsLayoutSubFieldsInline, )

    def pprint_sub_fields(self, obj):
        if obj.sub_fields:
            return mark_safe('''
            <pre class="pprint-json">{}</pre>
            {}
            '''.format(json.dumps(obj.sub_fields, indent=1), get_json_field_style()))
        return obj.sub_fields

    pprint_sub_fields.short_description = 'Sub Fields'


admin.site.register(CustomFieldsLayout, CustomFieldsLayoutAdmin)
