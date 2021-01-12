# Generated by Django 3.1.4 on 2021-01-11 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_wordpress_importer', '0048_auto_20210110_2231'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomFieldJsonValues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_value', models.JSONField()),
            ],
            options={
                'verbose_name': 'Custom Field Value',
                'verbose_name_plural': 'Custom Field Values',
                'ordering': ('id',),
            },
        ),
    ]
