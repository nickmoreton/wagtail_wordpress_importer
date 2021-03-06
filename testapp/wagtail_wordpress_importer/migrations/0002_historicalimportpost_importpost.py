# Generated by Django 3.1.4 on 2021-01-07 07:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wagtail_wordpress_importer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImportPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wp_id', models.PositiveIntegerField(verbose_name='Wordpress ID')),
                ('date_gmt', models.DateTimeField(blank=True, null=True)),
                ('modified_gmt', models.DateTimeField(blank=True, null=True)),
                ('sub_site', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(blank=True)),
                ('status', models.CharField(blank=True, max_length=255)),
                ('_type', models.CharField(blank=True, max_length=255)),
                ('link', models.URLField(blank=True)),
                ('title', models.TextField(blank=True)),
                ('content', models.TextField(blank=True)),
                ('excerpt', models.TextField(blank=True)),
                ('author', models.PositiveIntegerField(default=0)),
                ('featured_media', models.PositiveIntegerField(default=0)),
                ('comment_status', models.CharField(blank=True, max_length=255)),
                ('ping_status', models.CharField(blank=True, max_length=255)),
                ('sticky', models.BooleanField(blank=True)),
                ('template', models.CharField(blank=True, max_length=255)),
                ('_format', models.CharField(blank=True, max_length=255)),
                ('categories', models.TextField(blank=True)),
                ('tags', models.TextField(blank=True)),
                ('custom_fields', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
        migrations.CreateModel(
            name='HistoricalImportPost',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('wp_id', models.PositiveIntegerField(verbose_name='Wordpress ID')),
                ('date_gmt', models.DateTimeField(blank=True, null=True)),
                ('modified_gmt', models.DateTimeField(blank=True, null=True)),
                ('sub_site', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(blank=True)),
                ('status', models.CharField(blank=True, max_length=255)),
                ('_type', models.CharField(blank=True, max_length=255)),
                ('link', models.URLField(blank=True)),
                ('title', models.TextField(blank=True)),
                ('content', models.TextField(blank=True)),
                ('excerpt', models.TextField(blank=True)),
                ('author', models.PositiveIntegerField(default=0)),
                ('featured_media', models.PositiveIntegerField(default=0)),
                ('comment_status', models.CharField(blank=True, max_length=255)),
                ('ping_status', models.CharField(blank=True, max_length=255)),
                ('sticky', models.BooleanField(blank=True)),
                ('template', models.CharField(blank=True, max_length=255)),
                ('_format', models.CharField(blank=True, max_length=255)),
                ('categories', models.TextField(blank=True)),
                ('tags', models.TextField(blank=True)),
                ('custom_fields', models.TextField(blank=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Post',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
