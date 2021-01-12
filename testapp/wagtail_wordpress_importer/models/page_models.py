from django.db import models
from wagtail_wordpress_importer.models.base_models import \
    BaseImportWordpressDataModelMixin
from wagtail_wordpress_importer.models.custom_fields import CustomField

''' Django Models '''


class ImportPage(BaseImportWordpressDataModelMixin):
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
    parent = models.PositiveIntegerField(default=0)
    menu_order = models.IntegerField(default=0) # some are negative numbers
    comment_status = models.CharField(max_length=255, blank=True)
    ping_status = models.CharField(max_length=255, blank=True)
    template = models.CharField(max_length=255, blank=True)
    custom_fields = models.JSONField(blank=True)

    class Meta:
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'


    def __str__(self):
        return self.title

class ImportPageCustomField(models.Model):
    page = models.ForeignKey(
        ImportPage,
        on_delete=models.CASCADE
    )
    field = models.ForeignKey(
        CustomField,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Page Custom'
        verbose_name_plural = 'Pages Custom'
