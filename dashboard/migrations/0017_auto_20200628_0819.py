# Generated by Django 2.2.12 on 2020-06-28 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0016_auto_20200628_0812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
