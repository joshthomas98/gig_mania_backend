# Generated by Django 4.1.7 on 2023-06-10 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gig_mania_backend', '0053_venue_signup_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='signup_date',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Signup Date'),
        ),
    ]