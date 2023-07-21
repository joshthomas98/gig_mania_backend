# Generated by Django 4.1.7 on 2023-07-16 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gig_mania_backend', '0085_venuelistedgig_artist_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='GigApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_name', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=200)),
            ],
        ),
    ]