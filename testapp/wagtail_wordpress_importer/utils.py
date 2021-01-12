import ast
from html import unescape
from datetime import datetime

from django.utils.timezone import make_aware


def process_date(datestring):
    return make_aware(datetime.strptime(datestring, '%Y-%m-%dT%H:%M:%S'))


def stringify_integer_list(integer_list):
    lst = ''
    for item in integer_list:
        lst += str(item) + ','
    return lst.strip(',')


def html_entities(content):
    return unescape(content)


def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor


spinner = spinning_cursor()


def get_json_field_style():
    return '''
    <style>
        pre.pprint-json {
            height: 60px;
            overflow:hidden;
            max-width: 300px;
        }
        pre.pprint-json:hover {
            height: inherit;
            max-height: 600px;
            overflow:scroll;
        }
    </style>'''
