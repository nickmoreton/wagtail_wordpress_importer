# Generated by Django 3.1.4 on 2021-01-11 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_wordpress_importer', '0063_customfieldsgroup_has_layout'),
    ]

    operations = [
        migrations.AddField(
            model_name='customfield',
            name='layout',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='wagtail_wordpress_importer.customfieldslayout'),
            preserve_default=False,
        ),
    ]
