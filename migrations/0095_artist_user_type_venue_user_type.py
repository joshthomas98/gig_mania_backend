# Generated by Django 4.1.7 on 2023-07-23 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gig_mania_backend', '0094_remove_artistlistedgig_artist_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='user_type',
            field=models.CharField(choices=[('Artist', 'Artist'), ('Venue', 'Venue')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='venue',
            name='user_type',
            field=models.CharField(choices=[('Artist', 'Artist'), ('Venue', 'Venue')], max_length=50, null=True),
        ),
    ]