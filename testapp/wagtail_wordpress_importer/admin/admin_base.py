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
            '<a href="https://www.england.nhs.uk/{}wp-json/wp/v2/{}/{}" target="_blank">\
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 32 32"><title>file-json</title><g fill="#505050"><path d="M3,29v2a1,1,0,0,0,1,1H28a1,1,0,0,0,1-1V29Z"></path> <polygon points="22 1.586 22 7 27.414 7 22 1.586"></polygon> <path d="M31,13H29V9H21a1,1,0,0,1-1-1V0H4A1,1,0,0,0,3,1V13H1a1,1,0,0,0-1,1V26a1,1,0,0,0,1,1H31a1,1,0,0,0,1-1V14A1,1,0,0,0,31,13ZM8.275,22.441A2.643,2.643,0,0,1,7.768,24.2a1.894,1.894,0,0,1-1.524.6,3.763,3.763,0,0,1-.8-.082v-1.2c.084.015.172.033.266.052a1.461,1.461,0,0,0,.305.03.623.623,0,0,0,.547-.231,1.415,1.415,0,0,0,.164-.789V17.289h1.55Zm2.713-3.332a6.7,6.7,0,0,0,.944.485,2.591,2.591,0,0,1,1.025.713,1.552,1.552,0,0,1,.287.959,1.692,1.692,0,0,1-.269.943,1.769,1.769,0,0,1-.778.641,2.886,2.886,0,0,1-1.191.228,4.845,4.845,0,0,1-.957-.08,3.528,3.528,0,0,1-.8-.279V21.344a4.629,4.629,0,0,0,.918.353,3.448,3.448,0,0,0,.875.127.847.847,0,0,0,.5-.119.367.367,0,0,0,.16-.307.338.338,0,0,0-.064-.2.763.763,0,0,0-.207-.177c-.1-.061-.348-.182-.76-.368a3.65,3.65,0,0,1-.838-.492,1.514,1.514,0,0,1-.414-.547,1.809,1.809,0,0,1-.135-.73,1.469,1.469,0,0,1,.574-1.231,2.534,2.534,0,0,1,1.579-.441,4.435,4.435,0,0,1,1.808.41l-.473,1.192a3.418,3.418,0,0,0-1.382-.368.723.723,0,0,0-.438.106.32.32,0,0,0-.137.262A.38.38,0,0,0,10.988,19.109Zm7.776,3.219a2.711,2.711,0,0,1-2.071.75,2.71,2.71,0,0,1-2.06-.754,3.065,3.065,0,0,1-.717-2.2,3.05,3.05,0,0,1,.713-2.178A2.718,2.718,0,0,1,16.7,17.2a2.7,2.7,0,0,1,2.067.746,3.089,3.089,0,0,1,.7,2.192A3.081,3.081,0,0,1,18.764,22.328ZM25.939,23H23.916L21.83,18.977H21.8q.075.948.074,1.449V23H20.5V17.289h2.016L24.6,21.258h.023c-.036-.576-.055-1.037-.055-1.387V17.289h1.375Z" fill="#505050"></path> <path d="M16.7,18.465q-1.159,0-1.16,1.672,0,1.654,1.152,1.656a.992.992,0,0,0,.869-.4,2.2,2.2,0,0,0,.284-1.254,2.221,2.221,0,0,0-.287-1.264A.984.984,0,0,0,16.7,18.465Z" fill="#505050"></path></g></svg></a>'
            .format(sub_site, self.get_endpoint_name(),  obj.wp_id, obj.wp_id))
    get_wordpress_api_link.short_description = 'WP-API'

    def get_live_link(self, obj):
        return mark_safe('<a href="{}" target="_blank"> \
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><title>webpage</title><g fill="#505050"><path d="M23,1H1A1,1,0,0,0,0,2V22a1,1,0,0,0,1,1H23a1,1,0,0,0,1-1V2A1,1,0,0,0,23,1ZM7,3A1,1,0,1,1,6,4,1,1,0,0,1,7,3ZM3,3A1,1,0,1,1,2,4,1,1,0,0,1,3,3ZM22,21H2V7H22Z" fill="#505050"></path> <rect x="4" y="9" width="4" height="10"></rect> <rect x="10" y="9" width="10" height="10"></rect></g></svg>         </a>'.format(obj.link))
    get_live_link.short_description = 'Live'

    def pprint_custom_fields(self, obj):
        if obj.custom_fields:
            return mark_safe('''
            <pre class="pprint-json">{}</pre>
            {}
            '''.format(json.dumps(obj.custom_fields, indent=1), get_json_field_style()))
        return obj.custom_fields

    pprint_custom_fields.short_description = 'Custom Fields'
