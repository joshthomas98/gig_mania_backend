# Generated by Django 4.1.7 on 2023-05-13 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gig_mania_backend', '0030_remove_artist_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='summary',
            field=models.CharField(max_length=80, null=True),
        ),
    ]
