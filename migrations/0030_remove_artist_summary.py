# Generated by Django 4.1.7 on 2023-05-13 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gig_mania_backend', '0029_artist_summary_alter_artist_gigging_distance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='summary',
        ),
    ]