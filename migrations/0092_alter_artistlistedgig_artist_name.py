# Generated by Django 4.1.7 on 2023-07-17 23:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gig_mania_backend', '0091_alter_venuelistedgig_venue_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artistlistedgig',
            name='artist_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gig_mania_backend.artist'),
        ),
    ]
