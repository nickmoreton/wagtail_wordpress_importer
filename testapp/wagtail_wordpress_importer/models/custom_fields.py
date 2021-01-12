'''
the models here are not used directly when moving content to wagtail
they are about documenting the custom fields from the wordpress api
by viewing in django admin to better understand how they are set up
'''


from django.db import models


class CustomFieldsGroup(models.Model):
    sub_site = models.CharField(blank=True, null=True, max_length=100)
    key = models.CharField(max_length=100)
    title = models.TextField(blank=True)
    description = models.TextField(blank=True)
    location = models.JSONField(blank=True)
    has_layout = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Custom Group'
        verbose_name_plural = 'Custom Groups'
        unique_together = [['key', 'sub_site']]

    def __str__(self):
        return self.title


class CustomFieldsGroupLocation(models.Model):
    # a model to parse out the location json from
    # CustomFieldsGroup may be useful later on for querying
    fields_group = models.ForeignKey(
        CustomFieldsGroup,
        on_delete=models.CASCADE
    )
    _key = models.CharField(max_length=100, blank=True)
    _value = models.CharField(max_length=100, blank=True)
    _index = models.PositiveIntegerField(default=0)


class CustomFieldsLayout(models.Model):
    fields_group = models.ForeignKey(
        CustomFieldsGroup,
        on_delete=models.CASCADE
    )
    sub_site = models.CharField(blank=True, null=True, max_length=100)
    key = models.CharField(max_length=100)
    label = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=50, blank=True)
    display = models.CharField(max_length=100, blank=True)
    sub_fields = models.JSONField()

    class Meta:
        verbose_name = 'Custom Layout'
        verbose_name_plural = 'Custom Layouts'
        unique_together = [['fields_group', 'key', 'sub_site']]


class CustomFieldsLayoutSubField(models.Model):
    # a model to parse out the subfields json from
    # CustomFieldsLayout may be useful later on for querying
    # custom_field = models.ForeignKey(
    #     CustomField,
    #     on_delete=models.CASCADE
    # )
    fields_layout = models.ForeignKey(
        CustomFieldsLayout,
        on_delete=models.CASCADE
    )
    _key = models.CharField(max_length=100, blank=True)
    _value = models.CharField(max_length=100, blank=True)
    _index = models.PositiveIntegerField(default=0)


class CustomField(models.Model):
    fields_group = models.ForeignKey(
        CustomFieldsGroup,
        on_delete=models.CASCADE
    )
    layout = models.ForeignKey(
        CustomFieldsLayout,
        on_delete=models.CASCADE,
        blank=True, null=True
    )
    sub_site = models.CharField(blank=True, null=True, max_length=100)
    key = models.CharField(max_length=100)
    label = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=50, blank=True)
    _type = models.CharField(max_length=100, blank=True)
    sub_fields = models.JSONField()
    layouts = models.JSONField()
    is_layout = models.BooleanField(default=False)
    usage_count = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Custom Field'
        verbose_name_plural = 'Custom Fields'
        unique_together = [['key', 'sub_site']]

    def __str__(self):
        return '{} - {}'.format(self.key, self.fields_group)


class CustomFieldSubFieldsSubField(models.Model):
    # a model to parse out the subfields json from
    # CustomField may be useful later on for querying
    custom_field = models.ForeignKey(
        CustomField,
        on_delete=models.CASCADE
    )
    _key = models.CharField(max_length=100, blank=True)
    _value = models.CharField(max_length=100, blank=True)
    _index = models.PositiveIntegerField(default=0)
