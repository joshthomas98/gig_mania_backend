# Generated by Django 4.1.7 on 2023-03-08 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gig_mania_backend', '0010_band_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='email',
            field=models.EmailField(max_length=200),
        ),
    ]