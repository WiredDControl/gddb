# Generated by Django 3.2.12 on 2022-03-02 12:32

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0015_auto_20220302_1152'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diskfilename', models.CharField(max_length=250, verbose_name='Image-Datei der Medien')),
                ('disktype', models.CharField(choices=[('F35', 'Floppy 3,5"'), ('F52', 'Floppy 5,25"'), ('CDR', 'CD-ROM'), ('DVD', 'DVD-ROM'), ('DDL', 'Download')], default='F35', max_length=3, verbose_name='Medientyp:')),
                ('diskcount', models.IntegerField()),
                ('diskdescr', models.CharField(blank=True, max_length=250, verbose_name='Beschreibung')),
                ('diskcomment', models.TextField(blank=True, verbose_name='Kommentar')),
                ('source', models.CharField(default='Timber', max_length=300, verbose_name='Von wem ist der Rip')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('rlstitle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='releasetitle2', to='games.release', verbose_name='Release')),
            ],
        ),
    ]
