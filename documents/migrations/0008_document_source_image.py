# Generated by Django 3.2.7 on 2021-09-07 23:44

from django.db import migrations
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0007_remove_document_source_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='source_image',
            field=wagtail.fields.StreamField([('large_image', wagtail.images.blocks.ImageChooserBlock(help_text='Source image', template='large_image.html'))], blank=True, null=True),
        ),
    ]
