# Generated by Django 3.1.4 on 2021-01-09 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_wordpress_importer', '0035_auto_20210109_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customfield',
            name='sub_fields',
            field=models.JSONField(blank=True),
        ),
    ]
