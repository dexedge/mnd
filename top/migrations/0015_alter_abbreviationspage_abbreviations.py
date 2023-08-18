# Generated by Django 3.2.10 on 2022-02-10 20:33

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('top', '0014_alter_abbreviationspage_abbreviations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abbreviationspage',
            name='abbreviations',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(max_length=100, required=False))], icon='edit', label='Heading')), ('subheading', wagtail.blocks.StructBlock([('subheading', wagtail.blocks.CharBlock(max_length=100, required=False))], icon='edit', label='Subheading')), ('item', wagtail.blocks.StructBlock([('abbreviation', wagtail.blocks.RichTextBlock(features=['italic', 'underline'], form_classname='abbreviation')), ('link_id', wagtail.blocks.CharBlock(help_text='For making hyperlinks to this heading')), ('reference', wagtail.blocks.RichTextBlock(features=['italic', 'underline', 'link']))], icon='edit', label='Abbreviation'))], blank=True, null=True),
        ),
    ]
