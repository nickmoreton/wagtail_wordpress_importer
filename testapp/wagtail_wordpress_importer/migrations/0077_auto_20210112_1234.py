# Generated by Django 3.1.4 on 2021-01-12 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_wordpress_importer', '0076_auto_20210112_1200'),
    ]

    operations = [
        migrations.RenameField(
            model_name='importpagecustomfield',
            old_name='import_page',
            new_name='page',
        ),
    ]
