import json
import os
from datetime import datetime

from django.conf import settings
from django.utils.text import slugify
from django.utils.dateparse import parse_datetime

from wagtail_wordpress_importer.utils import process_date


class SimpleLog:
    def log_message(self, url, message):

        log_dir = os.path.join(os.path.dirname(settings.BASE_DIR), 'log')

        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        file_name = slugify(url) + '.log'
        file = '/'.join([log_dir, file_name])
        f = open(file, 'w')
        f.write(url + ' | ' + message)


class DataLog:

    def __init__(self):
        self.data_store = os.path.join(
            os.path.dirname(settings.BASE_DIR), 'data_store')
        # initalise a json data file
        if not os.path.exists(self.data_store):
            os.makedirs(self.data_store)
            data = {
                'atlas_case_study_date': '',
                'blog_date': '',
                'category_date': '',
                'document_date': '',
                'media_date': '',
                'media_fetched_date': '',
                'page_date': '',
                'post_date': '',
                'publication_type_date': '',
                'region_date': '',
                'setting_date': '',
                'import': '',
                'processed': '',
            }
            self.write_data(data)

    def read_data(self):
        f = open(os.path.join(self.data_store, 'importdata.json'), 'r')
        data_string = f.read()
        return json.loads(data_string)

    def write_data(self, data):
        f = open(os.path.join(self.data_store, 'importdata.json'), 'w')
        json.dump(data, f, indent=2)

    def get_data(self):
        data_string = self.read_data()
        for k,v in data_string.items():
            data_string[k] = parse_datetime(v)
        print(data_string)
        return data_string
