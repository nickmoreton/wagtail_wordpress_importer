import os
import time

from django.conf import settings
from django.core.management import BaseCommand, call_command
from django.utils import timezone
from wagtail_wordpress_importer.cls.logging import DataLog
from wagtail_wordpress_importer.utils import process_date, spinner


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        import_data_logger = DataLog()
        data = import_data_logger.read_data()

        self.stdout.write('This will take some time to finish ...')
        self.stdout.write(self.style.WARNING(
            '`404` and `zero results` may be shown but thats expected 😅'))

        time.sleep(2)  # only so one has time to read the message

        call_command('import_categories')
        data['category_date'] = str(process_date(
            timezone.now().strftime('%Y-%m-%dT%H:%M:%S')))
        import_data_logger.write_data(data)

        call_command('import_regions')
        data['region_date'] = str(process_date(
            timezone.now().strftime('%Y-%m-%dT%H:%M:%S')))
        import_data_logger.write_data(data)

        call_command('import_settings')
        data['setting_date'] = str(process_date(
            timezone.now().strftime('%Y-%m-%dT%H:%M:%S')))
        import_data_logger.write_data(data)

        call_command('import_publication_types')
        data['publication_type_date'] = str(process_date(
            timezone.now().strftime('%Y-%m-%dT%H:%M:%S')))
        import_data_logger.write_data(data)

        call_command('import_custom_fields')
        data['custom_field_groups_date'] = str(process_date(
            timezone.now().strftime('%Y-%m-%dT%H:%M:%S')))
        import_data_logger.write_data(data)

        call_command('import_atlas_case_studies')
        data['atlas_case_study_date'] = str(process_date(
            timezone.now().strftime('%Y-%m-%dT%H:%M:%S')))
        import_data_logger.write_data(data)

        call_command('import_blogs')
        data['blog_date'] = str(process_date(
            timezone.now().strftime('%Y-%m-%dT%H:%M:%S')))
        import_data_logger.write_data(data)

        call_command('import_posts')
        data['post_date'] = str(process_date(
            timezone.now().strftime('%Y-%m-%dT%H:%M:%S')))
        import_data_logger.write_data(data)

        call_command('import_pages')
        data['page_date'] = str(process_date(
            timezone.now().strftime('%Y-%m-%dT%H:%M:%S')))
        import_data_logger.write_data(data)

        call_command('import_documents')
        data['document_date'] = str(process_date(
            timezone.now().strftime('%Y-%m-%dT%H:%M:%S')))
        import_data_logger.write_data(data)

        call_command('import_media')
        data['media_date'] = str(process_date(
            timezone.now().strftime('%Y-%m-%dT%H:%M:%S')))
        import_data_logger.write_data(data)

        data['import'] = str(process_date(
            timezone.now().strftime('%Y-%m-%dT%H:%M:%S')))
        import_data_logger.write_data(data)

        self.stdout.write(self.style.SUCCESS('All Done 🎉 👍'))
