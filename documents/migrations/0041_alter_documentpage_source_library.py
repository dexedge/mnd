# Generated by Django 3.2.10 on 2021-12-20 00:15

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0040_auto_20211219_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentpage',
            name='source_library',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
    ]