# Generated by Django 3.2.10 on 2022-02-25 22:08

from django.db import migrations
import wagtail.contrib.typed_table_block.blocks
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0075_rename_transcription_test_documentpage_transcription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentpage',
            name='commentary',
            field=wagtail.fields.StreamField([('richtext', wagtail.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'bold', 'italic', 'underline', 'strikethrough', 'small', 'red', 'blue', 'green', 'blockquote', 'blockindent', 'doubleindent', 'center', 'superscript', 'subscript', 'ul', 'image', 'link', 'hr', 'embed'], template='streams/richtext_block.html')), ('heading', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(form_classname='full-title')), ('link_id', wagtail.blocks.CharBlock(help_text='For making hyperlinks to this heading'))], icon='title')), ('images', wagtail.blocks.StructBlock([('images', wagtail.blocks.RichTextBlock(features=['image'])), ('caption', wagtail.blocks.RichTextBlock(features=['italic', 'bold', 'strikethrough', 'link'], form_classname='centered', required=False))], icon='image', label='Images with Caption')), ('caption', wagtail.blocks.StructBlock([('caption', wagtail.blocks.RichTextBlock(features=['italic', 'bold', 'strikethrough', 'link'], form_classname='centered'))], icon='edit', label='Generic Caption')), ('annotation', wagtail.blocks.StructBlock([('annotation', wagtail.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'bold', 'italic', 'underline', 'strikethrough', 'small', 'red', 'blue', 'green', 'blockquote', 'blockindent', 'doubleindent', 'center', 'superscript', 'subscript', 'ul', 'image', 'link', 'hr', 'embed'], form_classname='centered-annotation'))], icon='edit', label='Annotation Box')), ('table', wagtail.contrib.typed_table_block.blocks.TypedTableBlock([('text', wagtail.blocks.CharBlock(required=False)), ('numeric', wagtail.blocks.FloatBlock(required=False)), ('rich_text', wagtail.blocks.RichTextBlock(features=['italic', 'bold', 'strikethrough', 'red', 'blue', 'green', 'link', 'h2'], required=False))])), ('centered_text', wagtail.blocks.StructBlock([('text', wagtail.blocks.RichTextBlock(features=['italic', 'bold', 'strikethrough', 'link'], form_classname='centered'))], icon='edit'))], blank=True, null=True),
        ),
    ]
