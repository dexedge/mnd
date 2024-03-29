# Generated by Django 3.2.10 on 2022-02-08 18:26

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('top', '0012_alter_abbreviationspage_abbreviations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abbreviationspage',
            name='abbreviations',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(max_length=100))], icon='edit', label='Heading', required=False)), ('subheading', wagtail.blocks.StructBlock([('subheading', wagtail.blocks.CharBlock(max_length=100))], icon='edit', label='Subheading', required=False)), ('item', wagtail.blocks.StructBlock([('abbreviation', wagtail.blocks.RichTextBlock(features=['italic', 'underline'], form_classname='abbreviation')), ('link_id', wagtail.blocks.CharBlock(help_text='For making hyperlinks to this heading')), ('reference', wagtail.blocks.RichTextBlock(features=['italic', 'underline']))], icon='edit', label='Abbreviation', required=False))]),
        ),
    ]
