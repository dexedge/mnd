# Generated by Django 3.2.7 on 2021-09-08 21:29

from django.db import migrations, models
import modelcluster.fields
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0008_document_source_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(allow_unicode=True, help_text='A slug to identify posts by this category', max_length=255, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['name'],
            },
        ),
        migrations.AlterField(
            model_name='document',
            name='source_image',
            field=wagtail.fields.StreamField([('large_image', wagtail.images.blocks.ImageChooserBlock(help_text='Source image'))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='transcription',
            field=models.TextField(help_text='Field allows HTML tagging'),
        ),
        migrations.AlterField(
            model_name='document',
            name='translation',
            field=models.TextField(blank=True, help_text='Field allows HTML tagging'),
        ),
        migrations.AddField(
            model_name='document',
            name='categories',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='documents.DocumentCategory'),
        ),
    ]
