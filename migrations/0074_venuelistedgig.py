# Generated by Django 4.1.7 on 2023-06-17 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gig_mania_backend', '0073_artistlistedgig_remove_gigapplication_artist_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='VenueListedGig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue_name', models.CharField(max_length=100)),
                ('date_of_gig', models.DateField(null=True)),
                ('country_of_venue', models.CharField(choices=[('England', 'England'), ('Wales', 'Wales'), ('Scotland', 'Scotland'), ('Northern Ireland', 'Northern Ireland')], max_length=100)),
                ('genre_of_gig', models.CharField(choices=[('Rock', 'Rock'), ('Pop', 'Pop'), ('Jazz', 'Jazz'), ('Country', 'Country'), ('Hip Hop', 'Hip Hop'), ('R&B', 'R&B'), ('Electronic', 'Electronic'), ('Classical', 'Classical'), ('Reggae', 'Reggae'), ('Metal', 'Metal'), ('Folk', 'Folk'), ('Blues', 'Blues'), ('World Music', 'World Music')], max_length=50, null=True)),
                ('type_of_gig', models.CharField(choices=[('Original Music', 'Original Music'), ('Covers', 'Covers'), ('Both', 'Both')], max_length=50, null=True)),
                ('payment', models.IntegerField(null=True)),
            ],
        ),
    ]
