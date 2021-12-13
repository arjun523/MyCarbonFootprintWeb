# Generated by Django 4.0 on 2021-12-13 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarbonWeb', '0013_co2web_overall_score'),
    ]

    operations = [
        migrations.RenameField(
            model_name='co2web',
            old_name='overall_score',
            new_name='score',
        ),
        migrations.AddField(
            model_name='co2web',
            name='msg1',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='co2web',
            name='msg2',
            field=models.CharField(default='', max_length=100),
        ),
    ]