# Generated by Django 4.1.7 on 2023-06-03 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gig_mania_backend', '0044_alter_artist_facebook_alter_artist_twitter_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='phone_number',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
