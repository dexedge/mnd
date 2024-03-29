# Generated by Django 3.2.7 on 2021-12-12 01:21

from django.db import migrations
import wagtail.contrib.typed_table_block.blocks
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0031_alter_documentpage_commentary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentpage',
            name='commentary',
            field=wagtail.fields.StreamField([('richtext', wagtail.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'bold', 'italic', 'underline', 'strikethrough', 'small', 'blockquote', 'blockindent', 'doubleindent', 'center', 'superscript', 'subscript', 'ul', 'image', 'link', 'hr', 'embed'], template='streams/richtext_block.html')), ('heading', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(form_classname='full title')), ('link_id', wagtail.blocks.CharBlock(help_text='For making hyperlinks to this heading'))])), ('table', wagtail.contrib.typed_table_block.blocks.TypedTableBlock([('text', wagtail.blocks.CharBlock(blank=True, null=True)), ('numeric', wagtail.blocks.FloatBlock(blank=True, null=True)), ('rich_text', wagtail.blocks.RichTextBlock(blank=True, features=['italic', 'bold', 'strikethrough', 'link', 'h2'], null=True))]))], blank=True, null=True),
        ),
    ]
