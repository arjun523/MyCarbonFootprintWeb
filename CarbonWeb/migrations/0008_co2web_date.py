# Generated by Django 3.2.7 on 2021-12-05 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarbonWeb', '0007_remove_co2web_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='co2web',
            name='date',
            field=models.CharField(default='', max_length=100),
        ),
    ]
