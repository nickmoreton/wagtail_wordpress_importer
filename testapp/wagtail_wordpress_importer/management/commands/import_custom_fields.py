import json
import sys

from django.db.models import fields

from wagtail_wordpress_importer.cls.api_fetcher_custom_fields import \
    WordpressCustomFieldsApiFetcher
from wagtail_wordpress_importer.cls.base_importer_command_custom_fields import \
    BaseImporterCustomFieldsCommand
from wagtail_wordpress_importer.models import CustomFieldsGroup, CustomField
from wagtail_wordpress_importer.models.custom_fields import CustomFieldsLayout
from wagtail_wordpress_importer.utils import (html_entities, process_date,
                                              spinner, stringify_integer_list)


class Command(BaseImporterCustomFieldsCommand):

    api_endpoint = 'wp-json/custom_fields/v1/groups'

    def save_data(self, data, subsite):
        for result in data:
            self.stdout.write(next(spinner), ending='\b')
            try:
                obj = CustomFieldsGroup.objects.get(
                    key=result.get('key'), sub_site=subsite)
            except CustomFieldsGroup.DoesNotExist:
                obj = CustomFieldsGroup(
                    key=result.get('key'),
                    title=html_entities(result.get('title')),
                    description=html_entities(result.get('description')),
                    location=result.get('location'),
                    sub_site=subsite,
                )
                obj.save()

            custom_fields_saver = CustomFieldsFieldParser(obj, subsite)


class CustomFieldsFieldParser:

    api_url = 'https://www.england.nhs.uk'
    api_endpoint = 'wp-json/custom_fields/v1/groups'

    '''
    at leats one subsite is required
    root means it's not actually a subsite and is treated accordingly
    e.g. if the url is a root sub_site the final url will be like
    https://www.england.nhs.uk/wp-json/custom_fields/v1/groups
    or if the url is a subsite the final url will be like
    https://www.england.nhs.uk/aac/wp-json/custom_fields/v1/groups
    implmented by self.get_url(subsite)
    '''
    api_sub_sites = [
        'root',
        'aac',
        'coronavirus',
        'commissioning',
        'greenernhs',
        'improvement-hub',
        'rightcare',
        'non-executive-opportunities',
    ]

    def __init__(self, group, subsite):
        url = '/'.join([self.api_url, self.api_endpoint, group.key])
        fetcher = WordpressCustomFieldsApiFetcher(url)
        self.subsite = subsite
        self.group = group
        self.save_data(fetcher.get_results())

    def save_data(self, data):
        # sys.stdout.write('Getting fields ... \n')
        for result in data:
            
            try:
                obj = CustomField.objects.get(
                    fields_group=self.group, key=result.get('key'), sub_site=self.subsite)
            except CustomField.DoesNotExist:
                obj = CustomField(
                    key=result.get('key'),
                    fields_group=self.group,
                    sub_fields=result.get('sub_fields', ''),
                    layouts=result.get('layouts', ''),
                    is_layout=True if result.get('layouts') else False,
                    # label = result.get('label'),
                    # name = result.get('name'),
                    # prefix = result.get('prefix'),
                    _type=result.get('type', ''),
                    # value = result.get('value'),
                    # menu_order = result.get('menu_order'),
                    # instuctions = result.get('instuctions', ''),
                    # required = result.get('required'),
                    # wp_id = result.get('id'),
                    # _class = result.get('_class', ''),
                    # conditional_logic = result.get('conditional_logic'),
                    # parent = result.get('parent'),
                    # wrapper = result.get('wrapper'),
                    # collapsed = result.get('collapsed', True),
                    # # min = result.get('min', '0'),
                    # # max = result.get('max', '0'),
                    # button_label = result.get('button_label', ''),
                    # _name = result.get('_name'),
                    # _valid = result.get('_valid'),
                    # sub_fields = json.dumps(result.get('sub_fields')),
                    sub_site=self.subsite,
                )
                obj.save()

            if result.get('layouts'):
                g = CustomFieldsGroup.objects.get(id=self.group.id)
                # if result.get('layouts'):
                g.has_layout = True
                g.save()

                for layout in result.get('layouts'):
                    try:
                        layout_obj = CustomFieldsLayout.objects.get(
                            fields_group=self.group, key=layout.get('key'), sub_site=self.subsite)
                    except CustomFieldsLayout.DoesNotExist:
                        layout_obj = CustomFieldsLayout(
                            fields_group=self.group,
                            sub_site=self.subsite,
                            key=layout.get('key'),
                            label=layout.get('label'),
                            name=layout.get('name'),
                            display=layout.get('display'),
                            sub_fields=layout.get('sub_fields'),
                        )
                        layout_obj.save()
