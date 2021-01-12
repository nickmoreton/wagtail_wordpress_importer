from django.core.management import BaseCommand
from wagtail_wordpress_importer.models import ImportAtlasCaseStudy
from wagtail_wordpress_importer.models.blog_models import ImportBlog
from wagtail_wordpress_importer.models.custom_fields import CustomField
from wagtail_wordpress_importer.models.documents import ImportDocument
from wagtail_wordpress_importer.models.page_models import ImportPage, ImportPageCustomField
from wagtail_wordpress_importer.models.post_models import ImportPost
from wagtail_wordpress_importer.utils import spinner

IGNORE_FIELDS = [
    # https://www.england.nhs.uk/wp-json/custom_fields/v1/fields/field_5891c93543cca
    # this always has the value of `Parallax` but seems to never be used so lets ignore it.
    # Pages
    'field_5891c93543cca'
]


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        # reset usage count to start with
        self.stdout.write(
            'Registering Custom Fields. This may take a while...')
        self.stdout.write('Resetting usage counts...')
        all_custom_fields = CustomField.objects.all().update(usage_count=0)

        '''ATLAS CASE STUDIES'''
        atlas_case_studies = ImportAtlasCaseStudy.objects.all()
        self.stdout.write('Counting Atlas Case Studies Usage...')
        for atlas_case_study in atlas_case_studies:
            self.stdout.write(next(spinner), ending='\b')
            custom_fields = self.custom_field_as_list(
                atlas_case_study.custom_fields)
            if custom_fields:
                subsite = atlas_case_study.sub_site
                for row in custom_fields:
                    for k, v in row.items():
                        if v:
                            field = CustomField.objects.get(
                                key=k, sub_site=subsite)
                            field.usage_count += 1
                            field.save()

        '''BLOGS'''
        blogs = ImportBlog.objects.all()
        self.stdout.write('Counting Blogs Usage...')
        for blog in blogs:
            self.stdout.write(next(spinner), ending='\b')
            custom_fields = self.custom_field_as_list(
                blog.custom_fields)
            if custom_fields:
                subsite = blog.sub_site
                for row in custom_fields:
                    for k, v in row.items():
                        if v:
                            field = CustomField.objects.get(
                                key=k, sub_site=subsite)
                            field.usage_count += 1
                            field.save()

        '''PAGES'''

        # clear the related table ImportPageCustomField
        ImportPageCustomField.objects.all().delete()
        pages = ImportPage.objects.all()
        self.stdout.write('Counting Pages Usage...')
        for page in pages:
            self.stdout.write(next(spinner), ending='\b')
            custom_fields = self.custom_field_as_list(
                page.custom_fields)
            if custom_fields:
                subsite = page.sub_site
                for row in custom_fields:
                    for k, v in row.items():
                        if v and k not in IGNORE_FIELDS:
                            field = CustomField.objects.get(
                                key=k, sub_site=subsite)
                            field.usage_count += 1
                            field.save()
                            ImportPageCustomField.objects.create(
                                field=field,
                                page=page,
                            )

        '''POSTS'''

        posts = ImportPost.objects.all()
        self.stdout.write('Counting Posts Usage...')
        for post in posts:
            self.stdout.write(next(spinner), ending='\b')
            custom_fields = self.custom_field_as_list(
                post.custom_fields)
            if custom_fields:
                subsite = post.sub_site
                for row in custom_fields:
                    for k, v in row.items():
                        if v:
                            field = CustomField.objects.get(
                                key=k, sub_site=subsite)
                            field.usage_count += 1
                            field.save()

        '''DOCUMENTS'''

        documents = ImportDocument.objects.all()
        self.stdout.write('Counting Documents Usage...')
        for document in documents:
            self.stdout.write(next(spinner), ending='\b')
            custom_fields = self.custom_field_as_list(
                document.custom_fields)
            if custom_fields:
                subsite = document.sub_site
                for row in custom_fields:
                    for k, v in row.items():
                        field = CustomField.objects.get(
                            key=k, sub_site=subsite)
                        field.usage_count += 1
                        field.save()

    def custom_field_as_list(self, custom_field=None):
        if custom_field and isinstance(custom_field, list):
            return custom_field
        elif custom_field and isinstance(custom_field, dict):
            return [custom_field]
