# Generated by Django 3.2.12 on 2022-06-20 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0032_auto_20220415_0038'),
    ]

    operations = [
        migrations.AddField(
            model_name='release',
            name='timberprice',
            field=models.CharField(blank=True, default='0,00', max_length=20, verbose_name='Kaufpreis (Netto) in EUR'),
        ),
    ]
