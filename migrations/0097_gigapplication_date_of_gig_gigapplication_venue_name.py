# Generated by Django 4.1.7 on 2023-08-21 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gig_mania_backend', '0096_rename_artist_type_artistlistedgig_type_of_artist'),
    ]

    operations = [
        migrations.AddField(
            model_name='gigapplication',
            name='date_of_gig',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='gigapplication',
            name='venue_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
