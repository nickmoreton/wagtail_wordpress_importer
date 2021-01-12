from django.db import models
from wagtail_wordpress_importer.models.base_models import \
    BaseImportWordpressDataModelMixin

''' Django Models '''


class ImportDocument(BaseImportWordpressDataModelMixin):
    ''' 
    a model intended for django admin management, 
    this will be the data source for the wagtail model 
    using BaseImportWordpressDataModelMixin to keep wordpress data
    '''
    slug = models.TextField(blank=True)
    status = models.CharField(max_length=255, blank=True)
    _type = models.CharField(max_length=255, blank=True)
    author = models.PositiveIntegerField(default=0)
    link = models.URLField(blank=True)
    title = models.TextField(blank=True)
    template = models.CharField(max_length=255, blank=True)
    categories = models.TextField(blank=True)
    publication_type = models.TextField(blank=True)
    medical_conditions = models.TextField(blank=True)
    improvement_challenges = models.TextField(blank=True)
    custom_fields = models.JSONField(blank=True)

    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'

    def __str__(self):
        return self.title
