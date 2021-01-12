from django.db import models
from wagtail_wordpress_importer.models.base_models import \
    BaseImportWordpressDataModelMixin

''' Django Models '''


class ImportAtlasCaseStudy(BaseImportWordpressDataModelMixin):
    ''' 
    a model intended for django admin management, 
    this will be the data source for the wagtail model 
    using BaseImportWordpressDataModelMixin to keep wordpress data
    '''
    slug = models.TextField(blank=True)
    status = models.CharField(max_length=255, blank=True)
    _type = models.CharField(max_length=255, blank=True)
    link = models.URLField(blank=True)
    title = models.TextField(blank=True)
    content = models.TextField(blank=True)
    template = models.CharField(max_length=255, blank=True)
    categories = models.TextField(blank=True)
    regions = models.TextField(blank=True)
    settings = models.TextField(blank=True)
    publication_type = models.TextField(blank=True)
    custom_fields = models.JSONField(blank=True)

    class Meta:
        verbose_name = 'Atlas Case Study'
        verbose_name_plural = 'Atlas Case Studies'

    def __str__(self):
        return self.title
