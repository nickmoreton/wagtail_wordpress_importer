# Generated by Django 3.1.4 on 2021-01-09 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_wordpress_importer', '0032_auto_20210109_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customfield',
            name='max',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='customfield',
            name='min',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
