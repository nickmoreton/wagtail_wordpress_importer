from django.db import models
from wagtail_wordpress_importer.models.base_models import \
    BaseImportWordpressDataModelMixin

''' Django Models '''


class ImportMedia(BaseImportWordpressDataModelMixin):
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
    author = models.PositiveIntegerField(default=0)
    comment_status = models.CharField(max_length=255, blank=True)
    ping_status = models.CharField(max_length=255, blank=True)
    template = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    caption = models.TextField(blank=True)
    alt_text = models.CharField(max_length=255, blank=True)
    media_type = models.CharField( max_length=255, blank=True)
    mime_type = models.TextField(blank=True)
    media_details = models.JSONField(blank=True)
    post = models.PositiveIntegerField(default=0)
    source_url = models.URLField(blank=True)
    source_404 = models.BooleanField(default=False)
    file = models.TextField(blank=True)
    file_parts = models.JSONField()

    class Meta:
        verbose_name = 'Media'
        verbose_name_plural = 'Media'

    def __str__(self):
        return self.title
