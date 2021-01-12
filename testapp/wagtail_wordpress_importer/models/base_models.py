from django.db import models
from simple_history.models import HistoricalRecords
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel


class BaseImportWordpressDataModelMixin(models.Model):
    ''' 
    to make sure we have wordpress meta data on all models 
    subclass this for all & only django models
    '''
    wp_id = models.PositiveIntegerField(
        verbose_name='Wordpress ID'
    )
    date_gmt = models.DateTimeField(blank=True, null=True)
    modified_gmt = models.DateTimeField(blank=True, null=True)
    sub_site = models.CharField(blank=True, null=True, max_length=100)
    history = HistoricalRecords(inherit=True)

    class Meta:
        abstract = True


class WagtailWordpressDataModelMixin(models.Model):
    ''' 
    to make sure we have wordpress meta data on all wagtail models 
    subclass this for all & only wagtail models
    '''
    wp_id = models.PositiveIntegerField(
        verbose_name='Wordpress ID'
    )
    date_gmt = models.DateTimeField(blank=True)
    modified_gmt = models.DateTimeField(blank=True)

    class Meta:
        abstract = True

    field_panels = [
        MultiFieldPanel([
            FieldPanel('wp_id'),
            FieldPanel('date_gmt'),
            FieldPanel('modified_gmt'),
        ])
    ]
