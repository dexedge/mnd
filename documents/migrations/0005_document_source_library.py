# Generated by Django 3.2.7 on 2021-09-06 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0004_auto_20210906_1828'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='source_library',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
