# Generated by Django 2.2.12 on 2020-06-29 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0024_clicks'),
    ]

    operations = [
        migrations.AddField(
            model_name='clicks',
            name='body',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
