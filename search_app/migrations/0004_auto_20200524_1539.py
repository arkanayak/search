# Generated by Django 2.2.1 on 2020-05-24 15:39

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('search_app', '0003_book_summary'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Freq',
            new_name='FreqIndex',
        ),
    ]
