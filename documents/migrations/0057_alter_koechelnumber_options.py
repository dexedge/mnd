# Generated by Django 3.2.10 on 2022-01-01 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0056_alter_koechelnumber_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='koechelnumber',
            options={'ordering': ('koechel_sortable',), 'verbose_name': 'Koechel Number', 'verbose_name_plural': 'Koechel Numbers'},
        ),
    ]
