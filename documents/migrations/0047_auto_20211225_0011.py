# Generated by Django 3.2.10 on 2021-12-25 00:11

from django.db import migrations
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0046_remove_documentpage_test_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentpage',
            name='document_title',
            field=wagtail.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='documentpage',
            name='source',
            field=wagtail.fields.RichTextField(blank=True),
        ),
    ]
