from django.db import models


class Band(models.Model):
    band_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)
    GENRE_CHOICES = (
        ('Rock', 'Rock'),
        ('Pop', 'Pop'),
        ('Jazz', 'Jazz'),
        ('Country', 'Country'),
        ('Hip Hop', 'Hip Hop'),
        ('R&B', 'R&B'),
        ('Electronic', 'Electronic'),
        ('Classical', 'Classical'),
        ('Reggae', 'Reggae'),
        ('Metal', 'Metal'),
        ('Folk', 'Folk'),
        ('Blues', 'Blues'),
        ('World Music', 'World Music'),
    )
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES, null=True)

    def __str__(self):
        return self.band_name


class Venue(models.Model):
    venue_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)
    MUSIC_TYPES = (
        ('Original Music', 'Original Music'),
        ('Covers', 'Covers'),
        ('Both', 'Both'),
    )
    type_of_music = models.CharField(max_length=50, choices=MUSIC_TYPES)

    def __str__(self):
        return self.venue_name


class ArtistListedGig(models.Model):
    artist_name = models.CharField(max_length=100)
    date_of_gig = models.DateField(null=True)
    UK_COUNTRIES = (
        ('England', 'England'),
        ('Wales', 'Wales'),
        ('Scotland', 'Scotland'),
        ('Northern Ireland', 'Northern Ireland'),
    )
    country_of_venue = models.CharField(max_length=100, choices=UK_COUNTRIES)
    venue_name = models.CharField(max_length=100)
    GENRE_CHOICES = (
        ('Rock', 'Rock'),
        ('Pop', 'Pop'),
        ('Jazz', 'Jazz'),
        ('Country', 'Country'),
        ('Hip Hop', 'Hip Hop'),
        ('R&B', 'R&B'),
        ('Electronic', 'Electronic'),
        ('Classical', 'Classical'),
        ('Reggae', 'Reggae'),
        ('Metal', 'Metal'),
        ('Folk', 'Folk'),
        ('Blues', 'Blues'),
        ('World Music', 'World Music'),
    )
    genre_of_gig = models.CharField(
        max_length=50, choices=GENRE_CHOICES, null=True)
    payment = models.IntegerField(null=True)

    def __str__(self):
        date_str = self.date_of_gig.strftime(
            '%d %b %Y') if self.date_of_gig else ''
        return f"{self.artist_name} - {self.venue_name} - {date_str}"
