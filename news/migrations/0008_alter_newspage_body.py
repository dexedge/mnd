# Generated by Django 3.2.10 on 2021-12-29 00:52

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_alter_newspage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspage',
            name='body',
            field=wagtail.core.fields.StreamField([('text', wagtail.core.blocks.RichTextBlock()), ('news_item', wagtail.core.blocks.StructBlock([('item', wagtail.core.blocks.PageChooserBlock()), ('description', wagtail.core.blocks.RichTextBlock())]))], blank=True, null=True),
        ),
    ]
