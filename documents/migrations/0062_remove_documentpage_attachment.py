# Generated by Django 3.2.10 on 2022-01-14 00:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0061_documentpage_attachment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documentpage',
            name='attachment',
        ),
    ]
