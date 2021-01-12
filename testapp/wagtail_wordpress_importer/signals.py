import json

from django.db.models.signals import post_save
from django.dispatch import receiver

from wagtail_wordpress_importer.models.custom_fields import CustomField, CustomFieldSubFieldsSubField

from .models import (CustomFieldsGroup, CustomFieldsGroupLocation,
                     CustomFieldsLayout, CustomFieldsLayoutSubField)


@receiver(post_save, sender=CustomFieldsGroup)
def parse_location(sender, instance, **kwargs):
    location_obj = instance.location
    '''[
        [{'param': 'post_type', 'operator': '==', 'value': 'post'}],
        [{'param': 'post_type', 'operator': '==', 'value': 'page'}],
        [{'param': 'attachment', 'operator': '==', 'value': 'all'}],
        [{'param': 'page_template', 'operator': '!==', 'value': 'page-landing.php'}],
        [...]
    ]
    '''

    _index = 1
    for location in location_obj:
        """order_no and group_no arn't always present"""
        for item in location:  # seems to alwasy be one but just to be sure

            for k, v in item.items():
                obj = CustomFieldsGroupLocation(
                    fields_group=instance,
                    _key=k,
                    _value=v,
                    _index=_index
                )
                obj.save()

            _index += 1


@receiver(post_save, sender=CustomFieldsLayout)
def parse_layout(sender, instance, **kwargs):
    subfields_obj = instance.sub_fields

    _index = 1
    for subfield in subfields_obj:
        # for item in subfield:  # each represents a row most likely

        for k, v in subfield.items():
            obj = CustomFieldsLayoutSubField(
                fields_layout=instance,
                _key=k,
                _value=v or '',
                _index=_index
            )
            obj.save()

        _index += 1


@receiver(post_save, sender=CustomField)
def parse_sub_fields(sender, instance, **kwargs):
    subfields_obj = instance.sub_fields

    _index = 1
    for subfield in subfields_obj:

        # for item in subfield.subfields:  # seems to alwasy be one but just to be sure

        for k, v in subfield.items():
            obj = CustomFieldSubFieldsSubField(
                custom_field=instance,
                _key=k,
                _value=v or '',
                _index=_index
            )
            obj.save()

        _index += 1
