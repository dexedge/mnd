# Generated by Django 3.2.7 on 2021-11-18 18:17

from django.db import migrations
import wagtail.contrib.table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0025_alter_documentpage_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentpage',
            name='commentary',
            field=wagtail.core.fields.StreamField([('richtext', wagtail.core.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'bold', 'italic', 'small,underline', 'strikethrough', 'blockquote', 'blockquote', 'blockindent', 'superscript', 'subscript', 'ul', 'image', 'link', 'hr', 'embed'], template='streams/richtext_block.html')), ('table', wagtail.contrib.table_block.blocks.TableBlock(table_options={'autoColumnSize': False, 'colHeaders': False, 'editor': 'text', 'height': 216, 'language': 'en', 'minSpareRows': 0, 'renderer': 'html', 'rowHeaders': False, 'startCols': 2, 'startRows': 1, 'stretchH': 'all'}, template='streams/table.html'))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='documentpage',
            name='notes',
            field=wagtail.core.fields.StreamField([('richtext', wagtail.core.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'bold', 'italic', 'underline', 'strikethrough', 'blockquote', 'blockindent', 'superscript', 'subscript', 'ul', 'image', 'link', 'hr', 'embed'], template='streams/richtext_block.html')), ('table', wagtail.contrib.table_block.blocks.TableBlock(table_options={'autoColumnSize': False, 'colHeaders': False, 'editor': 'text', 'height': 216, 'language': 'en', 'minSpareRows': 0, 'renderer': 'html', 'rowHeaders': False, 'startCols': 2, 'startRows': 1, 'stretchH': 'all'}, template='streams/table.html'))], blank=True, null=True),
        ),
    ]
