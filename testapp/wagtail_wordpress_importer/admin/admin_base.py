import json

from django.utils.safestring import mark_safe
from simple_history.admin import SimpleHistoryAdmin
from wagtail_wordpress_importer.utils import get_json_field_style


class AdminBase(SimpleHistoryAdmin):

    ordering = ('-modified_gmt',)

    class Meta:
        abstract = True

    def get_endpoint_name(self):
        return self.endpoint

    def truncate_title(self, obj):
        if obj.title:
            return obj.title[:50] + ' ...'
    truncate_title.short_description = 'Title'

    def truncate_content(self, obj):
        if obj.content:
            return obj.content[:50] + ' ...'
    truncate_content.short_description = 'Content'

    def truncate_excerpt(self, obj):
        if obj.excerpt:
            return obj.excerpt[:50] + ' ...'
    truncate_excerpt.short_description = 'Excerpt'

    def truncate_description(self, obj):
        if obj.description:
            return obj.description[:50] + ' ...'
    truncate_description.short_description = 'Description'

    def truncate_custom_fields(self, obj):
        if obj.custom_fields:
            return json.dumps(obj.custom_fields)[:50] + ' ...'
    truncate_custom_fields.short_description = 'Custom'

    def truncate_media_details(self, obj):
        if obj.media_details:
            return json.dumps(obj.media_details)[:50] + ' ...'
    truncate_media_details.short_description = 'Media Details'

    def get_wordpress_api_link(self, obj):
        sub_site = ''
        if not obj.sub_site == 'root':
            sub_site = obj.sub_site.replace('pages-', '') + '/'
        return mark_safe(
            '<a href="https://www.england.nhs.uk/{}wp-json/wp/v2/{}/{}" target="_blank">{}</a>'
            .format(sub_site, self.get_endpoint_name(),  obj.wp_id, obj.wp_id))
    get_wordpress_api_link.short_description = 'WP-API'

    def get_live_link(self, obj):
        return mark_safe('<a href="{}" target="_blank">Visit Page</a>'.format(obj.link))
    get_live_link.short_description = 'Live'

    def pprint_custom_fields(self, obj):
        if obj.custom_fields:
            return mark_safe('''
            <pre class="pprint-json">{}</pre>
            {}
            '''.format(json.dumps(obj.custom_fields, indent=1), get_json_field_style()))
        return obj.custom_fields

    pprint_custom_fields.short_description = 'Custom Fields'
