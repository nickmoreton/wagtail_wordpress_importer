# Generated by Django 3.1.4 on 2021-01-11 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_wordpress_importer', '0052_auto_20210111_0630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customfieldjsonvalues',
            name='custom_field_value',
            field=models.TextField(blank=True, null=True),
        ),
    ]