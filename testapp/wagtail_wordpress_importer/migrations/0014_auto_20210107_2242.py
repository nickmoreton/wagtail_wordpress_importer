# Generated by Django 3.1.4 on 2021-01-07 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_wordpress_importer', '0013_auto_20210107_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalimportmedia',
            name='file',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='importmedia',
            name='file',
            field=models.TextField(blank=True),
        ),
    ]