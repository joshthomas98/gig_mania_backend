# Generated by Django 4.1.7 on 2023-08-31 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gig_mania_backend', '0098_venue_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gigapplication',
            name='artist_name',
        ),
        migrations.RemoveField(
            model_name='gigapplication',
            name='venue_name',
        ),
        migrations.AddField(
            model_name='gigapplication',
            name='artist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gig_mania_backend.artist'),
        ),
        migrations.AddField(
            model_name='gigapplication',
            name='venue',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gig_mania_backend.venue'),
        ),
    ]