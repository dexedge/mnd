# Generated by Django 3.2.10 on 2022-02-27 20:52

from django.db import migrations
import wagtail.contrib.typed_table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0077_auto_20220227_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentpage',
            name='commentary',
            field=wagtail.core.fields.StreamField([('richtext', wagtail.core.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'bold', 'italic', 'underline', 'strikethrough', 'small', 'red', 'blue', 'green', 'blockquote', 'blockindent', 'doubleindent', 'superscript', 'subscript', 'ul', 'image', 'link', 'hr', 'embed'], template='streams/richtext_block.html')), ('images', wagtail.core.blocks.StructBlock([('images', wagtail.core.blocks.RichTextBlock(features=['image'])), ('caption', wagtail.core.blocks.RichTextBlock(features=['italic', 'bold', 'strikethrough', 'link'], form_classname='centered', required=False))], icon='image', label='Image(s) with Caption')), ('caption', wagtail.core.blocks.StructBlock([('caption', wagtail.core.blocks.RichTextBlock(features=['italic', 'bold', 'strikethrough', 'link'], form_classname='centered'))], icon='edit', label='Generic Caption')), ('heading', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(form_classname='full-title')), ('link_id', wagtail.core.blocks.CharBlock(help_text='For making hyperlinks to this heading'))], icon='title')), ('annotation', wagtail.core.blocks.StructBlock([('annotation', wagtail.core.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'bold', 'italic', 'underline', 'strikethrough', 'small', 'red', 'blue', 'green', 'blockquote', 'blockindent', 'doubleindent', 'superscript', 'subscript', 'ul', 'image', 'link', 'hr', 'embed'], form_classname='centered-annotation'))], icon='edit', label='Annotation Box')), ('left_justified_block', wagtail.core.blocks.StructBlock([('left_justified_block', wagtail.core.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'bold', 'italic', 'underline', 'strikethrough', 'small', 'red', 'blue', 'green', 'blockquote', 'blockindent', 'doubleindent', 'superscript', 'subscript', 'ul', 'image', 'link', 'hr', 'embed'], form_classname='left-justified-block'))], icon='edit', label='Left Justified Block')), ('table', wagtail.contrib.typed_table_block.blocks.TypedTableBlock([('text', wagtail.core.blocks.CharBlock(required=False)), ('numeric', wagtail.core.blocks.FloatBlock(required=False)), ('rich_text', wagtail.core.blocks.RichTextBlock(features=['italic', 'bold', 'strikethrough', 'red', 'blue', 'green', 'link', 'h2'], required=False))])), ('centered_text', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.RichTextBlock(features=['italic', 'bold', 'strikethrough', 'link'], form_classname='centered'))], icon='edit'))], blank=True, null=True),
        ),
    ]
