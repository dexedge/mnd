# Generated by Django 3.2.10 on 2022-02-08 18:26

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('top', '0012_alter_abbreviationspage_abbreviations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abbreviationspage',
            name='abbreviations',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(max_length=100))], icon='edit', label='Heading', required=False)), ('subheading', wagtail.core.blocks.StructBlock([('subheading', wagtail.core.blocks.CharBlock(max_length=100))], icon='edit', label='Subheading', required=False)), ('item', wagtail.core.blocks.StructBlock([('abbreviation', wagtail.core.blocks.RichTextBlock(features=['italic', 'underline'], form_classname='abbreviation')), ('link_id', wagtail.core.blocks.CharBlock(help_text='For making hyperlinks to this heading')), ('reference', wagtail.core.blocks.RichTextBlock(features=['italic', 'underline']))], icon='edit', label='Abbreviation', required=False))]),
        ),
    ]
