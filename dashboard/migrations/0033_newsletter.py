# Generated by Django 2.2.14 on 2020-08-08 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0032_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=200)),
                ('pdf', models.FileField(upload_to='documents/')),
            ],
        ),
    ]
