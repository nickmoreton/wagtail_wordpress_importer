# Generated by Django 3.1.4 on 2021-01-09 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_wordpress_importer', '0038_customfield_sub_site'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customfield',
            old_name='field',
            new_name='json_field',
        ),
    ]
