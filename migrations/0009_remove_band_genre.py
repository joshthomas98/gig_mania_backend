# Generated by Django 4.1.7 on 2023-02-23 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gig_mania_backend', '0008_band_genre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='band',
            name='genre',
        ),
    ]
