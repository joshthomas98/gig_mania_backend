# Generated by Django 4.1.7 on 2023-05-09 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gig_mania_backend', '0020_band_bio'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Band',
            new_name='Artist',
        ),
        migrations.RenameField(
            model_name='artist',
            old_name='band_name',
            new_name='artist_name',
        ),
        migrations.RenameField(
            model_name='availability',
            old_name='band',
            new_name='artist',
        ),
    ]
