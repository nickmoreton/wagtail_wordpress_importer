import os

from django.conf import settings
from django.template.loader import render_to_string
from django.urls import reverse
from wagtail.core import hooks

from wagtail_wordpress_importer.cls.logging import DataLog
from wagtail_wordpress_importer.models import (ImportAtlasCaseStudy,
                                               ImportBlog, ImportCategory,
                                               ImportDocument, ImportMedia,
                                               ImportPage, ImportPost,
                                               ImportPublicationType,
                                               ImportRegion, ImportSetting)
from wagtail_wordpress_importer.models.custom_fields import (CustomField,
                                                             CustomFieldsGroup, CustomFieldsLayout)


class DashboardPanel:
    order = 1000

    def render(self):

        context = {}
        context['django_dashboard'] = \
            reverse('admin:index')
        context['atlas_case_study_url'] = \
            reverse(
                'admin:wagtail_wordpress_importer_importatlascasestudy_changelist')
        context['blog_url'] = \
            reverse('admin:wagtail_wordpress_importer_importblog_changelist')
        context['category_url'] = \
            reverse('admin:wagtail_wordpress_importer_importcategory_changelist')
        context['document_url'] = \
            reverse('admin:wagtail_wordpress_importer_importdocument_changelist')
        context['media_url'] = \
            reverse('admin:wagtail_wordpress_importer_importmedia_changelist')
        context['page_url'] = \
            reverse('admin:wagtail_wordpress_importer_importpage_changelist')
        context['post_url'] = \
            reverse('admin:wagtail_wordpress_importer_importpost_changelist')
        context['publication_type_url'] = \
            reverse(
                'admin:wagtail_wordpress_importer_importpublicationtype_changelist')
        context['region_url'] = \
            reverse('admin:wagtail_wordpress_importer_importregion_changelist')
        context['setting_url'] = \
            reverse('admin:wagtail_wordpress_importer_importsetting_changelist')
        context['custom_groups_url'] = \
            reverse('admin:wagtail_wordpress_importer_customfieldsgroup_changelist')
        context['custom_fields_url'] = \
            reverse('admin:wagtail_wordpress_importer_customfield_changelist')
        context['custom_layouts_url'] = \
            reverse('admin:wagtail_wordpress_importer_customfieldslayout_changelist')

        context['atlas_case_study_count'] = ImportAtlasCaseStudy.objects.count()
        context['blog_count'] = ImportBlog.objects.count()
        context['category_count'] = ImportCategory.objects.count()
        context['document_count'] = ImportDocument.objects.count()
        context['media_count'] = ImportMedia.objects.count()
        context['page_count'] = ImportPage.objects.count()
        context['post_count'] = ImportPost.objects.count()

        context['publication_type_count'] = ImportPublicationType.objects.count()
        context['region_count'] = ImportRegion.objects.count()
        context['setting_count'] = ImportSetting.objects.count()

        context['custom_groups_count'] = CustomFieldsGroup.objects.count()
        context['custom_fields_count'] = CustomField.objects.count()
        context['custom_layouts_count'] = CustomFieldsLayout.objects.count()

        if os.path.isdir(os.path.join(os.path.dirname(settings.BASE_DIR), 'media_store')):
            media_store = os.path.join(os.path.dirname(
                settings.BASE_DIR), 'media_store')
            media_size = getFolderSize(media_store)
            if not media_size > 10000000: #10mb
                context['media_not_run'] = True
                context['media_size'] = 0
            else:
                context['media_size'] = media_size
        else:
            context['media_not_run'] = True
            context['media_size'] = 0

        data_log = DataLog().get_data()
        context['import_data'] = data_log

        template = render_to_string('admin/dashboard.html', context)
        return template


@hooks.register('construct_homepage_panels')
def add_dashboard_panel(request, panels):
    return panels.append(DashboardPanel())


def getFolderSize(folder):
    if os.path.isdir(folder):
        total_size = os.path.getsize(folder)
        for item in os.listdir(folder):
            itempath = os.path.join(folder, item)
            if os.path.isfile(itempath):
                total_size += os.path.getsize(itempath)
            elif os.path.isdir(itempath):
                total_size += getFolderSize(itempath)
        return total_size
    return 0
