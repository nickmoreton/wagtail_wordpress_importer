# Generated by Django 3.1.4 on 2021-01-11 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_wordpress_importer', '0062_customfield_is_layout'),
    ]

    operations = [
        migrations.AddField(
            model_name='customfieldsgroup',
            name='has_layout',
            field=models.BooleanField(default=False),
        ),
    ]