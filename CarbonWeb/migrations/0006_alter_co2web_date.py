# Generated by Django 3.2.7 on 2021-12-05 15:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarbonWeb', '0005_alter_co2web_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='co2web',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 5, 21, 13, 58, 533192)),
        ),
    ]