# Generated by Django 3.2.7 on 2021-09-11 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0016_alter_document_citation_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='citation_title',
            field=models.TextField(blank=True, help_text='Field allows HTML tagging'),
        ),
    ]
