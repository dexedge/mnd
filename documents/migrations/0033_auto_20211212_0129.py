# Generated by Django 3.2.7 on 2021-12-12 01:29

from django.db import migrations
import wagtail.contrib.typed_table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0032_alter_documentpage_commentary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentpage',
            name='commentary',
            field=wagtail.core.fields.StreamField([('richtext', wagtail.core.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'bold', 'italic', 'underline', 'strikethrough', 'small', 'blockquote', 'blockindent', 'doubleindent', 'center', 'superscript', 'subscript', 'ul', 'image', 'link', 'hr', 'embed'], template='streams/richtext_block.html')), ('heading', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(form_classname='full title')), ('link_id', wagtail.core.blocks.CharBlock(help_text='For making hyperlinks to this heading'))])), ('table', wagtail.contrib.typed_table_block.blocks.TypedTableBlock([('text', wagtail.core.blocks.CharBlock(required=False)), ('numeric', wagtail.core.blocks.FloatBlock(required=False)), ('rich_text', wagtail.core.blocks.RichTextBlock(features=['italic', 'bold', 'strikethrough', 'link', 'h2'], required=False))]))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='documentpage',
            name='notes',
            field=wagtail.core.fields.StreamField([('richtext', wagtail.core.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'bold', 'italic', 'underline', 'strikethrough', 'small', 'blockquote', 'blockindent', 'doubleindent', 'center', 'superscript', 'subscript', 'ul', 'image', 'link', 'hr', 'embed'], template='streams/richtext_block.html')), ('table', wagtail.contrib.typed_table_block.blocks.TypedTableBlock([('text', wagtail.core.blocks.CharBlock(required=False)), ('numeric', wagtail.core.blocks.FloatBlock(required=False)), ('rich_text', wagtail.core.blocks.RichTextBlock(features=['italic', 'bold', 'strikethrough', 'link', 'h2'], required=False))]))], blank=True, null=True),
        ),
    ]
