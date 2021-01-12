# Generated by Django 3.1.4 on 2021-01-12 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_wordpress_importer', '0075_auto_20210112_1157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='importpagecustomfield',
            name='sub_site',
        ),
        migrations.AlterField(
            model_name='importpagecustomfield',
            name='key',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wagtail_wordpress_importer.customfield'),
        ),
    ]
