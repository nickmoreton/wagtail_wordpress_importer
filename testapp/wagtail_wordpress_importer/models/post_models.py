from django.db import models
from wagtail_wordpress_importer.models.base_models import \
    BaseImportWordpressDataModelMixin

''' Django Models '''


class ImportPost(BaseImportWordpressDataModelMixin):
    ''' 
    a model intended for django admin management, 
    this will be the data source for the wagtail model 
    using BaseImportWordpressDataModelMixin to keep wordpress data
    '''
    slug = models.SlugField(blank=True)
    status = models.CharField(max_length=255, blank=True)
    _type = models.CharField(max_length=255, blank=True)
    link = models.URLField(blank=True)
    title = models.TextField(blank=True)
    content = models.TextField(blank=True)
    excerpt = models.TextField(blank=True)
    author = models.PositiveIntegerField(default=0)
    featured_media = models.PositiveIntegerField(default=0)
    comment_status = models.CharField(max_length=255, blank=True)
    ping_status = models.CharField(max_length=255, blank=True)
    sticky = models.BooleanField(blank=True)
    template = models.CharField(max_length=255, blank=True)
    _format = models.CharField(max_length=255, blank=True)
    categories = models.TextField(blank=True)
    tags = models.TextField(blank=True)
    custom_fields = models.JSONField(blank=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title
