# Generated by Django 4.0.2 on 2023-04-03 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0042_remove_release_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='release',
            name='i3dbox',
            field=models.BooleanField(default=False, verbose_name='Addon?'),
        ),
        migrations.AddField(
            model_name='release',
            name='i3dboxlower',
            field=models.BooleanField(default=False, verbose_name='Addon?'),
        ),
        migrations.AddField(
            model_name='release',
            name='i3dboxupper',
            field=models.BooleanField(default=False, verbose_name='Addon?'),
        ),
        migrations.AddField(
            model_name='release',
            name='i3djewelcase',
            field=models.BooleanField(default=False, verbose_name='Addon?'),
        ),
    ]
