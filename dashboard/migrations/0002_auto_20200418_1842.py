# Generated by Django 3.0.5 on 2020-04-18 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Events',
            new_name='Eventss',
        ),
        migrations.AlterModelTable(
            name='eventss',
            table='Eventss',
        ),
    ]
