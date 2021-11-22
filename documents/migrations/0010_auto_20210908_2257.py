# Generated by Django 3.2.7 on 2021-09-08 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0009_auto_20210908_2129'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='documentcategory',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='document',
            name='source_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='documentcategory',
            name='slug',
            field=models.SlugField(allow_unicode=True, help_text='A slug to identify posts in this category', max_length=255, verbose_name='slug'),
        ),
    ]
