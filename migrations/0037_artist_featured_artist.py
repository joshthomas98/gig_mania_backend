# Generated by Django 4.1.7 on 2023-05-31 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gig_mania_backend', '0036_newslettersignup'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='featured_artist',
            field=models.BooleanField(default=False),
        ),
    ]
