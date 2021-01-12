import json
import os

from django.conf import settings
from django.core.management import call_command
from django.db.models import base
from django.test import TestCase
from wagtail_wordpress_importer.management.commands import (
    import_atlas_case_studies, import_blogs, import_categories,
    import_documents, import_media, import_pages, import_posts,
    import_publication_types, import_regions, import_settings)
from wagtail_wordpress_importer.models import ImportAtlasCaseStudy
from wagtail_wordpress_importer.models.blog_models import ImportBlog
from wagtail_wordpress_importer.models.classification import (
    ImportCategory, ImportPublicationType, ImportRegion, ImportSetting)
from wagtail_wordpress_importer.models.documents import ImportDocument
from wagtail_wordpress_importer.models.media import ImportMedia
from wagtail_wordpress_importer.models.page_models import ImportPage
from wagtail_wordpress_importer.models.post_models import ImportPost


class AtlasCaseStudyCommandsTestCase(TestCase):

    def tearDown(self):
        fixtures_dir = os.path.join(
            settings.BASE_DIR, 'wagtail_wordpress_importer/fixtures')
        os.system('rm -R {}'.format(fixtures_dir))

    def setUp(self):

        call_command('get_fixtures') # make sure we have fixtures in place

        subsite = 'root'

        fixtures_dir = os.path.join(
            settings.BASE_DIR, 'wagtail_wordpress_importer/fixtures')

        atlas_case_studies_json = open(os.path.join(
            fixtures_dir, 'atlas_case_studies_data.json'), 'r').read()
        atlas_case_studies_data = json.loads(atlas_case_studies_json)
        self.atlas_case_studies_data_count = len(atlas_case_studies_data)

        import_atlas_case_studies.Command().save_data(
            atlas_case_studies_data, subsite)

        blogs_json = open(os.path.join(
            fixtures_dir, 'blogs_data.json'), 'r').read()
        blogs_data = json.loads(blogs_json)
        self.blogs_data_count = len(blogs_data)

        import_blogs.Command().save_data(
            blogs_data, subsite)

        categories_json = open(os.path.join(
            fixtures_dir, 'categories_data.json'), 'r').read()
        categories_data = json.loads(categories_json)
        self.categories_data_count = len(categories_data)

        import_categories.Command().save_data(
            categories_data, subsite)

        pages_json = open(os.path.join(
            fixtures_dir, 'pages_data.json'), 'r').read()
        pages_data = json.loads(pages_json)
        self.pages_data_count = len(pages_data)

        import_pages.Command().save_data(
            pages_data, subsite)

        posts_json = open(os.path.join(
            fixtures_dir, 'posts_data.json'), 'r').read()
        posts_data = json.loads(posts_json)
        self.posts_data_count = len(posts_data)

        import_posts.Command().save_data(
            posts_data, subsite)

        publication_types_json = open(os.path.join(
            fixtures_dir, 'publication_types_data.json'), 'r').read()
        publication_types_data = json.loads(publication_types_json)
        self.publication_types_data_count = len(publication_types_data)

        import_publication_types.Command().save_data(
            publication_types_data, subsite)

        regions_json = open(os.path.join(
            fixtures_dir, 'regions_data.json'), 'r').read()
        regions_data = json.loads(regions_json)
        self.regions_data_count = len(regions_data)

        import_regions.Command().save_data(
            regions_data, subsite)

        settings_json = open(os.path.join(
            fixtures_dir, 'settings_data.json'), 'r').read()
        settings_data = json.loads(settings_json)
        self.settings_data_count = len(settings_data)

        import_settings.Command().save_data(
            settings_data, subsite)

        media_json = open(os.path.join(
            fixtures_dir, 'media_data.json'), 'r').read()
        media_data = json.loads(media_json)
        self.media_data_count = len(media_data)

        import_media.Command().save_data(
            media_data, subsite)

        documents_json = open(os.path.join(
            fixtures_dir, 'documents_data.json'), 'r').read()
        documents_data = json.loads(documents_json)
        self.documents_data_count = len(documents_data)

        import_documents.Command().save_data(
            documents_data, subsite)

    def test_atlas_case_study_commands(self):
        atlas_case_studies = ImportAtlasCaseStudy.objects.count()
        self.assertEqual(atlas_case_studies,
                         self.atlas_case_studies_data_count)

        call_command('delete_atlas_case_studies')
        atlas_case_studies = ImportAtlasCaseStudy.objects.count()
        self.assertEqual(atlas_case_studies, 0)

    def test_blogs_commands(self):
        blogs = ImportBlog.objects.count()
        self.assertEqual(blogs, self.blogs_data_count)

        call_command('delete_blogs')
        blogs = ImportBlog.objects.count()
        self.assertEqual(blogs, 0)
    
    def test_categories_commands(self):
        categories = ImportCategory.objects.count()
        self.assertEqual(categories, self.categories_data_count)

        call_command('delete_categories')
        categories = ImportCategory.objects.count()
        self.assertEqual(categories, 0)
    
    def test_pages_commands(self):
        pages = ImportPage.objects.count()
        self.assertEqual(pages, self.pages_data_count)

        call_command('delete_pages')
        pages = ImportPage.objects.count()
        self.assertEqual(pages, 0)
    
    def test_posts_commands(self):
        posts = ImportPost.objects.count()
        self.assertEqual(posts, self.posts_data_count)

        call_command('delete_posts')
        posts = ImportPost.objects.count()
        self.assertEqual(posts, 0)
    
    def test_publication_types_commands(self):
        publication_types = ImportPublicationType.objects.count()
        self.assertEqual(publication_types, self.publication_types_data_count)

        call_command('delete_publication_types')
        publication_types = ImportPublicationType.objects.count()
        self.assertEqual(publication_types, 0)
    
    def test_regions_commands(self):
        regions = ImportRegion.objects.count()
        self.assertEqual(regions, self.regions_data_count)

        call_command('delete_regions')
        regions = ImportRegion.objects.count()
        self.assertEqual(regions, 0)
    
    def test_settings_commands(self):
        settings = ImportSetting.objects.count()
        self.assertEqual(settings, self.settings_data_count)

        call_command('delete_settings')
        settings = ImportSetting.objects.count()
        self.assertEqual(settings, 0)
    
    def test_media_commands(self):
        media = ImportMedia.objects.count()
        self.assertEqual(media, self.media_data_count)

        call_command('delete_media')
        media = ImportMedia.objects.count()
        self.assertEqual(media, 0)
    
    def test_documents_commands(self):
        documents = ImportDocument.objects.count()
        self.assertEqual(documents, self.documents_data_count)

        call_command('delete_documents')
        documents = ImportDocument.objects.count()
        self.assertEqual(documents, 0)

    # this will actually remove some dirs so choosing not to enable it by default
    # def test_run_delete_command(self):
    #     call_command('run_delete')
    #     log_dir = os.path.join(os.path.dirname(settings.BASE_DIR), 'log')
    #     log_isdir = os.path.isdir(log_dir)
    #     self.assertFalse(log_isdir)

    #     data_dir = os.path.join(os.path.dirname(settings.BASE_DIR), 'data_store')
    #     data_isdir = os.path.isdir(data_dir)
    #     self.assertFalse(data_isdir)

    #     media_dir = os.path.join(os.path.dirname(settings.BASE_DIR), 'media_store')
    #     media_isdir = os.path.isdir(media_dir)
    #     self.assertFalse(media_isdir)