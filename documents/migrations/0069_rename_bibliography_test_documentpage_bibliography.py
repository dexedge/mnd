# Generated by Django 3.2.10 on 2022-02-06 02:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0068_remove_documentpage_bibliography'),
    ]

    operations = [
        migrations.RenameField(
            model_name='documentpage',
            old_name='bibliography_test',
            new_name='bibliography',
        ),
    ]
