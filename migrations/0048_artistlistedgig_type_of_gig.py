# Generated by Django 4.1.7 on 2023-06-08 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gig_mania_backend', '0047_rename_type_of_music_venue_type_of_act'),
    ]

    operations = [
        migrations.AddField(
            model_name='artistlistedgig',
            name='type_of_gig',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
