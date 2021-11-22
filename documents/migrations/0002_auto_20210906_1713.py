# Generated by Django 3.2.7 on 2021-09-06 17:13

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='document',
            name='transcription',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
    ]
