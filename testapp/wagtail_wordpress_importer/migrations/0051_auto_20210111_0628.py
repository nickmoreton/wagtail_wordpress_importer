# Generated by Django 3.1.4 on 2021-01-11 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_wordpress_importer', '0050_customfieldjsonvalues__field'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customfieldjsonvalues',
            old_name='_field',
            new_name='custom_field',
        ),
        migrations.RenameField(
            model_name='customfieldjsonvalues',
            old_name='_value',
            new_name='custom_field_value',
        ),
    ]
