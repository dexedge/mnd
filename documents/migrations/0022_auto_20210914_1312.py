# Generated by Django 3.2.7 on 2021-09-14 13:12

from django.db import migrations
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0021_rename_document_documentpage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentpage',
            name='transcription',
            field=wagtail.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='documentpage',
            name='translation',
            field=wagtail.fields.RichTextField(blank=True),
        ),
    ]
