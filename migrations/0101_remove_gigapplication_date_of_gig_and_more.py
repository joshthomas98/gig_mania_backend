# Generated by Django 4.1.7 on 2023-09-22 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gig_mania_backend', '0100_alter_gigapplication_venue'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gigapplication',
            name='date_of_gig',
        ),
        migrations.RemoveField(
            model_name='gigapplication',
            name='email',
        ),
        migrations.RemoveField(
            model_name='gigapplication',
            name='venue',
        ),
        migrations.AddField(
            model_name='gigapplication',
            name='artist_gig',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gig_mania_backend.artistlistedgig'),
        ),
    ]
