# Generated by Django 3.2.10 on 2021-12-28 18:24

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_remove_newspage_custom_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='newspage',
            name='images',
            field=wagtail.fields.StreamField([('news_images', wagtail.blocks.StructBlock([('images', wagtail.blocks.RichTextBlock(features=['image'])), ('caption', wagtail.blocks.RichTextBlock(features=['italic', 'bold', 'strikethrough', 'link'], form_classname='centered', required=False))], icon='image', label='Images with Optional Caption'))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='newspage',
            name='body',
            field=wagtail.fields.StreamField([('text', wagtail.blocks.RichTextBlock())], blank=True, null=True),
        ),
    ]
