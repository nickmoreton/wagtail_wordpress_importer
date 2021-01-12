
import os
import json

import requests
from django.core.management import BaseCommand
from django.conf import settings


class Command(BaseCommand):
        

    def handle(self, *args, **kwargs):
        
        self.fixtures_dir = os.path.join(
                settings.BASE_DIR, 'wagtail_wordpress_importer/fixtures')
        if not os.path.isdir(self.fixtures_dir):
            os.makedirs(self.fixtures_dir)

        self.blogs_data()
        self.posts_data()
        self.categories_data()
        self.publication_types_data()
        self.regions_data()
        self.settings_data()
        self.pages_data()
        self.atlas_case_studies_data()
        self.media_data()
        self.documents_data()



    def blogs_data(self):
        r = requests.get(
            'https://www.england.nhs.uk/wp-json/wp/v2/blogs?per_page=100')
        with open(os.path.join(self.fixtures_dir, 'blogs_data.json'), 'w') as outfile:
            json.dump(r.json(), outfile, indent=2)

    def posts_data(self):
        r = requests.get(
            'https://www.england.nhs.uk/wp-json/wp/v2/posts?per_page=100')
        with open(os.path.join(self.fixtures_dir, 'posts_data.json'), 'w') as outfile:
            json.dump(r.json(), outfile, indent=2)

    def categories_data(self):
        r = requests.get(
            'https://www.england.nhs.uk/wp-json/wp/v2/categories?per_page=100')
        with open(os.path.join(self.fixtures_dir, 'categories_data.json'), 'w') as outfile:
            json.dump(r.json(), outfile, indent=2)

    def publication_types_data(self):
        r = requests.get(
            'https://www.england.nhs.uk/wp-json/wp/v2/publication-type?per_page=100')
        with open(os.path.join(self.fixtures_dir, 'publication_types_data.json'), 'w') as outfile:
            json.dump(r.json(), outfile, indent=2)

    def regions_data(self):
        r = requests.get(
            'https://www.england.nhs.uk/wp-json/wp/v2/region?per_page=100')
        with open(os.path.join(self.fixtures_dir, 'regions_data.json'), 'w') as outfile:
            json.dump(r.json(), outfile, indent=2)

    def settings_data(self):
        r = requests.get(
            'https://www.england.nhs.uk/wp-json/wp/v2/setting?per_page=100')
        with open(os.path.join(self.fixtures_dir, 'settings_data.json'), 'w') as outfile:
            json.dump(r.json(), outfile, indent=2)

    def pages_data(self):
        r = requests.get(
            'https://www.england.nhs.uk/wp-json/wp/v2/pages?per_page=100')
        with open(os.path.join(self.fixtures_dir, 'pages_data.json'), 'w') as outfile:
            json.dump(r.json(), outfile, indent=2)

    def atlas_case_studies_data(self):
        r = requests.get(
            'https://www.england.nhs.uk/wp-json/wp/v2/atlas_case_studies?per_page=100')
        with open(os.path.join(self.fixtures_dir, 'atlas_case_studies_data.json'), 'w') as outfile:
            json.dump(r.json(), outfile, indent=2)

    def media_data(self):
        r = requests.get(
            'https://www.england.nhs.uk/wp-json/wp/v2/media?per_page=100')
        with open(os.path.join(self.fixtures_dir, 'media_data.json'), 'w') as outfile:
            json.dump(r.json(), outfile, indent=2)

    def documents_data(self):
        r = requests.get(
            'https://www.england.nhs.uk/wp-json/wp/v2/documents?per_page=100')
        with open(os.path.join(self.fixtures_dir, 'documents_data.json'), 'w') as outfile:
            json.dump(r.json(), outfile, indent=2)
