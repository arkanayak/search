# Generated by Django 2.2.1 on 2020-05-24 15:34

from django.db import migrations, models


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('search_app', '0002_auto_20200524_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='summary',
            field=models.TextField(blank=True, null=True),
        ),
    ]