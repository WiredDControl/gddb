# Generated by Django 4.0.2 on 2022-03-13 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0024_remove_extra_extraquality_disk_quali_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='timbercomment',
        ),
        migrations.RemoveField(
            model_name='image',
            name='timberown',
        ),
        migrations.RemoveField(
            model_name='image',
            name='timberquali',
        ),
    ]
