# Generated by Django 4.1.7 on 2023-06-10 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gig_mania_backend', '0057_alter_artist_signup_date_alter_venue_signup_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='signup_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='venue',
            name='signup_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]