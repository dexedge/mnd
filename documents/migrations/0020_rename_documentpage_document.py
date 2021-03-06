# Generated by Django 3.2.7 on 2021-09-11 23:30

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('documents', '0019_rename_document_documentpage'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DocumentPage',
            new_name='Document',
        ),
    ]
