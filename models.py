from django.db import models
from .choices import GENRE_CHOICES, UK_COUNTRY_CHOICES, UK_COUNTY_CHOICES, MUSIC_TYPES, ARTIST_TYPES, GIGGING_DISTANCE
from multiselectfield import MultiSelectField


class Artist(models.Model):
    artist_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)
    bio = models.CharField(max_length=5000, null=True)
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES, null=True)
    country = models.CharField(
        max_length=50, choices=UK_COUNTRY_CHOICES, null=True)
    county = models.CharField(
        max_length=100, choices=UK_COUNTY_CHOICES, null=True)
    type_of_artist = models.CharField(
        max_length=50, choices=ARTIST_TYPES, null=True)
    gigging_distance = MultiSelectField(
        choices=GIGGING_DISTANCE, blank=True, max_length=200)

    def __str__(self):
        return self.artist_name


class Unavailability(models.Model):
    artist = models.ForeignKey(
        Artist, on_delete=models.CASCADE, related_name='unavailabilities')
    date = models.DateField()

    def __str__(self):
        return f"{self.artist} - {self.date}"


class Venue(models.Model):
    venue_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)
    type_of_music = models.CharField(
        max_length=100, choices=MUSIC_TYPES, null=True)

    def __str__(self):
        return self.venue_name


class ArtistListedGig(models.Model):
    artist_name = models.CharField(max_length=100)
    date_of_gig = models.DateField(null=True)
    country_of_venue = models.CharField(
        max_length=100, choices=UK_COUNTRY_CHOICES)
    venue_name = models.CharField(max_length=100)
    genre_of_gig = models.CharField(
        max_length=50, choices=GENRE_CHOICES, null=True)
    payment = models.IntegerField(null=True)

    def __str__(self):
        date_str = self.date_of_gig.strftime(
            '%d %b %Y') if self.date_of_gig else ''
        return f"{self.artist_name} - {self.venue_name} - {date_str}"
