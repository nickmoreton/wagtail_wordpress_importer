# Generated by Django 3.1.4 on 2021-01-09 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_wordpress_importer', '0026_customfield_sub_site'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customfield',
            name='value',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
