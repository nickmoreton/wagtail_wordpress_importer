# Generated by Django 3.1.4 on 2021-01-11 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_wordpress_importer', '0065_auto_20210111_1416'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='customfieldslayout',
            unique_together={('fields_group', 'key', 'sub_site')},
        ),
    ]
