# Generated by Django 2.2.12 on 2020-06-28 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_auto_20200628_0757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='time',
            field=models.TimeField(null=True),
        ),
    ]
