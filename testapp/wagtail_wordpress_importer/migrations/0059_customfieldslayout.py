# Generated by Django 3.1.4 on 2021-01-11 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_wordpress_importer', '0058_customfield_sub_fields'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomFieldsLayout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_site', models.CharField(blank=True, max_length=100, null=True)),
                ('key', models.CharField(max_length=100)),
                ('label', models.CharField(blank=True, max_length=50)),
                ('name', models.CharField(blank=True, max_length=50)),
                ('_type', models.CharField(blank=True, max_length=100)),
                ('sub_fields', models.JSONField()),
                ('fields_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wagtail_wordpress_importer.customfieldsgroup')),
            ],
            options={
                'verbose_name': 'Custom Layout',
                'verbose_name_plural': 'Custom Layouts',
                'unique_together': {('key', 'sub_site')},
            },
        ),
    ]
