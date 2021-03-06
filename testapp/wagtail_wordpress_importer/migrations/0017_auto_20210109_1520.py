# Generated by Django 3.1.4 on 2021-01-09 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_wordpress_importer', '0016_auto_20210109_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customfieldsgroup',
            name='description',
            field=models.TextField(blank=True, default='empty'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customfieldsgroup',
            name='key',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='customfieldsgroup',
            name='location',
            field=models.TextField(blank=True, default='empty'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customfieldsgroup',
            name='title',
            field=models.TextField(blank=True, default='empty'),
            preserve_default=False,
        ),
    ]
