# Generated by Django 3.1.4 on 2021-01-12 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_wordpress_importer', '0077_auto_20210112_1234'),
    ]

    operations = [
        migrations.RenameField(
            model_name='importpagecustomfield',
            old_name='key',
            new_name='field',
        ),
    ]
