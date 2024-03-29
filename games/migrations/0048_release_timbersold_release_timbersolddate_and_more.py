# Generated by Django 4.0.2 on 2023-07-11 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0047_release_rlsregion'),
    ]

    operations = [
        migrations.AddField(
            model_name='release',
            name='timbersold',
            field=models.CharField(blank=True, default='0,00', max_length=20, verbose_name='Verkaufspreis (Netto) in EUR'),
        ),
        migrations.AddField(
            model_name='release',
            name='timbersolddate',
            field=models.DateField(blank=True, null=True, verbose_name='Verkaufs-Datum'),
        ),
        migrations.AddField(
            model_name='release',
            name='timberworth',
            field=models.CharField(blank=True, default='0,00', max_length=20, verbose_name='Aktueller Verkaufswert (Netto) in EUR'),
        ),
    ]
