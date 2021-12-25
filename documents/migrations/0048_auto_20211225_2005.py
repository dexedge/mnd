# Generated by Django 3.2.10 on 2021-12-25 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0047_auto_20211225_0011'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentpage',
            name='date_custom',
            field=models.CharField(blank=True, help_text='Use only for date ranges', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='documentpage',
            name='date_precision',
            field=models.CharField(choices=[('full', 'Full'), ('month', 'Month'), ('year', 'Year'), ('custom', 'Custom')], default='full', max_length=10, null=True),
        ),
    ]
