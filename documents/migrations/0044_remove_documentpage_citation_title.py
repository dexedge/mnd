# Generated by Django 3.2.10 on 2021-12-23 22:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0043_auto_20211223_0058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documentpage',
            name='citation_title',
        ),
    ]