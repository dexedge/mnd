# Generated by Django 3.2.10 on 2022-01-19 02:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0063_author_authororderable'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documentpage',
            name='author',
        ),
    ]