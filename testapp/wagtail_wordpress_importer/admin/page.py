from django.contrib import admin
from django.urls import reverse
from django.urls.conf import path
from django.utils.safestring import mark_safe
from wagtail_wordpress_importer.models import ImportPage, ImportPageCustomField

from .admin_base import AdminBase


class LevelFilter(admin.SimpleListFilter):
    title = 'Level'
    parameter_name = 'parent'
    # template = 'admin/dropdown_filter.html'

    def lookups(self, request, model_admin):
        qs = model_admin.get_queryset(request).order_by('title')
        options = [('0', 'Top Level')]
        # for q in qs:
        #     options.append((q.wp_id, q.title))
        return options

    def queryset(self, request, queryset):
        if self.value():
            qs = queryset.filter(parent=str(request.GET.get('parent')))
            return qs
        return queryset


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
        'parent_level',
        'siblings',
        'children',
        'slug',
        'status',
        '_type',
        'get_live_link',
        'get_wordpress_api_link',
        'author',
        'featured_media',
        'comment_status',
        'ping_status',
        'template',
        'pprint_custom_fields',
        'date_gmt',
        'modified_gmt',
    )
    list_filter = ('sub_site', 'template', LevelFilter)
    search_fields = ('wp_id', 'title')

    inlines = (ImportPageCustomInline,)

    def siblings(self, obj):
        admin_url = reverse(
            'admin:wagtail_wordpress_importer_importpage_changelist')
        query = '?parent={}&sub_site={}'.format(obj.parent, obj.sub_site)
        has_siblings = ImportPage.objects.filter(
            parent=obj.parent, sub_site=obj.sub_site).count()
        if has_siblings > 1:
            return mark_safe('<a href="{}{}">\
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><title>table-move</title><g fill="#505050"><path fill="#505050" d="M13,6H1C0.448,6,0,5.552,0,5V3c0-0.552,0.448-1,1-1h12c0.552,0,1,0.448,1,1v2C14,5.552,13.552,6,13,6z"></path> <path fill="#505050" d="M13,14H1c-0.552,0-1-0.448-1-1v-2c0-0.552,0.448-1,1-1h12c0.552,0,1,0.448,1,1v2C14,13.552,13.552,14,13,14z "></path> <path fill="#505050" d="M13,22H1c-0.552,0-1-0.448-1-1v-2c0-0.552,0.448-1,1-1h12c0.552,0,1,0.448,1,1v2C14,21.552,13.552,22,13,22z "></path> <path d="M17,18l7-6l-7-6V18z"></path></g></svg> \
                </a>'.format(admin_url, query))
        return mark_safe('<svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 12 12"><title>ban</title><g fill="#505050"><path d="M10.242,1.758l-.011-.008A6,6,0,0,0,1.75,10.231l.008.011.011.008A6,6,0,0,0,10.25,1.769ZM6,2a3.947,3.947,0,0,1,2.019.567L2.567,8.019A3.947,3.947,0,0,1,2,6,4,4,0,0,1,6,2Zm0,8a3.947,3.947,0,0,1-2.019-.567L9.433,3.981A3.947,3.947,0,0,1,10,6,4,4,0,0,1,6,10Z" fill="#505050"></path></g></svg>')
    siblings.short_description = 'Siblings'

    def parent_level(self, obj):
        admin_url = reverse(
            'admin:wagtail_wordpress_importer_importpage_changelist')
        query = '?wp_id={}&sub_site={}'.format(obj.parent, obj.sub_site)
        if obj.parent == 0:
            return mark_safe('<svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 12 12"><title>target</title><g fill="#505050"><path d="M6,12a6,6,0,1,1,6-6A6.006,6.006,0,0,1,6,12ZM6,2a4,4,0,1,0,4,4A4,4,0,0,0,6,2Z" fill="#505050"></path> <circle cx="6" cy="6" r="2"></circle></g></svg>')
        return mark_safe('<a href="{}{}"> \
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><title>box-arrow-top-left</title><g fill="#505050"><path d="M22,1H2A1,1,0,0,0,1,2V22a1,1,0,0,0,1,1H22a1,1,0,0,0,1-1V2A1,1,0,0,0,22,1ZM12.293,13.707,7,8.414V13H5V5h8V7H8.414l5.293,5.293Z" fill="#505050"></path></g></svg> \
        </a>'.format(admin_url, query))
    parent_level.short_description = 'Parent'

    def children(self, obj):
        admin_url = reverse(
            'admin:wagtail_wordpress_importer_importpage_changelist')
        query = '?parent={}&sub_site={}'.format(obj.wp_id, obj.sub_site)
        has_children = ImportPage.objects.filter(
            parent=obj.wp_id, sub_site=obj.sub_site)
        if not has_children:
            return mark_safe('<svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 12 12"><title>ban</title><g fill="#505050"><path d="M10.242,1.758l-.011-.008A6,6,0,0,0,1.75,10.231l.008.011.011.008A6,6,0,0,0,10.25,1.769ZM6,2a3.947,3.947,0,0,1,2.019.567L2.567,8.019A3.947,3.947,0,0,1,2,6,4,4,0,0,1,6,2Zm0,8a3.947,3.947,0,0,1-2.019-.567L9.433,3.981A3.947,3.947,0,0,1,10,6,4,4,0,0,1,6,10Z" fill="#505050"></path></g></svg>')
        return mark_safe('<a href="{}{}"> \
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><title>box-arrow-bottom-right</title><g fill="#505050"><path d="M2,23H22a1,1,0,0,0,1-1V2a1,1,0,0,0-1-1H2A1,1,0,0,0,1,2V22A1,1,0,0,0,2,23Zm9.707-12.707L17,15.586V11h2v8H11V17h4.586l-5.293-5.293Z" fill="#505050"></path></g></svg> \
            </a>'.format(admin_url, query))
    children.short_description = 'Children'


admin.site.register(ImportPage, ImportPageAdmin)


class ImportPageCustomAdmin(AdminBase):

    model = ImportPageCustomField
    ordering = ()
    list_display = ('field', 'page',)
    list_filter = ('field__fields_group__title',)


admin.site.register(ImportPageCustomField, ImportPageCustomAdmin)
