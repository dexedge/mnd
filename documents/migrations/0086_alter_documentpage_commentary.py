# Generated by Django 3.2.10 on 2022-07-24 22:23

from django.db import migrations
import wagtail.contrib.typed_table_block.blocks
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0085_auto_20220724_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentpage',
            name='commentary',
            field=wagtail.fields.StreamField([('richtext', wagtail.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'bold', 'italic', 'underline', 'strikethrough', 'small', 'red', 'blue', 'green', 'blockquote', 'blockindent', 'doubleindent', 'superscript', 'subscript', 'ul', 'image', 'link', 'hr', 'embed'], template='streams/richtext_block.html')), ('images', wagtail.blocks.StructBlock([('images', wagtail.blocks.RichTextBlock(features=['image'])), ('caption', wagtail.blocks.RichTextBlock(features=['italic', 'bold', 'strikethrough', 'link'], form_classname='centered', required=False))], icon='image', label='Image(s) with Caption')), ('caption', wagtail.blocks.StructBlock([('caption', wagtail.blocks.RichTextBlock(features=['italic', 'bold', 'strikethrough', 'link'], form_classname='centered'))], icon='edit', label='Generic Caption')), ('heading', wagtail.blocks.StructBlock([('heading', wagtail.blocks.RichTextBlock(features=['italic', 'bold', 'strikethrough', 'link'], form_classname='full-title')), ('link_id', wagtail.blocks.CharBlock(help_text='For making hyperlinks to this heading'))], icon='title')), ('annotation', wagtail.blocks.StructBlock([('annotation', wagtail.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'bold', 'italic', 'underline', 'strikethrough', 'small', 'red', 'blue', 'green', 'blockquote', 'blockindent', 'doubleindent', 'superscript', 'subscript', 'ul', 'image', 'link', 'hr', 'embed'], form_classname='centered-annotation'))], icon='edit', label='Annotation Box')), ('left_justified_block', wagtail.blocks.StructBlock([('left_justified_block', wagtail.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'bold', 'italic', 'underline', 'strikethrough', 'small', 'red', 'blue', 'green', 'blockquote', 'blockindent', 'doubleindent', 'superscript', 'subscript', 'ul', 'image', 'link', 'hr', 'embed'], form_classname='left-justified-block'))], icon='edit', label='Left Justified Block')), ('side_by_side', wagtail.blocks.StructBlock([('transcription_text', wagtail.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'bold', 'italic', 'underline', 'strikethrough', 'small', 'red', 'blue', 'green', 'blockquote', 'blockindent', 'doubleindent', 'superscript', 'subscript', 'ul', 'image', 'link', 'hr', 'embed'])), ('source_image', wagtail.images.blocks.ImageChooserBlock(help_text='Source image', required=False))], icon='edit', label='Transcription with Source')), ('table', wagtail.contrib.typed_table_block.blocks.TypedTableBlock([('text', wagtail.blocks.CharBlock(required=False)), ('numeric', wagtail.blocks.FloatBlock(required=False)), ('rich_text', wagtail.blocks.RichTextBlock(features=['italic', 'bold', 'strikethrough', 'red', 'blue', 'green', 'link', 'h2'], required=False))])), ('centered_text', wagtail.blocks.StructBlock([('text', wagtail.blocks.RichTextBlock(features=['italic', 'bold', 'strikethrough', 'superscript', 'subscript', 'link'], form_classname='centered'))], icon='edit'))], blank=True, null=True),
        ),
    ]
