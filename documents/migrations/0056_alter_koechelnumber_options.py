# Generated by Django 3.2.10 on 2022-01-01 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0055_koechelnumber_koechelnumberorderable'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='koechelnumber',
            options={'ordering': ('koechel_sortable',)},
        ),
    ]