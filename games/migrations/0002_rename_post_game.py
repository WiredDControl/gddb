# Generated by Django 3.2.12 on 2022-02-24 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Game',
        ),
    ]
