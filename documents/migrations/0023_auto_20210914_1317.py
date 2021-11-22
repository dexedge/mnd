# Generated by Django 3.2.7 on 2021-09-14 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0022_auto_20210914_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentpage',
            name='transcription',
            field=models.TextField(help_text='Field allows HTML tagging'),
        ),
        migrations.AlterField(
            model_name='documentpage',
            name='translation',
            field=models.TextField(blank=True, help_text='Field allows HTML tagging'),
        ),
    ]
