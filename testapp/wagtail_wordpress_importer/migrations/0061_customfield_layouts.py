# Generated by Django 3.1.4 on 2021-01-11 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_wordpress_importer', '0060_auto_20210111_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='customfield',
            name='layouts',
            field=models.JSONField(default=''),
            preserve_default=False,
        ),
    ]