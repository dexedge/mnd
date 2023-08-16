# Generated by Django 3.2.10 on 2023-01-27 00:15

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0015_alter_newspage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspage',
            name='body',
            field=wagtail.core.fields.StreamField([('text', wagtail.core.blocks.RichTextBlock(features=['underline', 'bold', 'italic', 'small', 'red', 'hr', 'blockquote', 'ul', 'link'])), ('news_item', wagtail.core.blocks.StructBlock([('item', wagtail.core.blocks.PageChooserBlock()), ('description', wagtail.core.blocks.RichTextBlock(features=['underline', 'bold', 'italic', 'red', 'blockquote', 'ul', 'hr', 'link'], required=False))], icon='edit'))], blank=True, null=True),
        ),
    ]