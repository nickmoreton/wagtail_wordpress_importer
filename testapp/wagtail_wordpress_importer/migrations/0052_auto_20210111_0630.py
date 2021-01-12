# Generated by Django 3.1.4 on 2021-01-11 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_wordpress_importer', '0051_auto_20210111_0628'),
    ]

    operations = [
        migrations.AddField(
            model_name='customfieldjsonvalues',
            name='custom_field_key',
            field=models.CharField(default='1', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customfieldjsonvalues',
            name='custom_field_value',
            field=models.TextField(blank=True),
        ),
    ]
