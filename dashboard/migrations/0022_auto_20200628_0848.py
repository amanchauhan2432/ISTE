# Generated by Django 2.2.12 on 2020-06-28 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0021_auto_20200628_0843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(max_length=15),
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.TimeField(max_length=10),
        ),
    ]
