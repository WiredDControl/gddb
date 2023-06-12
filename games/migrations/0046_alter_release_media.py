# Generated by Django 4.0.2 on 2023-06-12 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0045_alter_disk_disktype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='release',
            name='media',
            field=models.CharField(choices=[('F3', 'Floppy 3,5"'), ('F5', 'Floppy 5,25"'), ('CD', 'CD-ROM'), ('DD', 'DVD-ROM'), ('DL', 'Download'), ('TP', 'Tape')], default='F3', max_length=2),
        ),
    ]
