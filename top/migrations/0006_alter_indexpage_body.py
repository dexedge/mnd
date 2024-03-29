# Generated by Django 3.2.7 on 2021-12-11 02:50

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('top', '0005_categorylistingpage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indexpage',
            name='body',
            field=wagtail.fields.StreamField([('year_or_kv', wagtail.blocks.CharBlock(help_text='Year or Köchel number', required=True, template='streams/h2.html')), ('page', wagtail.blocks.RichTextBlock(features=['italic', 'link'], template='streams/page.html'))]),
        ),
    ]
