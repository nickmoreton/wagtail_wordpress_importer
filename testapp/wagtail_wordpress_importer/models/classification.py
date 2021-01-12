from django.db import models
from wagtail_wordpress_importer.models.base_models import \
    BaseImportWordpressDataModelMixin

''' Django Models '''


class ImportCategory(BaseImportWordpressDataModelMixin):
    ''' 
    a model intended for django admin management, 
    this will be the data source for the wagtail model 
    using BaseImportWordpressDataModelMixin to keep wordpress data
    '''
    count = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True)
    link = models.URLField(blank=True)
    name = models.TextField(blank=True)
    slug = models.SlugField(blank=True)
    taxonomy = models.CharField(max_length=255, blank=True)
    parent = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class ImportRegion(BaseImportWordpressDataModelMixin):
    ''' 
    a model intended for django admin management, 
    this will be the data source for the wagtail model 
    using BaseImportWordpressDataModelMixin to keep wordpress data
    '''
    count = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True)
    link = models.URLField(blank=True)
    name = models.TextField(blank=True)
    slug = models.SlugField(blank=True)
    taxonomy = models.CharField(max_length=255, blank=True)
    parent = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Region'
        verbose_name_plural = 'Regions'

    def __str__(self):
        return self.name


class ImportSetting(BaseImportWordpressDataModelMixin):
    ''' 
    a model intended for django admin management, 
    this will be the data source for the wagtail model 
    using BaseImportWordpressDataModelMixin to keep wordpress data
    '''
    count = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True)
    link = models.URLField(blank=True)
    name = models.TextField(blank=True)
    slug = models.SlugField(blank=True)
    taxonomy = models.CharField(max_length=255, blank=True)
    parent = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Setting'
        verbose_name_plural = 'Settings'

    def __str__(self):
        return self.name


class ImportPublicationType(BaseImportWordpressDataModelMixin):
    ''' 
    a model intended for django admin management, 
    this will be the data source for the wagtail model 
    using BaseImportWordpressDataModelMixin to keep wordpress data
    '''
    count = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True)
    link = models.URLField(blank=True)
    name = models.TextField(blank=True)
    slug = models.SlugField(blank=True)
    taxonomy = models.CharField(max_length=255, blank=True)
    parent = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Publication Type'
        verbose_name_plural = 'Publication Types'

    def __str__(self):
        return self.name
