# Generated by Django 4.1.7 on 2023-09-22 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gig_mania_backend', '0104_alter_artistlistedgig_num_applications'),
    ]

    operations = [
        migrations.AddField(
            model_name='venuelistedgig',
            name='num_applications',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
